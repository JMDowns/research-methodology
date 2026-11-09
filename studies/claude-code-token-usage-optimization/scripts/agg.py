import json,sys,os,glob,time,collections
root=os.path.expanduser('~/.claude/projects')
cut=time.time()-2*86400
rows=[]
tools=collections.Counter(); toolres=collections.Counter(); toolcnt=collections.Counter()
for f in glob.glob(root+'/**/*.jsonl',recursive=True):
    if os.path.getmtime(f)<cut: continue
    seen=set(); s=dict(inp=0,cw=0,cr=0,out=0,turns=0,maxctx=0,models=collections.Counter(),first=None,last=None,tools=0)
    pending={}
    with open(f,errors='ignore') as fh:
        for line in fh:
            try: d=json.loads(line)
            except: continue
            ts=d.get('timestamp')
            if ts:
                s['first']=s['first'] or ts; s['last']=ts
            m=d.get('message') or {}
            if d.get('type')=='assistant':
                mid=m.get('id'); u=m.get('usage')
                if isinstance(m.get('content'),list):
                    for c in m['content']:
                        if c.get('type')=='tool_use':
                            pending[c['id']]=c['name']; s['tools']+=1
                if not u or mid in seen: continue
                if ts and ts<'2026-11-05T10': continue
                seen.add(mid)
                s['inp']+=u.get('input_tokens',0); s['cw']+=u.get('cache_creation_input_tokens',0)
                s['cr']+=u.get('cache_read_input_tokens',0); s['out']+=u.get('output_tokens',0); s['turns']+=1
                ctx=u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0)
                s['maxctx']=max(s['maxctx'],ctx); s['models'][m.get('model')]+=1
            elif d.get('type')=='user' and isinstance(m.get('content'),list):
                for c in m['content']:
                    if c.get('type')=='tool_result':
                        n=pending.get(c.get('tool_use_id'),'?')
                        cc=c.get('content'); L=len(json.dumps(cc)) if not isinstance(cc,str) else len(cc)
                        toolres[n]+=L; toolcnt[n]+=1
    rel=os.path.relpath(f,root)
    rows.append((rel,s))
json.dump({'rows':[(r,{**s,'models':dict(s['models'])}) for r,s in rows],'toolres':toolres,'toolcnt':toolcnt},open(sys.argv[1],'w'))
