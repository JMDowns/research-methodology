---
title: "Claude Code Token Usage Optimization"
date: 2026-11-07
status: complete
confidence: medium
confidence_reason: "Local numbers are measured from 290 transcripts and cost mechanics come from official Claude Code docs, but the Max-plan weighting of cache reads is unpublished and no local quality test (Sonnet vs Opus, short vs long threads) has been run yet."
completeness: 70
completeness_reason: "Covers billing/caching, main-thread context, subagents, tool output and a metric set. Missing: plan-limit weighting, notification coalescing, the Q5 before/after re-measure, a Sonnet-vs-Opus A/B, and screenshot legibility at lower resolution."
category: methodology
tier: 3
objective: "Which changes to session length, subagent use, model choice and tool output most reduce tokens per finished task in the owner's Claude Code workflow, without a measurable drop in quality, and how should 'effectiveness' be measured?"
summary: "Ranked list of Claude Code habit changes (small orchestrator, Sonnet for mechanical agents, shorter agents, fewer wake-ups) plus a metric set that counts a saving only if quality signals don't get worse."
why: "2 days of local data show ~3.1B cache-read tokens, 80% from 283 subagents and the rest from main threads running at 0.5-0.9M context; the owner wants rules for ~/.claude/CLAUDE.md and project memories."
blockers:
  - "The Max-plan weight of cache reads vs input/output is not published, so savings are given in tokens and API-price units, not in plan-limit percent."
  - "Q5 (2-day re-measure after the rules are adopted) blocks the final verdict on each change."
source_count: 33
known_gaps:
  - "How Max-plan limits weight cache reads, cache writes, input and output is not published; only a community fit (~0.1x input for cache reads) exists."
  - "No measurement of Opus 5.5 / Sonnet 5.5 quality at 500k-900k context in an agent loop."
  - "No controlled data on Sonnet vs Opus for mechanical subagent jobs (edits, test runs, triage)."
  - "Whether Claude Code merges several background-agent completion notices into one main-thread turn is not documented."
  - "Whether settings.json keys, env vars and new agent definitions take effect in an already-running session is not stated in the sources."
  - "Screenshot resolution needed for the owner's UI checks is untested."
  - "Restart/correction/revert signals are not validated as quality measures for agent work in any fetched study."
  - "Savings estimates are the writer's arithmetic on local data, not measured before/after results."
next_steps:
  - "Adopt the rules in ai-instructions.md, then after 2 days re-run scripts/agg*.py and compare cache read per user turn, per subagent, restart rate and correction rate against this baseline (Q5)."
  - "Run the null check from metrics.md: split the 2026-11-05 to 07 baseline into halves and measure the noise band before comparing."
  - "Run a small A/B: one mechanical agent job on Sonnet vs Opus, 3 trials each, judged on a code-checkable checklist."
  - "Check local transcripts for whether consecutive task-notifications arrive in one main-thread turn or several."
  - "Test subagentPromptCacheTtl=1h on one long, pausing agent job and compare cache writes."
  - "Test a downscaled (~1000 px) screenshot on a real UI check for legibility."
  - "Compare /usage plan bars before and after a known cache-read-heavy workload to estimate the plan weight of cache reads."
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

# Claude Code Token Usage Optimization

All local numbers below come from `sources/local-usage-2026-11-05-to-07.md` (290 transcript files, 2026-11-05 10:00 UTC to 2026-11-07 16:37 UTC). "Cache read" means context re-sent from the prompt cache on each turn. It grows with context size, so it is the best single measure of how much context was re-sent. Lines marked "(estimate)" are my arithmetic on that data, not a measured before/after result.

## Short answer

### Question 1: "Look at my claude usage in all my sessions over the past 2 days and tell me how I can optimize my token usage without sacrificing quality — find places where I'm using more tokens than needed."

Where the tokens went in 2 days:

