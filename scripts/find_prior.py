#!/usr/bin/env python3
"""Find earlier work in this repo before starting new research.

Usage:
  python3 scripts/find_prior.py "topic or question text"
  python3 scripts/find_prior.py --file path/to/proposal.md
  python3 scripts/find_prior.py --urls https://a.example/x https://b.example/y
  add --rebuild to refresh the cached index (it refreshes itself after 24 h)

Prints, as Markdown:
  1. the closest existing studies (with status, date, one-line summary and
     where their source notes are), and the closest open proposals;
  2. for given URLs (or for URLs found in --file), which studies already
     have notes on that page and the accessed date written next to it.

Built for the duplication study (research-duplication-and-reuse/). It does not
decide anything: a reader still checks whether the earlier work answers the
new question, and re-checks headline facts against the original page.
"""
import argparse, json, os, re, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scripts", ".cache", "find_prior_index.json")
SKIP = {".git", "node_modules", "probe", "dl-ghidra", "__pycache__", ".cache"}
URL_RE = re.compile(r"https?://[^\s)>\"'`\]]+")
DATE_RE = re.compile(r"accessed\s+(\d{4}-\d{2}-\d{2})")


def front(txt):
    if not txt.startswith("---"):
        return None
    end = txt.find("\n---", 3)
    if end < 0:
        return None
    try:
        import yaml
        d = yaml.safe_load(txt[3:end])
        return d if isinstance(d, dict) else None
    except Exception:
        return None


def clean(u):
    return re.sub(r"[.,;:]+$", "", u.split("#")[0])


def build():
    studies, proposals, urls = {}, [], {}
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP]
        rel = os.path.relpath(dp, ROOT)
        if "README.md" in fns:
            txt = open(os.path.join(dp, "README.md"), encoding="utf-8", errors="ignore").read()
            fm = front(txt)
            if fm and "status" in fm:
                heads = " ".join(re.findall(r"^#{1,3} (.+)$", txt, re.M)[:30])
                studies[rel] = {
                    "title": str(fm.get("title", "")), "status": str(fm.get("status", "")),
                    "date": str(fm.get("date", "")), "summary": str(fm.get("summary", ""))[:300],
                    "text": " ".join(str(fm.get(k, "")) for k in ("title", "objective", "summary", "why")) + " " + heads,
                    "notes": 0,
                }
        if os.path.basename(dp) == "research_proposals":
            for fn in fns:
                if fn.endswith(".md") and fn != "README.md":
                    t = open(os.path.join(dp, fn), encoding="utf-8", errors="ignore").read()
                    m = re.search(r'^summary:\s*"(.+?)"\s*$', t, re.M)
                    title = t.splitlines()[0].lstrip("# ") if t else fn
                    cq = re.search(r"## Central question\s*\n+>\s*(.+)", t)
                    proposals.append({"path": os.path.join(rel, fn), "title": title,
                                      "summary": m.group(1) if m else "",
                                      "text": title + " " + (m.group(1) if m else "") + " " + (cq.group(1) if cq else "")})
    # URLs: map to the nearest study folder, remember note files and dates
    def study_of(r):
        d = r
        while True:
            if d in studies:
                return d
            if d in ("", "."):
                return None
            d = os.path.dirname(d)
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP]
        rel = os.path.relpath(dp, ROOT)
        s = study_of(rel)
        if not s:
            continue
        in_notes = "/sources" in "/" + rel
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(rel, fn)
            if in_notes:
                studies[s]["notes"] += 1
            for line in open(os.path.join(dp, fn), encoding="utf-8", errors="ignore"):
                for u in URL_RE.findall(line):
                    d = DATE_RE.search(line)
                    entry = urls.setdefault(clean(u), {})
                    prev = entry.get(path)
                    entry[path] = d.group(1) if d else (prev or "")
    idx = {"built": time.time(), "studies": studies, "proposals": proposals, "urls": urls}
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(idx, open(CACHE, "w"))
    return idx


def load(rebuild):
    if not rebuild and os.path.exists(CACHE):
        idx = json.load(open(CACHE))
        if time.time() - idx.get("built", 0) < 86400:
            return idx
    print("_(building index, about a minute)_", file=sys.stderr)
    return build()


def related(idx, query, k_studies=10, k_props=5, complete_only=False):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    keys = [
        s for s in idx["studies"]
        if "/per-genre/" not in s
        and (not complete_only or idx["studies"][s].get("status") == "complete")
    ]
    docs = [idx["studies"][s]["text"] for s in keys] + [p["text"] for p in idx["proposals"]]
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1, sublinear_tf=True)
    X = vec.fit_transform(docs + [query])
    sims = cosine_similarity(X[-1], X[:-1]).ravel()
    n = len(keys)
    st = sorted(((sims[i], keys[i]) for i in range(n)), reverse=True)[:k_studies]
    pr = sorted(((sims[n + j], idx["proposals"][j]) for j in range(len(idx["proposals"]))), key=lambda x: -x[0])[:k_props]
    return st, pr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--urls", nargs="*")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--complete-only", action="store_true", help="Exclude in_progress/draft studies from prior-art results (robust-llm-wiki gate)")
    a = ap.parse_args()
    idx = load(a.rebuild)
    text = " ".join(a.query)
    urls = list(a.urls or [])
    if a.file:
        t = open(a.file, encoding="utf-8", errors="ignore").read()
        text += " " + t[:6000]
        urls += [clean(u) for u in URL_RE.findall(t)]
    if text.strip():
        st, pr = related(idx, text, complete_only=a.complete_only)
        print("## Closest existing studies\n")
        print("| Score | Study | Status, date | Source notes | Summary |\n|---|---|---|---|---|")
        for sc, s in st:
            d = idx["studies"][s]
            status_label = d["status"] if d["status"] == "complete" else f"{d['status']} [UNVERIFIED DRAFT — do not cite]"
            print(f"| {sc:.2f} | `{s}/` | {status_label}, {d['date']} | {d['notes']} files in `{s}/sources/` | {d['summary'][:160]} |")
        print("\n## Closest open proposals\n")
        for sc, p in pr:
            print(f"- {sc:.2f} `{p['path']}` — {p['summary'][:160] or p['title']}")
        print("\nScores are word overlap (0-1) and depend on query length. Open the top 3 and anything scoring at least half the top score. A high score is not proof of duplication.")
    if urls:
        print("\n## Pages that already have notes in the repo\n")
        hit = 0
        for u in dict.fromkeys(urls):
            e = idx["urls"].get(clean(u))
            if not e:
                continue
            hit += 1
            where = "; ".join(f"`{p}` ({dt or 'no date'})" for p, dt in sorted(e.items(), key=lambda x: x[1], reverse=True)[:4])
            print(f"- {u} — {len(e)} file(s): {where}")
        print(f"\n{hit} of {len(set(urls))} URLs already have notes.")


if __name__ == "__main__":
    main()
