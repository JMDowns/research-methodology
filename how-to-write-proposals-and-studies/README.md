---
title: "How to Write Better Research Proposals and Studies (Meta-Methodology)"
date: 2026-06-14
status: complete
confidence: high
confidence_reason: "Built on the canonical proposal frameworks (NIH Specific Aims, NSF merit review, DARPA Heilmeier Catechism — each from a primary source and cross-verified), the de-risking canon (OSF pre-registration, Annie Duke kill criteria, Platt strong inference, Value-of-Information/ISPOR, FINER), product/portfolio prioritization (RICE/ICE/MoSCoW/WSJF, each cross-referenced ≥2 domains), and reporting/reproducibility standards (PRISMA, IMRaD, FAIR, BLUF, evergreen notes). The AI-author failure-mode section rests on 2025–2026 peer-reviewed + arXiv measurements (citation-fabrication rates, RAG faithfulness, sycophancy, overconfidence). Each strand was researched as an independent Tier-2 sweep and triangulated. Lower confidence only on the synthesis-into-a-single-rubric step (constructed recommendation) and on a few practitioner-only frameworks (RAT, atomicity)."
completeness: 85
completeness_reason: "Covers both requested pillars at equal weight (proposal craft + study craft), audits the repo's own proposal corpus against the literature, and ships two operational artifacts (PROPOSAL_TEMPLATE.md + STUDY_REVIEW_CHECKLIST.md). Gaps: no empirical A/B of proposals authored with vs without the new pre-commitment fields; prioritization scoring is recommended, not yet wired into the roadmap viewer; a few sources (ISPOR VoI, PRISMA PMC) were gated and used via snippet + cross-check."
category: methodology
tier: 3
objective: "Produce a literature-grounded, operational methodology for writing better research PROPOSALS (the upstream 'what to research and why' doc) and better STUDIES (the deliverable), tuned to this repo's AI-authored, decision-driven research practice — and patch the concrete gaps in the current proposal house-style."
summary: "A dual-pillar meta-methodology: Pillar 1 (proposal craft) distills NIH/NSF/Heilmeier proposal anatomy + a de-risking layer (pre-registration, riskiest-assumption test, kill criteria, strong inference, value-of-information) + RICE/WSJF prioritization; Pillar 2 (study craft) distills PRISMA/IMRaD reporting, FAIR reproducibility, BLUF actionability, and AI-author failure modes (citation fabrication, sycophancy, overconfidence). Audits our own proposals (already strong on why-now/gap/deliverables/dependencies) and adds 4 missing pre-commitment fields. Ships a proposal template + study-review checklist."
why: "We author a large and growing volume of research proposals off a good-but-unvalidated house style (_STYLE.md). This study grounds that practice, fills its blind spots (kill criteria, success metrics, expected-answer priors, prioritization rigor), and gives a reusable template — raising the floor on every future proposal and study."
blockers: []
source_count: 47
known_gaps:
  - "No empirical A/B: proposals written with vs without the four new pre-commitment fields (kill criterion, success metric, expected answer, VoI/decision) scored for downstream usefulness"
  - "Prioritization (RICE/WSJF) is recommended for the roadmap but not wired into viewer/roadmap.py"
  - "A few primary sources (ISPOR VoI task force, PRISMA PMC full text) could not be read and rest on search snippets"
  - "Practitioner-only frameworks (Riskiest-Assumption Test, RFC 'atomicity') lack peer-reviewed primary anchors"
  - "The pipeline claim-support check judges support from the page vs the citation's DESCRIPTION (a title-ish proxy), not the exact sentence in the README the citation backs — so a real-but-unsupportive citation whose description happens to match the page can still slip through"
next_steps:
  - "Run the A/B in known_gaps once ~10 proposals use the new template + the four pre-commitment fields"
  - "Backfill the four pre-commitment fields into more live proposals beyond the two exemplars (31, 33) as they're next touched"
  - "Consider claim-checking against the specific README sentence (not just the citation description) for a stronger support test"
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

# How to Write Better Research Proposals and Studies (Meta-Methodology)

This study sits in the repo's meta-methodology layer and is scoped to two artifacts we produce constantly: the **research proposal** (the upstream "what to research and why" document that gates a study) and the **study** (the deliverable). It is the missing third leg beside [[how-to-research]] (the *doing* of inquiry — question formulation, sourcing, triangulation, synthesis, bias control), [[research-quality-metrics]] (how to *grade* a finished study), and [[web-search-methodology]] (the empirically A/B-tested R3 *search* tactics). Where those answer "how do I inquire / search / score," this answers **"what makes the proposal worth executing, and what makes the study worth trusting and reusing"** — and it patches concrete blind spots in our current proposal house style.

The two pillars are given **equal weight** per the brief.

---

## The spine (BLUF)

Across every authoritative proposal framework (NIH, NSF, DARPA) the same load-bearing argument recurs, and the de-risking literature adds a second half. A complete proposal answers, in order:

