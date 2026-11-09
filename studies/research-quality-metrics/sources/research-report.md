# Research-Quality Metrics — Source Synthesis Note

Raw synthesis backing `../README.md`. Tier-3 meta-research, dated 2026-06-07. The judge-bias catalogue and LLM-as-judge reliability bounds are **inherited** from the sibling study an earlier private study and cited, not re-fetched, this run.

## Theme 1 — Research-quality appraisal frameworks (the "gate, don't average" precedent)

- **GRADE** (Grading of Recommendations, Assessment, Development and Evaluations): adopted by 110+ orgs (Cochrane, WHO, NICE). Rates certainty across **5 downgrade domains** (risk of bias, inconsistency, indirectness, imprecision, publication bias) + 3 upgrade domains → High/Moderate/Low/Very-Low. Key import: **decomposed, named domains**, not a single quality number.
- **AMSTAR 2** (Shea et al. 2017): the standard systematic-review appraisal tool. **16 items, 7 critical.** Critical-domain *gating* algorithm (verbatim): no/one non-critical weakness → **High**; >1 non-critical → **Moderate**; **one critical flaw → Low**; **>1 critical flaw → Critically Low**. The 7 critical domains: protocol registration (2), literature-search adequacy (4), exclusion justification (7), risk-of-bias assessment (9), meta-analytic method (11), bias interpretation (13), publication-bias assessment (15). This is the strongest external precedent for the README's **multiplicative gating on must-pass dimensions** — and it independently matches the eval-rubrics study's gating rule.

## Theme 2 — Generation-faithfulness / groundedness (claim-level accuracy)

- **FActScore** (Min et al. 2023, EMNLP): decompose generation into **atomic facts**, score = **fraction supported by a reliable knowledge source**. Automated estimator **<2% error** vs human. Pipeline: atomic-fact generation → evidence retrieval → fact validation → score. ChatGPT scored 58% on biography generation (i.e. ~42% of atomic facts unsupported) — illustrates why binary "is it factual" is inadequate for long-form.
- **ALCE** (Gao et al. 2023): first benchmark for citation evaluation. Three dims: fluency (MAUVE), correctness (dataset-specific), citation quality. **Citation recall** = NLI-entailment of the sentence by the concatenation of its cited docs. **Citation precision** = each citation is load-bearing (removing it breaks entailment). Human agreement: **κ 0.698 recall (85.1% auto acc), 0.525 precision (77.6%)**. Built on the AIS ("attributable to identified sources") concept. This is the precise instrument for "every claim has a source that actually supports it."
- **RAGAS**: engineering-friendly. Faithfulness = supported-claims / total-claims (0–1). Answer-relevancy = reverse-question-generation + cosine back to the query. Context precision/recall measure retrieval. Nvidia-integrated variants score groundedness/relevance on 0–2 then normalize.
- **Cross-domain contradiction flagged:** all three check *faithfulness to cited source*, NOT *truth*. A study faithful to a wrong source scores high. Groundedness gates hallucination, not source error.

## Theme 3 — Calibration scoring (does confidence match correctness)

