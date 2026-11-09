---
title: "How to Research as an AI Agent — The AI-Specific Layer of Rigorous LLM-Driven Research"
date: 2026-06-07
status: complete
confidence: high
confidence_reason: "Built on the user's three empirically-grounded existing assets (R3 web-search methodology with A/B data, peer-developer cite-or-retract study, eval-rubrics study) and extended with 6+ freshly-fetched primary/secondary sources across 4+ domains: Anthropic's own multi-agent and context-engineering engineering posts (primary), the Chain-of-Verification paper, RAG-faithfulness research, the Claude Code agentic-search-vs-RAG analysis, and deep-research-product writeups. Process-audit section is grounded in this project's own observed behavior (pipeline-bug band errors, README-stub risk) recorded in MEMORY.md."
completeness: 85
completeness_reason: "Covers the full agentic research loop, orchestration economics, grounding/anti-hallucination, cross-referencing, context budgeting, verification passes, AI-specific failure modes, human-in-the-loop, a candid process audit, and an operating-procedure checklist. Gaps: no fresh A/B for the verification-pass / firm-up wave specifically (inherited from the R3 study's design, not re-measured here); deep-research-product internals are vendor-described, not independently verified; the OpenAI Deep Research primary page could not be read."
category: methodology
tier: 3
objective: "How should an AI agent (Claude + web search + subagent fan-out) conduct rigorous, cited research — the AI-specific operational layer above general research methodology: the agentic loop, orchestration economics, grounding, context budgeting, verification, and AI-specific failure modes."
source_count: 9
known_gaps:
  - "No fresh A/B measuring the marginal quality lift of a dedicated firm-up/verification wave on medium-confidence outputs; the value is inherited from the R3 study's +7.1pt cross-reference finding, not re-measured for the wave pattern."
  - "Deep-research products (OpenAI/Gemini/Perplexity) are described from vendor and secondary writeups; internal orchestration is not independently verified."
  - "The OpenAI Deep Research primary page could not be read, so its limitation claims are unverified."
  - "No measured token-budget ceiling for when fan-out stops paying off on THIS project's craft-study workload specifically; the 15x multiplier and effort tiers are Anthropic's general numbers."
  - "Provenance-loss rate across subagent handoffs is asserted from observed README-stub incidents, not quantified."
next_steps:
  - "Run an A/B on the firm-up wave: take 10 medium-confidence craft-study cells, re-source half with a dedicated verification subagent and half not, score citation accuracy and contradiction-catch rate."
  - "Add a deterministic provenance check to the pipeline: every claim in an assembled README must trace to a line in sources/; a Stop hook blocks assembly if the README has un-sourced assertions (closes the README-stub gap)."
  - "Instrument fan-out cost: log tokens-per-subagent and quality delta per study tier to find the project-specific point where fan-out stops paying."
quality_checklist:
  sourced_claims: true
  cross_referenced: true
  flagged_contradictions: true
  verified_surprising: true
  noted_confidence: true
  listed_gaps: true
  targeted_prompts: true
  within_budget: true
---

# How to Research as an AI Agent

## Question / Objective

How should an AI agent — Claude with web search plus subagent fan-out — conduct rigorous, cited research? This is the **AI-specific layer**. The sibling [[how-to-research]] covers general research methodology (what makes any inquiry sound); [[research-quality-metrics]] covers how to score the output. This study covers the part that only exists because the researcher is an LLM agent: the agentic loop, the economics of fanning out, grounding against the model's own training-data fabrications, the reality that half the web won't fetch, and the failure modes that are unique to confident statistical text generators doing research.

It extends three existing assets rather than re-deriving them:
- [[web-search-methodology]] — the empirically A/B-tested R3 search loop (Tier 1/2/3, WebSearch→WebFetch, cross-reference 2+ domains, "never fill gaps from training data"). **This study assumes that loop and builds the orchestration/verification/audit layer on top.**
- The eval-rubrics study — LLM-as-judge for grading. **The verification section borrows its decomposed/adversarial judging.**

---

## TL;DR — the eight load-bearing rules

