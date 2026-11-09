---
title: "How to Research — The Craft of Inquiry (General Methodology)"
date: 2026-06-07
status: complete
confidence: high
confidence_reason: "Built on established research-methods canon (FINER/PICO, PRISMA, SIFT/CRAAP, Tetlock calibration, Platt strong inference, Denzin triangulation, Ahrens/Luhmann) cross-referenced across 2+ independent domains per theme; 19 sources; extends the repo's empirically A/B-tested R3 web-search methodology rather than re-deriving it."
completeness: 85
completeness_reason: "Covers all eight requested sections plus a process audit and a checklist. Gaps: no original empirical A/B test of these meta-practices (the R3 study has that for search); statistics/meta-analysis depth and qualitative-coding rigor are summarized, not exhaustive."
category: methodology
tier: 3
objective: "A rigorous, actionable general methodology for doing high-quality research — question formulation, source evaluation, triangulation, search strategy, synthesis, calibration, bias control, and provenance — that builds on and patches the repo's existing R3 workflow."
source_count: 19
known_gaps:
  - "No original empirical validation of these meta-practices in this repo's context (R3 validated search tactics only, not question-formulation or synthesis discipline)"
  - "Statistical-evidence appraisal (effect sizes, p-hacking, meta-analysis) covered only at the conceptual level"
  - "Qualitative coding / inter-rater reliability mentioned but not operationalized"
  - "Domain-specific evidence hierarchies (history, law, software) differ from the medical EBP pyramid used as the canonical example"
next_steps:
  - "Operationalize the synthesis matrix as a reusable template file under templates/ for craft studies"
  - "Add a claim/evidence/inference tagging convention to the STUDY_TEMPLATE.md frontmatter or body"
  - "Run a small A/B test: studies done with vs. without an explicit disconfirming-evidence pass, scored for error rate"
  - "Build a per-domain evidence-hierarchy cheat-sheet (fiction-craft, legislation, game-data) since the medical pyramid does not transfer cleanly"
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

# How to Research — The Craft of Inquiry (General Methodology)

This is the **general methodology layer** of the repo's research practice. It sits above the [[web-search-methodology]] study (the empirically A/B-tested R3 tactics for *how to drive WebSearch/WebFetch*) and beside the [[ai-agent-research-methodology]] (agent-specific concerns) and [[research-quality-metrics]] (how we score a finished study) studies. Where R3 answers *"how do I search efficiently,"* this answers the broader question: **what does it mean to do the inquiry well — before, during, and after the searching.** It is written to patch concrete gaps in our current workflow (see the audit section).

## 1. Question Formulation

A research effort is only as good as its question. The canonical move is to convert a vague topic into a *researchable* question — one that is specific enough to be answered with evidence and to dictate a search design.