- About 3.09 B cache-read tokens in total. Subagents used about 2.46 B (80%). The main threads used the other ~0.63 B (estimate: total minus subagents per session).
- Output was only about 13 M tokens. Cache writes were about 75 M.
- 283 subagents ran. Only 9 of them used Sonnet. The rest used Opus 5.5.
- The project A main thread ran at a median of 467k context, the project B main thread at 822k.
- In project A, 322 of the 379 turns that woke the main thread were background-agent completion notices. Each one was processed at about 0.5 M context.

Ranked changes (biggest, best-supported first):

| # | Change | Evidence from your data | Expected saving | Quality risk | Confidence |
|---|---|---|---|---|---|
| 1 | **Keep the main orchestrator small.** Start a fresh session from a handoff file at a natural break, around 200-300k context (my suggestion, no source gives this number). Set the auto-compact window to 400k as a backstop. | project A main thread: 1,039 turns, median 467k, 500 turns over 500k. project B: median 822k. The project A session has been resumed for a month. | ~14% of total cache read if both main threads averaged ~150k (estimate, see Estimate arithmetic below; ignores handoff cost). | Low to unknown. Docs say a focused context "gets you better answers", but no test shows Opus 5.5 gets worse at 500k+. Handoff can lose detail. | Medium |
| 2 | **Run mechanical subagent jobs on Sonnet.** Test runs, file edits from a clear spec, log triage, recurring "cycle" jobs, summaries. Keep Opus for design, unknown bugs and reviews. | 274 of 283 agents on Opus. 30 agents were recurring "cycle" jobs. | Sonnet costs half of Opus per token on the API, including cache reads. If half the subagent work moved and plan usage follows API price (unverified), about 20% of total weighted cost (estimate, see Estimate arithmetic below). Token count stays the same. | Medium-low. Vendor benchmarks show small gaps on agentic coding. No controlled test of mechanical agent work. | Medium-low |
| 3 | **Keep long subagents short.** Give long jobs a per-agent auto-compact window, or end them at about 60 tool calls (the number comes from your own project A memory note, not from a source) with a state file and start a fresh agent. | Median agent: 65 turns, 101k context, 6.6 M cache read. The biggest project B agents ran 150-239 turns, reached 450k-670k, and read 40-97 M each. | Large for the long agents (cache read per turn grows with context), but not computed per agent yet. | Low if the state file is good. Compaction drops detail. | Medium |
| 4 | **Fewer main-thread wake-ups.** Agents write results to files and return a one-line reference. One aggregator agent reports for a batch. Recurring cycle jobs move to dynamic workflows. | 322 notice turns x ~0.5 M = ~160 M cache read, about 5% of the total, before any follow-up turns (estimate). Overlaps with #1. | Up to ~5% directly, more with follow-up turns. Smaller once #1 is in place. | Low. Anthropic warns that passing state through files is worse for sequential work. | Medium |
| 5 | **Do small tasks inline, or use a fork.** | Every new subagent starts at ~32k tokens. 283 agents cost ~4.9 M cache writes and ~4.3 M cache reads before doing any work. | ~6.5% of all cache writes (estimate: 4.9 M of ~75 M). Under 1% of cache reads. | Low. | High (measured) |
| 6 | **Smaller, fewer screenshots.** Downscale to about 1000 px on the long edge, crop to the region, never re-read the same PNG, and let a subagent judge and return text. | 277 PNG reads. Each added a median 2.1k tokens (p90 6.7k), which stays for every later turn of that agent. The same screenshot was read 3 times in several agents. | A 1920x1080 image is 2,691 tokens. 1000x563 would be about 756 (estimate from the formula). Second-order overall. | Medium. Small text may become unreadable. Untested. | Medium |
| 7 | **No repeated file slices.** Read a file range once, use summary scripts, and filter test output with a hook. | 36,768 Bash calls, 78 M chars. Heaviest: repeated `sed -n` slices of the same large files and `cat` of scratchpad files. | Second-order, not computed. | Low. | Medium |
| 8 | **Avoid cache rebuilds you can control.** Don't `/compact` or resume a session after a long idle break. Don't switch the main model or MCP servers mid-session. | 7 large cache rewrites (>100k in one turn), ~5 M tokens total. | Small (<1% of reads), but each rewrite is billed as a write. | None. | High |
| 9 | **Test, don't adopt yet: 1-hour subagent cache TTL.** | Subagents get a 5-minute cache by default. Cache writes (75 M) are small next to reads. | Unknown. 1-hour writes cost more per write. | None. | Low |