1. **Search → read → assess → iterate, then stop on a budget.** The loop is adaptive depth, not fixed depth; reason between every call.
2. **Fan out only on breadth-first work.** Multi-agent pays when sub-questions are independent; it wastes tokens (and corrupts results) when they're interdependent.
3. **Every fact comes from a fetched source. No exceptions.** Training-data fill is the #1 AI-research error and it is invisible because it sounds right.
4. **A citation is not grounding.** Citation presence has near-zero correlation with factual accuracy; verify the source *says* the claim.
5. **A page you could not read is not a source.** Mark claims that depend on it as unverified instead of trusting a snippet.
6. **Subagents return digests, not dumps.** Keep verbose content out of the orchestrator's context (1–2k-token summaries).
7. **Re-source medium-confidence outputs in a dedicated pass.** A firm-up wave catches what the first pass fabricated or single-sourced.
8. **Escalate to the human on contradiction, ethics, or central claims that have no readable source** — not on routine gaps.

---

## 1. The agentic research loop

The atomic unit is **search → read → assess → iterate**, with explicit reasoning between every step. Anthropic's own guidance is to "start with short, broad queries, evaluate what's available, then progressively narrow focus" rather than defaulting to "overly long, specific queries that return few results" ([Anthropic — multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-06-07).

**Query reformulation** is the skill that separates good agentic search from naive search. A query that returns thin snippets is a signal to broaden, not to fetch the thin results. The R3 methodology operationalizes this: WebSearch returns titles+URLs (cheap), you read snippets, then WebFetch only the 2–3 best with a *targeted* prompt — never fetch every result ([[web-search-methodology]]).

