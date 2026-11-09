---
title: "Research-Quality Metrics — A Framework for Grading Research Output (Including AI-Produced Research)"
date: 2026-06-07
status: complete
confidence: high
confidence_reason: "Anchored on established, widely-adopted appraisal frameworks (GRADE, used by 110+ orgs; AMSTAR 2, the standard SR appraisal tool) and on peer-reviewed generation-faithfulness metrics with reported human-correlation numbers (FActScore <2% automated error; ALCE citation recall/precision Cohen's κ 0.698/0.525; RAGAS faithfulness formula). Calibration scoring rests on standard proper-scoring-rule literature (Brier, ECE, reliability diagrams). The LLM-as-judge reliability bounds and judge-bias catalogue are inherited (cited, not re-derived) from the sibling eval-rubrics study, whose own confidence is high. Lower confidence only on the synthesis step — no single source proposes exactly this composite rubric, so the metric set is a constructed recommendation, not a validated instrument."
completeness: 80
completeness_reason: "Covers the seven quality dimensions, a full proposed metric set with scoring method + thresholds, an item-by-item audit of the existing quality_checklist, the deterministic/judged/human split, groundedness adaptation, calibration scoring, an LLM-judge rubric with reliability caveats, a worked example, and the honest not-auto-gradable section. Missing: empirical validation of the proposed rubric against hand-labeled study scores (no κ measured yet); no built tooling (the deterministic gates are specified, not implemented); calibration loop needs a corpus of resolved predictions to actually compute Brier over."
category: methodology
tier: 3
objective: "Define a metric/rubric framework to grade the quality of research output (human- or AI-produced) — auditing the project's existing per-study quality_checklist against the measurement/evaluation literature, proposing an improved metric set, and specifying HOW to score each metric (deterministic check vs LLM-judge vs human)."
source_count: 14
known_gaps:
  - "The proposed composite rubric is constructed, not empirically validated — no Cohen's κ measured between this rubric's scores and hand-labeled study quality yet."
  - "Deterministic gates (citation-resolves, claim-has-source, source-diversity) are specified but not implemented as tooling; thresholds are reasoned defaults, not tuned."
  - "Calibration scoring needs a corpus of resolved predictions (claims later confirmed/refuted) to compute Brier/ECE over; for a single study, calibration is only checkable at the claim level, not aggregated."
  - "RAGAS answer-relevancy internal formula (reverse-question + cosine) is taken from the sibling study + secondary sources, not re-fetched from primary RAGAS source this run."
  - "No coverage of cost-normalized quality (quality-per-token) beyond a cross-ref to web-search-methodology; a research-grading rubric arguably should include an efficiency axis."
next_steps:
  - "Implement the four deterministic gates as a pre-commit / pipeline script: (a) every markdown citation URL resolves (HTTP 200), (b) every factual paragraph contains >=1 citation, (c) source_count >= tier threshold AND distinct registrable-domain count >= diversity threshold, (d) no duplicate-domain monoculture."
  - "Run the proposed LLM-judge rubric (5 anchored dimensions, swap/critic-defender per the sibling protocol) over 10-20 existing studies; hand-label the same set; compute per-dimension Cohen's κ; flag dimensions with κ<0.4 for revision."
  - "Build a claim-ledger format so calibration is checkable: log each surprising/unverified claim with its stated confidence, then revisit on study revision to mark confirmed/refuted and compute Brier."
  - "Adopt the upgraded 12-item checklist (see Verdict) in the STUDY_TEMPLATE.md frontmatter; keep the 8 current keys as a subset for backward compatibility."
  - "Decide whether to add a quality-per-token efficiency axis, importing the A/B numbers from web-search-methodology."
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

# Research-Quality Metrics — A Framework for Grading Research Output

## Question / Objective

This repo already grades each study with three frontmatter signals: a binary 8-key `quality_checklist`, a `confidence` rating (high/medium/low), and a `completeness` percentage. That scheme was designed by intuition. **This study evaluates it against the measurement and evaluation literature** — research-quality appraisal frameworks (GRADE, AMSTAR 2), generation-faithfulness metrics (FActScore, ALCE, RAGAS), and calibration scoring (Brier/ECE) — then proposes an improved, scoring-method-explicit metric set: which dimensions matter, and for each, whether it is gradable **deterministically**, by **LLM-judge**, or only by **human**.

