---
title: "Research Pipeline Comparison: Repo Default vs Deep-Research Skill vs Hybrid"
date: 2026-10-09
status: complete
confidence: low
confidence_reason: "One question, one run per method, Claude judging Claude, and claim-check samples of 16-35 claims. No spot-check difference is statistically significant (Fisher exact p >= 0.14). The direction of the trade-offs is consistent across measures and judge runs, but the size is not established."
completeness: 70
completeness_reason: "All three methods run end to end on the same question and scored with automated checks, claim spot-checks, two blind 3-way judge runs and two post-hoc pairwise runs. Missing: a second question, repeated runs per method, a human spot-check of the judge, and per-method cost for scoring."
category: methodology
tier: 3
objective: "Measure whether the hybrid research approach (repo proposal + repo search rules + parallel researchers + separate writer) improves or reduces research quality compared to the repo's default Tier-3 method and the deep-research skill as shipped."
summary: "The hybrid gave the most usable package (study + setup instructions) and the widest sourcing, at ~1.5x the tokens and ~2.5x the wall time. The skill's single report read best and won the blind judge, but had the most claims that drifted from their sources. The repo default had the cleanest claims."
why: "Decide which research pipeline to use for future studies in this repo, and what to change in the hybrid."
blockers: []
source_count: 0
known_gaps:
  - "Single question and single run per method; differences may be noise."
  - "Judge is Claude Sonnet judging Opus-written reports; no different model family and no human check of the judge."
  - "Claim checks used a different checker agent per report, so checker strictness varies."
  - "Arm A's synthesis was written by the coordinator, who had seen B and C researcher summaries and wrote the proposal."
  - "Scoring-side token cost not attributed per method; arm A synthesis tokens estimated, not measured."
next_steps:
  - "Repeat the 3-way comparison on a second, narrower question (Tier 2) to see if the pattern holds."
  - "Change the hybrid writer prompt: lead with a plain answer to the user's own questions (not the proposal's Q-numbers) and cap the README at ~3,500 words, moving the prior/disconfirmer audit to an appendix."
  - "Add a claim-faithfulness pass to the separate-writer step (re-check every number and quote against the notes) — the drift seen in B's and C's reports came from the writing step."
  - "Have one checker agent check all three arms' claims in one run, to remove checker-strictness variance."
quality_checklist:
  sourced_claims: true
  cross_referenced: false
  flagged_contradictions: true
  verified_surprising: true
  noted_confidence: true
  listed_gaps: true
  targeted_prompts: true
  within_budget: true
---

# Research Pipeline Comparison: Repo Default vs Deep-Research Skill vs Hybrid

## Question / Objective