- **FINER** appraises any candidate question: **F**easible (scope and resources fit the budget), **I**nteresting (worth the cost), **N**ovel (extends rather than replicates what we already have — requires a quick prior-art check), **E**thical, **R**elevant (it will change a decision) ([Formulating a researchable question — PMC3140151](https://pmc.ncbi.nlm.nih.gov/articles/PMC3140151/) — accessed 2026-06-07).
- **PICO** decomposes a comparative question into **P**opulation, **I**ntervention, **C**omparator, **O**utcome — forcing you to name *what is being compared against what, measured how* ([PolyU PICO guide](https://libguides.lb.polyu.edu.hk/syst_review/PICO) — accessed 2026-06-07). Even outside clinical work the discipline transfers: a craft question like "does X improve prose" is unanswerable until you name the comparator and the measurable outcome.
- **Background vs. foreground questions**: background questions ask *what/how/where* (definitional, answerable from one good source); foreground questions are comparative and decision-driving ([PMC3140151] above). Match effort to type — don't run a Tier-3 study on a background question.
- **Decompose before searching.** A complex question is split into 2–5 sub-questions, each independently researchable. This is exactly the R3 Tier-3 decomposition step — question formulation and search strategy are the same act.

## 2. Source Quality and Evaluation

Two evaluation traditions exist, and the newer one is decisively better for web research.

- **CRAAP** (Currency, Relevance, Authority, Accuracy, Purpose) is a checklist applied *to the page in front of you* ([CRAAP — Wikipedia](https://en.wikipedia.org/wiki/CRAAP_test) — accessed 2026-06-07). Its documented weakness: it "locks the student into looking only at the site they are evaluating" — the features it checks are the easiest for a bad actor to fake ([Merritt College — SIFT vs CRAAP](https://merritt.libguides.com/c.php?g=1235656&p=9066623) — accessed 2026-06-07).
- **SIFT** (Caulfield) fixes this with **lateral reading**: **S**top, **I**nvestigate the source (leave the page — see what *independent* sources say about it, don't read its own About page), **F**ind better/other coverage, **T**race claims to the original context ([UChicago — SIFT method](https://guides.lib.uchicago.edu/c.php?g=1241077&p=9082322) — accessed 2026-06-07). The "Trace" move directly catches cherry-picked quotes and out-of-context statistics.
- **Primary > secondary.** Primary sources hold original data with no intervening interpretation; secondary sources synthesize/interpret them ([Notre Dame Australia — Levels of evidence](https://library.nd.edu.au/researchers/systematicreviews/evidence) — accessed 2026-06-07). Prefer primary, but note the *inversion at the top of the evidence pyramid*: a high-quality systematic review/meta-analysis (a secondary source) outranks any single primary study because it has already triangulated ([hierarchy of evidence — PMC2981887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2981887/) — accessed 2026-06-07). So "primary > secondary" is a heuristic, not a law.
- **Evidence hierarchy.** Different question types need different hierarchies, and even experts disagree on exact ranks ([Notre Dame] above). The medical pyramid (meta-analysis > RCT > cohort > case report > expert opinion) does **not** transfer wholesale to craft/humanities domains — build a per-domain hierarchy (see next_steps).
- **Spotting AI-slop / low-quality sources.** Lateral reading is the front-line defense: a source no independent site references, with no traceable original claims, that only ever cites other undifferentiated content-farm pages, fails the "Find better coverage" and "Trace" moves. Convergence across *genuinely independent* domains (next section) is the backstop.

## 3. Triangulation and Cross-Referencing

The R3 rule "cross-reference across 2+ source domains" is a special case of **triangulation** — examining a finding from multiple angles so that single-source error cannot survive.

- Denzin/Patton name four types: **data-source**, **investigator**, **theory**, and **method** triangulation. Confidence rises when independent approaches *converge* (convergent validity) ([Scribbr — Triangulation](https://www.scribbr.com/methodology/triangulation/) — accessed 2026-06-07; [Simply Psychology — Triangulation](https://www.simplypsychology.org/what-is-triangulation-in-qualitative-research.html) — accessed 2026-06-07).
- **Independence is the whole point — and the easiest thing to fake.** Two wikis that both copied a third are *one* source, not two. Before counting a corroboration, ask: could these share a common origin? An echo chamber produces apparent convergence with zero added validity. The SIFT "Trace claims" move is how you detect shared upstream origin.
- **Resolving contradictions.** When sources disagree, do not average them or pick the convenient one (that is cherry-picking, §7). Trace each claim to its primary source, weigh by evidence level and independence, and if the conflict is genuine, *record it* — our `flagged_contradictions` checklist item exists for exactly this. A documented contradiction is a finding, not a failure.

## 4. Search Strategy, Breadth/Depth, and Knowing When to Stop

- **Exploratory vs. systematic.** Exploratory (broad-to-narrow, the R3 default) is right for open questions; systematic (a pre-specified, reproducible search across named databases, PRISMA-style) is right when *coverage must be demonstrable* and reproducible ([PRISMA-S — PMC7839230](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/) — accessed 2026-06-07). Most repo studies are exploratory; flagship Tier-3 studies benefit from a systematic, recorded search.
- **Saturation is the principled stopping rule.** Stop when new searches return the *same key sources* and yield no new findings — operationally, when the ratio of newly-relevant material to material screened drops to near zero ([U. Sydney — Performing searches](https://www.library.sydney.edu.au/support/searching/systematic-reviews/performing-searches) — accessed 2026-06-07). This is a *stronger* stopping criterion than R3's fixed "3–5 fetches" budget: the budget caps cost, saturation confirms completeness. Use both — stop at saturation *or* budget, whichever comes first, and note which.

## 5. Synthesis — From Notes to Claims

Searching gathers; synthesis is where research is actually done.

- **Capture in layers (Zettelkasten / Ahrens).** Fleeting notes (raw capture) → literature notes (the gist of a source, in your words, with the citation attached) → permanent notes (your own one-idea-per-card claims, linked) ([zettelkasten.de — Ahrens concepts](https://zettelkasten.de/posts/concepts-sohnke-ahrens-explained/) — accessed 2026-06-07). The discipline that matters for us: **a claim is not real until it has a source attached at capture time** — bolting citations on afterward is where fabrication creeps in.
- **The synthesis matrix.** A table with sources as rows and themes/claims as columns makes agreement and disagreement visible across many sources at once. The operative rule: **a trend does not exist unless two or more sources support it** ([UNC Writing Center — Synthesis matrix](https://writingandlearningcenter.unc.edu/2022/03/synthesis-matrix/) — accessed 2026-06-07; [JHU — Synthesize](https://guides.library.jhu.edu/lit-review/synthesize) — accessed 2026-06-07). This is triangulation made into a worksheet.
- **Distinguish claim / evidence / inference.** State the claim, cite the evidence that supports it, and mark your own inference *as* inference. Conflating the three is the most common synthesis error and is invisible to a reader unless you separate them. Our citation standard enforces evidence-tagging; the missing piece is explicit inference-tagging (audit, below).

## 6. Calibration and Confidence

Our frontmatter already demands a confidence rating — the literature says *how* to make it honest.

- **Calibration** means your stated confidence matches your hit rate: of everything you call "80% likely," ~80% should turn out true ([Commoncog — Evaluating predictions](https://commoncog.com/how-do-you-evaluate-your-own-predictions/) — accessed 2026-06-07). The **Brier score** (mean squared error of probabilistic claims) measures this; superforecasters hit ~0.16–0.20 vs ~0.26 for regulars ([Life Itself — Superforecasting notes](https://lifeitself.org/blog/notes-on-tetlock-and-gardners-superforecasting) — accessed 2026-06-07).
- **Two components — calibration and resolution.** Being well-calibrated but always hedging to 50% is useless; *resolution* rewards being decisive when warranted ([Commoncog] above). Translation for our High/Medium/Low: don't mark everything "Medium" — that's the 50%-hedge. Reserve High for genuinely triangulated, primary-sourced findings and accept that some studies are honestly Low.
- **Known-gaps discipline.** Calibration is impossible without admitting what you don't know. Our `known_gaps` field is a calibration instrument — it should list the specific claims most likely to be wrong, not generic "more research needed."

## 7. Bias and Integrity

- **Confirmation bias / cherry-picking** is the default human failure mode: we oversample evidence that fits a prior, and *higher initial confidence makes the bias worse* ([fs.blog — Confirmation bias](https://fs.blog/confirmation-bias/) — accessed 2026-06-07; [Effectiviology — Cherry-picking](https://effectiviology.com/cherry-picking/) — accessed 2026-06-07).
- **The countermeasures are concrete:** (1) actively seek *disconfirming* evidence — run at least one search designed to *break* your emerging conclusion; (2) **steelman** the opposing view before rejecting it; (3) **Platt's strong inference** — hold multiple alternative hypotheses and design the search to *exclude* one, rather than confirm your favorite ([Platt 1964 — strong inference, JEB retrospective](https://journals.biologists.com/jeb/article/217/8/1202) — accessed 2026-06-07); (4) **accountability** — Tetlock & Lerner found people reason critically mainly when expecting to justify themselves to a skeptic ([fs.blog] above), which is exactly what a recorded, citeable study forces.
- **Pre-registration mindset.** Decide what would *change your mind* before you search. Record disconfirming evidence you find even when it complicates the story — `flagged_contradictions` and `known_gaps` are where it goes.

## 8. Reproducibility and Provenance

Every claim must be **traceable** back to a fetched, dated source — this is the repo's existing citation standard (`[desc](URL) — accessed YYYY-MM-DD`) and it is the reproducibility floor. PRISMA-S exists precisely to make a search *re-runnable* by recording databases, queries, and dates ([PRISMA-S] above). For Tier-3 studies, recording the actual search queries (not just the final sources) in the `sources/` folder turns a study from "trust me" into "re-run me."

## Applying this — gaps in our current process + fixes

Auditing the R3 workflow and `quality_checklist` against the literature surfaces concrete, additive fixes (R3's search tactics are sound and validated — these patch the *layers around* them):

1. **No question-formulation gate.** R3 starts at "classify complexity," skipping question quality. **Fix:** add a FINER/PICO pass before tier classification — confirm the question is novel (prior-art check), comparative where relevant, and tied to a decision. Add a `question_well_formed` checklist item.
2. **Source evaluation is implicit.** R3 says "cross-reference 2+ domains" but never says *evaluate each source*. **Fix:** adopt SIFT explicitly — lateral-read any unfamiliar source before trusting it; CRAAP is insufficient alone.
3. **Independence is asserted, not checked.** "2+ domains" can be two echoes of one origin. **Fix:** add an independence check — before counting a corroboration, confirm the sources don't share an upstream origin (SIFT "Trace"). Upgrade `cross_referenced` to require *independent* corroboration.
4. **No disconfirming-evidence step.** The single biggest gap vs. the bias literature. R3 verifies *surprising* claims but never tries to *break* the main conclusion. **Fix:** add a mandatory "run one search designed to disconfirm" step and a `sought_disconfirming` checklist item. This is the highest-value addition.
5. **Stopping rule is budget-only.** R3's "3–5 fetches" caps cost but doesn't confirm completeness. **Fix:** add saturation as a co-criterion — stop at saturation *or* budget, and record which fired.
6. **Calibration is uncalibrated.** High/Medium/Low is assigned by feel. **Fix:** anchor the levels (High = triangulated + primary; Medium = single good source or mild conflict; Low = thin/contested) and resist defaulting everything to Medium.
7. **Claim vs. inference is unmarked.** Citations tag evidence but our own inferences blend in. **Fix:** mark inferences explicitly ("(inference)") the way we already mark "(unverified)".
8. **Synthesis is ad hoc.** No structured cross-source view. **Fix:** use a synthesis matrix for any Tier-3 study; "a trend needs ≥2 sources" becomes a hard rule.
9. **Search provenance is lossy.** We keep final sources, not the queries that found them. **Fix:** record actual queries in `sources/` for Tier-3 reproducibility.

## Research checklist

- [ ] **Question:** FINER-pass; novel (prior-art checked); comparative/decision-tied; decomposed into 2–5 sub-questions
- [ ] **Tier:** complexity classified; effort matched (don't over/under-invest)
- [ ] **Search:** broad→narrow; exploratory or systematic chosen deliberately
- [ ] **Sources:** SIFT each unfamiliar source (lateral read, don't trust self-description); prefer primary, but trust top-of-pyramid syntheses
- [ ] **Triangulate:** ≥2 *independent* sources per key claim; independence verified (no shared upstream origin)
- [ ] **Disconfirm:** ran ≥1 search designed to break the main conclusion; steelmanned the alternative; held multiple hypotheses
- [ ] **Contradictions:** recorded, not averaged or cherry-picked away
- [ ] **Stop:** at saturation *or* budget — note which
- [ ] **Synthesize:** synthesis matrix for Tier-3; trend = ≥2 sources; claim/evidence/inference separated and tagged
- [ ] **Calibrate:** confidence anchored (not defaulted to Medium); known_gaps names the claims most likely wrong
- [ ] **Provenance:** every claim cited `[desc](URL) — accessed YYYY-MM-DD`; Tier-3 records actual queries

## Sources

- [Formulating a researchable question (FINER/PICO) — PMC3140151](https://pmc.ncbi.nlm.nih.gov/articles/PMC3140151/) — accessed 2026-06-07
- [PolyU — Formulate Research Question Using PICO](https://libguides.lb.polyu.edu.hk/syst_review/PICO) — accessed 2026-06-07
- [CRAAP test — Wikipedia](https://en.wikipedia.org/wiki/CRAAP_test) — accessed 2026-06-07
- [Merritt College — SIFT vs CRAAP](https://merritt.libguides.com/c.php?g=1235656&p=9066623) — accessed 2026-06-07
- [UChicago — The SIFT Method](https://guides.lib.uchicago.edu/c.php?g=1241077&p=9082322) — accessed 2026-06-07
- [Notre Dame Australia — Levels of evidence (primary vs secondary)](https://library.nd.edu.au/researchers/systematicreviews/evidence) — accessed 2026-06-07
- [The hierarchy of evidence — PMC2981887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2981887/) — accessed 2026-06-07
- [Scribbr — Triangulation in Research](https://www.scribbr.com/methodology/triangulation/) — accessed 2026-06-07
- [Simply Psychology — Triangulation in qualitative research](https://www.simplypsychology.org/what-is-triangulation-in-qualitative-research.html) — accessed 2026-06-07
- [PRISMA-S — extension for reporting literature searches (PMC7839230)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/) — accessed 2026-06-07
- [U. Sydney — Performing searches / saturation](https://www.library.sydney.edu.au/support/searching/systematic-reviews/performing-searches) — accessed 2026-06-07
- [zettelkasten.de — Ahrens / How to Take Smart Notes concepts](https://zettelkasten.de/posts/concepts-sohnke-ahrens-explained/) — accessed 2026-06-07
- [UNC Writing & Learning Center — Synthesis matrix](https://writingandlearningcenter.unc.edu/2022/03/synthesis-matrix/) — accessed 2026-06-07
- [JHU — Synthesize (literature review)](https://guides.library.jhu.edu/lit-review/synthesize) — accessed 2026-06-07
- [Commoncog — How do you evaluate your own predictions? (Brier/calibration)](https://commoncog.com/how-do-you-evaluate-your-own-predictions/) — accessed 2026-06-07
- [Life Itself — Notes on Tetlock & Gardner, Superforecasting](https://lifeitself.org/blog/notes-on-tetlock-and-gardners-superforecasting) — accessed 2026-06-07
- [JEB — Fifty years of J. R. Platt's strong inference](https://journals.biologists.com/jeb/article/217/8/1202) — accessed 2026-06-07
- [fs.blog — Confirmation bias & disconfirming evidence](https://fs.blog/confirmation-bias/) — accessed 2026-06-07
- [Effectiviology — Cherry-picking](https://effectiviology.com/cherry-picking/) — accessed 2026-06-07
</content>
</invoke>