It is a sibling to [[how-to-research]] (the human methodology) and [[ai-agent-research-methodology]] (the agent methodology), and extends an earlier private study (the LLM-as-judge mechanics) and [[web-search-methodology]] (the quality-vs-cost A/B framing). The judge-bias catalogue and reliability floor are **inherited from the eval-rubrics study and cited, not re-derived.**

---

## 1. What "research quality" decomposes into

Single "is this good research?" scores correlate poorly with reality — the same lesson the eval-rubrics study found for monolithic judging. Established appraisal tools all decompose. GRADE rates certainty across **five downgrade domains** (risk of bias, inconsistency, indirectness, imprecision, publication bias) plus three upgrade domains, producing High/Moderate/Low/Very-Low certainty ([GRADE Working Group](https://www.gradeworkinggroup.org/) — accessed 2026-06-07). AMSTAR 2 decomposes methodological quality into **16 items, 7 of them "critical"** ([AMSTAR 2, Shea et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-06-07). Borrowing from both, plus the generation-faithfulness literature, research quality decomposes into **seven dimensions**:

1. **Accuracy / groundedness** — are the claims true, and supported by the cited sources? (the faithfulness axis)
2. **Coverage / completeness** — does it answer the whole question; are the obvious sub-questions and counter-evidence addressed?
3. **Source quality + diversity** — are sources authoritative, primary where possible, and *independent* of each other?
4. **Calibration** — does stated confidence match actual correctness? (overconfidence is a defect even when accuracy is high)
5. **Reproducibility / traceability** — can a reader re-walk the evidence trail to the same conclusion?
6. **Relevance-to-question** — does the output actually address what was asked, vs. an adjacent easier question?
7. **Honesty about gaps** — are limitations, contradictions, and unverified claims surfaced rather than smoothed over?

These map cleanly onto the repo's existing signals but expose what those signals *miss* (see §2).

---

## 2. Proposed metric set (and audit of the existing `quality_checklist`)

The current checklist is eight binary self-assertions. Binary, self-asserted, and unverified is the weakest possible measurement: it captures intent, not the artifact. The literature offers stronger, often *deterministic or claim-level*, measures. The table below gives the proposed metric set; **scored-how** is the central contribution.

| Metric | Definition | Scored how | Threshold / target |
|---|---|---|---|
| **Citation resolves** | Every citation URL returns HTTP 200 (no dead/hallucinated links) | **Deterministic** (HTTP check) | 100% — hard gate |
| **Claim-has-source** | Every factual paragraph carries ≥1 citation | **Deterministic** (regex: factual para w/o `](http`) → flag) | 100% of factual paras — hard gate |
| **Source count** | Number of distinct fetched sources | **Deterministic** (count) | ≥ tier floor (T1≥3, T2≥8, T3≥14) |
| **Source diversity** | Distinct registrable domains / total sources | **Deterministic** (domain dedup) | ≥0.5; no domain >40% — gate |
| **Source independence** | Sources don't all trace to one origin (wiki forks, syndication, citation-of-citation) | **LLM-judge + human** | judged 1–5; flag monoculture |
| **Claim-level groundedness** | Fraction of atomic claims entailed by their cited source | **LLM-judge (NLI-style)** (FActScore/ALCE-adapted) | ≥0.9 (see §4) |
| **Citation precision/recall** | Recall: cited docs entail the sentence; Precision: each citation is load-bearing | **LLM-judge (NLI)** (ALCE) | recall ≥0.8, precision ≥0.7 |
| **Coverage** | Are the obvious sub-questions + counter-evidence addressed | **LLM-judge** (1–5, anchored) | ≥4 |
| **Insight / synthesis** | Does it integrate sources into non-obvious conclusions, not just summarize | **LLM-judge** (1–5) + **human** | ≥4 (human confirm) |
| **Relevance-to-question** | Output answers the asked question, not an adjacent one | **LLM-judge** (1–5) | ≥4 |
| **Calibration error** | Gap between stated confidence and measured correctness | **Deterministic over a claim ledger** (Brier/ECE) | Brier ≤0.15 (see §5) |
| **Gap honesty** | Limitations/contradictions/unverified items surfaced | **LLM-judge + human** | ≥4 |

**Audit of the existing 8 keys:**

- `sourced_claims` — **good intent, weak measure.** Replace the self-assertion with the deterministic *claim-has-source* gate + the judged *claim-level groundedness* metric. "I cited things" ≠ "the citation supports the claim" — that distinction is exactly what FActScore and ALCE exist to measure.
- `cross_referenced` — **good but unmeasured.** Operationalize as deterministic *source diversity* (domain count) plus judged *source independence*. The current key can't tell apart "3 independent domains" from "3 mirrors of one wiki."
- `flagged_contradictions` — **keep**, maps to *gap honesty*; promote from binary to a judged 1–5.
- `verified_surprising` — **strong and underrated.** This is a calibration practice in disguise: surprising claims are exactly where overconfidence bites. Keep it, and feed it into the calibration ledger (§5).
- `noted_confidence` — **necessary but insufficient.** Stating a confidence is step one; *checking whether it was right* (calibration error) is the missing step. This is the single biggest gap in the current scheme.
- `listed_gaps` — **keep**, maps to *gap honesty*.
- `targeted_prompts` — **process metric, not output metric.** Keep for AI-agent diagnostics but it grades method, not the artifact. Don't let it inflate a quality score.
- `within_budget` — **efficiency, not quality.** Belongs on a separate cost axis (cross-ref [[web-search-methodology]]'s quality-per-token), not mixed into a quality grade.

**What's entirely missing from the current scheme:** citation precision/recall, source independence (vs. mere count), claim-level groundedness, and **calibration error**. These are the four highest-value additions.

---

## 3. The three-tier scoring split: deterministic gates / judged dimensions / human ship

The most important design decision is *not which model judges* but *which dimensions should never go to a judge at all.* AMSTAR 2's architecture is the precedent: it does not average its 16 items into a mean. It **gates** on critical domains — *one* critical flaw caps the review at "Low," *more than one* caps it at "Critically Low," regardless of how well the non-critical items score ([AMSTAR 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-06-07). This is multiplicative gating, and the eval-rubrics study independently reached the same rule ("multiplicative gating on must-pass dimensions"; an earlier private study). Adopt it here.

- **Deterministic gates (cheap, exact, run first — a failure short-circuits the grade):** citation-resolves (no broken/hallucinated links), claim-has-source, source_count ≥ tier floor, source diversity ≥ threshold, no single-domain monoculture. These cost no tokens, can't be gamed by an articulate write-up, and catch the most damaging failure mode — fabricated or unsupported sourcing. A study failing any hard gate is **"Critically Low"** before a judge ever runs. (This mirrors AMSTAR's critical-domain veto and is why the deterministic layer comes first.)
- **LLM-judged dimensions (require interpretation):** claim-level groundedness, citation precision/recall, coverage, insight/synthesis, relevance, gap honesty, source independence. These are anchored 1–5 with the bias-mitigation protocol from §6.
- **Human (final ship):** insight and gap-honesty get a human confirmation before "complete," because the judge's reliability floor (CoBBLEr's ~49.6% human–machine rank overlap, inherited) means a high judge score on a *subjective* dimension is necessary but not sufficient. Human spot-checks also feed the judge-calibration loop.

