# Proposal levels: study, meta, meta-meta

Written 2026-11-07. These terms were used across the repo but never defined.
The definitions below match how existing folders already use them.

## The three levels

| Level | What it answers | What it produces | Spawns |
|---|---|---|---|
| **Study** (plain proposal) | One question tied to one decision. | Findings, a verdict, a schema or a table that a build step uses. | Nothing, or a few gap-fill follow-ups. |
| **Meta-study** (meta-proposal) | "What is the full range of X, and which parts of it need their own study?" | A broad map or catalogue of the whole topic, plus a ranked list of child studies. | Several child studies (often in a `*-followups/` folder). |
| **Meta-meta** (meta-meta-proposal) | "What areas does a whole project need researched, and in what order?" | A list of research areas, each of which becomes a meta-proposal, with dependencies, run order, and the decisions the user has to make. | Several meta-proposals. |

A meta-meta-proposal does not research the topic at all. It only scopes the
research program. A meta-study does real research, but broadly: it surveys the
whole space so the child studies can go deep on the parts that matter.

## How to tell which one you are writing

- If you can name the one decision it unblocks and it can be answered in one
  study: **study**.
- If the first job is to find out how big the topic is and split it into
  parts: **meta-study**.
- If the topic is a whole project or product, and you can't yet say which
  meta-studies it needs: **meta-meta**.

## Examples

- **Study:** one focused question, such as how save systems affect player trust.
- **Meta-study:** surveys a whole topic, then ranks follow-up studies. Its children live in a follow-up folder.
- **Meta-meta:** splits a large program into research areas, each of which becomes a meta-proposal.

## Format rules

- All three use [`PROPOSAL_TEMPLATE.md`](PROPOSAL_TEMPLATE.md), including the
  four ★ fields (prior + disconfirmer, riskiest assumption, kill/pivot
  criterion, success metric).
- **Meta-study proposals** must also fill in Q0 from the template: what counts
  as an item in the catalogue, and the stopping rule (when the enumeration is
  done).
- **Meta-meta proposals** must also include:
  - the list of areas, each with its central question, child investigations,
    what the repo already has (so it is not re-researched), and what would make
    it fail;
  - a dependency diagram and a run order in tiers;
  - the decisions only the user can make, and when in the run order each is
    needed;
  - a cheap probe to run before any area, if the whole program rests on one
    untested assumption.
- File naming: number a group's entry-point proposal `00-` (for example
  `00-<slug>-meta-study-YYYY-MM-DD.md` or `00-meta-meta-scope-YYYY-MM-DD.md`), so
  it sorts first in its `research_proposals/` folder.
- A meta-meta proposal is the only kind that may have no sources, since it
  scopes rather than researches. Every area proposal it spawns still follows
  the normal sourcing rules in the root `CLAUDE.md`.