**Adaptive depth beats fixed depth.** Scale effort to query complexity: "Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents" ([Anthropic — multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-06-07). This is the Tier 1/2/3 split already in CLAUDE.md.

**When to stop.** Agentic loops have no natural terminator — left alone they run until the context fills. Stop when: (a) the same facts recur across new sources (saturation), (b) you've cross-checked the load-bearing claims on 2+ domains, or (c) you hit the budget. Even OpenAI Deep Research caps its search count; unbounded loops are a cost failure, not thoroughness.

## 2. Orchestration — single agent vs lead + parallel subagents

Anthropic's orchestrator-worker pattern: a lead agent decomposes the query and spawns 3–5 subagents in parallel, each given "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." Without those, agents "duplicate work, leave gaps, or fail to find necessary information" ([Anthropic — multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-06-07). Their documented failure: a vague "research the semiconductor shortage" caused subagents to scatter across 2021 and 2025 and duplicate each other.

**The economics.** Multi-agent systems "use about 15× more tokens than chats," and "token usage by itself explains 80% of the variance" in research-eval performance — but only when those tokens are *directed*. The multi-agent system beat single-agent Opus by **90.2%** on internal evals ([Anthropic — multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-06-07).

**When fan-out pays vs wastes.** It pays on "breadth-first queries that involve pursuing multiple independent directions simultaneously" and when information "exceeds single context windows." It *wastes* (or corrupts) when tasks are interdependent: "Domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today" ([Anthropic — multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-06-07). The practical test: *can each sub-question be answered without seeing the others' answers?* If yes, fan out. If a subagent needs another's output to even form its query, keep it sequential in one context.

**The wave / self-write patterns this project uses.** This project runs Tier-3 work as parallel subagent *waves* (each cell is an independent strand) and uses "self-write" subagents that produce both findings and the file. Both are correct applications of the breadth-first rule: the cells are genuinely independent. The fragility is in §"Auditing our process."

## 3. Grounding and anti-hallucination

This is the rule that, in the R3 A/B, eliminated the fabrication errors that had dropped quality 7 points: **never state something as fact unless it came from a fetched source; mark unverified claims "(unverified)"; if you can't ground a claim, retract it** ([[web-search-methodology]]; an earlier private study). It is the research-task form of cite-or-retract.

Why it matters more for an agent than a human: an LLM's training-data fill is fluent, plausible, and *indistinguishable in tone* from a sourced claim. A human researcher who doesn't know a fact feels the gap; the model generates over it seamlessly. Chain-of-Verification formalizes the countermeasure — draft, then *plan verification questions, answer them against sources, and revise* — and reports F1 improving 23% (0.39→0.48) on list/long-form tasks ([Chain-of-Verification, arXiv 2309.11495](https://arxiv.org/pdf/2309.11495) — accessed 2026-06-07).

**A citation is not grounding.** The subtler trap: the model generates a claim from parametric memory and *then* "scans retrieved documents for post-hoc supporting tokens" rather than deriving the answer from evidence. One study found "57% of citations in a RAG-optimized model showed unfaithful behavior," and "over 95% of answers produced by tested open-source LLMs contain at least one sentence lacking any attribution." Most damning: "citation presence has been shown to have near-zero correlation with factual accuracy ... supported and unsupported statements [are] cited at nearly identical rates" ([Why Citation-Based RAG Still Hallucinates](https://yaihq.com/research/citation-based-rag-still-hallucinates) — accessed 2026-06-07). The operational consequence: don't trust that a claim is grounded because it *has* a citation — the verifier must confirm the cited source actually *says* it.

## 4. Pages that cannot be read

Some sources will not load for an agent. When that happens, the page has not been read, and the study should say so.

The wrong response is to fall back on the search snippet and treat it as a verified read. A single snippet is the weakest possible source. The right responses, in order:
1. **Mark the claim "(unverified)"** and leave it out of the headline findings.
2. **Prefer primary documents.** Official docs, the actual paper/PDF, the vendor's own page are more authoritative than aggregators.
3. **If the claim is central to the study, tell the human** rather than guessing.

Separately, agentic search (grep/glob over the live filesystem) beats RAG indexing for code: precision (exact match vs "fuzzy positives"), freshness (no index drift during edits), and no preprocessing — the tradeoff being token burn on common terms ([Claude Code doesn't index your codebase](https://vadim.blog/claude-code-no-indexing) — accessed 2026-06-07). For *web* research the analog holds: fetch-and-read the live source beats trusting a stale cache or a snippet.

## 5. Cross-referencing and contradiction handling at agent speed

The R3 finding is blunt: skipping cross-reference cost 7.1 quality points; "different wikis contain different errors; using 2+ sources catches most of them" ([[web-search-methodology]]). At agent speed this is cheap — a second fetch is seconds — so there is no excuse to single-source a load-bearing claim.

When sources **contradict**, do not silently pick one. Surface it: state both, note which is more authoritative (primary > secondary > aggregator > snippet) and *why*, and flag it in a Contradictions section. This project's frontmatter has a `flagged_contradictions` checklist item precisely to force this. The eval-rubrics study's adversarial critic/defender pattern is the formal version: have one pass argue for the claim and one against, then judge.

## 6. Context budgeting — digests, not dumps

Context is "a finite resource" with a depleting "attention budget," and **context rot** is real: "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases" — independent of whether the window is full ([Anthropic — effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — accessed 2026-06-07). Across 18 frontier models tested, every one degraded as input grew. For a long research session this is the silent killer: by the time you synthesize, the early sources are "lost in the middle."

Mitigations, all in use or recommendable here:
- **Subagent isolation** — the highest-impact move. A subagent burns its whole context on verbose WebFetch output and returns "a condensed, distilled summary of its work (often 1,000-2,000 tokens)" to the lead. The orchestrator's context stays clean ([Anthropic — context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — accessed 2026-06-07).
- **Just-in-time retrieval** — carry lightweight identifiers (URLs, file paths, the `sources/` dir) and load content at the moment of need, not all up front.
- **Structured note-taking / artifacts** — write findings to `sources/research-report.md` as you go; the README is assembled from the durable note, not from scrollback that may have been compacted away.
- **Smallest high-signal token set** — Anthropic's core principle: find "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." Digest, don't dump.

## 7. Verification passes — re-sourcing and firm-up

A single forward pass is not a finished study. Two verification layers, both already practiced here:

- **The firm-up / re-sourcing wave.** Medium-confidence outputs get a second dedicated pass that re-fetches and confirms the load-bearing claims (this is what the project calls firming up medium-confidence cells). It is Chain-of-Verification applied at the study level: the first wave drafts, the firm-up wave plans and answers verification questions, then revises.
- **Adversarial / self-consistency checks.** For a contested claim, generate the verification independently (different query, different domain) rather than re-reading the same source — independent derivation catches post-hoc-citation fabrication that a re-read of the original will not. Self-consistency (sample multiple independent reasoning paths, keep what agrees) is the same idea.

Decide *which claims* deserve a verification pass by confidence and load-bearing-ness: a surprising or central claim gets cross-checked; a corroborated background fact does not. The `confidence`/`completeness` frontmatter is the trigger — anything below "high" should have had a firm-up pass before it's marked complete.

## 8. Failure modes and anti-patterns specific to AI research

| Failure mode | What it looks like | Mitigation |
|---|---|---|
| **Confident fabrication** | Fluent, sourced-sounding claim with no fetched basis; training-data fill | Fetched-source-only rule; mark "(unverified)"; cite-or-retract |
| **Single-snippet trust** | Treating a search snippet as a verified read | Fetch the page; cross-check on a 2nd domain |
| **Citation theater** | Claim has a citation but the source doesn't say it (post-hoc citation) | Verifier confirms the source *contains* the claim |
| **Echo-chamber sourcing** | "2 sources" that are the same content syndicated; SEO content farms over primaries | Require distinct *domains* + prefer primary docs (Anthropic saw agents pick "SEO-optimized content farms over authoritative ... academic PDFs") |
| **Over-fan-out** | Spawning subagents on interdependent sub-questions; 15x cost, scattered/duplicated work | Fan out only on independent strands; the "can each answer without the others?" test |
| **Lost provenance** | Subagent returns a polished summary; the claim-to-source link is gone | Subagents return claim→URL pairs, not just prose; persist to `sources/` |
| **Context rot at synthesis** | Early sources forgotten by the time the README is written | Note-take to disk; assemble from the durable note, not scrollback |
| **Pipeline band/label drift** | An automated stage mislabels a result (see audit below) | Human sanity-check on surprising labels; don't trust a stage's self-report |

## 9. Human-in-the-loop and when to escalate

Automation and verification trade off: the more autonomous the agent, the more its errors compound silently. Escalate to the human — don't churn — when:
- **Sources contradict on a load-bearing claim** and authority can't break the tie.
- **A central claim has no source you could read.**
- **The task has an ethical, legal, or factual-stakes dimension** the agent shouldn't adjudicate alone.
- **Scope is ambiguous** — per the peer-developer discipline, ask before guessing (an earlier private study).

Conversely, do *not* escalate routine gaps the loop can close, and don't ask the user to pick a subset of a documented backlog — process it in priority batches. Anthropic's own note: humans "find edge cases that evals miss," including "hallucinated answers on unusual queries" — the human is the verifier of last resort, so reserve them for what the loop genuinely can't settle.

---

## Auditing our process

What this project does well, and what's fragile — assessed against the above.

**Works:**
- **Parallel-subagent waves on independent cells.** Separate topic cells are genuinely independent strands → textbook breadth-first fan-out. Each subagent isolates verbose fetches and returns a digest. This is the pattern Anthropic validates.
- **Cite-or-propose + fetched-source-only discipline.** The "(unverified)" tagging and the cross-reference-2-domains rule are exactly the grounding controls the literature says matter most, and the R3 A/B *measured* their value (+7.1 pts).
- **Confidence/completeness frontmatter as a verification trigger.** Forces an explicit grounding self-assessment and gives the firm-up wave a target (anything < high).
- **The deterministic-vs-judged cut.** Grading what can be rule-checked deterministically and only LLM-judging the subjective remainder is the right division (eval-rubrics study) — it keeps the judge's known biases off the parts that don't need it.
- **Firm-up passes on medium-confidence output.** A real second verification layer, not a single forward pass.

**Fragile:**
- **README-stub risk (provenance loss).** Bundle subprocesses sometimes write `presets.yaml` but leave the README a scaffold; the gap-detector misses it. This is the *lost-provenance* failure mode — the durable note exists but the assembled artifact doesn't trace to it. **Fix in next_steps:** a deterministic provenance check that blocks assembly when the README has un-sourced assertions.
- **Pipeline band/label drift.** The pipeline has assigned Band A to a known Band-D sub-study (recorded as a likely systemic bug). This is the *pipeline self-report trust* failure — a stage's own label is treated as ground truth. Mitigation: human sanity-check on surprising labels; never trust the stage's self-classification.
- **Subagent write-block / "I wrote it" trust.** In this repo, subagents can't persist files and return text only; trusting a subagent's claim that it wrote a file is the lost-provenance trap. The main thread must verify on disk. (This very run self-writes from the main thread for exactly that reason.)
- **The snippet temptation.** The fragile habit is treating a search snippet as a read page. The rule against it is documented but enforced by people, not automated.
- **Over-fan-out cost is unmeasured.** We fan out by default on Tier-3 without a project-specific measurement of where it stops paying. The 15x multiplier is Anthropic's general number; ours is uninstrumented.

---

## AI research operating procedure (checklist)

1. **Classify tier** (1/2/3) and set a tool-call budget before searching.
2. **Broad query → read snippets → fetch the best 2–3** with a targeted extraction prompt. Reason between calls.
3. **Fan out only if sub-questions are independent** (the "answerable without each other?" test). Give each subagent objective + output format + tools + boundaries.
4. **Subagents return digests** (1–2k tokens) with **claim→URL pairs**, not raw dumps. Persist to `sources/`.
5. **Every fact traces to a fetched source.** No training-data fill. Mark "(unverified)".
6. **Cross-check every load-bearing claim on a 2nd, distinct domain.** Prefer primary docs.
7. **When a page cannot be read:** mark the claim unverified or ask the human. Never promote a snippet to a verified read.
8. **Confirm citations actually say the claim** (no citation theater).
9. **Surface contradictions explicitly**; rank by source authority.
10. **Firm-up pass** on anything below `confidence: high` — re-derive independently, don't just re-read.
11. **Assemble the artifact from the durable note**, not scrollback (context-rot guard).
12. **Escalate** on unbreakable contradiction, central claim with no readable source, or ethical/scope ambiguity.
13. **Fill frontmatter honestly** — confidence/completeness/known_gaps/checklist reflect what was actually verified.

---

## Cross-references

- [[web-search-methodology]] — the R3 search loop this study sits on top of (Tier 1/2/3, WebSearch→WebFetch, cross-reference, no-training-fill).
- [[how-to-research]] — sibling: general (non-AI-specific) research methodology.
- [[research-quality-metrics]] — sibling: how to score research output quality.

---

## Sources

- [Anthropic — How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-06-07 (primary: orchestrator/subagent pattern, 15x token economics, 80%-variance, 90.2% lift, fan-out fit, LLM-as-judge eval, content-farm failure)
- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — accessed 2026-06-07 (primary: attention budget, context rot, compaction/note-taking/subagent isolation, just-in-time retrieval, 1–2k-token digests)
- [Chain-of-Verification Reduces Hallucination in LLMs (arXiv 2309.11495)](https://arxiv.org/pdf/2309.11495) — accessed 2026-06-07 (draft→plan-verification→execute→revise; +23% F1)
- [Why Citation-Based RAG Still Hallucinates](https://yaihq.com/research/citation-based-rag-still-hallucinates) — accessed 2026-06-07 (post-hoc citation; 57% unfaithful; 95%+ un-attributed; citation–accuracy near-zero correlation)
- [Claude Code doesn't index your codebase — Vadim's blog](https://vadim.blog/claude-code-no-indexing) — accessed 2026-06-07 (agentic search vs RAG: precision/freshness/simplicity/privacy; token-burn tradeoff)
- [Why Claude Code is special for not doing RAG / vector search (Aram, Medium)](https://zerofilter.medium.com/why-claude-code-is-special-for-not-doing-rag-vector-search-agent-search-tool-calling-versus-41b9a6c0f4d9) — accessed 2026-06-07 (cross-check: agentic-search-over-RAG rationale)
- [OpenAI — Introducing deep research](https://openai.com/index/introducing-deep-research/) — accessed 2026-06-07 (primary page not read; limitation claims unverified)
- [Perplexity Deep Research — how it works, limitations (DataStudios)](https://www.datastudios.org/post/perplexity-ai-deep-research-how-it-works-limitations-and-use-cases-for-professionals) — accessed 2026-06-07 (query decomposition → agentic browsing → critical synthesis → cited output; manual verification still required)
- [Deepchecks — RAG evaluation metrics: faithfulness, groundedness, citation accuracy](https://deepchecks.com/rag-evaluation-metrics-answer-relevancy-faithfulness-accuracy/) — accessed 2026-06-07 (faithfulness/groundedness/hallucination-rate definitions; attribution maps)

**Built on (existing project assets, not re-fetched):**
- `web-search-methodology/` — R3 A/B-tested search methodology (own prior study)
- `MEMORY.md` — recorded process incidents (pipeline band bug, README-stub risk, subagent write-block)
