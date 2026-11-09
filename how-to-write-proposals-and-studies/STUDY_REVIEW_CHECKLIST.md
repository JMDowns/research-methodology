# Study Review Checklist (pre-publish pass)

Run this against any study `README.md` before marking it `status: complete`.
Grounded in `how-to-write-proposals-and-studies/README.md` (Pillar 2). Complements
`templates/STUDY_TEMPLATE.md` (the frontmatter schema), [[how-to-research]]
(the inquiry), and [[research-quality-metrics]] (the scoring rubric).

## 1. Structure & reporting
- [ ] Standard skeleton; sections are where a reader expects them (frontmatter → findings → sources).
- [ ] `summary` / `why` / `blockers` are present and **stand alone** (a reader decides relevance from these without opening the body — the roadmap viewer surfaces them).
- [ ] `objective` states the question the study answers.
- [ ] Method, results, and interpretation are separable — synthesis/inference isn't smuggled in as evidence.
- [ ] Conclusion is **up front (BLUF)**, not buried under the evidence trail.

## 2. Completeness
- [ ] `quality_checklist` reflects reality (not all `true` by reflex).
- [ ] Nothing load-bearing is left implicit.
- [ ] `known_gaps` names the **specific claims most likely to be wrong**, not generic "more research needed," and matches the gaps in the body.

## 3. Reproducibility & provenance
- [ ] The method/queries are recorded enough that someone could **re-run** it (Tier-3: actual search queries in `sources/`).
- [ ] Every citation carries an access date (`— accessed YYYY-MM-DD`); volatile sources ideally snapshotted.
- [ ] Frontmatter is machine-parseable (the viewer/roadmap depend on it).

## 4. Actionability
- [ ] Findings are framed as **decisions enabled**, not a fact pile.
- [ ] Where applicable, findings are converted into an **operational artifact** (`presets.yaml`, anti-pattern table, diagnostic checklist, schema).
- [ ] Content is atomic, concept-oriented, and `[[linked]]` to related studies so it gets reused.

## 5. AI-author guards (we are LLM-authored — do not skip)
- [ ] **Every citation resolves AND supports its *specific* claim** — not just that the URL loads (up to ~57% of RAG citations are post-rationalized; verify the source actually backs the sentence).
- [ ] **High citation count is treated as a risk flag**, not a quality signal (deep-research agents hallucinate citations *more*, not less).
- [ ] **No gaps filled from model memory** — anything not from a fetched source is marked "(unverified)" / "(inference)".
- [ ] **Sycophancy countered** — the study tests, not just confirms, the hypothesis implied by the task; disconfirming evidence is stated, contradictions flagged.
- [ ] An explicit **citation-verification pass** was run before finalizing.

## 6. Calibration
- [ ] Confidence is anchored to **evidence strength** (source count, cross-domain agreement), not the model's felt certainty (LLMs run 20–60 points overconfident).
- [ ] No **false precision** / overprecision in numbers or claims.
- [ ] `confidence` is not reflexively "Medium" — High is reserved for triangulated + primary-sourced; Low is honest when the evidence is thin.
- [ ] Any single-source or surprising claim is flagged and, where it matters, independently corroborated.