Exact settings and wording for CLAUDE.md are in `ai-instructions.md`.

**Estimate arithmetic** (all inputs from `sources/local-usage-2026-11-05-to-07.md`; none of this is a measured before/after result):

- Total cache read: 2,019 + 969 + 95 + 3 + 1 = 3,087 M. Subagents: 1,488 + 884 + 87 = 2,459 M (80%). Main threads: 3,087 - 2,459 = 628 M. Cache writes: 57.2 + 15.2 + 2.6 + 0.1 = 75.1 M.
- #1: project A 1,039 turns x (467k - 150k) = 329 M. project B 161 turns x (822k - 150k) = 108 M. Sum 437 M, which is 14.2% of 3,087 M. It uses the median context as the average, so it is rough. The 150k target is my choice.
- #2: in input-price units for Opus 5.5 (cache read 0.05, 5-minute cache write 1.25, output 5): reads 3,087 x 0.05 = 154, writes 75 x 1.25 = 94, output 13 x 5 = 65, total about 313. I assumed subagents are about 80% of that (about 250) because they are 80% of cache reads. That share is my assumption, not measured. Moving half of it to Sonnet (half the price) saves 250 x 0.5 x 0.5 = about 63, which is about 20% of 313.
- #4: 322 notices x 0.5 M = 161 M, which is 5.2% of 3,087 M.
- #5: 283 agents x 17.2k = 4.9 M written, and 283 x 15.3k = 4.3 M read. 4.9 / 75 = 6.5%. 4.3 / 3,087 = 0.14%. (The per-agent averages come from 291 first-turn transcripts, so this applies them to 283 agents.)
- #8: 4 (project A) + 3 (project B) = 7 rewrites, 2.5 M + 2.5 M = 5 M tokens.

### Question 2: "How to measure 'effectiveness'?"

Count a token saving as real only if the cost per finished task goes down **and** the quality signals do not get worse beyond the normal day-to-day noise.

