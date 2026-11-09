import json,sys,os,glob,time,collections,re
root=os.path.expanduser('~/.claude/projects')
cut=time.time()-2*86400
readext=collections.Counter(); readn=collections.Counter(); big=[]; bashcmd=collections.Counter(); bashn=collections.Counter()
mainctx={}; repeats=collections.Counter()
for f in glob.glob(root+'/**/*.jsonl',recursive=True):
    if os.path.getmtime(f)<cut: continue
    pending={}; issub='subagents' in f; ctxs=[]; seen=set()
    for line in open(f,errors='ignore'):
        try: d=json.loads(line)
        except: continue
        ts=d.get('timestamp') or ''
        if ts<'2026-11-05T10': 
            if d.get('type')=='assistant' and isinstance((d.get('message') or {}).get('content'),list):
                for c in d['message']['content']:
                    if c.get('type')=='tool_use': pending[c['id']]=None
            continue
        m=d.get('message') or {}
        if d.get('type')=='assistant':
            u=m.get('usage')
            if u and m.get('id') not in seen:
                seen.add(m.get('id')); ctxs.append(u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0))
            for c in m.get('content') or []:
                if isinstance(c,dict) and c.get('type')=='tool_use': pending[c['id']]=(c['name'],c.get('input',{}))
        elif d.get('type')=='user' and isinstance(m.get('content'),list):
            for c in m['content']:
                if c.get('type')!='tool_result': continue
                p=pending.get(c.get('tool_use_id'))
                if not p: continue
                n,inp=p; cc=c.get('content'); L=len(cc) if isinstance(cc,str) else len(json.dumps(cc))
                if n=='Read':
                    fp=inp.get('file_path',''); ext=os.path.splitext(fp)[1] or 'none'
                    readext[ext]+=L; readn[ext]+=1
                    repeats[(os.path.basename(os.path.dirname(f)) if issub else f[-20:],fp)]+=1
                if n=='Bash':
                    cmd=inp.get('command','').strip().split()[0] if inp.get('command') else '?'
                    bashcmd[cmd]+=L; bashn[cmd]+=1
                if L>40000: big.append((L,n,(inp.get('file_path') or inp.get('command','') or '')[:110], issub))
    if not issub and ctxs: mainctx[os.path.relpath(f,root)]=ctxs
print("READ by ext (Mchars,count):"); [print(f"  {e} {v/1e6:.1f}M {readn[e]}") for e,v in readext.most_common(10)]
print("BASH by first word:"); [print(f"  {e} {v/1e6:.1f}M {bashn[e]}") for e,v in bashcmd.most_common(12)]
print("results >40k chars:",len(big),"total",sum(b[0] for b in big)/1e6,"M"); 
for b in sorted(big,reverse=True)[:15]: print("  ",b)
print("same file read >=4x in one transcript:",sum(1 for k,v in repeats.items() if v>=4), "extra reads", sum(v-1 for v in repeats.values() if v>1))
for k,v in repeats.most_common(8): print("  ",v,k)
for k,c in mainctx.items():
    s=sorted(c); print("MAIN",k[:60],"turns",len(c),"median ctx",s[len(s)//2],"p90",s[int(len(s)*.9)],"turns>500k",sum(1 for x in c if x>500000))