The split matters because the existing checklist treats all eight keys as equivalent binary self-reports. In reality: half are deterministically checkable (and currently aren't checked), three need a judge, and two genuinely need a human.

---

## 4. Groundedness / faithfulness adapted to research

Generated-text faithfulness metrics transfer directly to grading research, because a research study *is* a long-form generation that claims to be grounded in retrieved sources.

- **FActScore** decomposes a generation into **atomic facts** and computes the **fraction supported by a reliable knowledge source**; its automated estimator reports **<2% error** vs. human judgment ([FActScore, Min et al. 2023](https://arxiv.org/abs/2305.14251) — accessed 2026-06-07). Adapted: decompose a study's claims into atomic units, check each against its *cited* source. The score is the supported fraction — a direct, claim-level replacement for the binary `sourced_claims`.
- **ALCE** defines **citation recall** (the concatenation of cited docs must *entail* the sentence, via an NLI model) and **citation precision** (each citation must be load-bearing — removing it breaks entailment). Reported human agreement: **Cohen's κ 0.698 for recall, 0.525 for precision**; automatic accuracy 85.1% / 77.6% ([ALCE, Gao et al. 2023](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-06-07). This is the precise instrument for the repo's "every claim has a source *that actually supports it*" requirement.
- **RAGAS faithfulness** is the engineering-friendly version: claims in the response / claims supported by context, scored 0–1 ([RAGAS metrics](https://redis.io/blog/get-better-rag-responses-with-ragas/) — accessed 2026-06-07). Its **answer-relevancy** uses reverse-question-generation (generate questions from the answer, measure similarity back to the original question) — a cheap reference-free relevance check (per an earlier private study).

**Caveat (cross-domain):** these metrics check *consistency with the cited source*, not *truth*. A study perfectly faithful to a wrong wiki scores high on groundedness and is still wrong. Groundedness gates hallucination; it does not gate source error — that's what source-quality and human review are for.

---

## 5. Calibration scoring — does stated confidence match correctness?

This is the dimension the current scheme names (`noted_confidence`) but never checks. Stating "confidence: high" is worthless unless high-confidence claims are in fact usually right. The standard instruments:

- **Brier score** — mean squared error between stated probability and outcome (0=perfect, 1=worst; good ≈0.1–0.2). A **proper scoring rule** — it can't be gamed by hedging ([Brier/reliability, StatsTest](https://www.statstest.com/calibration-checks-brier-score-reliability-diagrams) — accessed 2026-06-07).
- **Expected Calibration Error (ECE)** — bin predictions by stated confidence, measure the gap between confidence and accuracy per bin, average. ECE 0.10 ≈ "off by 10% on average." Not a proper scoring rule (binning artifacts), so report alongside Brier, not instead of it ([calibration metrics survey, StatsTest](https://www.statstest.com/calibration-checks-brier-score-reliability-diagrams) — accessed 2026-06-07).
- **Reliability diagram** — plot accuracy vs. stated confidence; the diagonal is perfect calibration.

**Why this matters acutely for AI-produced research:** LLMs are **systematically overconfident** in their verbalized confidence across models, domains, and elicitation strategies, absent explicit calibration ([ConfTuner / verbalized-confidence survey, 2026](https://arxiv.org/pdf/2508.18847) — accessed 2026-06-07). An AI study that says "confidence: high" is, by default, *less* trustworthy than the words suggest. The fix is the same proper-scoring-rule logic (tokenized Brier) used to train calibrated models.

**How to actually check it in this repo:** confidence is per-study and three-valued, so you can't compute Brier from one study. You need a **claim ledger** — log each surprising/unverified claim with its stated confidence; on later revision, mark confirmed/refuted; compute Brier/ECE over the accumulated ledger. Map high/medium/low → 0.9/0.65/0.4 for the math. Over time this tells you whether "high" actually means ~90% right (well-calibrated) or ~60% (overconfident).

---

## 6. LLM-judge rubric for research output

For the judged dimensions, use anchored 1–5 scales with per-level descriptions (Prometheus reached 0.897 Pearson with humans using exactly this; inherited from an earlier private study). Five judged dimensions:

| Dim | 1 | 3 | 5 |
|---|---|---|---|
| **Groundedness** | claims contradict/exceed sources | most supported, some drift | every claim traceable to a cited source |
| **Coverage** | answers a narrower question | main question covered, sub-questions thin | question + sub-questions + counter-evidence |
| **Insight/synthesis** | list of source summaries | some integration | non-obvious conclusions sources don't state alone |
| **Relevance** | answers an adjacent question | mostly on-target | precisely addresses the asked question |
| **Gap honesty** | overclaims, no limits | gaps listed generically | specific gaps, contradictions, unverified items flagged |

**Mandatory reliability caveats (all inherited, cited, not re-derived from an earlier private study):**
- **Decompose, never score "overall quality" monolithically** — per-dimension only.
- **Different model family for the judge than produced the study** — self-enhancement adds 10–25pp spurious favorability.
- **Swap-augmentation** for any pairwise comparison; **length-controlled** scoring (long ≠ good — verbosity bias >90% on weaker judges).
- **Critic + defender + meta-judge** for release-gate; **per-dimension disagreement is the confidence signal** (high variance flags rubric ambiguity).
- **The floor:** CoBBLEr's ~49.6% human–machine rank overlap is inherited and *not eliminable* — hence the human spot-check in §3. Track per-dimension Cohen's κ vs. human; revise any dimension with κ<0.4.

**Calibration loop vs. human spot-check:** run the judge on every study; human-grade a rotating ~15% sample; compute κ; the judge is trusted on a dimension only while its κ holds. This is the calibration loop *for the judge itself*, parallel to §5's calibration loop for the study's confidence claims.

---

## 7. Practical scoring workflow + worked example

**Workflow:**
1. **Deterministic gates** (no tokens). Any hard-gate failure → **Critically Low**, stop.
2. **Groundedness pass** — claim-level FActScore/ALCE-style check; <0.9 → flag, may cap grade.
3. **LLM-judge** the 5 anchored dimensions (different family; decomposed; swap/length-controlled).
4. **Calibration** — append surprising claims to the ledger; recompute Brier when prior claims resolve.
5. **Human ship** — confirm insight + gap-honesty; record spot-check for judge-κ.
6. **Aggregate by gating, not averaging** — any critical dimension <4 caps the overall (AMSTAR/eval-rubrics rule); otherwise weighted mean of judged dims.

**Worked example — a hypothetical "Best budget GPU 2026" study.** Deterministic: 11/12 citations resolve (one 404) → broken-link gate **fails** → grade floored at **Critically Low** until fixed. Suppose the link is fixed. Re-run: source_count 9 (≥T2 floor), but 6 of 9 are the same retailer's domain → diversity 0.44, monoculture >40% → **diversity gate fails**, grade capped at **Low**; action: add independent benchmarks. After adding 4 independent sources: gates pass. Judge: Groundedness 5, Coverage 3 (omits power-draw/availability), Insight 4, Relevance 5, Gap-honesty 2 (claims "definitive" with no limits). Gating rule: Gap-honesty 2 (<4 on a critical dim) caps overall at **Moderate**. Calibration: it rated a benchmark claim "high" that a second source contradicts → logged for the ledger. **Verdict: Moderate, with two concrete fixes (coverage, gap-honesty).** Note how the *deterministic gates caught the two most damaging problems for zero tokens* before any judge ran — the core efficiency argument.

---

## Verdict — recommended research-grading rubric

Replace the flat 8-key binary self-report with a **gated three-layer grade**:

**Layer 1 — Deterministic hard gates (must all pass; any failure = Critically Low):**
1. `citations_resolve` — 100% of URLs return 200.
2. `claims_have_sources` — 100% of factual paragraphs cited.
3. `source_count_meets_tier` — ≥3/8/14 for T1/T2/T3.
4. `source_diversity` — ≥0.5 distinct domains, no domain >40%.

**Layer 2 — Judged dimensions (anchored 1–5; any critical dim <4 caps the grade):**
5. `groundedness` (claim-level, FActScore/ALCE-style) — *critical*.
6. `coverage` — *critical*.
7. `insight_synthesis`.
8. `relevance_to_question` — *critical*.
9. `gap_honesty` — *critical*.

**Layer 3 — Tracked over time (not per-study pass/fail):**
10. `calibration_brier` — over the claim ledger; flag if >0.15.
11. `judge_kappa` — judge vs. human spot-check per dimension; revise if <0.4.
12. `source_independence` — judged + human; flag monoculture.

**Procedure:** run layers in order; gate, don't average; human-confirm insight + gap-honesty before `status: complete`; rotate a ~15% human spot-check to keep the judge honest. Keep the 8 current keys as a backward-compatible subset (they map onto the new metrics; none is *wrong*, several are just unmeasured or self-asserted).

## What can't be reliably auto-graded

- **Truth of well-sourced claims.** Groundedness checks faithfulness to the cited source, not whether the source is right. A study faithful to a wrong source scores high. Only source-quality judgment + human review catch this.
- **Genuine insight / non-obviousness.** Judges reward fluent synthesis; they cannot reliably distinguish a real novel conclusion from a confident-sounding restatement (CoBBLEr floor, inherited). Human confirm required.
- **Whether the *right question* was asked.** Relevance-to-question grades fit to the stated question; it can't tell you the stated question was the wrong one to research.
- **Source independence at depth.** Detecting that "independent" sources all trace to one origin (syndication, citation-of-citation, a single press release) often needs human tracing.
- **Calibration from a single artifact.** Brier/ECE need a corpus of *resolved* predictions; one study only supports claim-level confidence annotation, not an aggregate calibration score.

These five are exactly where the human stays in the loop — the rest is automatable, and most of the automatable part (the deterministic gates) is currently not being run at all.

---

## Sources

- [GRADE Working Group — certainty domains & ratings](https://www.gradeworkinggroup.org/) — accessed 2026-06-07
- [Cochrane Handbook Ch.14 — GRADE / Summary of Findings](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14) — accessed 2026-06-07
- [AMSTAR 2 — Shea et al. 2017 (PMC5833365), 16 items / 7 critical / rating algorithm](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-06-07
- [FActScore — Min et al. 2023, arXiv:2305.14251 (atomic facts, <2% error)](https://arxiv.org/abs/2305.14251) — accessed 2026-06-07
- [ALCE — Gao et al. 2023, arXiv:2305.14627 (citation recall/precision, κ 0.698/0.525)](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-06-07
- [RAGAS metrics (faithfulness / answer-relevancy / context precision-recall) — Redis guide](https://redis.io/blog/get-better-rag-responses-with-ragas/) — accessed 2026-06-07
- [RAGAS Nvidia metrics (groundedness 0-2 scaling) — docs.ragas.io](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/) — accessed 2026-06-07
- [Brier score & reliability diagrams — StatsTest](https://www.statstest.com/calibration-checks-brier-score-reliability-diagrams) — accessed 2026-06-07
- [Expected Calibration Error / proper scoring rules — calibration survey, StatsTest](https://www.statstest.com/calibration-checks-brier-score-reliability-diagrams) — accessed 2026-06-07
- [ConfTuner — verbalized confidence overconfidence + tokenized Brier, arXiv:2508.18847](https://arxiv.org/pdf/2508.18847) — accessed 2026-06-07
- [Royal Society Open Science — reproducible-analysis transparency / provenance trace + badge](https://royalsocietypublishing.org/doi/10.1098/rsos.241936) — accessed 2026-06-07
- [Reproducibility badges (ACM/NISO/OSF) — Frontiers in Computer Science survey](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1491823/full) — accessed 2026-06-07

**Inherited (cited, not re-derived):**
- `~/dev/research/web-search-methodology/README.md` — quality-vs-cost A/B framing, quality-per-token.

**Cross-references:** [[how-to-research]] · [[ai-agent-research-methodology]] · an earlier private study · [[web-search-methodology]]

## Quality checklist

- [x] All factual claims sourced (deterministic gates, faithfulness metrics, calibration, AMSTAR/GRADE all cite fetched sources).
- [x] Cross-referenced across 2+ domains per theme (appraisal: GRADE+AMSTAR+Cochrane; faithfulness: FActScore+ALCE+RAGAS; calibration: Brier/ECE+ConfTuner).
- [x] Flagged contradictions (groundedness ≠ truth; ECE not a proper scoring rule; self-asserted vs measured).
- [x] Verified surprising claims (AMSTAR gating algorithm, ALCE κ numbers, FActScore <2%, LLM systematic overconfidence).
- [x] Noted confidence level (high; synthesis step is the lower-confidence part).
- [x] Listed known gaps (rubric unvalidated; gates unimplemented; calibration needs ledger).
- [x] Targeted prompts (specific extraction prompts per fetch).
- [x] Within Tier 3 budget (8 searches + 5 fetches, judge-bias catalogue reused not re-fetched).
