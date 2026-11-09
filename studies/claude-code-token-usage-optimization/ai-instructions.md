# AI instructions: Claude Code token use

Rules and settings from `README.md`, ready to paste into `~/.claude/CLAUDE.md` or project memories. Each item gives the exact setting names as the sources give them, plus the evidence line. Local numbers come from `sources/local-usage-2026-11-05-to-07.md`. Values marked "(suggestion)" are not given by any source. They are the writer's starting points to test.

## 1. Main-thread context: auto-compact window and fresh sessions

**Settings** (all from [Model configuration](https://code.claude.com/docs/en/model-config) — accessed 2026-11-07):
- In session: `/autocompact 400k`
- settings.json: `autoCompactWindow`
- Env var: `CLAUDE_CODE_AUTO_COMPACT_WINDOW=400000`
- CLI flag: `--autocompact`
- `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` makes 1M models compact at 200K (too blunt for most uses).

**Rule:**
- Set the auto-compact window to 400000 as a backstop. A Claude Code team member suggested this value in [GitHub issue #45756](https://github.com/anthropics/claude-code/issues/45756) — accessed 2026-11-07 (read via a summarizing fetch).
- Before that point, at a natural break and at around 200-300k context (suggestion), write a handoff file and start a fresh session.
- Use `/clear` when switching to unrelated work.
- Don't resume a weeks-old session. Start fresh from the handoff file instead.

**Evidence:**
- The default auto-compact point for native-1M models (Opus 4.7+, Sonnet 5+) is about 967K, so 0.5-0.9 M threads are the default behavior [Model configuration](https://code.claude.com/docs/en/model-config) — accessed 2026-11-07.
- Locally, the project A main thread had a median of 467k context, with 500 of 1,039 turns over 500k. project B had a median of 822k. The project A session started 2026-10-03 and has been resumed for a month.
- `/clear` "costs nothing" [Best practices](https://code.claude.com/docs/en/best-practices) — accessed 2026-11-07.

## 2. Handoff file pattern

**Rule:** keep a handoff file in the project (for example `HANDOFF.md` or the existing `SESSION_NOTES.md`). A fresh session reads it, plus `git log`, first. Update it at each natural break. Contents:
1. The goal and the definition of done.
2. What is finished, with commit hashes.
3. What is in progress, plus running background agents and where their result files will appear.
4. Open decisions and questions for the owner.
5. The next 1-3 steps.
6. File paths the next session must read. Give paths, not pasted content.

**Rules that must survive compaction go in files** (CLAUDE.md, memory), not in chat. Instructions given only in conversation are lost at compaction. Root CLAUDE.md and auto memory survive [Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07.

**Evidence:** Anthropic's harness uses a progress file, git log and `init.sh`, read at the start of each fresh session, and ends each session with a commit and a progress update [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — accessed 2026-11-07. "Once SPEC.md exists, start a fresh session to build from it" [Best practices](https://code.claude.com/docs/en/best-practices) — accessed 2026-11-07.

## 3. Subagent model defaults

**Settings** ([Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07):
- Per call: the Agent tool's `model` parameter. It accepts the aliases `sonnet`, `opus`, `haiku`, `fable` only.
- Agent definition frontmatter: `model: sonnet`. Accepts an alias, a full ID, or `inherit`.
- Env var: `CLAUDE_CODE_SUBAGENT_MODEL=sonnet`. Since v2.1.251 this is only a default. Order: per-call parameter, then frontmatter, then this variable, then the main model. To force it on every subagent, also set `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`. It does not change the built-in Explore and Plan agents.
- Built-in Explore uses the main model (Opus on a subscription). To change it, define a user or project agent named `Explore` with its own `model:`. The docs mention `model: haiku` for simple subagents [Manage costs](https://code.claude.com/docs/en/costs) — accessed 2026-11-07. Haiku coding quality is reported weaker (unverified), and Haiku 5.5 costs 5x more on the API above 100k tokens [API pricing](https://platform.claude.com/docs/en/about-claude/pricing) — accessed 2026-11-07. So `sonnet` is the safer choice for an Explore override (suggestion).

**Rule:**
- Pass `model: "sonnet"` for mechanical jobs: test runs, edits from a clear spec, log triage, recurring cycle jobs, summaries, file searches.
- Keep Opus for architecture and design, unknown failures, reviews, and anything the owner will judge on quality.
- Don't run Sonnet subagents at max effort (suggestion, based on the Sonnet 5.5 page's timeout note).
- Don't set `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`, so explicit Opus choices still work.

**Evidence:**
- Locally, 274 of 283 subagents ran on Opus.
- Sonnet 5.5 is half Opus 5.5's price ($2/$10 vs $4/$20 per M; cache read $0.10 vs $0.20). It scores close on agentic coding benchmarks. It "complements Opus 5.5 best when running at lower effort settings". At max effort it caused timeouts by fanning out to many subagents [Claude Sonnet 5.5](https://www.anthropic.com/news/claude-sonnet-5-5) — accessed 2026-11-07 (vendor numbers, read via summarizer).
- A fresh subagent has no cache, so a different model loses nothing. Switching the main thread's model does lose its cache [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.

## 4. Long subagents: per-agent compaction and handoff

**Settings** ([Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07):
- Agent frontmatter `autoCompactWindow`: a plain integer from 100000 to 1000000, v2.1.296+.
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` also applies to subagents.

**Rule:**
- Long agent jobs end at about 60 tool calls with a state file. The next pass is a fresh agent with a short brief and the state file path. This matches the existing project A memory rule.
- For agent definitions that run long, set `autoCompactWindow: 200000` (suggestion).
- To continue an agent, resume it with SendMessage right away. Within 5 minutes it reads its old cache. Otherwise start a fresh agent from the state file, because resumed history keeps growing.

**Evidence:**
- Locally, the median agent ran 65 turns at 101k context. The biggest project B agents ran 150-239 turns, reached 450k-670k, and read 40-97 M cache tokens each.
- A resumed subagent can read its original cache if within TTL [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.
- Anthropic's research system summarizes finished phases to external memory and spawns fresh subagents near limits [Multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) — accessed 2026-11-07.

## 5. Subagent cache TTL (test before adopting)

**Settings** ([How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07):
- Main thread: `promptCacheTtl` / `CLAUDE_CODE_PROMPT_CACHE_TTL`.
- Subagents and other requests: `subagentPromptCacheTtl` / `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` (v2.1.242+).
- Per agent: frontmatter `experimental.cacheTtl` (v2.1.248+). 1h is ignored while on usage credits.
- `idleCompaction` (v2.1.290+) compacts long idle conversations on the 1-hour TTL.

**Rule:**
- Leave the default (5 minutes for subagents) globally.
- Test `experimental.cacheTtl: 1h` on one agent type that pauses more than 5 minutes between turns, such as agents waiting on game test runs. Compare its cache writes before and after.

**Evidence:**
- Subagents "get five minutes even on a subscription". The main thread gets 1 hour within plan usage. 1-hour writes cost 2x base input vs 1.25x for 5-minute writes [API prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — accessed 2026-11-07.
- Locally, cache writes (~75 M) are small next to cache reads (3.09 B), so the upside is uncertain.

## 6. Result files instead of one wake-up per agent

**Rule:**
- A background agent writes its full result to a file (for example `results/<task>-<agent>.md`) and returns one line: status plus the file path.
- When launching several agents for one job, either launch one aggregator agent that waits for them and reports once, or let the orchestrator read the result files only when all are done.
- Recurring cycle jobs (read cycle, triage cycle) become dynamic workflows, so their intermediate results stay out of the orchestrator's context.

**Evidence:**
- Locally, 322 of 379 project A main-thread wake-ups were completion notices, each at ~0.5 M context (~160 M cache read, estimate). 30 agents were recurring cycle jobs.
- A background result arrives "as a completion notification in a later turn" [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07.
- With workflows, "Claude's context holds only the final answer". Up to 16 concurrent agents, 1,000 per run, and `agent()` accepts a JSON `schema` [Dynamic workflows](https://code.claude.com/docs/en/workflows) — accessed 2026-11-07.
- Subagents "pass lightweight references back to the coordinator" [Multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) — accessed 2026-11-07.
- Caution: a relay of agents passing state through files is worse than one session for sequential work [How and when to use subagents](https://claude.com/blog/how-and-when-to-use-subagents-in-claude-code) — accessed 2026-11-07.

## 7. Inline vs subagent vs fork

**Rule:**
- Do a job inline if it needs only a few tool calls.
- Spawn a subagent for verbose output (tests, logs, docs), self-contained work, or 10+ files / 3+ independent pieces.
- Use a fork when the job needs the same context the main thread already has.

**Settings:** `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (default 20). Fork mode has been on by default since v2.1.302. In fork mode Claude cannot wait for a subagent. `CLAUDE_CODE_FORK_SUBAGENT=0` turns this off [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07.

**Evidence:**
- Locally, every subagent starts at ~32k tokens. 283 agents cost ~4.9 M cache writes plus ~4.3 M cache reads before doing any work.
- A fork "costs less than a fresh subagent for tasks that need the same context" [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — accessed 2026-11-07.
- The 10+ files / 3+ pieces rule of thumb comes from [How and when to use subagents](https://claude.com/blog/how-and-when-to-use-subagents-in-claude-code) — accessed 2026-11-07.

## 8. Screenshot handling

**Rule:**
- Downscale screenshots to about 1000 px on the long edge before reading them, unless small text must be read (suggestion; legibility untested).
- Crop to the region being checked.
- Never Read the same PNG twice in one agent. Write down what you saw instead.
- Do visual checks in a subagent that returns a text verdict, so the image never enters the orchestrator's context.

**Evidence:**
- Tokens = ceil(w/28) x ceil(h/28). 1920x1080 = 2,691 and 1000x1000 = 1,296 on the high-res tier used by Opus 5.5 / Sonnet 5.5. The docs say to downsample if the extra fidelity is not needed, and warn that resizing can make text less legible [Vision docs](https://platform.claude.com/docs/en/build-with-claude/vision) — accessed 2026-11-07.
- Claude Code drops the oldest images in batches when limits are hit, which rebuilds part of the cache [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.
- Locally, 277 PNG reads added a median 2.1k tokens each (p90 6.7k), and the same screenshot was re-read 3 times in several agents.

## 9. Bash and Read output

**Rule:**
- Find the location with `grep -n` first, then read that range once with Read offset/limit.
- Don't re-slice the same large file with repeated `sed -n`. Note what you learned instead.
- For repeated checks, write a small summary script that prints only the numbers needed.
- Filter test output with a PreToolUse hook, for example piping through `| grep -A 5 -E '(FAIL|ERROR|error:)' | head -100`.
- Don't raise `bashOutputMaxChars` or `BASH_MAX_OUTPUT_LENGTH` (suggestion: the caps are per call, so raising them does not help).

**Evidence:**
- Bash returns about 30,000 chars inline. Larger output goes to a file with a 2,000-char preview. Read returns at most 25,000 tokens (`CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`) [Tools reference](https://code.claude.com/docs/en/tools-reference) — accessed 2026-11-07.
- The hook example "reduc[es] context from tens of thousands of tokens to hundreds" [Manage costs](https://code.claude.com/docs/en/costs) — accessed 2026-11-07.
- Locally: 36,768 Bash calls, 78 M chars, mostly repeated `sed -n` slices and `cat` of scratchpad files.

## 10. Things that rebuild the cache

**Rule:** in a long main session, don't switch the main model (this includes `opusplan` toggles and skills with a `model` frontmatter), don't toggle fast mode, and don't connect or remove MCP servers. Changing effort is fine. Don't `/compact` after a break longer than the cache TTL. Compact at a natural break while the cache is warm, or start fresh instead.

**Evidence:** [How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07. Locally there were 7 large cache rewrites (~5 M tokens).

## 11. Measure before and after

Run `/usage` before the changes and again 2 days later. On Max it shows usage by skill, subagent, plugin and MCP server, and flags long context and cache misses when they reach about 10% of usage [Manage costs](https://code.claude.com/docs/en/costs) — accessed 2026-11-07. Then re-run `scripts/agg*.py` (with `python3 -I`) and compare against the metrics in `metrics.md`.

## Applying to sessions that are already running

Based only on what the sources say. Anything they don't cover is listed as an open question.

**Works right away in a running session:**
- `/autocompact 400k`, `/compact focus on X`, `/clear`, and `/rewind` > "Summarize from here" are in-session commands [Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07. Whether `/autocompact` also carries over to later sessions is not stated.
- Per-call `model: "sonnet"` on the Agent tool. The orchestrator can use it on its next spawn. Tell it in a message, but the instruction is lost at the next compaction unless it is also in a file that survives compaction (root CLAUDE.md or auto memory) [Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07.
- Behavior rules (result files, handoff at ~60 calls, screenshot handling, no repeated slices) can be given by message the same way, with the same compaction caveat.
- Changing effort does not break the cache on Opus 5.5 / Sonnet 5.5 / Haiku 5.5 [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.
- Background agents keep running through compaction [Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07. Compacting or handing off does not kill running agents. A fresh session does not receive their completion notices, though (inference, not stated). Let them finish or record their result-file paths in the handoff file first.

**Needs a new session:**
- Edits to CLAUDE.md made mid-session are not applied to the running session (and do not break its cache) [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.
- The main fix (a small orchestrator) means a fresh session from a handoff file. The first turn of that session writes a new cache. That is cheaper than a cold `/compact` of a large thread, which "costs the most" [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.

**Avoid in a running large session:** switching the main model, toggling fast mode, connecting or removing MCP servers, and upgrading Claude Code. Each one invalidates the cache [Prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07.

**Open questions (not in the sources):**
- Whether settings.json keys (`autoCompactWindow`, `subagentPromptCacheTtl`, `promptCacheTtl`, `bashOutputMaxChars`, `idleCompaction`) are re-read by a running session, or only at startup.
- Whether env vars (`CLAUDE_CODE_AUTO_COMPACT_WINDOW`, `CLAUDE_CODE_SUBAGENT_MODEL`, `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL`) can change for a running session at all. Env vars are normally fixed at process start, but the sources don't say (unverified).
- Whether a new or edited agent definition file (with `model:`, `autoCompactWindow`, `experimental.cacheTtl`) is picked up by a running session.
- Whether CLAUDE.md edits are picked up after a compaction in the same session. The docs say root CLAUDE.md survives compaction, but not whether it is re-read from disk.
- Whether new auto-memory files are seen by a running session before its next compaction.
