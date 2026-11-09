# Claude Code token usage optimization — research proposal (2026-11-07)

This proposal grounds a set of changes to how the owner runs Claude Code
(long-lived main sessions, many background subagents, screenshot checks) so that
fewer tokens are spent per unit of finished work, without lowering output quality.
Model knowledge isn't enough because Claude Code's billing, caching, compaction and
subagent behaviour change between releases, and the local measurements
(`../sources/local-usage-2026-11-05-to-07.md`) need to be checked against current
official docs before acting on them.

## What this is (plain language)
Find out which of my Claude Code habits use the most tokens, and which changes cut
that use without making the work worse.

## Why this, why now — the gap tied to a decision
- Already known: `claude-prompt-caching-optimization/` (2026-02) covers caching in
  `claude -p` batch pipelines, not interactive sessions with subagents.
  `web-search-methodology/` covers web search cost only. The project A memory
  `project notes` already has rules (narrow briefs, handoff at ~60 calls,
  summary scripts, Sonnet for mechanical jobs).
- Local data (2 days, 290 transcripts): ~3.1 B cache-read tokens, 80% from 283
  subagents. Two main threads run at a median of 467k and 822k context. In
  project A, 322 of 379 main-thread wake-ups are background-agent notices, each
  processed at ~0.5M context. Only 9 of 283 subagents ran on Sonnet. 52 subagents
  were continuations or restarts.
- Gap: I don't know from docs (a) whether context above some size costs more per
  token on the current plan/models, (b) how Claude Code bills and caches subagents
  and notifications, (c) what quality cost, if any, Sonnet subagents or shorter main
  contexts have for this kind of work.
- Decision this unblocks: a short rule set for `~/.claude/CLAUDE.md` and the
  project memories (when to start a fresh main session, how to batch agent
  notifications, which agent jobs default to Sonnet, how to handle screenshots).

## Central question
> Which changes to session length, subagent use, model choice and tool output most
> reduce tokens per finished task in my Claude Code workflow, without a measurable
> drop in quality?

## Core questions to answer
- **Q1 — Billing and caching facts.** How are cache reads/writes, 1M-context turns,
  images, and subagent turns counted against a Max plan's usage limits on current
  models? Does a long context cost more per token? What are the cache TTLs in
  Claude Code, and what triggers a full rewrite?
- **Q2 — Main-thread context.** What do official docs and practitioners recommend
  for /compact, /clear, fresh sessions, and handoff files? Is there evidence that
  quality drops at very large contexts ("context rot"), which would make shorter
  sessions a quality win as well as a cost win?
- **Q3 — Subagents.** Cost of a subagent (system prompt + brief + re-reading files)
  vs doing the work inline; effect of Sonnet/Haiku vs Opus on mechanical tasks
  (file edits, test runs, triage); best way to collect many background results
  without waking a large main thread for each one.
- **Q4 — Tool output.** Image token cost (screenshot size vs tokens), and patterns
  for keeping Bash/Read output small (summary scripts, `grep` before `sed -n`,
  output caps).
- **Q6 — Measuring effectiveness (added 2026-11-07 at the owner's request).** How
  do we tell that a change saved tokens *without* hurting quality? Candidate metric:
  tokens per finished task, paired with quality signals that can be read from
  transcripts (restart/redo agents, owner corrections, failed tests, reverted
  commits, tasks reopened). What do Anthropic and others use (cost per resolved
  task on agent benchmarks, Claude Code's OpenTelemetry metrics, ccusage-style
  tools)? What sample size / time window is needed before a difference is real
  rather than noise from different workloads?
- **Q5 — Local check (empirical).** Re-run the local scripts after the changes for
  2 days and compare tokens per finished task. Optional small A/B: one mechanical
  agent job on Sonnet vs Opus, judged on the same checklist.

## ★ Expected answer (prior) + disconfirmer
- Prior: the biggest wins are (1) not running main threads at 500k–900k context
  (start fresh sessions from a handoff file; keep the orchestrator small),
  (2) fewer, batched wake-ups from background agents, (3) Sonnet for mechanical
  subagent jobs. Screenshots and Bash output are second-order (<10%).
- Disconfirmer: docs show cache reads at large context are nearly free against
  plan limits, or that subagent turns don't count the way I think. Then main-thread
  size matters less and output/agent count matter more.
- Rival: quality drops on Sonnet for this work are big enough that restarts eat
  the savings (the 18 "restart" agents suggest failures are already costly).

## ★ Riskiest assumption (test first, cheaply)
That cache-read tokens count against Max-plan usage in proportion to their API
price. Check the official docs/help pages first (one researcher, ~10 calls).

## ★ Kill / pivot criterion
If after Q1 (≤ 15 tool calls) cache reads turn out to be a minor part of plan
usage, pivot the study to output tokens and agent count instead of context size.

## Deliverables (Definition of Done)
- `README.md` answering the owner's question in their words: ranked list of
  changes with measured or estimated savings and the quality risk of each.
- `ai-instructions.md` with concrete rules to paste into `~/.claude/CLAUDE.md` and
  project memories.
- `sources/` notes per question, plus the local usage data and scripts.

## ★ Success metric (the exam)
Two days after the rules are adopted, the local scripts show lower cache read per
user turn and per subagent, with no rise in "restart" agents.

## Scope
- In: Claude Code interactive use with subagents, on this machine.
- Out: `claude -p` pipelines (covered by `claude-prompt-caching-optimization/`),
  web search cost (covered by `web-search-methodology/`), switching providers.

## Tier, cost & priority
- Tier 2–3: 4 parallel researchers (Q1, Q2+Q4, Q3, Q6), ~30 tool calls each, then one
  writer and one faithfulness check. Researchers on Sonnet, writer on Opus.

**Priority:** 6.4 (RICE)

Reach 4 (every project) × Impact 2 × Confidence 0.8 ÷ Effort 1.

## Suggested research order
1. Q1 researcher first-pass (kills or confirms the riskiest assumption).
2. Q2+Q4 and Q3 researchers in parallel.
3. Writer → faithfulness pass.
4. Q5 local re-measure after 2 days of use.

## Sources to chase
- Anthropic: Claude Code docs (costs, memory/compaction, subagents, model config,
  settings), Max plan usage-limit help pages, prompt caching docs, vision/image
  token docs, pricing page.
- Anthropic engineering blog posts on context engineering and multi-agent research.
- Context-length quality evidence (e.g. Chroma "context rot" report, long-context
  benchmarks).
- Practitioner reports on Sonnet vs Opus subagents in Claude Code.

## Cross-references
- `claude-prompt-caching-optimization/`, `web-search-methodology/`,
  `research-pipeline-hybrid-comparison/`.

```yaml
summary: "Ranked changes to Claude Code habits that cut token use without lowering quality."
why: "2 days of local data show ~3.1B cache-read tokens, mostly from subagents and 0.5–0.9M main threads."
blockers: []
```
