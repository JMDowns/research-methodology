# Research Project Instructions

This repo holds a research method for running studies with Claude Code. Each study gets its own folder. Start one with `./research.sh "<topic>"`.

The `studies/` folder holds only studies about the method itself: how to search, how to grade evidence, how to write proposals, and what research runs cost in tokens. Topic studies go in new folders at the root of your own copy.

## Repository Layout

```
.
├── CLAUDE.md                              # the method (this file)
├── AUTONOMOUS-RESEARCH-STANDARD.md        # running a queue of studies without the owner
├── INDEX.md                               # list of studies, updated as they start and finish
├── research.sh                            # starts a new study session
├── how-to-write-proposals-and-studies/    # proposal template, levels, review checklist
├── templates/STUDY_TEMPLATE.md            # study README template
├── scripts/find_prior.py                  # finds earlier studies on a topic
└── studies/                               # the evidence behind this method
```

## Research Methodology

### Proposal levels

Study vs meta-study vs meta-meta proposal are defined in `how-to-write-proposals-and-studies/PROPOSAL_LEVELS.md`, with the extra sections each level needs.

When a meta-meta proposal (or several programs written together) needs the same support work, such as evidence grading, plan it once as a shared study and have each program point to it. Before writing a program's areas, run `scripts/find_prior.py` on each area and check the other programs' scopes for the same area (`studies/research-duplication-and-reuse/`).

### Running studies without the owner

When the owner says "run autonomously", "run overnight" or "run the proposals and follow-ups", follow `AUTONOMOUS-RESEARCH-STANDARD.md` (queue file, per-study pipeline, questions file, depth limits).

### Starting a Study

1. Pick a category (`methodology` or a topic name of your own).
2. Run `python3 scripts/find_prior.py --file <proposal>` (or with the topic text). Open the top 3 results and anything scoring at least half the top score. Paste the results you kept into the proposal's prior-art line. The tool finds near-copies well but misses about 60% of cross-domain prior work (measured in `studies/research-duplication-and-reuse/`), so still search by hand for related studies in other groups.
3. Create `<study-slug>/README.md` from `templates/STUDY_TEMPLATE.md`.
4. Fill in ALL YAML frontmatter fields (see schema below).
5. Conduct research using the web search strategy below.
6. Update `INDEX.md` when the study is created and when it's completed.

### YAML Frontmatter (Required)

Every study `README.md` MUST begin with YAML frontmatter delimited by `---`, so tools can read it. The template at `templates/STUDY_TEMPLATE.md` has the full schema.

```yaml
---
title: "Study Title"
date: 2026-03-01
status: complete        # complete | in_progress
confidence: medium      # high | medium | low
confidence_reason: "brief justification"
completeness: 75        # integer 0-100
completeness_reason: "what's covered vs missing"
category: methodology
tier: 2                 # 1 | 2 | 3 (research complexity)
objective: "What this study answers"
summary: "One line: what this research produced / concluded (plain language)."
why: "Why we're doing it: which decision or feature this informs."
blockers:
  - "What's blocking completion, or what downstream work this blocks (omit / [] if none)"
source_count: 15
known_gaps:
  - "Gap description"
next_steps:
  - "Actionable continuation step"
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
```

**Rules:**
- ALL fields are required.
- Always update `status`, `completeness`, `source_count`, and `quality_checklist` when finishing research.
- `next_steps` must be actionable: what would an AI do to continue or improve the study?
- `known_gaps` must match the gaps listed in the Markdown body.
- The Markdown body below the frontmatter contains the human-readable content (Findings, Sources, etc.).
- When updating an existing study, update the frontmatter fields too.

### Web Search Strategy (Empirically Tested, R3 Methodology)

Full details and experimental evidence are in `studies/web-search-methodology/`. The method below was A/B tested across 3 rounds and reached 93.5% quality at 53% of naive token cost.

#### Step 1: Classify Complexity

| Complexity | Signal | Strategy |
|-----------|--------|----------|
| **Tier 1**: Simple fact | 1-2 facts needed | 1 WebSearch, read snippets, maybe 1 WebFetch |
| **Tier 2**: Moderate question | Single topic, multiple details | 1-3 WebSearch + 3-5 WebFetch |
| **Tier 3**: Deep research | Multi-faceted, many sources | 3-5 parallel subagents, each running Tier 2 |

#### Step 2: Execute (Tier 2, Most Common)

