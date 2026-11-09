# <Topic> — research proposal (<YYYY-MM-DD>)

<!--
Proposal skeleton grounded in how-to-write-proposals-and-studies/README.md.
Keep it ATOMIC: one proposal = one decision/deliverable. Skip the heavyweight
treatment for small, well-understood, or easily reversible work — a one-paragraph
note is fine there. Delete sections that genuinely don't apply, but think before
cutting the four pre-commitment fields (★) — they are the point of this template.

A proposal is NOT the research. It says what to research before building, and why,
so the work can be dispatched deliberately instead of authored from model knowledge.
-->

One framing paragraph: what this proposal grounds, and the one-sentence reason
**model knowledge isn't enough here** (the research-first rule).

## What this is (plain language)
One sentence, **no jargon** — what are we trying to find out? (Heilmeier Q1)

## Why this, why now — the gap tied to a decision
- What's already in the repo (prior-art check). Paste the `scripts/find_prior.py --file` top results you kept. Then mark each core question: **covered** (an existing study answers it: cut it and point to that study), **partly** (narrow the question to what is missing), or **new**. Only facts the new question needs count as covered. A study on the same topic often holds none.
- The precise **gap**: what model knowledge / existing studies cannot settle.
- **The decision or downstream artifact this unblocks *right now*.** Name it.
  (A gap with no consequence is the #1 reason a proposal isn't worth doing.)

## Central question
> The single question all the others depend on, in a blockquote.

## Core questions to answer
Numbered, **independent** clusters (Q0/Q1/Q2…) so they can be cited later. Each
should be specific, have real build consequences, and surface *competing*
traditions/options where they exist. Aims must be non-contingent — design each so
it still yields something even if another fails. (FINER-frame where useful.)

- **Q0 — (for discovery proposals) the inclusion test + stopping rule:** what
  counts as a valid X, and when is the enumeration done?
- **Q1 — …**
- **Q2 — …**

Use **comparison tables** wherever traditions/options disagree; mark provisional
taxonomies "candidate — confirm/expand during research."

## ★ Expected answer (prior) + disconfirmer
- What I currently expect the research to conclude (a stated prior — so the study
  can *surprise* me rather than confirm the prompt's implied answer).
- **The specific result that would disconfirm it.** If no finding could, this is
  rhetoric, not research — reframe the question.
- 2–3 rival hypotheses, if the space is wide, designed to *exclude* not confirm.

## ★ Riskiest assumption (test first, cheaply)
The one assumption that, if false, makes this study pointless (highest impact ×
uncertainty). Can a short scoping probe kill or green-light it before the full run?

## ★ Kill / pivot criterion (state + date)
"If I am (or am not) in [measurable state] after [N sources / X hours / step], I
**stop or pivot** to ___." Pre-committed, so sunk cost doesn't carry it.

## Deliverables (Definition of Done)
The concrete consumable artifacts a later build step / generator / eval can use
(e.g. study folder, taxonomy tables, schema, enum, an operational `presets.yaml`,
a verdict). State the boundary that means "done."

## ★ Success metric (the exam)
Per deliverable: how do we know the study actually *worked*, not just finished?
(Heilmeier Q8 / NSF assess-success.) e.g. "enum covers all 8 genres' mandated +
forbidden endings with no overlap, reconciled against the outcome contract."

## Scope
- **In scope:** …
- **Out of scope / non-goals:** … (the "Won't, this time" list — anti-creep)
- **Delimitations (chosen boundaries) + rationale:** …
- **Does NOT re-research:** … (point at the study that already owns it)

## Tier, cost & priority
- **Tier:** 1 / 2 / 3 + rough effort (hours / subagent count). Timebox if uncertain.
- **Explore vs exploit:** new-area discovery / deepening a mature area.
- **Priority score** so the roadmap orders To-Do work by value, not alphabetically.
  **RICE is the canonical scored method** (so every proposal's number is comparable
  across the backlog): RICE = Reach × Impact × Confidence ÷ Effort. Emit it on its
  own line in exactly this form — the roadmap viewer parses it and sorts To-Do
  descending:

  **Priority:** <score> (RICE)

  Show your working next to it, e.g. `Reach 4 × Impact 3 × Confidence 0.8 ÷ Effort 0.5`.
  - **Reach** = how many downstream studies / build steps this unblocks.
  - **Confidence** ∈ {1.0, 0.8, 0.5} — the brake on speculative deep-dives.
  - **Effort** in tiers (Tier-1 ≈ 0.25, Tier-2 ≈ 0.5, Tier-3 ≈ 1+).
  - **WSJF is a lens, not a competing number:** for an enabler/taxonomy proposal that
    unblocks many others, express that by giving it a **high Reach** — don't emit a
    WSJF score (its scale isn't comparable to RICE, so it would mis-sort the list).
  - A high-score proposal **blocked by** a lower-score prerequisite still yields to it
    (dependencies override raw score).

## What this blocks and doesn't block
- **Blocks:** … (downstream studies/build steps that wait on this)
- **Blocked by:** … (prerequisites — if a prerequisite is lower-priority but on the
  critical path, it goes first; note that dependency-override here)

## Suggested research order
Numbered steps with rough time budgets and how many parallel subagents/clusters
the run could use. Discovery/taxonomy before per-type design.

## Sources to chase
Grouped by tradition/cluster, **named and concrete** (author + work + what to look
at; specific games/books/talks/primary docs to teardown), not "search the web."

## Cross-references
`[[NN-slug]]` wikilinks to sibling proposals (a link to a not-yet-written proposal
is fine — it marks intended structure) and any external research dirs.

<!--
If this proposal will be tracked by the roadmap viewer, also embed the
summary/why/blockers YAML block the viewer scans:

```yaml
summary: "One line: what this research will produce / conclude."
why: "Which pipeline decision or feature this informs."
blockers:
  - "What this blocks downstream, or what blocks it (omit / [] if none)."
```
-->
