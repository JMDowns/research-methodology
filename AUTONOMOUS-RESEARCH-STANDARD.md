# Autonomous research standard

Written 2026-11-08 at the owner's request ("run all three autonomously ... write that as an
'autonomous research standard'"). It describes how a Claude session runs a batch of studies without
stopping to ask, based on a series of overnight runs (2026-10-25 to 2026-11-07), which ran more than 100
studies this way. Use it whenever the owner says "run autonomously", "run overnight", "go with
recommendations", or "run the proposals and follow-ups".

Everything in `CLAUDE.md` (frontmatter, citations, tiers) and
`how-to-write-proposals-and-studies/` (proposal template, levels) still applies. This file only adds
how to run many studies in a row without the owner.

## 1. What "autonomous" allows and does not allow

- **Allowed without asking:** writing proposals; launching researchers, writers and checkers;
  editing queued proposals with what finished studies found; writing follow-up proposals and
  running them, one level deep; small fixes to study files the checker finds.
- **Not allowed:** making a design decision for the owner. Every decision that is the owner's goes
  into `questions.md` with options and a recommendation (section 5). Code in a project repo is not
  changed by a research run unless the owner said so in the same request ("research only" is the
  default).
- **The owner's earlier rules still hold:** the ★ kill/pivot criterion of each proposal is obeyed
  (a triggered kill check is a result, not a failure); account and machine limits in the global
  `~/.claude/CLAUDE.md` apply (weekly cap, GPU one job at a time, disk check, no fan-out over the
  plan bar).

## 1b. The vision profile (owner, 2026-11-08)

> "a 'vision' questionnaire - knowing what my goal is for a game might help you autonomously
> recommend options inline with my vision"