1. `WebSearch("broad topic query")`: read snippets, identify 2-3 best URLs
2. `WebFetch(best_url, prompt="Extract [specific data]. Format as [table/list].")`: targeted extraction
3. Assess: What do I have? What's missing?
4. If gaps remain, do one more targeted `WebSearch` and `WebFetch` on the best result
5. **VERIFY**: Fetch 1-2 MORE pages from a DIFFERENT source domain to cross-check key claims
6. Synthesize only from fetched sources

#### Critical Rules (Violating These Caused a 7.1% Quality Drop in Testing)

1. **NEVER state something as fact unless it came from a fetched source.** Do not fill gaps from training data. Mark unverified claims as "(unverified)". If multiple models or parametric knowledge agree without a fetched URL, mark it `(unverified — consensus only)`.
2. **Verify counts and specific details explicitly.** Don't assume from memory. Fetch and confirm. Split general parent claims from specific child numbers so a retracted child detail does not corrupt the supported parent claim.
3. **Cross-reference across 2+ independent source origins (`independence_group`).** Different sources contain different errors, and multiple secondary posts summarizing the same upstream paper or press release count as **1 source**, not 2+.
4. **Do NOT stop at 1-2 fetches** for Tier 2+ questions. Testing showed this drops quality from ~93% to ~86%.
5. **Write targeted WebFetch prompts & score relevance.** WebFetch uses Haiku internally. Vague prompts ("summarize this page") waste extraction capacity. Specify exactly what data you need, and tag extracted source blocks in `sources/*.md` with `[RCS: 0-10, Primary/Secondary]` (prune `<=1`).

#### For Tier 3 (Deep Research): hybrid pipeline (v2)

Tested against the plain Tier 3 method and the deep-research skill in `studies/research-pipeline-hybrid-comparison/`, and upgraded with the mechanical verification and context-hygiene guards from `studies/github-survey/`.

1. **Proposal first (with consequence tiers).** Write `research_proposals/<slug>-YYYY-MM-DD.md` (prior, disconfirmer, rival hypotheses, kill criterion, and `[context]` / `[finding]` / `[decision]` tags on Q1..Qn). Run `python3 scripts/find_prior.py --complete-only --file <proposal>` so unverified `in_progress` drafts never contaminate prior art. Show it to the user before launching researchers.
2. **Parallel researchers.** Decompose into 2-5 sub-questions. Launch one researcher subagent (Sonnet, about 30 turns maximum) per sub-question in the background. Give each the proposal path, these R3 rules, and an output path in `sources/`.
3. **Researcher budget & context hygiene.** Each researcher follows the Tier 2 steps with a cap of about 30 turns. A capped run returns partial and can be resumed.
   - **Context-rot guard:** Write extracted facts + exact `[Label](URL) — accessed YYYY-MM-DD` citations + verbatim quotes to `sources/<part>.md` incrementally. Never bulk-read more than 5 raw step logs at once, and preserve exact domain terms and URLs across summaries. When aggregating structured JSON/CSV/code outputs, inject a deterministic schema manifest first.
   - **Trial rule (3 questions):** for a sub-question that surveys published studies, launch two Sonnet researchers with the same brief and separate output files. Together they cost about the same tokens as one Opus researcher and found as many sources. When the 10% quality guard fires, rerun that area once on Sonnet before switching to Opus, because Opus also went over 10% on 1 of 3 questions.
   - **Trial rule:** for a sub-question marked "partly" covered in the proposal, give the researcher the narrowed question and a cap of about 15 turns instead of 30. Don't add a "reuse repo notes" step to researcher briefs: in the A/B it saved 3% of tokens and copied a repo error into a headline.
4. **Separate writer, answer first.** One writer subagent reads only `sources/*.md` and writes `README.md` (plus `ai-instructions.md` when there are setup steps). The README must:
   - open with a plain answer to the user's own questions, in the user's wording and order, not the proposal's Q-numbers
   - stay under about 3,500 words, with detail moved to other files
   - include explicit unresolved uncertainties and rejected hypotheses in `## Known Gaps`
   - put the prior / disconfirmer / hypothesis audit in an appendix at the end