- **Main cost metric:** cost-weight per finished task. Add up every turn of the task, including its subagents and failed or restarted attempts, with API-price weights (input 1, cache write 1.25 or 2, cache read 0.1, output 5). Failed attempts must be counted, because in agent benchmarks failures cost much more than successes (8.8 M vs 1.8 M tokens in SWE-Effi's example) [SWE-Effi](https://arxiv.org/html/2509.09853v2) — accessed 2026-11-07.
- **Quality guards, read from transcripts:** restart rate, owner correction rate, tool error rate, tests that fail and then get fixed (or end failing), commits reverted or re-edited within 24 h, rejected edits.
- **Process metrics** that explain changes: wake-ups per task, cache read per user turn, cache read per subagent.
- **Gold standard for model choices:** a fixed bank of repeatable tasks, run both ways, 3 trials each, scored on a checklist. Report pass^k (all k trials pass). This follows Anthropic's eval guidance [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — accessed 2026-11-07.

Full formulas, data sources and statistics rules are in `metrics.md`.

## Details

### Do cache reads even count against the Max plan?

This was the riskiest assumption. It is **not settled**.

- Anthropic's help pages describe Max limits only as a 5-hour session limit plus a weekly limit, shared by claude.ai and Claude Code. They do not say how input, output, cache reads or cache writes are weighted [Using Claude Code with Pro/Max](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) — accessed 2026-11-07; [How usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) — accessed 2026-11-07.
- What the docs do say: "a one-line question in a session that has been open all day still draws usage for the whole conversation". They list long context, cache misses, subagents and compaction as reasons usage climbs [Claude Code: Manage costs](https://code.claude.com/docs/en/costs) — accessed 2026-11-07.
- Community telemetry fits cache reads at about 0.1x input weight. An earlier fit gave 0x. A Claude Code team member said "prompt cache misses when using 1M token context window are expensive" and suggested `CLAUDE_CODE_AUTO_COMPACT_WINDOW=400000`. He did not confirm the weighting (read through a summarizing fetch) [GitHub issue #45756](https://github.com/anthropics/claude-code/issues/45756) — accessed 2026-11-07.
- On the API, Opus 5.5 cache reads cost 0.05x the input price ($0.20 vs $4 per M). There is no long-context premium for Opus 5.5 or Sonnet 5.5. A 900k request costs the same per token as a 9k one. Only Haiku 5.5 costs more above 100k [API pricing](https://platform.claude.com/docs/en/about-claude/pricing) — accessed 2026-11-07.

What this means for you (estimate): with API-style weights, 3.09 B cache reads at 0.05-0.1x equal about 155-310 M input-tokens' worth. Output (13 M x 5) is about 65 M and cache writes (75 M x 1.25) about 94 M. So cache reads would still be the biggest item. If the plan really weights cache reads at 0x, output, cache writes and agent count would matter more, and changes #1 and #3 would lose most of their value. The `/usage` command on Max shows usage by skill, subagent, plugin and MCP server, and flags long context and cache misses when they reach about 10% of usage [Manage costs](https://code.claude.com/docs/en/costs) — accessed 2026-11-07. Run it before and after the changes.

### Main thread: why 0.5-0.9 M context is the default and why to change it

- Models with a native 1M window, including Opus 4.7 and later and Sonnet 5 and later, auto-compact at about 967K by default. So your 467k-960k threads are normal default behavior, not a bug [Model configuration](https://code.claude.com/docs/en/model-config) — accessed 2026-11-07.
- The window can be set with `/autocompact`, the `autoCompactWindow` setting, `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, `--autocompact`, or per subagent [Model configuration](https://code.claude.com/docs/en/model-config) — accessed 2026-11-07.
- Docs: use `/clear` between unrelated tasks. It "costs nothing, and it means the next task doesn't keep paying for the previous one's history". The same page calls "manage the window aggressively" largely outdated advice, but still says "a focused context gets you better answers and costs less" [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) — accessed 2026-11-07.
- Quality at large context: Chroma tested 18 models including Claude Opus 4 and Sonnet 4 and found performance "consistently degrades with increasing input length" [Context Rot (Chroma)](https://www.trychroma.com/research/context-rot) — accessed 2026-11-07. RULER and NoLiMa found big drops by 32k on older models [RULER](https://arxiv.org/abs/2404.06654) — accessed 2026-11-07; [NoLiMa](https://arxiv.org/abs/2502.05167) — accessed 2026-11-07. Anthropic says Opus 4.6 is "markedly better" at this than earlier models [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) — accessed 2026-11-07. None of these test a 500k-900k Claude Code thread on Opus 5.5. So a quality gain from shorter threads is plausible, not shown.
- Handoff pattern: Anthropic's long-running agent harness uses a progress file, git log and an init script, read at the start of each fresh session [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — accessed 2026-11-07. Their context-engineering post recommends structured notes outside the window, and says subagents often return "1,000-2,000 tokens" to the lead [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — accessed 2026-11-07.
- What survives compaction: root CLAUDE.md, auto memory, up to 5 recent files, and skill bodies. Instructions given only in conversation are lost [Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07. So rules must live in files, not chat.

### Cache lifetimes and what breaks the cache

From [How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07:

- On a subscription within plan usage, the main conversation gets a 1-hour cache. Subagents, workflows, forks and compaction get 5 minutes.
- A non-fork subagent's "first request doesn't read the parent's cache". A fork does read it. A resumed subagent can read its earlier cache if it is still warm.
- These break the cache: switching model (each model has its own cache), toggling fast mode, changing the tool set (for example connecting an MCP server when tool search does not defer it), compaction, dropping old images, a Claude Code upgrade, and idling past the TTL. Changing effort does not break it on Opus 5.5 / Sonnet 5.5 / Haiku 5.5. Editing CLAUDE.md mid-session does not break it, and the edit is also not applied.
- `/compact` with a warm cache costs "a fraction of what the context size suggests". After a break longer than the TTL it reprocesses the whole history uncached, so compacting an old resumed session "costs the most".
- The API prompt-caching docs give the same TTL and prices [API prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — accessed 2026-11-07.

### Subagents

- A subagent's requests "count toward the same usage limits as your main conversation" [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07.
- Docs give no token count for start-up cost. Locally it is ~32k per agent (p10 31.7k, p90 35.2k), with ~17.2k newly written each time.
- Docs: use the main conversation for quick targeted changes and shared-context work. Use subagents for verbose output and self-contained work that returns a summary. A fork "costs less than a fresh subagent for tasks that need the same context" [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07. Anthropic's blog gives a rule of thumb of 10+ files or 3+ independent pieces before splitting work out [How and when to use subagents](https://claude.com/blog/how-and-when-to-use-subagents-in-claude-code) — accessed 2026-11-07.
- Multi-agent systems use about 15x the tokens of chat. Anthropic calls them a poor fit for work that needs shared context, and names coding as an example [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) — accessed 2026-11-07. These are research-task numbers, not coding numbers.
- Sonnet 5.5 vs Opus 5.5: Terminal-Bench 4.0 70.6 vs 66.4, CursorBench 4.0 55.5 vs 57.8, FrontierCode 1.1 52.1 vs 54.4. Sonnet is half the price. The page says Sonnet "complements Opus 5.5 best when running at lower effort settings". At max effort it sometimes fanned out to many subagents and timed out [Claude Sonnet 5.5](https://www.anthropic.com/news/claude-sonnet-5-5) — accessed 2026-11-07. These are vendor numbers, read once through a summarizer. Blog claims about Haiku and Sonnet quality are (unverified).
- Model selection order: per-call `model` parameter, then agent frontmatter, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the main model. The built-in Explore agent uses the main model (Opus on a subscription), not Haiku [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07. A fresh subagent has no cache anyway, so putting it on Sonnet loses no cache [How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.
- Collecting results: a background subagent's result reaches the main thread "as a completion notification in a later turn" [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07. The docs say nothing about merging several notices into one turn. Dynamic workflows keep intermediate results in the script, so "Claude's context holds only the final answer" [Dynamic workflows](https://code.claude.com/docs/en/workflows) — accessed 2026-11-07. Anthropic's research system has subagents store work externally and "pass lightweight references back" [Multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) — accessed 2026-11-07.

### Tool output and screenshots

- Image cost is ceil(w/28) x ceil(h/28) tokens. Opus 5.5 and Sonnet 5.5 use the high-res tier: up to 2,576 px and 4,784 tokens. 1000x1000 is 1,296 tokens, 1920x1080 is 2,691. The docs say to downsample if the detail is not needed, and warn that resizing can make text harder to read [Vision docs](https://platform.claude.com/docs/en/build-with-claude/vision) — accessed 2026-11-07. This matches the local 2-7k tokens per screenshot.
- Bash returns about 30,000 chars inline. Larger output is saved to a file with a 2,000-char preview. Read returns at most 25,000 tokens per call [Tools reference](https://code.claude.com/docs/en/tools-reference) — accessed 2026-11-07. These caps are per call, so they do not help with 36,768 small calls. A `sed -n` slice is not cheaper than Read with offset/limit. The saving comes from not reading the same file again.
- A PreToolUse hook can pipe test output through `grep ... | head -100`, "reducing context from tens of thousands of tokens to hundreds" [Manage costs](https://code.claude.com/docs/en/costs) — accessed 2026-11-07.
- Keep CLAUDE.md under 200 lines [How Claude remembers your project](https://code.claude.com/docs/en/memory) — accessed 2026-11-07. Yours appears to be within that (the researcher's line count, not measured), so no change is needed there.

### Measuring effectiveness: background

- Claude Code can export OpenTelemetry metrics (`claude_code.token.usage`, `claude_code.cost.usage` with main/subagent split, `code_edit_tool.decision`) and events (`tool_result`, `api_request`) [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage) — accessed 2026-11-07. They give cost and a few outcome signals, but no task boundaries and no correctness measure. Your local JSONL files already hold the same facts.
- ccusage reports tokens by day, session and 5-hour block, with cache reads and writes kept separate. It says nothing about quality [ccusage](https://github.com/ryoppippi/ccusage) — accessed 2026-11-07.
- Reading the next user prompt as a rating of the previous answer worked with "reasonable accuracy" in Google's study of 372 developers [Reading Between the Lines](https://arxiv.org/abs/2509.18361) — accessed 2026-11-07. This supports the correction-rate signal, but no study validates restart or revert counts for agent work.
- Don't trust "it felt fine". In METR's trial, developers believed AI made them 20% faster. The measured result was 19% slower [METR RCT](https://arxiv.org/abs/2507.09089) — accessed 2026-11-07.
- Treat evals as experiments with error bars [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) — accessed 2026-11-07. LLM judges show position, verbosity and self-enhancement bias [MT-Bench](https://arxiv.org/abs/2306.05685) — accessed 2026-11-07; [Self-Preference Bias](https://arxiv.org/html/2410.21819v1) — accessed 2026-11-07. A Claude judge grading Opus vs Sonnet output has that risk, so put code-checkable items first.

## Known Gaps

- How Max-plan limits weight cache reads, cache writes, input and output is not published. Only a community fit (~0.1x input for cache reads) exists.
- No measurement of Opus 5.5 / Sonnet 5.5 quality at 500k-900k context in an agent loop.
- No controlled data on Sonnet vs Opus for mechanical subagent jobs.
- Whether Claude Code merges several completion notices into one main-thread turn is not documented. The local transcripts could answer this.
- Whether settings.json keys, env vars and new agent definitions take effect in a running session is not stated in the sources (see `ai-instructions.md`).
- Screenshot resolution needed for the owner's UI checks is untested.
- Restart, correction and revert signals are not validated as quality measures in any fetched study.
- Savings estimates are the writer's arithmetic on local data, not measured before/after results. Q5 is still to do.

## Confidence

**Medium.** The local numbers are measured and the Claude Code mechanics (TTLs, compaction thresholds, subagent billing, image cost) come from current official docs that agree with each other. Confidence drops because the plan weighting is unknown, the quality side of every change is untested locally, and some numbers (Sonnet 5.5 benchmarks, GitHub issue quotes) were read through a summarizer.

## Completeness

**~70%.** Q1 (billing and caching), Q2 (main thread), Q3 (subagents), Q4 (tool output) and Q6 (metrics) are covered. Missing: the plan weight of cache reads, the Q5 before/after re-measure, a Sonnet vs Opus A/B, notification merging, and screenshot legibility.

## Appendix: prior, disconfirmer and rival hypothesis audit

**Prior:** the biggest wins are (1) smaller main threads, (2) fewer, batched wake-ups, (3) Sonnet for mechanical subagents. Screenshots and Bash output are second-order.

- (1) **Partly confirmed, but not the biggest pool.** Main threads are ~20% of cache read. Subagents are 80%. Shrinking the main thread is still the clearest single change (~14% estimate), but subagent changes (#2, #3, #5) together act on a larger pool.
- (2) **Confirmed as a cost, smaller than expected.** About 5% directly (estimate), and it overlaps with (1).
- (3) **Supported by vendor benchmarks and price, untested locally.**
- Screenshots and Bash being second-order: consistent with the data, but not measured exactly.

**Disconfirmer:** "cache reads at large context are nearly free against plan limits." **Not triggered, not ruled out.** The only fit (~0.1x, community, unverified) still leaves cache reads as the biggest weighted item. A 0x fit was also reported once.

**Riskiest assumption** (cache reads count in proportion to API price): **unverified.** The kill/pivot rule (pivot to output and agent count if cache reads are minor) was not triggered, because there is no evidence either way that they are minor.

**Rival hypothesis:** Sonnet quality drops cause enough restarts to eat the savings. **No local evidence either way.** Only 9 agents ran on Sonnet, so at least 9 of the 18 "restart" agents were restarts on Opus (arithmetic). Today's failures are not a Sonnet problem. The Sonnet 5.5 page reports small benchmark gaps and timeouts at max effort. The A/B in `metrics.md` is the test.

**Success metric (unchanged):** two days after the rules are adopted, the local scripts show lower cache read per user turn and per subagent, with no rise in restart agents.

## Sources

Local data: `sources/local-usage-2026-11-05-to-07.md` (scripts in `scripts/`). Research notes: `sources/q1-billing-and-caching.md`, `sources/q2-q4-context-and-tool-output.md`, `sources/q3-subagents.md`, `sources/q6-measuring-effectiveness.md`.

- [Using Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) — accessed 2026-11-07
- [How do usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) — accessed 2026-11-07
- [Claude Code: Manage costs effectively](https://code.claude.com/docs/en/costs) — accessed 2026-11-07
- [Claude Code: How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07
- [Claude Code: Model configuration](https://code.claude.com/docs/en/model-config) — accessed 2026-11-07
- [Claude Code: Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07
- [Claude Code: Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07
- [Claude Code: Best practices](https://code.claude.com/docs/en/best-practices) — accessed 2026-11-07
- [Claude Code: Tools reference](https://code.claude.com/docs/en/tools-reference) — accessed 2026-11-07
- [Claude Code: How Claude remembers your project](https://code.claude.com/docs/en/memory) — accessed 2026-11-07
- [Claude Code: Dynamic workflows](https://code.claude.com/docs/en/workflows) — accessed 2026-11-07
- [Claude Code: Monitoring (OpenTelemetry)](https://code.claude.com/docs/en/monitoring-usage) — accessed 2026-11-07
- [GitHub issue anthropics/claude-code #45756](https://github.com/anthropics/claude-code/issues/45756) — accessed 2026-11-07 (read via a summarizing fetch)
- [Anthropic API pricing](https://platform.claude.com/docs/en/about-claude/pricing) — accessed 2026-11-07
- [Anthropic API prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — accessed 2026-11-07
- [Anthropic vision docs](https://platform.claude.com/docs/en/build-with-claude/vision) — accessed 2026-11-07
- [Claude Sonnet 5.5 announcement](https://www.anthropic.com/news/claude-sonnet-5-5) — accessed 2026-11-07 (read via summarizer)
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) — accessed 2026-11-07
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) — accessed 2026-11-07
- [How and when to use subagents in Claude Code](https://claude.com/blog/how-and-when-to-use-subagents-in-claude-code) — accessed 2026-11-07
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — accessed 2026-11-07
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — accessed 2026-11-07
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — accessed 2026-11-07
- [Context Rot (Chroma)](https://www.trychroma.com/research/context-rot) — accessed 2026-11-07
- [RULER (arXiv 2404.06654)](https://arxiv.org/abs/2404.06654) — accessed 2026-11-07
- [NoLiMa (arXiv 2502.05167)](https://arxiv.org/abs/2502.05167) — accessed 2026-11-07
- [SWE-Effi (arXiv 2509.09853)](https://arxiv.org/html/2509.09853v2) — accessed 2026-11-07
- [Reading Between the Lines (arXiv 2509.18361)](https://arxiv.org/abs/2509.18361) — accessed 2026-11-07
- [METR developer productivity RCT (arXiv 2507.09089)](https://arxiv.org/abs/2507.09089) — accessed 2026-11-07
- [Adding Error Bars to Evals (arXiv 2411.00640)](https://arxiv.org/abs/2411.00640) — accessed 2026-11-07
- [MT-Bench / LLM-as-a-judge (arXiv 2306.05685)](https://arxiv.org/abs/2306.05685) — accessed 2026-11-07
- [Self-Preference Bias in LLM judges (arXiv 2410.21819)](https://arxiv.org/html/2410.21819v1) — accessed 2026-11-07
- [ccusage](https://github.com/ryoppippi/ccusage) — accessed 2026-11-07