- **Brier score**: mean squared error between stated probability and outcome; 0 perfect, 1 worst; good ≈0.1–0.2. **Proper scoring rule** (can't be gamed by hedging).
- **ECE** (Expected Calibration Error): bin by confidence, average |confidence − accuracy| per bin. ECE 0.10 ≈ off by 10%. **Not** a proper scoring rule (binning artifacts, trivial optima) — report alongside Brier, not instead.
- **Reliability diagram**: accuracy vs confidence; diagonal = perfect.
- **LLMs are systematically overconfident** in verbalized confidence across models/domains/elicitation absent explicit calibration (ConfTuner 2026). Fix = proper scoring rule (tokenized Brier) in training. Direct implication: an AI study's "confidence: high" is, by default, overstated.
- **Repo application:** per-study 3-valued confidence can't yield Brier alone; need a **claim ledger** (log surprising/unverified claims + stated confidence; resolve on revision; map high/med/low → 0.9/0.65/0.4; compute Brier/ECE over the corpus).

## Theme 4 — Reproducibility / traceability

- Reproducibility **badges** (ACM/NISO/OSF) — visual artifact-level certification; data-sharing mandates raised data availability.
- **Provenance / full trace** (Royal Society Open Science 241936): share the whole analysis trace so steps can be re-executed; "certificate of reproducibility" = full trace + badge + DOI. Repo analogue: the `sources/` raw-material requirement + citation trail = the traceability layer; deterministic citation-resolves gate is its minimal automated check.

## Theme 5 — LLM-as-judge for research output (INHERITED — cited, not re-derived)

From an earlier private study: decompose (Prometheus 0.897 Pearson w/ humans on 1–5 anchored); per-level descriptions; different model family (self-enhancement +10–25pp); swap-augmentation (position bias: GPT-4 65% / Claude-v1 24% consistency); length-control (verbosity bias >90% weaker judges); critic+defender+meta-judge; **CoBBLEr ~49.6% human–machine rank overlap = reliability floor (not eliminable)**; track per-dimension Cohen's κ, revise if <0.4.

## Synthesis → the recommended rubric

Three layers: (1) **deterministic hard gates** (citations resolve, claims sourced, source count ≥ tier floor, diversity ≥0.5/no domain >40%) — any failure = Critically Low, zero tokens, catches the most damaging failures first; (2) **judged 1–5 anchored dims** (groundedness, coverage, insight, relevance, gap-honesty) with AMSTAR-style critical-dim gating, not averaging; (3) **tracked over time** (calibration Brier over a claim ledger, judge-κ vs human spot-check, source independence). Audit verdict on the existing 8-key checklist: `verified_surprising` is underrated (a calibration practice); `noted_confidence` is necessary-but-insufficient (states confidence, never checks it — biggest gap); `sourced_claims`/`cross_referenced` are good intent but self-asserted where deterministic checks exist; `within_budget`/`targeted_prompts` are cost/process axes, not quality. Missing entirely: citation precision/recall, source independence, claim-level groundedness, calibration error.

**Not auto-gradable:** truth of well-sourced claims; genuine insight; whether the right question was asked; deep source independence; calibration from a single artifact.

## Deduplicated source list

| # | Source | Theme | Used for |
|---|--------|-------|----------|
| 1 | GRADE Working Group (gradeworkinggroup.org) | appraisal | 5+3 domains, 4-level certainty |
| 2 | Cochrane Handbook Ch.14 | appraisal | GRADE / summary-of-findings |
| 3 | AMSTAR 2 — Shea et al. 2017 (PMC5833365) | appraisal | 16 items/7 critical/gating algorithm |
| 4 | FActScore — arXiv:2305.14251 | faithfulness | atomic facts, <2% error |
| 5 | ALCE — arXiv:2305.14627 (ar5iv) | faithfulness | citation recall/precision, κ 0.698/0.525 |
| 6 | RAGAS — Redis guide | faithfulness | faithfulness/relevancy/context formulas |
| 7 | RAGAS — docs.ragas.io Nvidia metrics | faithfulness | groundedness 0-2 scaling |
| 8 | Brier/reliability — StatsTest | calibration | Brier, ECE, reliability diagram |
| 9 | ConfTuner — arXiv:2508.18847 | calibration | LLM systematic overconfidence, tokenized Brier |
| 10 | Royal Society Open Science 241936 | reproducibility | provenance trace + certificate |
| 11 | Frontiers Comp Sci reproducibility survey | reproducibility | ACM/NISO/OSF badges |
| 12 | an earlier private study (internal, inherited) | judging | bias catalogue, κ, CoBBLEr floor |
| 13 | web-search-methodology (internal, inherited) | cost framing | quality-per-token |
| 14 | how-to-research / ai-agent-research-methodology (siblings) | context | methodology counterparts |
