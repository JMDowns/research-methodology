import json,os,glob,time,collections,re
root=os.path.expanduser('~/.claude/projects'); cut=time.time()-2*86400
pat=collections.Counter(); patL=collections.Counter(); compact=collections.Counter(); subdesc=[]
for f in glob.glob(root+'/**/*.jsonl',recursive=True):
    if os.path.getmtime(f)<cut: continue
    pending={}
    for line in open(f,errors='ignore'):
        try: d=json.loads(line)
        except: continue
        if (d.get('timestamp') or '')<'2026-11-05T10': continue
        if d.get('isCompactSummary') or d.get('subtype')=='compact_boundary': compact[f[len(root)+1:][:60]]+=1
        m=d.get('message') or {}
        if d.get('type')=='assistant':
            for c in m.get('content') or []:
                if isinstance(c,dict) and c.get('type')=='tool_use' and c['name']=='Bash': pending[c['id']]=c['input'].get('command','')
        elif d.get('type')=='user' and isinstance(m.get('content'),list):
            for c in m['content']:
                if c.get('type')=='tool_result' and c.get('tool_use_id') in pending:
                    cmd=pending[c['tool_use_id']]; cc=c.get('content'); L=len(cc) if isinstance(cc,str) else len(json.dumps(cc))
                    k=re.sub(r'\d+','N',re.sub(r'^(cd \S+ && |[A-Z]=\S+;? *)+','',cmd))[:60]
                    pat[k]+=1; patL[k]+=L
for k,v in patL.most_common(20): print(f"{v/1e6:5.1f}M {pat[k]:5d}  {k!r}")
print(compact)