1. **What** — in plain language, no jargon (Heilmeier Q1 / problem statement).
2. **Why now / the gap** — what's known, the precise gap, *tied to a critical need* (NIH para 2). The #1 failure is naming a gap but never the consequence of not closing it.
3. **What's new + why it'll work** — central hypothesis/objective + why your approach beats current practice (Heilmeier Q3 / NSF Intellectual Merit). For us: *why model knowledge can't settle this* — already a signature strength of our proposals.
4. **Aims** — 2–4 **independent, non-contingent**, hypothesis-driven aims, each measurable (NIH para 4 / FINER).
5. **Who cares + payoff** — the decision this changes and the downstream artifact it unblocks (Heilmeier Q4 / NSF Broader Impacts).
6. **De-risking** — the disconfirming result, the riskiest assumption tested first, a pre-committed kill criterion, feasibility/cost/tier.
7. **Success exams** — the predefined mid-term/final tests that say the study *worked* (Heilmeier Q8 / NSF "mechanisms to assess success").

Then **pressure-test against the rejection corpus** (§1.7) and **prioritize** against the rest of the backlog (§1.6).

---

# Pillar 1 — Proposal Craft

## 1.1 The load-bearing logic: three frameworks, one argument

The three canonical frameworks converge on the same skeleton, just emphasized differently:

| Framework | Core demand | Best-fit lens for us |
|---|---|---|
| **NIH Specific Aims** (one page) | Hook → known + **gap tied to a critical need** → central hypothesis/objective/long-term goal → 2–4 aims each with a payoff | The *narrative argument* of a proposal |
| **NSF Merit Review** | Two separate statements: **Intellectual Merit** (advance knowledge) + **Broader Impacts** (benefit), both judged with a **mechanism to assess success** | Separating "advances the pipeline" from "who it helps" |
| **DARPA Heilmeier Catechism** (8 Qs) | Plain-language what; current practice + limits; what's new + why it'll work; who cares; risks; cost; time; **mid-term & final exams** | The *builder's* proposal — best fit for this repo |

The Heilmeier Catechism is the closest match to a builder's research proposal: *"What are you trying to do — articulate your objectives using absolutely no jargon. How is it done today and what are the limits? What's new and why will it succeed? Who cares? What are the risks? How much will it cost? How long? What are the mid-term and final exams to check for success?"* ([DARPA — Heilmeier Catechism](https://www.darpa.mil/about/heilmeier-catechism) — accessed 2026-06-14; verbatim-corroborated [RIT CS736](https://www.cs.rit.edu/~ago/courses/736/heilmeier.html) — accessed 2026-06-14). Q8 — *predefined exams* — is the single item our proposals most consistently omit.