Before a run makes recommendations for a project, the project needs a **vision profile**:
`<project research folder>/VISION-PROFILE.md`, the owner's answers to a short questionnaire
(what the game is for, the feeling it should give, who it is for, what to avoid, and how the owner
ranks its parts against each other). Build the questionnaire as a page with saved answers,
pre-filled from the project's design docs so the owner mostly confirms, and ask only the gaps.
Every recommendation in `questions.md` then names the profile answer it follows ("fits V3: calm
over tense"). Where the profile says nothing, say so and give the craft reason instead. When the
profile changes, re-check open recommendations against it.

## 2. Files every run keeps

All in the project's research folder.

| File | What it holds |
|---|---|
| `overnight-queue.md` (or `queue-YYYY-MM-DD.md`) | The run's state. Header: the owner's words (quoted), limits, queue order, rules. Body: a progress log. **It is the handoff:** a fresh session must be able to continue from it alone. |
| `research_proposals/brief-YYYY-MM-DD-<batch>.md` | Shared brief for every agent in a batch: the owner's words, the table of studies (number, slug, topic, prior studies to read), paths, style rules, "research only" or not. Agents read it instead of a long prompt. |
| `questions.md` | Numbered questions for the owner (Q1, Q2, ...), newest at the bottom, grouped by study (section 5). |
| `research_proposals/README.md` | The list of proposals with status (queued, running, complete), so the roadmap viewer and the next session see the state. |

## 3. The pipeline per study

```
proposal (Opus) -> researchers a, b, c (Sonnet, parallel) -> writer (Opus) -> verify_study.py gate
               -> patch-only fact-check (fresh Opus, Edit-only) -> verify_study.py --strict
               -> questions to questions.md -> update dependent proposals -> follow-up proposals
```

- **Proposal.** Written from `PROPOSAL_TEMPLATE.md` at the right level (`PROPOSAL_LEVELS.md`), tagging subquestions `[context]`, `[finding]`, or `[decision]`. Run `python3 scripts/find_prior.py --complete-only --file <proposal>` so unverified drafts are excluded. Split the research into 2-4 independent parts (a, b, c, ...) so researchers can run in parallel; a part that needs another part's result (a probe that needs data) waits for it.
- **Researchers (Sonnet).** One per part. Each writes `sources/<letter>-<topic>.md` (tagging extracted sources `[RCS: 0-10, Primary/Secondary]` and including exact `[Label](URL) — accessed YYYY-MM-DD` citations + verbatim quotes) and returns one line. Prefer primary sources; mark snippet-only claims `(snippet)` and multi-model agreement without a fetched URL `(unverified — consensus only)`. Multiple secondary posts summarizing the same upstream paper count as 1 source (`independence_group`). A part may be a probe or a small simulation instead of web research.
- **Writer (Opus).** Reads the proposal, the source notes and the prior studies it builds on; writes `README.md` (full frontmatter, answer-first under ~3,500 words, explicit unresolved uncertainties in `## Known Gaps`, `## Self-check`, `## Sources`), any decision tables, and adds the study's owner decisions to `questions.md`.
- **Mechanical gate (`scripts/verify_study.py`) + Patch-only Fact-check (fresh Opus).** First run `python3 scripts/verify_study.py <study-dir>` to catch missing frontmatter keys, ghost URLs not in `sources/*.md`, untraced numbers, or uncited factual paragraphs. Next, a fresh checker checks every headline number, every `[decision]` claim, and at least 25 other claims against `sources/*.md` (and the primary source for `[decision]`, headline, and surprising claims); fixes errors in place using **surgical `Edit` calls only ("Patch, Never Regenerate" — never full-file `Write`)**; adds a `## Fact-check` section with claims checked, claims changed, and the `verify_study.py` composite gate score. Quality guard (from the global `CLAUDE.md`): if more than 10% of checked claims change, or a headline number was wrong, redo that area's gathering on Opus, unless the errors were in the writer's own reading (then the checker's fixes stand; say so in the study).
- **Complete** only after both the fact-check and `python3 scripts/verify_study.py --strict <study-dir>` pass. Then: mark it complete in `research_proposals/README.md`, add a row to `INDEX.md`, log it (section 4).

## 4. Running the queue

- **At most 4 agents at once** (the limit those runs used). Launch the next item when one finishes.
  Proposal writers for a new batch may run as an exception. A second study may use free slots when
  the first has fewer than 4 agents running.
- **Order:** a meta-meta scope first; then its areas in its tier order; inside a level, dependency
  order (a study that another study needs goes first, even if its priority score is lower), then by
  RICE.
- **Before each study starts:** re-read its proposal and update it with what studies finished since
  it was written. Add a line `Updated after study NN: <what changed>` (owner's rule, 2026-10-25).
- **Progress log:** one line per event, dated, with the key result in numbers and what is running
  now. Example: `- 15 (c) done (refuse 68/13.5/0.1% by bond band). Started 15 writer. Running: 38 A,
  32 catalog, 15 writer.` Log kill checks, pivots, contradictions found between studies, and any
  fix made to an earlier study.
- **Results in files.** Every agent writes its result to a file and returns one line. The
  orchestrating session never reads whole transcripts.
- **Background agents and limits.** If agents stop on a usage or session limit, note it in the log
  and resume them by message when the limit resets.
- **Context and handoff.** When the orchestrating session passes about 300k context, at the next
  break make sure the queue file is current (it is the handoff), wait for running agents to finish,
  and restart from it (`~/.claude/usage-automation/restart/handoff-restart.sh`), as the global
  `CLAUDE.md` says.

## 5. Questions for the owner

Each question in `questions.md`:

```
### Q57. <one-line question> (<study numbers>)
<2-4 plain sentences: what the study found that makes this a question, with numbers.>
- (a) ..., (b) ..., (c) ...
- **Recommendation:** (x). <one or two reasons>
- **Blocks:** <studies or build steps that wait on it>
```

- **Read the last Q number right before appending** (two writers once used the same numbers).
- When a run should not wait for an answer, it goes on with the recommendation and says so in the
  study ("assumed Q57 (a)").
- When the owner wants to answer 3 or more related questions, offer a decision page (global
  `CLAUDE.md`, "Decision pages") built from these entries.

## 6. Depth: when to stop

- **Studies and meta-studies:** run the batch, then follow-up proposals from each study's backlog,
  **top items only, one level deep**, run the same way. Then stop. The rest are owner decisions
  or later work.
- **Meta-meta programs:** a meta-meta proposal scopes; it is not research. Running one
  autonomously means: (1) write the meta-meta scope; (2) write one meta-proposal per area; (3) run
  the meta-studies in the scope's tier order; (4) from each meta-study's ranked child list, write
  and run **every** child study it recommends, not just the top few (owner, 2026-11-08: "I don't
  want you to stop at 2-3 studies"); (5) then follow-up proposals from those child studies'
  backlogs, top items, one level deep; (6) stop. Areas the scope marks "later" or
  "needs an owner decision first" get a proposal but are not run; their decision goes to
  `questions.md`.
- **Budget check before each tier:** check the plan bar as the global `CLAUDE.md` says. On the main
  account, if the weekly bar is ahead of the day's share of its 80% budget, run gathering on Sonnet
  only and skip optional child studies; at 75% start nothing new; at 80% hand off.

- **"No depth limit" runs** (owner, 2026-11-08: "no depth limit, keep going until it's done"):
  follow-ups go as deep as they need. A branch is done when its latest study's backlog holds only
  owner decisions (to `questions.md`), build steps, or questions an existing study already answers
  (check the repo before each new proposal). The run is done when every branch is done. The budget
  check above still applies.

## 7. The final report

When the run ends (or stops on a limit), write at the top of the queue file a short report: what
ran (study numbers, slugs), what each one concluded in one line, kill checks and pivots, the
question range added (e.g. Q389-Q453), and what is left (queued but not run, and why). Give the
owner the same in 3-6 lines, plus a decision page link when there are 3 or more related questions.
