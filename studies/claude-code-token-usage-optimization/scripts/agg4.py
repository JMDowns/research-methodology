import json,os,glob,time,collections
root=os.path.expanduser('~/.claude/projects'); cut=time.time()-2*86400
imgdelta=[]; 
for f in glob.glob(root+'/**/*.jsonl',recursive=True):
    if os.path.getmtime(f)<cut: continue
    sub='subagents' in f; seen=set(); last=None; pendimg=False; pending={}
    trig=collections.Counter(); misses=[]; 
    for line in open(f,errors='ignore'):
        try: d=json.loads(line)
        except: continue
        if (d.get('timestamp') or '')<'2026-11-05T10': continue
        m=d.get('message') or {}
        if d.get('type')=='assistant':
            u=m.get('usage')
            for c in m.get('content') or []:
                if isinstance(c,dict) and c.get('type')=='tool_use': pending[c['id']]=c['name'],c['input']
            if u and m.get('id') not in seen:
                seen.add(m.get('id')); ctx=u['input_tokens']+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0)
                if pendimg and last: imgdelta.append(ctx-last)
                pendimg=False
                if u.get('cache_creation_input_tokens',0)>100000: misses.append(u['cache_creation_input_tokens'])
                last=ctx
        elif d.get('type')=='user':
            c=m.get('content')
            if isinstance(c,list) and any(x.get('type')=='tool_result' for x in c):
                n=0
                for x in c:
                    if x.get('type')=='tool_result':
                        p=pending.get(x.get('tool_use_id'))
                        if p and p[0]=='Read' and str(p[1].get('file_path','')).endswith('.png'): n+=1
                        elif p: n=-99
                pendimg = n==1
            else:
                s=json.dumps(c)[:300]
                k='task-notification' if 'task-notification' in s else 'wakeup/loop' if ('loop' in s or 'wakeup' in s.lower()) else 'system-reminder' if s.startswith('"<system') or 'system-reminder' in s[:40] else 'user-text'
                if not d.get('isMeta'): trig[k]+=1
    if not sub and seen: print(os.path.relpath(f,root)[:58], dict(trig), "cache rewrites >100k:",len(misses),"tokens",sum(misses))
s=sorted(imgdelta); print("image read ctx delta: n",len(s),"median",s[len(s)//2] if s else None,"p90",s[int(len(s)*.9)] if s else None)