NSF makes both criteria carry a **mechanism to assess outcomes** — "a proposal isn't complete without a way to check it worked" ([NSF — Merit Review](https://www.nsf.gov/funding/merit-review) — accessed 2026-06-14).

## 1.2 The gap must tie to a critical need (the #1 lever)

The NIH Specific Aims page is "an abbreviated version of the full grant" — get it right and the rest follows ([BioscienceWriters — Anatomy of a Specific Aims page](https://www.biosciencewriters.com/NIH-Grant-Applications-The-Anatomy-of-a-Specific-Aims-Page.aspx) — accessed 2026-06-14; [Granted AI — NIH Specific Aims guide](https://grantedai.com/learn/guides/nih-specific-aims-guide) — accessed 2026-06-14). Its second paragraph names what's known, then *the gap*, then — the move most proposals skip — **connects the gap to the consequence of not closing it**. "We don't know X" is weak; "we can't do Y until we know X, and Y is blocked right now" is strong. This is the inverse of the most-cited rejection reason: *failure to convince reviewers of the need* ([UAB CCTS — Top 10 NIH pitfalls](https://www.uab.edu/ccts/news-events/center-news/top10-nih-pitfalls) — accessed 2026-06-14; [GrantCentral — 30 reasons not funded](https://www.grantcentral.com/30-reasons-your-grant-proposal-may-not-have-been-funded/) — accessed 2026-06-14).

**Our proposals already do this well** — the good ones tie a specific gap directly to the downstream step it blocks. Keep that; just make "the decision this unblocks" an explicit field, not prose to be inferred.

## 1.3 Aims: independent, measurable, hypothesis-driven

- **2–4 aims**, each in 2–4 sentences, with its own payoff; each *"valuable, testable, and independent"* ([BioscienceWriters](https://www.biosciencewriters.com/NIH-Grant-Applications-The-Anatomy-of-a-Specific-Aims-Page.aspx) — accessed 2026-06-14).
- **The independence rule (load-bearing, cross-verified across 3 domains):** aims must be thematically related but **experimentally independent — not contingent**. Reviewers distrust a plan where "failure of Aim 1 makes Aim 2 impossible"; structure each to succeed even if others fail ([URMC Rochester — Specific Aims tips](https://www.urmc.rochester.edu/MediaLibraries/URMCMedia/medicine/documents/Tips-for-Writing-Specific-Aims-CEQ.pdf) — accessed 2026-06-14). "Interdependence of aims" is independently listed as a rejection reason ([GrantCentral](https://www.grantcentral.com/30-reasons-your-grant-proposal-may-not-have-been-funded/) — accessed 2026-06-14).
- **Aim ≠ method.** An aim is a question to answer, not a technique to run; use strong active language ("We will determine…"), not hedges ([Granted AI](https://grantedai.com/learn/guides/nih-specific-aims-guide) — accessed 2026-06-14).
- **The vocabulary, disambiguated** ([Farrugia et al. — research questions, hypotheses, objectives, PMC2912019](https://pmc.ncbi.nlm.nih.gov/articles/PMC2912019/) — accessed 2026-06-14): *aim* = broad end purpose; *objective* = measurable step that delivers it (primary drives scope; secondary must "never compromise the primary question"); *question* = what you want to find out; *hypothesis* = a testable prediction, set **prospectively** (forming it after seeing the data is an error — see §1.4 pre-registration).

This maps onto our existing `### Q1/Q2…` clusters; the upgrade is to keep them **independent** (our `00-INDEX` subgenre proposals are a good model) and to attach a **measurable success condition** to each.

## 1.4 De-risking: make the study falsifiable and abandonable *before* you commit

Six lenses on one move — front-load the falsifiable, decision-relevant, abandonable parts:

- **Pre-registration mindset.** Decide, in advance, the hypothesis/prediction *and the result that would disconfirm it* — "the same data cannot be used to generate *and* test a hypothesis." Labeling analyses **confirmatory vs exploratory** up front prevents HARKing and hindsight bias ([COS — choosing a preregistration template](https://www.cos.io/blog/choosing-preregistration-template-guide-for-researchers) — accessed 2026-06-14; [COS — Prereg initiative](https://www.cos.io/initiatives/prereg) — accessed 2026-06-14; [Bekkers — Preregistration: why and how](https://renebekkers.wordpress.com/2023/09/20/preregistration-why-and-how/) — accessed 2026-06-14). **For us:** state an **expected answer / prior** in the proposal, so the study can surprise you rather than confirm the prompt's implied conclusion. This directly counters the LLM-sycophancy failure in §2.4.
- **Riskiest-Assumption Test (RAT).** Identify the one assumption that, if false, makes the whole study pointless (highest impact × uncertainty), and test *that* first, cheaply — invert build-measure-learn into learn-test ([ModelThinkers — RAT](https://modelthinkers.com/mental-model/riskiest-assumption-test) — accessed 2026-06-14; [Apptunix — RAT steps](https://www.apptunix.com/blog/riskiest-assumption-test/) — accessed 2026-06-14). **For us:** if a one-hour scoping search can kill a Tier-3 study, run it before scoping the full thing.
- **Kill criteria (state + date).** Pre-commit: *"If I am (or am not) in [measurable state] at [point], I stop or pivot."* Deciding in advance defeats sunk-cost escalation, and a pre-committed criterion is far more likely to be honored — ideally with an outside checker ([Behavioral Scientist — Annie Duke on cutting losses](https://behavioralscientist.org/annie-duke-quit-mental-models-to-help-you-cut-your-losses/) — accessed 2026-06-14). This generalizes [[how-to-research]]'s "saturation *or* budget" stop rule into the proposal itself.
- **Strong inference / falsifiability.** Frame the question so at least one finding would disconfirm the thesis; list **2–3 rival hypotheses** and design to *exclude*, not confirm, the favorite (Platt's 4 steps; Chamberlin's multiple working hypotheses; Popper) ([Wikipedia — Strong inference](https://en.wikipedia.org/wiki/Strong_inference) — accessed 2026-06-14; [Britannica — falsifiability](https://www.britannica.com/topic/criterion-of-falsifiability) — accessed 2026-06-14). If no result could disconfirm it, it's rhetoric, not research.
- **Value of Information (VoI).** Only research what could change a decision: value ≈ (probability the finding flips the decision) × (cost of being wrong), compared against the study's cost — *if every possible finding leads to the same action, the study has zero VoI; don't run it* ([Springer — Practical Guide to VoI](https://link.springer.com/article/10.1007/s40273-014-0219-x) — accessed 2026-06-14; [PubMed — EVPI example](https://pubmed.ncbi.nlm.nih.gov/19602213/) — accessed 2026-06-14).
- **FINER** as the integrating gate — Feasible, Interesting, Novel (prior-art checked), Ethical, Relevant — already used by name in one of our proposals ([Farrugia et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC2912019/) — accessed 2026-06-14; [Cosmoderma — FINER](https://cosmoderma.org/finer-criteria-what-does-it-mean/) — accessed 2026-06-14).

These four — **expected answer, riskiest assumption, kill criterion, decision-this-feeds** — are exactly what our proposals omit (§1.8 audit). They are the highest-value additions.

## 1.5 Scope, atomicity, and "definition of done"

- **Scope = explicitly what is *and is not* included.** State **in-scope / out-of-scope / non-goals**, and **delimitations with rationale** (the boundaries you *chose* vs limitations you can't control) ([PapersOwl — scope & delimitation](https://papersowl.com/blog/scope-and-delimitations-in-research) — accessed 2026-06-14; [Research.com — scope](https://research.com/tutorials/what-is-scope-in-project-management) — accessed 2026-06-14).
- **Atomicity: one proposal = one decision/deliverable.** RFC/design-doc best practice — keep a proposal atomic, state non-goals, and *skip the heavyweight treatment entirely for small, well-understood, or easily reversible work* ([Pragmatic Engineer — RFCs & design docs](https://blog.pragmaticengineer.com/rfcs-and-design-docs/) — accessed 2026-06-14). Our discovery-vs-design split (`08`/`13a` taxonomy proposals gate `09-*`/`13b-*` per-type ones) already embodies this.
- **Definition of Done** = the specific deliverable artifact + boundary, so completion is unambiguous, and route mid-study additions through a **change gate** rather than silent scope creep ([Asana — scope creep](https://asana.com/resources/what-is-scope-creep) — accessed 2026-06-14).

## 1.6 Prioritization & sequencing (which proposal, in what order)

When the backlog is large (it is), order by value, not narrative:

| Framework | Formula / shape | Use when |
|---|---|---|
| **RICE** | (Reach × Impact × Confidence) ÷ Effort | Impact-per-effort at study granularity; the **Confidence** factor is the natural brake on speculative deep-dives |
| **ICE** | Impact × Confidence × Ease (1–10) | Fast first-pass triage of a big backlog (~30 items in 20 min) |
| **WSJF** | Cost of Delay ÷ Job Size | Time-sensitive or **enabler** work — a taxonomy that unblocks many later studies has high opportunity-enablement and should jump the queue |
| **MoSCoW** | Must / Should / Could / Won't | In-or-out within a fixed deadline; the **"Won't (this time)"** is the underrated anti-creep move |

([Fygurs — prioritization frameworks compared](https://www.fygurs.com/blog/product-prioritization-frameworks-compared) — accessed 2026-06-14; [SAFe — WSJF](https://framework.scaledagile.com/wsjf) — accessed 2026-06-14; [Centercode — RICE vs WSJF](https://www.centercode.com/blog/rice-vs-wsjf-prioritization-framework) — accessed 2026-06-14; [Agile Business Consortium — MoSCoW](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html) — accessed 2026-06-14.)

**Sequencing beats raw score.** Surface dependencies up front ("blocked by" / "blocks"); identify whether a study is on the **critical path** (an enabler with zero float) — if so it goes first regardless of standalone score — and honor **discovery before design** ([Asana — critical path](https://asana.com/resources/critical-path-method) — accessed 2026-06-14; [Mural — dependency mapping](https://www.mural.co/blog/dependency-mapping) — accessed 2026-06-14). After scoring, run a **dependency-override pass**: a high-score item blocked by a low-score prerequisite must yield to it. RICE's Effort denominator and WSJF's job-size both formalize **right-sizing** (match effort to tier; timebox uncertain spikes with a pre-stated success metric) — this is exactly the repo's R3 tiering ([Agile Alliance — sizing spikes](https://agilealliance.org/the-practice-of-sizing-spikes-with-story-points/) — accessed 2026-06-14). Tag each proposal **explore vs exploit** so one mature area can't monopolize the backlog ([Linden Innovation — innovation portfolio](https://lindeninnovation.com/innovation-portfolio-management/) — accessed 2026-06-14).

## 1.7 Why proposals fail (the rejection corpus = the inverse checklist)

Reviewer-side failure modes converge tightly ([UAB CCTS](https://www.uab.edu/ccts/news-events/center-news/top10-nih-pitfalls); [GrantCentral](https://www.grantcentral.com/30-reasons-your-grant-proposal-may-not-have-been-funded/) — both accessed 2026-06-14):

1. **Significance not articulated** — gap stated, critical need never connected *(the single highest-leverage failure)*.
2. **Not novel** — duplicates existing work (for us: a prior-art check against existing studies/proposals).
3. **Diffuse / unfocused** — fails atomicity.
4. **Unrealistic workload** — fails feasibility/right-sizing.
5. **Aims interdependent / irrelevant to the hypothesis.**
6. **No alternatives / no consideration of what could go wrong** — fails the de-risking layer.
7. **Uncertain future directions / outcomes.**
8. **Too complicated to understand** — fails plain-language (Heilmeier Q1).

## 1.8 Audit: our proposal corpus vs the literature

Sampled the house style guide and three proposals. The house style is genuinely strong:

| Element | We do it? | Literature anchor |
|---|---|---|
| Plain-language framing + "why model knowledge isn't enough" | ✅ strong | Heilmeier Q1, Q3 |
| "What triggered this / why now" naming the gated artifact | ✅ strong | NIH gap; significance |
| "What model knowledge can't settle" — gap + risks of guessing | ✅ **signature strength** | Heilmeier Q3; novelty |
| Central question + independent numbered Q-clusters (Q0 = inclusion test/stopping rule) | ✅ strong | aims; scope; saturation |
| FINER/PICO framing | ✅ (resolution-type) | FINER |
| Comparison tables marking "candidate — confirm during research" | ✅ signature | — |
| Concrete deliverables (enum, schema-change, mapping) | ✅ strong | expected outcomes |
| Tier & scope + "does NOT re-research X" | ✅ strong | feasibility; atomicity |
| Blocks / doesn't-block + `[[wikilinks]]` | ✅ strong | dependency hygiene |
| Named source anchors, not "search the web" | ✅ strong | — |
| Time budgets + parallel-subagent count | ✅ | right-sizing |

**Four confirmed gaps** (each maps to a literature lever, none currently in the house style):

| Gap | Fix (new proposal field) | Anchor |
|---|---|---|
| **No kill criterion** — proposals pose open questions but never a pre-committed stop/pivot condition | `Kill / pivot criterion:` state + date | Duke kill criteria; how-to-research saturation |
| **No success "exam"** — deliverables listed, but no acceptance test that says the study *worked* | `Success metric:` per deliverable | Heilmeier Q8; NSF assess-success |
| **No expected-answer / prior** — open questions with no stated prediction to be surprised against | `Expected answer (prior):` + disconfirmer | Pre-registration; anti-sycophancy |
| **Prioritization is qualitative** — `00-INDEX` has "why this priority" prose but no value/effort score or dependency-override | `RICE/WSJF score:` + dependency note | RICE/WSJF; critical path |

These four are folded into `PROPOSAL_TEMPLATE.md`.

---

# Pillar 2 — Study Craft (the deliverable)

This pillar complements (does not duplicate) [[research-quality-metrics]] (scoring) and [[how-to-research]] (inquiry); it focuses on **design, reporting, reproducibility, actionability, and AI-author failure modes**.

## 2.1 Structure & reporting

- **Use a standardized skeleton.** IMRaD-style sectioning means "the reader will expect to find particular things in each part," which is what makes a study fast to evaluate ([Newcastle — IMRaD](https://www.ncl.ac.uk/mediav8/academic-skills-kit/file-downloads/Structuring%20a%20Science%20Report%20IMRaD.pdf); [GMU — IMRaD report](https://writingcenter.gmu.edu/writing-resources/imrad/writing-an-imrad-report) — both accessed 2026-06-14). Our `STUDY_TEMPLATE.md` frontmatter is exactly this skeleton.
- **The summary is a triage device and must stand alone** — readers and indexers "rely heavily on abstracts to decide whether a paper is worth reading" ([GMU — IMRaD abstracts](https://writingcenter.gmu.edu/writing-resources/imrad/abstracts-in-scientific-research-papers-imrad) — accessed 2026-06-14). This validates the mandatory `summary`/`why`/`blockers` frontmatter the roadmap viewer surfaces.
- **A checklist enforces completeness** so nothing load-bearing is left implicit — PRISMA is a 27-item checklist for exactly this reason ([PRISMA 2020](https://www.prisma-statement.org/prisma-2020); statement [PMC8005924](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — both accessed 2026-06-14). Our `quality_checklist` is the analog; keep it honest.

## 2.2 Reproducibility & provenance

- **Record method + queries + sources so the study is *re-runnable*, not just *believable*.** "Incomplete information in methods" and "unreported methods" are top drivers of the reproducibility crisis ([PMC8067906 — reproducibility practices](https://pmc.ncbi.nlm.nih.gov/articles/PMC8067906/); [Wikipedia — replication crisis](https://en.wikipedia.org/wiki/Replication_crisis) — both accessed 2026-06-14). This is why [[how-to-research]] says Tier-3 studies record the actual queries in `sources/`, not just final URLs.
- **Provenance + timestamps**: pages get silently edited or rot, so record access dates (our `— accessed YYYY-MM-DD` standard) and ideally archived snapshots ([ARTS framework, arXiv 2504.08171](https://arxiv.org/html/2504.08171v1) — accessed 2026-06-14).
- **FAIR metadata** — findable/accessible/interoperable/reusable; machine-parseable YAML frontmatter *is* a FAIR-style layer ([FAIR principles — Nature Sci Data](https://www.nature.com/articles/sdata201618); [GO FAIR](https://www.go-fair.org/fair-principles/) — both accessed 2026-06-14).

## 2.3 Actionability — knowledge that gets used

- **Lead with the answer (BLUF).** Put conclusions/recommendations at the *front*, specific and actionable, to prevent the info-dump and "cognitive overload" ([BLUF — Wikipedia](https://en.wikipedia.org/wiki/BLUF_(communication)) — accessed 2026-06-14). (This study's "spine (BLUF)" section above is the pattern.)
- **Frame findings as decisions enabled, not facts collected.** For this repo this is already operationalized: a study counts as ready for use only when its findings become an operational artifact (config presets, anti-pattern tables, diagnostic checklists).
- **Write findings to be reused (evergreen discipline):** atomic (one self-contained idea), concept-oriented (reusable across projects), densely linked ([Evergreen notes — Matuschak](https://notes.andymatuschak.org/Evergreen_notes) — accessed 2026-06-14). The repo's per-topic studies + `[[wikilinks]]` + registries are exactly this.

## 2.4 AI-author failure modes (the section unique to our practice)

Our studies are LLM-authored; these failure modes are measured, recent, and decision-relevant:

- **Citation fabrication is common — and deep-research agents are *worse*.** On DRBench, hallucinated URLs ran 3–13%; **deep-research agents pooled 10.7% vs 4.8%** for plain search-augmented LLMs, *while emitting far more citations* (41–113 vs 3–24 per query). "More citations per query do not mean fewer errors per citation." Earlier work found 55% fabrication for GPT-3.5, 18% for GPT-4 ([Reference hallucinations in LLMs & deep-research agents, arXiv 2604.03173](https://arxiv.org/html/2604.03173v1); [Citation hallucinations — EmergentMind](https://www.emergentmind.com/topics/citation-hallucinations) — both accessed 2026-06-14). **Implication: treat a high citation count as a *risk flag*, not a quality signal.**
- **A citation can resolve and still be wrong.** Three failure types: nonexistent, stale, and **real-but-unsupportive**; and up to **57% of RAG citations are "post-rationalized"** (generated from memory, then a superficially matching source attached after the fact) ([arXiv 2604.03173](https://arxiv.org/html/2604.03173v1) — accessed 2026-06-14). **Verify each source supports its *specific claim*, not just that the URL loads.**
- **Ground every claim in retrieved text; never fill gaps from model memory** — the rationale behind R3's "NEVER state something as fact unless it came from a fetched source"; mitigation is iterative retrieve + NLI-verify until each statement is backed ([Trustworthiness of LLMs in RAG, arXiv 2409.11242](https://arxiv.org/pdf/2409.11242) — accessed 2026-06-14).
- **Sycophancy biases toward confirming the prompt's framing** — LLMs "adopt user assumptions without challenge" at rates far above humans, "entrenching unfounded conclusions" ([Social sycophancy, arXiv 2505.13995](https://arxiv.org/html/2505.13995v1) — accessed 2026-06-14). This is *why* the proposal-side **expected-answer + disconfirmer** field (§1.4) matters: it pre-commits a falsification target the author can't quietly rationalize away.
- **Self-correction works, but needs tool-use competence** — agentic verify-and-fix loops cut broken citations to <1% on capable models, but a weak model "called tools but ignored results." So an explicit **citation-verification pass** should be a required final step ([arXiv 2604.03173](https://arxiv.org/html/2604.03173v1) — accessed 2026-06-14).

## 2.5 Calibration

LLMs are systematically **overconfident** (accuracy-vs-confidence gaps of 20–60 points; beware **overprecision** / false precision) — so a self-reported confidence rating is untrustworthy by default and should be anchored to **evidence strength** (source count, cross-domain agreement), not felt certainty ([Competing biases / overconfidence in LLMs — Nature Machine Intelligence](https://www.nature.com/articles/s42256-026-01217-9); [arXiv 2507.03120](https://arxiv.org/pdf/2507.03120) — both accessed 2026-06-14). Keep an explicit **known-gaps register** naming the claims most likely to be wrong — the dangerous failure is a confident, complete-looking study with silent gaps. This matches [[how-to-research]] §6 ("don't default everything to Medium") and our `confidence_reason`/`completeness_reason` fields.

---

## The Proposal Checklist

- [ ] **What** — one plain-language sentence, no jargon (Heilmeier Q1)
- [ ] **Why now** — gap named *and tied to the decision/artifact it blocks right now* (NIH; the #1 lever)
- [ ] **Why not model knowledge** — what reasoning-from-training can't settle (our signature move)
- [ ] **What's new + why it'll work** vs current practice
- [ ] **Aims** — 2–4, **independent/non-contingent**, hypothesis-driven, each with a payoff
- [ ] **Expected answer (prior) + the result that would disconfirm it** *(new)*
- [ ] **Riskiest assumption**, tested first and cheaply *(new)*
- [ ] **Kill / pivot criterion** — state + date *(new)*
- [ ] **Success metric** — the "exam" per deliverable (Heilmeier Q8) *(new)*
- [ ] **Scope** — in / out / non-goals + delimitations with rationale; atomic (one decision)
- [ ] **Deliverables** — concrete consumable artifacts + Definition of Done
- [ ] **Tier & cost** — effort matched to complexity; timebox if uncertain
- [ ] **Dependencies** — blocked-by / blocks; on the critical path? discovery-before-design?
- [ ] **Priority** — RICE/WSJF score + dependency-override note *(new)*; explore vs exploit
- [ ] **Sources** — named anchors, not "search the web"
- [ ] **Pressure-test** against the rejection corpus (§1.7)

## The Study Checklist

- [ ] **Structure** — standard skeleton; standalone `summary`/`why`/`blockers`; objective stated; method separated from results separated from interpretation
- [ ] **Completeness** — `quality_checklist` honest; nothing load-bearing implicit; known-gaps register names the claims most likely wrong
- [ ] **Reproducibility** — queries + sources + synthesis path recorded; access dates (ideally snapshots); machine-readable frontmatter
- [ ] **Actionability** — conclusion up front (BLUF); findings framed as decisions enabled; converted to an operational artifact; atomic, concept-oriented, `[[linked]]`
- [ ] **AI-author guards** — every citation resolves **and supports its exact claim**; high citation count treated as risk; no memory-filled gaps (mark "(unverified)"/"(inference)"); sycophancy countered by stating disconfirming evidence; ran an explicit citation-verification pass
- [ ] **Calibration** — confidence anchored to evidence not certainty; no false precision; single-source/unverified claims flagged

## Templates & artifacts

- [`PROPOSAL_TEMPLATE.md`](PROPOSAL_TEMPLATE.md) — the proposal skeleton with the four new pre-commitment fields, matching our house style.
- [`STUDY_REVIEW_CHECKLIST.md`](STUDY_REVIEW_CHECKLIST.md) — a pre-publish review pass for any study README (the Study Checklist above, expanded).
- [`PROPOSAL_LEVELS.md`](PROPOSAL_LEVELS.md) — definitions of study vs meta-study vs meta-meta proposals, how to pick one, and the extra sections each level needs (added 2026-11-07).
- Existing: `templates/STUDY_TEMPLATE.md` (study frontmatter), a private house style file (house style this study patches).

## Known gaps & next steps

**Done as of 2026-06-14** (the original follow-ups): the house-style guides
(the private house style files)
now carry the four pre-commitment fields and point at `PROPOSAL_TEMPLATE.md`; the
Research Roadmap parses a `**Priority:** <score> (RICE)` line and orders To-Do work
by it (`viewer/parser.py` + `viewer/roadmap.py`; also fixed: `_STYLE.md` no longer
leaks into the roadmap as a fake proposal); two live exemplars carry the full field
set (`31-companion-and-enemy-combat-ai`, `33-world-state-flags-and-continuity`); and a
**warn-only citation-verification pass** is wired into the research pipeline's
apply step (a private script, surfaced in
`fix-gaps` output) with three escalating tiers — offline structural checks by
default, `--verify-citation-urls` (network reachability probe), and
`--verify-citation-claims` (a `claude -p`+WebFetch judgement of whether each source
actually *supports* its claim).

**Also done 2026-06-14:** the roadmap slug-mismatch is fixed — a proposal carrying an
`## Execution log` heading or an `executed_by:` pointer drops out of To-Do even when its
resulting study was renamed (`viewer/parser.py`), with a regression test guarding the
false-positive case (`viewer/test_parser.py`); and the citation pass gained the
LLM-backed claim-support check above.

Remaining follow-ups are in frontmatter `next_steps` — chiefly the A/B once ~10
proposals use the template, and strengthening the claim check to judge against the
specific README sentence rather than the citation's description.

## Sources

**Proposal frameworks**
- [DARPA — The Heilmeier Catechism](https://www.darpa.mil/about/heilmeier-catechism) — accessed 2026-06-14
- [RIT CS736 — Heilmeier Catechism / critical questions for research proposals](https://www.cs.rit.edu/~ago/courses/736/heilmeier.html) — accessed 2026-06-14
- [NSF — Merit Review](https://www.nsf.gov/funding/merit-review) — accessed 2026-06-14
- [BioscienceWriters — Anatomy of a Specific Aims page](https://www.biosciencewriters.com/NIH-Grant-Applications-The-Anatomy-of-a-Specific-Aims-Page.aspx) — accessed 2026-06-14
- [Granted AI — Writing an effective NIH Specific Aims page](https://grantedai.com/learn/guides/nih-specific-aims-guide) — accessed 2026-06-14
- [URMC Rochester — Tips for writing Specific Aims (aim independence)](https://www.urmc.rochester.edu/MediaLibraries/URMCMedia/medicine/documents/Tips-for-Writing-Specific-Aims-CEQ.pdf) — accessed 2026-06-14
- [Farrugia et al. — Research questions, hypotheses and objectives (PMC2912019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2912019/) — accessed 2026-06-14
- [Texas A&M-CC — Parts of a research proposal](https://guides.library.tamucc.edu/c.php?g=1370951&p=10559128) — accessed 2026-06-14
- [UAB CCTS — Top 10 NIH grant submission pitfalls](https://www.uab.edu/ccts/news-events/center-news/top10-nih-pitfalls) — accessed 2026-06-14
- [GrantCentral — 30 reasons your grant proposal may not have been funded](https://www.grantcentral.com/30-reasons-your-grant-proposal-may-not-have-been-funded/) — accessed 2026-06-14

**De-risking & decision-driven design**
- [COS — Choosing the right preregistration template](https://www.cos.io/blog/choosing-preregistration-template-guide-for-researchers) — accessed 2026-06-14
- [COS — Preregistration initiative (confirmatory vs exploratory)](https://www.cos.io/initiatives/prereg) — accessed 2026-06-14
- [Bekkers — Preregistration: why and how?](https://renebekkers.wordpress.com/2023/09/20/preregistration-why-and-how/) — accessed 2026-06-14
- [ModelThinkers — Riskiest Assumption Test](https://modelthinkers.com/mental-model/riskiest-assumption-test) — accessed 2026-06-14
- [Apptunix — Riskiest Assumption Test (steps)](https://www.apptunix.com/blog/riskiest-assumption-test/) — accessed 2026-06-14
- [Behavioral Scientist — Annie Duke, mental models to cut losses (kill criteria)](https://behavioralscientist.org/annie-duke-quit-mental-models-to-help-you-cut-your-losses/) — accessed 2026-06-14
- [Wikipedia — Strong inference (Platt; Chamberlin; Popper)](https://en.wikipedia.org/wiki/Strong_inference) — accessed 2026-06-14
- [Britannica — Criterion of falsifiability](https://www.britannica.com/topic/criterion-of-falsifiability) — accessed 2026-06-14
- [Springer — A practical guide to value of information analysis](https://link.springer.com/article/10.1007/s40273-014-0219-x) — accessed 2026-06-14
- [PubMed — EVPI: empirical example](https://pubmed.ncbi.nlm.nih.gov/19602213/) — accessed 2026-06-14
- [Cosmoderma — FINER criteria](https://cosmoderma.org/finer-criteria-what-does-it-mean/) — accessed 2026-06-14

**Scoping, prioritization, sequencing**
- [Fygurs — Product prioritization frameworks compared (RICE/WSJF/ICE/MoSCoW)](https://www.fygurs.com/blog/product-prioritization-frameworks-compared) — accessed 2026-06-14
- [SAFe — WSJF](https://framework.scaledagile.com/wsjf) — accessed 2026-06-14
- [Centercode — RICE vs WSJF](https://www.centercode.com/blog/rice-vs-wsjf-prioritization-framework) — accessed 2026-06-14
- [Agile Business Consortium (DSDM) — MoSCoW prioritisation](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html) — accessed 2026-06-14
- [PapersOwl — Scope and delimitation](https://papersowl.com/blog/scope-and-delimitations-in-research) — accessed 2026-06-14
- [Research.com — Scope in project management](https://research.com/tutorials/what-is-scope-in-project-management) — accessed 2026-06-14
- [Asana — Scope creep](https://asana.com/resources/what-is-scope-creep) — accessed 2026-06-14
- [Pragmatic Engineer — RFCs and design docs (atomicity)](https://blog.pragmaticengineer.com/rfcs-and-design-docs/) — accessed 2026-06-14
- [Asana — Critical path method](https://asana.com/resources/critical-path-method) — accessed 2026-06-14
- [Mural — Dependency mapping](https://www.mural.co/blog/dependency-mapping) — accessed 2026-06-14
- [Agile Alliance — Sizing spikes with story points](https://agilealliance.org/the-practice-of-sizing-spikes-with-story-points/) — accessed 2026-06-14
- [Linden Innovation — Innovation portfolio management (explore/exploit)](https://lindeninnovation.com/innovation-portfolio-management/) — accessed 2026-06-14

**Study craft — reporting, reproducibility, actionability, AI failure modes**
- [PRISMA 2020 statement (PMC8005924)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-06-14
- [PRISMA 2020 (prisma-statement.org)](https://www.prisma-statement.org/prisma-2020) — accessed 2026-06-14
- [Newcastle — Structuring a science report: IMRaD](https://www.ncl.ac.uk/mediav8/academic-skills-kit/file-downloads/Structuring%20a%20Science%20Report%20IMRaD.pdf) — accessed 2026-06-14
- [GMU Writing Center — Writing an IMRaD report](https://writingcenter.gmu.edu/writing-resources/imrad/writing-an-imrad-report) — accessed 2026-06-14
- [GMU Writing Center — Abstracts in IMRaD reports](https://writingcenter.gmu.edu/writing-resources/imrad/abstracts-in-scientific-research-papers-imrad) — accessed 2026-06-14
- [PMC8067906 — Understanding experiments and research practices for reproducibility](https://pmc.ncbi.nlm.nih.gov/articles/PMC8067906/) — accessed 2026-06-14
- [Wikipedia — Replication crisis](https://en.wikipedia.org/wiki/Replication_crisis) — accessed 2026-06-14
- [ARTS framework — archival, reproducible, transparent science (arXiv 2504.08171)](https://arxiv.org/html/2504.08171v1) — accessed 2026-06-14
- [FAIR Guiding Principles (Nature Scientific Data)](https://www.nature.com/articles/sdata201618) — accessed 2026-06-14
- [GO FAIR — FAIR principles](https://www.go-fair.org/fair-principles/) — accessed 2026-06-14
- [Wikipedia — BLUF (communication)](https://en.wikipedia.org/wiki/BLUF_(communication)) — accessed 2026-06-14
- [Andy Matuschak — Evergreen notes](https://notes.andymatuschak.org/Evergreen_notes) — accessed 2026-06-14
- [Detecting/correcting reference hallucinations in LLMs & deep-research agents (arXiv 2604.03173)](https://arxiv.org/html/2604.03173v1) — accessed 2026-06-14
- [EmergentMind — Citation hallucinations](https://www.emergentmind.com/topics/citation-hallucinations) — accessed 2026-06-14
- [Measuring/enhancing trustworthiness of LLMs in RAG (arXiv 2409.11242)](https://arxiv.org/pdf/2409.11242) — accessed 2026-06-14
- [Social sycophancy in LLMs (arXiv 2505.13995)](https://arxiv.org/html/2505.13995v1) — accessed 2026-06-14
- [Competing biases underlie overconfidence in LLMs (Nature Machine Intelligence)](https://www.nature.com/articles/s42256-026-01217-9) — accessed 2026-06-14
- [Overconfidence & change-of-mind in LLMs (arXiv 2507.03120)](https://arxiv.org/pdf/2507.03120) — accessed 2026-06-14
