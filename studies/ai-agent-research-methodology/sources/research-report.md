# Research Report — How to Research as an AI Agent (sources & synthesis note)

Tier-3 meta-research. Method: WebSearch → WebFetch across 4+ domains per theme, building on three existing project assets rather than re-deriving them. Date 2026-06-07.

## Synthesis note

The study answers a layered question: given that the user already has an empirically A/B-tested *web-search* methodology (the R3 study), a *grounding/pushback* discipline (peer-developer mindset), and an *evaluation* discipline (eval-rubrics), what is the connective AI-agent layer that makes those into a rigorous research *process*? The answer decomposes into nine operational concerns plus a candid self-audit:

1. **The loop** — adaptive depth, reason-between-calls, query reformulation, budget-based stopping. (Anthropic multi-agent + R3.)
2. **Orchestration** — fan out on independent breadth-first strands only; 15x token cost; 80% of variance is token usage *when directed*; interdependent tasks (coding) are a poor fit. (Anthropic multi-agent.)
3. **Grounding** — fetched-source-only; mark "(unverified)"; cite-or-retract. The model's training-data fill is fluent and invisible — the central AI-specific hazard. (peer-developer + R3 + CoVe.)
4. **Unread pages** — a page that could not be read is not a source; mark claims that depend on it unverified; never promote a snippet to a verified read.
5. **Cross-referencing** — 2+ *distinct domains*; surface contradictions; rank by authority. (R3 +7.1pt finding; eval-rubrics adversarial pattern.)
6. **Context budgeting** — context rot is real and length-dependent; subagent isolation returns 1–2k-token digests; note-take to disk; smallest-high-signal-token-set. (Anthropic context engineering.)
7. **Verification passes** — firm-up wave on medium-confidence output = CoVe at study level; independent re-derivation beats re-reading the same source (catches post-hoc citation).
8. **AI-specific failure modes** — confident fabrication, single-snippet trust, citation theater, echo-chamber sourcing, over-fan-out, lost provenance, context rot at synthesis, pipeline label drift. (Table in README.)
9. **Human-in-the-loop** — escalate on unbreakable contradiction, central claim with no readable source, ethics/scope ambiguity; not on routine gaps.

**Process audit (this project):** Works — parallel waves on independent cells, cite-or-propose, confidence frontmatter as verification trigger, deterministic-vs-judged cut, firm-up passes. Fragile — README-stub provenance loss, pipeline band/label drift, subagent write-block "I wrote it" trust, unmeasured over-fan-out cost. Audit is grounded in MEMORY.md incidents.

**Key surprising/load-bearing findings:**
- Citation presence has **near-zero correlation with factual accuracy**; supported and unsupported statements are cited at nearly identical rates — so "it has a citation" proves nothing.
- **Token usage explains 80% of research-eval variance** — but only when directed; over-fan-out on interdependent work is the inverse trap.
- **Every one of 18 frontier models degraded as input grew** (context rot) — synthesis-time recall of early sources is a silent failure for long research.

**Contradiction / tension flagged:** Anthropic frames multi-agent fan-out as a 90.2% win, but explicitly excludes interdependent/shared-context tasks — so "fan out more" is *not* universally correct; the independence test gates it.


## Deduped source list

Freshly fetched / searched (2026-06-07):
1. Anthropic — Building a multi-agent research system (engineering blog) — FETCHED, primary
2. Anthropic — Effective context engineering for AI agents (engineering blog) — FETCHED, primary
3. Chain-of-Verification Reduces Hallucination in LLMs — arXiv 2309.11495 — searched (verbatim snippet: +23% F1, four-stage process)
4. Why Citation-Based RAG Still Hallucinates — yaihq.com — FETCHED (57% unfaithful; 95%+ un-attributed; near-zero citation–accuracy correlation)
5. Claude Code doesn't index your codebase — vadim.blog — FETCHED (agentic search vs RAG rationale + tradeoffs)
6. Why Claude Code is special for not doing RAG/vector search — zerofilter.medium.com — searched (cross-check for #5)
7. OpenAI — Introducing deep research — page not read
8. Perplexity Deep Research how-it-works/limitations — datastudios.org — searched (5-step pipeline; manual verification required)
9. Deepchecks — RAG evaluation metrics (faithfulness/groundedness/citation accuracy) — searched (metric definitions)

Existing project assets built on (not re-fetched):
- web-search-methodology/ (R3 A/B methodology)
- MEMORY.md (recorded process incidents)

Domain spread: anthropic.com (primary x2), arxiv.org, yaihq.com, vadim.blog, medium.com, openai.com (blocked), datastudios.org, deepchecks.com + 3 internal assets = 4+ external domains per major theme, satisfying the cross-reference rule.