5. **Mechanical gate (`scripts/verify_study.py`) + Patch-only faithfulness pass.**
   - First, run `python3 scripts/verify_study.py <study-dir>`. It deterministically verifies YAML frontmatter (`G1`), zero ghost URLs between `README.md` and `sources/*.md` (`G2`), domain diversity (`G3`), verbatim quote matching $\ge 6$ words (`G4`), numerical token traceability (`G5`), and factual paragraph citation coverage (`G6`).
   - Second, a fresh subagent re-checks every number, quote, `[decision]` claim, and attribution in the draft against the `sources/` notes (and the cited page when the notes are unclear). **Patch, Never Regenerate:** post-draft verification and polish passes are restricted to surgical `Edit` calls and must NEVER overwrite `README.md` with a full-file `Write` regeneration. Any fact the writer or a researcher took from an earlier repo study, rather than a page fetched in this study, is marked `[repo: <path>]` and re-checked against its original page.
   - Re-run `python3 scripts/verify_study.py --strict <study-dir>` after patching to confirm all deterministic gates pass.
6. **Gap fill (optional).** Launch 1-2 more researchers only for gaps the writer or checker named.

#### Token use

Evidence is in `studies/claude-code-token-usage-optimization/` and `studies/claude-prompt-caching-optimization/`.

- Research-gathering subagents (web search + source notes) run on Sonnet. The writer and a fresh fact-check pass run on Opus. The fact-check is required whenever gathering used Sonnet.
- Quality guard: if the fact-check changes more than 10% of the claims it checks, or finds a wrong headline number, redo that area's gathering and note it in the study.
- Background agents write results to a file and return one line. For batches, one aggregator reports instead of waking the main session per agent.
- A new subagent costs about 32k tokens before it does anything. Do jobs of a few tool calls inline.

#### Anti-Patterns

- Fetching every search result without evaluating snippets first
- Vague WebFetch prompts ("tell me about this page")
- Stopping at 1-2 fetches on moderate questions
- Filling knowledge gaps from training data instead of fetching
- Not reasoning between searches: pause to assess after each fetch
- Using only one source domain for verification

### Citation Standard (Medium)

Every factual claim must include a citation in this format:
```
[Brief description](URL) — accessed YYYY-MM-DD
```
Collect all citations in a `## Sources` section at the bottom of each study file.

### Confidence & Completeness

Every study README.md must include (in both frontmatter AND Markdown body):
- **Confidence Rating**: High / Medium / Low. How reliable are the findings?
- **Completeness**: Percentage estimate and what is missing
- **Known Gaps**: Bulleted list of what's missing or uncertain

### File Organization

```
<topic-slug>/
├── README.md          # Synthesized findings with YAML frontmatter
├── ai-instructions.md # Instructions for AI to implement/use findings (if applicable)
├── sources/           # Raw source material (full texts, data dumps)
│   ├── source-1.md
│   └── ...
└── (other supporting files as needed)
```

### Content Rules

- Studies are **revisable**: update in place, no versioning needed
- Split large results across multiple files (keep individual files readable)
- Always provide both human-readable summaries AND raw source material
- Include `ai-instructions.md` when the research has actionable implementation steps

### Quality Standards

- Do NOT take process claims at face value. Test hypotheses empirically when possible
- Cross-reference multiple sources; flag contradictions
- Prefer primary sources over secondary summaries
- If a source is a wiki or fan site, note that in the citation

## Studies that feed a project

Some studies gather domain knowledge before or during work on a code repo. Start those with `./research.sh --for <repo path> "<topic>"`.

Rules for a study that feeds a project:
1. **Frontmatter:** add `feeds: ["<repo path>"]`, a list of repo paths.
2. **Read the repo's intent first.** If `<repo>/docs/INTENT.md` exists, read it before researching. Say which items (I1, D2, P1, ...) the study bears on. If a finding contradicts a confirmed item, say so plainly in the Short answer.
3. **Candidate intent.** End `ai-instructions.md` with `## Candidate intent for <repo>`. List the 3-10 decisions the findings support that matter most, one per item:
   ```
   - [DELIBERATE-CHOICE | INVARIANT | NON-GOAL | PLANNED-EXTENSION | BOUNDARY | CRITICAL-AREA]
     <one-line rule>
     Why: <one line, with the finding's citation>. Confidence: <high|medium|low>
     Bears on: <existing INTENT.md item id, or "new">
   ```
   These are candidates only. Nothing here is binding until the user confirms it.
4. **Self-check.** End `README.md` (before Sources) with `## Self-check`. Write three questions about the domain that the user should be able to answer before building: what real situation it handles, why the recommended approach beats the obvious alternative, and what would break if a key assumption changed. Put the answers in a `<details><summary>Answers</summary>` block.
