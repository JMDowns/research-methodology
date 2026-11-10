#!/usr/bin/env python3
"""Deterministic verification and quality-scoring gate for research studies.

Implements the mechanical ship gates borrowed from the GitHub research survey
(research-method-benchmarking/github-survey/):
  - G1 Frontmatter & schema gate (CLAUDE.md required YAML fields)
  - G2 Citation provenance & zero-ghost-URL check (Ankit V4 citation_audit.py)
  - G3 Domain diversity & monoculture gate (research-quality-metrics O2)
  - G4 Verbatim quote entailment >=6 words against sources/*.md (hyperresearch / zissa-wiki)
  - G5 Numerical token traceability between README.md and sources/*.md (hyperresearch)
  - G6 Factual paragraph citation coverage & epistemic hygiene (Fact-check / Residue / Self-check)

Does NOT replace semantic NLI/Opus claim-faithfulness checking; runs in <1s at $0 API cost
before and after the semantic fact-check pass.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from urllib.parse import urlparse

import yaml

REQUIRED_FM_KEYS = {
    "title", "date", "status", "confidence", "confidence_reason",
    "completeness", "completeness_reason", "category", "tier",
    "objective", "summary", "why", "blockers", "source_count",
    "known_gaps", "next_steps", "quality_checklist",
}
TIER_URL_FLOORS = {1: 3, 2: 8, 3: 14}
URL_RE = re.compile(r"https?://[^\s)>\"'`\]]+")
ACCESSED_RE = re.compile(r"accessed\s+\d{4}-\d{2}-\d{2}", re.IGNORECASE)
REPO_REF_RE = re.compile(r"\[repo:\s*([^\]]+)\]")
QUOTE_RE = re.compile(r'"([^"\n]{25,})"')
NUMBER_RE = re.compile(r"\b\d+(?:\.\d+)?%|\$\d+(?:\.\d+)?|\b\d+\.\d+\b")


@dataclass
class StudyScore:
    study_path: str
    tier: int = 3
    status: str = "unknown"
    fm_valid: bool = False
    fm_missing: list[str] = field(default_factory=list)
    readme_words: int = 0
    unique_urls_readme: int = 0
    unique_urls_sources: int = 0
    distinct_domains: int = 0
    top_domain: str = ""
    top_domain_share: float = 0.0
    accessed_date_rate: float = 0.0
    url_provenance_rate: float = 0.0
    ghost_urls: list[str] = field(default_factory=list)
    repo_refs_valid: bool = True
    quote_count: int = 0
    quote_match_rate: float = 1.0
    unmatched_quotes: list[str] = field(default_factory=list)
    number_count: int = 0
    number_trace_rate: float = 1.0
    untraced_numbers: list[str] = field(default_factory=list)
    factual_para_count: int = 0
    factual_para_cited_rate: float = 0.0
    has_fact_check_section: bool = False
    has_residue_or_gaps: bool = False
    has_self_check: bool = False
    composite_gate_score: float = 0.0
    passed_hard_gates: bool = False


def clean_url(u: str) -> str:
    return re.sub(r"[.,;:]+$", "", u.split("#")[0]).rstrip("/")


def registrable_domain(u: str) -> str:
    try:
        parsed = urlparse(u)
        host = (parsed.hostname or "").lower()
        if host.startswith("www."):
            host = host[4:]
        if host in ("github.com", "raw.githubusercontent.com", "huggingface.co"):
            seg = [s for s in parsed.path.split("/") if s]
            if seg:
                return f"{host}/{seg[0].lower()}"
        parts = host.split(".")
        if len(parts) >= 3 and parts[-2] in ("co", "ac", "org", "gov", "edu") and len(parts[-1]) == 2:
            return ".".join(parts[-3:])
        return ".".join(parts[-2:]) if len(parts) >= 2 else host
    except Exception:
        # intent: Deliberate silence — malformed URL falls back to empty domain string
        return ""


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    try:
        fm = yaml.safe_load(text[3:end])
        body = text[end + 4:]
        return (fm if isinstance(fm, dict) else None), body
    except Exception:
        # intent: Deliberate silence — invalid YAML returns None frontmatter for gate reporting
        return None, text


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s%$.-]", " ", s.lower())).strip()


def load_sources_corpus(study_dir: str, repo_root: str, body: str) -> tuple[str, set[str]]:
    chunks: list[str] = []
    source_urls: set[str] = set()
    for pat in ("sources/*.md", "sources/**/*.md", "SCORECARD.md", "catalogue.md", "scorecard-results.md"):
        for p in glob.glob(os.path.join(study_dir, pat), recursive=True):
            if os.path.isfile(p):
                txt = open(p, encoding="utf-8", errors="ignore").read()
                chunks.append(txt)
                for u in URL_RE.findall(txt):
                    source_urls.add(clean_url(u))
    for m in REPO_REF_RE.finditer(body):
        ref_rel = m.group(1).strip().split("#")[0].strip()
        cand = os.path.join(repo_root, ref_rel)
        if os.path.isdir(cand):
            cand = os.path.join(cand, "README.md")
        if os.path.isfile(cand):
            txt = open(cand, encoding="utf-8", errors="ignore").read()
            chunks.append(txt)
            for u in URL_RE.findall(txt):
                source_urls.add(clean_url(u))
    return "\n".join(chunks), source_urls


def score_study(study_dir: str, repo_root: str) -> StudyScore:
    readme_path = os.path.join(study_dir, "README.md")
    rel_dir = os.path.relpath(study_dir, repo_root)
    res = StudyScore(study_path=rel_dir)
    if not os.path.isfile(readme_path):
        return res

    raw = open(readme_path, encoding="utf-8", errors="ignore").read()
    fm, body = parse_frontmatter(raw)
    if fm:
        res.missing = sorted(REQUIRED_FM_KEYS - set(fm.keys()))
        res.fm_missing = res.missing
        res.fm_valid = len(res.fm_missing) == 0
        res.tier = int(fm.get("tier", 3) or 3)
        res.status = str(fm.get("status", "unknown"))

    res.readme_words = len(re.findall(r"\b\w+\b", body))
    readme_urls = [clean_url(u) for u in URL_RE.findall(body)]
    uniq_readme_urls = sorted(set(readme_urls))
    res.unique_urls_readme = len(uniq_readme_urls)

    domains: dict[str, int] = {}
    for u in uniq_readme_urls:
        d = registrable_domain(u)
        if d:
            domains[d] = domains.get(d, 0) + 1
    res.distinct_domains = len(domains)
    if domains and uniq_readme_urls:
        top_d, top_c = max(domains.items(), key=lambda kv: kv[1])
        res.top_domain = top_d
        res.top_domain_share = round(top_c / len(uniq_readme_urls), 3)

    url_lines = [ln for ln in body.splitlines() if "http://" in ln or "https://" in ln]
    if url_lines:
        with_date = sum(1 for ln in url_lines if ACCESSED_RE.search(ln))
        res.accessed_date_rate = round(with_date / len(url_lines), 3)

    sources_text, source_urls = load_sources_corpus(study_dir, repo_root, body)
    res.unique_urls_sources = len(source_urls)
    if uniq_readme_urls:
        if source_urls:
            matched_urls = [u for u in uniq_readme_urls if u in source_urls or any(u.startswith(s) or s.startswith(u) for s in source_urls)]
            res.url_provenance_rate = round(len(matched_urls) / len(uniq_readme_urls), 3)
            res.ghost_urls = [u for u in uniq_readme_urls if u not in matched_urls][:10]
        else:
            res.url_provenance_rate = 0.0
            res.ghost_urls = uniq_readme_urls[:10]
    else:
        res.url_provenance_rate = 1.0

    norm_sources = normalize_ws(sources_text)
    quotes = [q.strip() for q in QUOTE_RE.findall(body) if len(q.strip().split()) >= 6 and "http" not in q]
    res.quote_count = len(quotes)
    if quotes and norm_sources:
        matched_q = 0
        for q in quotes:
            nq = normalize_ws(q)
            if nq in norm_sources:
                matched_q += 1
            else:
                words = nq.split()
                if len(words) >= 6 and " ".join(words[:6]) in norm_sources:
                    matched_q += 1
                else:
                    res.unmatched_quotes.append(q[:80])
        res.quote_match_rate = round(matched_q / len(quotes), 3)
    elif quotes and not norm_sources:
        res.quote_match_rate = 0.0

    body_main = re.split(r"^##\s+(?:Sources|Self-check|Fact-check)\b", body, flags=re.M)[0]
    nums = sorted(set(NUMBER_RE.findall(body_main)))
    res.number_count = len(nums)
    if nums and sources_text:
        traced = [n for n in nums if n in sources_text]
        res.number_trace_rate = round(len(traced) / len(nums), 3)
        res.untraced_numbers = [n for n in nums if n not in sources_text][:15]
    elif nums and not sources_text:
        res.number_trace_rate = 0.0

    paras = [p.strip() for p in re.split(r"\n\s*\n", body_main) if len(p.strip().split()) >= 25]
    factual_paras = [
        p for p in paras
        if not p.startswith("#") and not p.startswith("|") and not p.startswith("```") and not p.startswith(">")
    ]
    res.factual_para_count = len(factual_paras)
    if factual_paras:
        cited_p = sum(
            1 for p in factual_paras
            if (
                "http://" in p
                or "https://" in p
                or "[repo:" in p
                or "sources/" in p
                or "catalogue.md" in p
                or "scorecard-results.md" in p
                or "SCORECARD.md" in p
                or "[[" in p
            )
        )
        res.factual_para_cited_rate = round(cited_p / len(factual_paras), 3)

    res.has_fact_check_section = bool(re.search(r"^##\s+Fact-check\b", body, re.M | re.I))
    res.has_residue_or_gaps = bool(re.search(r"^##\s+(?:Known Gaps|Residue)", body, re.M | re.I))
    res.has_self_check = bool(re.search(r"^##\s+Self-check\b", body, re.M | re.I))

    floor = TIER_URL_FLOORS.get(res.tier, 14)
    url_floor_ok = 1.0 if res.unique_urls_readme >= floor else min(1.0, res.unique_urls_readme / max(1, floor))
    diversity_ok = 1.0 if (res.distinct_domains >= 4 and res.top_domain_share <= 0.45) else 0.5
    hygiene_score = (
        (0.4 if res.has_fact_check_section else 0.0)
        + (0.3 if res.has_residue_or_gaps else 0.0)
        + (0.3 if res.has_self_check else 0.0)
    )
    res.composite_gate_score = round(
        100.0 * (
            0.15 * (1.0 if res.fm_valid else 0.5)
            + 0.15 * url_floor_ok
            + 0.10 * diversity_ok
            + 0.20 * res.url_provenance_rate
            + 0.15 * res.number_trace_rate
            + 0.15 * res.factual_para_cited_rate
            + 0.10 * hygiene_score
        ),
        1,
    )
    res.passed_hard_gates = (
        res.fm_valid
        and res.unique_urls_readme >= floor
        and res.url_provenance_rate >= 0.80
        and res.number_trace_rate >= 0.75
        and res.factual_para_cited_rate >= 0.70
    )
    return res


def format_markdown_table(scores: list[StudyScore]) -> str:
    lines = [
        "| Study | Tier | FM OK | URLs (Domains) | URL Provenance (`sources/`) | Number Traceability | Para Citation Rate | Fact-Check / Self-Check | Composite Gate Score | Gate Pass |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for s in scores:
        fc_sc = f"{'Yes' if s.has_fact_check_section else 'No'} / {'Yes' if s.has_self_check else 'No'}"
        lines.append(
            f"| `{s.study_path}` | T{s.tier} | {'Yes' if s.fm_valid else 'No'} | "
            f"{s.unique_urls_readme} ({s.distinct_domains} dom, top {s.top_domain_share*100:.0f}%) | "
            f"{s.url_provenance_rate*100:.1f}% | {s.number_trace_rate*100:.1f}% ({s.number_count}) | "
            f"{s.factual_para_cited_rate*100:.1f}% | {fc_sc} | **{s.composite_gate_score:.1f}/100** | "
            f"{'PASS' if s.passed_hard_gates else 'WARN'} |"
        )
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic study verification gate.")
    ap.add_argument("paths", nargs="+", help="Study directories to verify")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    ap.add_argument("--strict", action="store_true", help="Exit non-zero if any study fails hard gates")
    args = ap.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scores = [score_study(os.path.abspath(p), repo_root) for p in args.paths]
    if args.json:
        print(json.dumps([asdict(s) for s in scores], indent=2))
    else:
        print(format_markdown_table(scores))
        for s in scores:
            if s.fm_missing:
                print(f"  [{s.study_path}] Missing frontmatter keys: {', '.join(s.fm_missing)}")
            if s.ghost_urls:
                print(f"  [{s.study_path}] URLs in README not found in sources/ ({len(s.ghost_urls)} shown): {s.ghost_urls[:3]}")
            if s.untraced_numbers:
                print(f"  [{s.study_path}] Untraced numbers in README ({len(s.untraced_numbers)} shown): {s.untraced_numbers[:8]}")
    if args.strict and any(not s.passed_hard_gates for s in scores):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