Does the hybrid approach (write a repo-style proposal, run parallel researchers under the repo's search rules, then have a separate writer agent produce the study) make research better or worse than (A) the repo's default Tier-3 method and (B) the deep-research skill as shipped?

All three methods researched the same real question: the user's four questions on reviewing AI-written code and preventing intent debt. Method C's output became a separate private study.

**Confidence:** Low. **Completeness:** ~70%.

## Setup (full detail in [PLAN.md](PLAN.md))

| Method | Proposal | Researcher rules | Who wrote the final report | Output |
|---|---|---|---|---|
| A — repo default | no | repo CLAUDE.md R3 rules | the main session | `arm-a-repo-default/README.md` |
| B — deep-research skill | no | skill `researcher.md` | separate writer, skill `report-writer.md` | `arm-b-deep-research-skill/report.md` |
| C — hybrid | yes | repo R3 rules + proposal | separate writer, repo format | a separate private study |

Each method used the same four research clusters, run as 4 parallel researchers. All 12 researchers launched at the same time.

## Results

### Cost

| | A | B | C |
|---|---|---|---|
| Researcher + writer tokens | ~348k (+ ~25k main-session synthesis, estimated) | ~382k | ~548k (+ proposal) |
| Researcher tool calls (sum) | 153 | 87 | 180 |
| Wall time (parallel) | ~5 min + main-session writing | ~5.5 min | ~14 min |
| Main report length | 3,280 words | 3,231 words | 7,739 words (+ 4,874-word ai-instructions.md) |

The skill's researchers stayed close to its 15-call guidance (19-27 calls each). The repo-rule researchers in A and C ran 31-52 calls each. The repo rules say "don't stop at 1-2 fetches" but set no upper limit, and the proposal's extra questions (prior, disconfirmers, rival hypotheses) pushed C's researchers further.

### Automated checks (`scoring/auto_checks_all.json`)

| | A | B | C |
|---|---|---|---|
| Unique cited URLs | 57 | 40 | 88 |
| Distinct sites | 24 | 22 | 36 |
| URLs that resolve | 100% | 100% | 100% |
| Content blocks with ≥1 citation | 58% | 66% | 79% |
| Citations per 100 words | 2.47 | 1.47 | 2.97 |
| "(unverified)" markers kept | 0 | 0 | 3 |

Every cited link in all three reports resolved. C cited the most sources from the most sites. B had the lowest citation density, because the skill's writer works citations into prose paragraphs.

### Claim spot-check (primary measure, `scoring/claimcheck_*.json`)

10 randomly sampled cited blocks per report (fixed seed). Each block was split into single claims, and each claim was checked against its cited page.

| | A | B | C |
|---|---|---|---|
| Claims checked | 16 | 35 | 32 |
| Fully supported | 15 (94%) | 26 (74%) | 26 (81%) |
| Partly supported | 1 | 8 | 5 |
| Unsupported | 0 | 1 | 1 |

- None of these differences is statistically significant (Fisher exact test: A vs B p = 0.14, A vs C p = 0.40, B vs C p = 0.57).
- The kinds of errors differ by method:
  - **B:** most were quotes reworded inside quote marks (Storey's definition, the Storey blog quote, the doc-drift article's "misses implied architectural changes"). Others were small added details ("week 7" instead of "weeks 7 or 8", "formatting" added to a list of tested variations), and one wrong attribution: Wataoka et al. tested dialogue, not summaries.
  - **C:** mostly scope stretched ("more than any other surface change tested", a benchmark-specific 67% presented as a general figure), plus one claim that a paper studied self-bias when it didn't.
  - **A:** the one partly supported claim (the "28% useful alerts" wording) came from the main session's own paraphrase.
- So in B and C, the drift appears where a writer turns notes into prose. The notes themselves were not checked.

### Blind 3-way judge (`scoring/judge_run1.json`, `judge_run2.json`)

Sonnet judged all three main reports, with labels removed and the reading order reversed between runs. There were 8 dimensions scored 1–5, for a maximum of 40.

| | A | B | C |
|---|---|---|---|
| Run 1 total | 30 | **39** | 30 |
| Run 2 total | 37 | **37** | 29 |
| Picked as best | 0/2 | 2/2 | 0/2 |

- B won on insight, relevance, actionability and readability. Both runs said it was the only report the developer "could build from the text alone".
- C scored highest on groundedness, coverage and gap honesty. It scored lowest on relevance (3), actionability (2) and readability (2). Both judge runs said it is organized around the proposal's Q1–Q5 and hypotheses instead of the user's four questions, and that it leaves the setup steps to a separate file.
- A's score moved 7 points between runs: 30 when read last, 37 when read first. That is a position effect, so treat A's judge score as unstable.
- The judge gave B 4–5 on groundedness. The claim check found B had the most drift, so the judge cannot see this kind of error.

### Post-hoc pairwise: C's full package vs B (`scoring/pairwise_run*.json`)

This round was added after the main results came in, so it is post-hoc. It gave C's README plus `ai-instructions.md` to the judge, compared against B's report, and ran twice with the order swapped.

| | C package | B report |
|---|---|---|
| Answers all 4 | 5, 5 | 4, 5 |
| Actionability | **5, 5** | 3, 3 |
| Readability | 3, 3 | **5, 5** |
| Groundedness | 5, 5 | 4, 4 |
| Gap honesty | 5, 5 | 4, 4 |
| Picked | **2/2** | 0/2 |

Both runs picked C's package. The reason given: it has working templates, a hook script, prompts and a prioritized skip list. B "describes the design but leaves everything to be written". Both runs also said B's report is the better quick overview.

## What each part of the hybrid did

| Hybrid component | Effect seen | Evidence |
|---|---|---|
| **Proposal** (prior, disconfirmers, rival hypotheses, sources to chase) | Wider and more critical sourcing. C cited 88 URLs from 36 sites, and its researchers reported evidence against the prior (for example, fresh-context review was not significantly better than same-session review). It also pulled the write-up toward the proposal's structure instead of the user's questions, and lowered relevance and readability scores. | Automated checks; judge comments on C |
| **Repo search rules** | More tool calls, more sources, and kept "(unverified)" markers. A's and C's researchers ran 31–52 calls each, against 19–27 for the skill's. | Cost log; automated checks |
| **Separate writer agent** | Kept the main session clean and produced the most actionable output (C's ai-instructions.md). It also brought in the most claim drift (B and C), and C's writer produced a very long README. | Claim check; pairwise judge |
| **Repo output format** (frontmatter, Known Gaps, Quality Checklist) | Highest gap-honesty scores (A and C). It also made the reports read "like an internal study write-up", which cost readability. | Judge comments |

## Verdict

- **Improvements from the hybrid:**
  - The most usable deliverable for actually doing the work (pairwise, 2/2).
  - The widest and most varied sourcing.
  - Explicit testing of the prior. This surfaced findings that weaken the starting assumptions, which A and B didn't frame as clearly.
- **Decrements from the hybrid:**
  - About 1.5x the tokens and about 2.5x the wall time of the other two.
  - A README twice as long that reads like a lab report, not an answer.
  - More claim drift than the repo default, though not significantly more.
- **Against the prior in PLAN.md:**
  - Partly confirmed: C beat A on question coverage, and with the instructions file it beat B on actionability.
  - Disconfirmed: "B and C beat A on citation accuracy". A, where the main session wrote the report, had the cleanest claims, and the separate writers introduced the drift.
  - Confirmed: B was the cheapest per finished report.
- **Practical recommendation:** keep the hybrid, but change the writer step:
  1. Open the README with a plain answer to the user's own questions, in their words.
  2. Move the prior/disconfirmer audit to the end or an appendix.
  3. Cap the README at about 3,500 words.
  4. Add a faithfulness pass in which a fresh agent re-checks every number and quote in the draft against the notes.
  5. Put a soft cap of about 30 tool calls on researchers.

## Known Gaps

- Single question and single run per method; differences may be noise.
- Judge is Claude Sonnet judging Opus-written reports; no different model family and no human check of the judge.
- Claim checks used a different checker agent per report, so checker strictness varies.
- Arm A's synthesis was written by the coordinator, who had seen B and C researcher summaries and wrote the proposal.
- Scoring-side token cost not attributed per method; arm A synthesis tokens estimated, not measured.

## Quality Checklist

- [x] All factual claims come from this experiment's own measurements (files in `scoring/`)
- [ ] Cross-referenced across 2+ sources (not applicable: single experiment)
- [x] Flagged contradictions (judge groundedness vs claim check)
- [x] Verified surprising results (unblinded only after both judge runs finished; significance tested)
- [x] Noted confidence
- [x] Listed known gaps
- [x] Targeted prompts (shared checker and judge prompt files)
- [x] Within budget

## Sources

This study's evidence is its own data, all in this folder:
- [PLAN.md](PLAN.md): setup written before the runs, plus dated amendments
- `scoring/auto_checks.py`, `scoring/sample_claims.py`: deterministic checks and claim sampling
- `scoring/claim_checker_prompt.md`, `scoring/judge_prompt.md`: shared prompts
- `scoring/auto_checks_all.json`, `scoring/claimcheck_{A,B,C}.json`, `scoring/judge_run{1,2}.json`, `scoring/pairwise_run{1,2}.json`, `scoring/cost_log.tsv`, `scoring/blind_key.json`
- Scoring rubric from [`research-quality-metrics/`](../research-quality-metrics/README.md); search rules from the repo [CLAUDE.md](../CLAUDE.md)
