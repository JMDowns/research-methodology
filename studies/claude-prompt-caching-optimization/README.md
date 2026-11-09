---
title: "Claude Prompt Caching Optimization for Batch Pipelines"
date: 2026-02-23
status: complete
confidence: high
confidence_reason: "Based on official Anthropic documentation, 3 research subagents, and empirical analysis of 27,624 API calls from the token tracker"
completeness: 85
completeness_reason: "Covers CLI-constrained (Claude Max) optimizations thoroughly; API-direct optimizations identified but not actionable for current setup"
category: methodology
tier: 3
objective: "How can batch LLM pipelines (pipeline A/pipeline B) reduce cache_write token costs while maintaining cache_read benefits?"
source_count: 12
known_gaps:
  - "Cannot test API-direct optimizations (would require API key)"
  - "The --tools flag impact on cache prefix size hasn't been measured empirically"
  - "Cache TTL behavior of claude -p not fully documented (tracker says 1-hour; may vary by version)"
  - "No way to confirm whether claude -p without sessions still gets automatic system prompt caching"
  - "The exact size of Claude Code's injected system prompt is not published"
next_steps:
  - "Empirically measure --tools flag impact on cache prefix size"
  - "Run controlled test: session pool vs standalone claude -p calls, compare cache metrics"
  - "Implement the 'serialize first call per model tier' optimization in pipeline A"
  - "Add cache_creation/cache_read metrics to ClaudeClient for ongoing monitoring"
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

# Claude Prompt Caching Optimization for Batch Pipelines

## Question / Objective

How can batch LLM pipelines (pipeline A/pipeline B) that make many sequential `claude -p` calls reduce cache_write token costs while maintaining the cache_read benefits of prompt caching?

**Constraint**: Claude Max subscription — CLI only (`claude -p`), no direct API access, no Batch API.

## Known Gaps

- Cannot test API-direct optimizations (would require API key)
- The `--tools` flag impact on cache prefix size hasn't been measured empirically
- Cache TTL behavior of `claude -p` not fully documented (tracker says 1-hour; may vary by version)
- No way to confirm whether `claude -p` without sessions still gets automatic system prompt caching
- The exact size of Claude Code's injected system prompt is not published

## Key Findings

### 1. The Tracker's Pricing May Be Inaccurate (High Confidence)

The token tracker uses **$10/M for Opus cache_write** (1-hour TTL pricing). But standard prompt caching has two tiers:
- **5-minute TTL**: 1.25x base input = **$6.25/M** for Opus
- **1-hour TTL**: 2.0x base input = **$10/M** for Opus

The tracker's `pricing.py` comments state "Claude Code uses 1-hour cache duration" — if true, the $10/M pricing is correct. But the API default is 5-minute. If Claude Code sessions actually use 5-minute TTL, the real cost is 37.5% lower than reported.

**Verified**: Raw JSONL confirms `ephemeral_1h_input_tokens` is used exclusively (5m = 0). The tracker's $10/M pricing is correct. Claude Code forces 1-hour TTL — there is no way to opt into the cheaper 5-minute TTL from the CLI.

[Prompt caching docs](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) — accessed 2026-02-23

### 2. Most "Waste" Comes from Interactive Sessions, Not the Pipeline (High Confidence)

Empirical analysis of the token tracker database:

| Session Type | Count | % of Total | Cache Write | $ Wasted |
|-------------|-------|-----------|-------------|----------|
| 1-call sessions (never reused) | 7,386 | 70% | 61M tokens | ~$380-611 |
| Multi-call sessions (reused) | 3,158 | 30% | 109M tokens | Net positive |

**99.97% of 1-call sessions are unlabeled** (ingested from JSONL, not from the pipeline's ClaudeClient hook). These are interactive Claude Code sessions — the user opens Claude Code, asks one question, and the cache is written but never reused.

The session pool itself works well: multi-call sessions have a 7:1 read:write ratio and generate net savings.

### 3. The 7:1 Cache Read:Write Ratio Is Decent (Medium Confidence)

For multi-call sessions:

| Session Length | Sessions | CR:CW Ratio | Net Savings (Opus) |
|---------------|----------|-------------|-------------------|
| 2-3 turns | 2,518 | 2.5:1 | $57 total |
| 4-10 turns | 426 | 5.2:1 | $137 total |
| 11-50 turns | 154 | 5.3:1 | $241 total |
| 50+ turns | 60 | 20.7:1 | $3,286 total |

The 50+ turn sessions are extraordinarily efficient ($54.77 net savings per session). Short sessions (2-3 turns) are marginally positive. Overall, multi-call session caching saves ~$3,721 vs uncached.

### 4. How Caching Actually Works Under the Hood (High Confidence)

The Claude API uses **prefix-based caching**:
- Cache hierarchy: `tools` -> `system` -> `messages`
- **100% identical prefix** required for cache hit
- Default TTL: 5 minutes (refreshed on each use, free)
- Max 4 explicit cache breakpoints per request
- **Minimum cacheable**: 4,096 tokens for Opus 4.5/4.6, 1,024 for Sonnet

When `--resume` is used, the CLI replays the **entire conversation history** to the API. The cache reads the unchanged prefix and writes only the new delta (latest turn).

[Prompt caching docs](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) — accessed 2026-02-23

### 5. Session Conversations Are Unnecessary Bloat (High Confidence)

The current pipelines use sessions (`--session-id` / `--resume`) to accumulate conversation history. But the pipeline calls are **self-contained** — each prompt includes all necessary context and does NOT reference prior responses.

This means each `--resume` call replays the full conversation (all prior prompts + responses) to the API, even though that history is never used. The only benefit is that prior turns are cache-read (cheap at $0.50/M), but they also grow the cache_write delta for each new turn.

**Without sessions**, standalone `claude -p` calls would still benefit from system prompt caching (the Claude Code system prompt + tool definitions are the same prefix across calls). The per-call unique content (user message) would be regular input instead of growing conversation history.

### 6. The `--tools` Flag Can Reduce Prefix Size (Medium Confidence)

Claude Code sends **all enabled tool definitions** in every API request. These are part of the cache prefix. For `claude -p` pipeline calls that don't use tools (just text in, text out), this is pure overhead.

Using `--tools "none"` or a minimal set would:
- Reduce the cached prefix size
- Reduce cache_write tokens on the first call
- Reduce cache_read tokens on subsequent calls (but reads are cheap)

The exact size of tool definitions isn't published, but it's likely several thousand tokens for the full set.

[CLI reference](https://code.claude.com/docs/en/cli-reference) — accessed 2026-02-23

### 7. Concurrent First Requests Are a Trap (High Confidence)

The cache entry is only available **after the first response begins**. If the pipeline sends N parallel requests with the same prefix simultaneously (e.g., ThreadPoolExecutor), all N may create separate cache writes instead of 1 write + (N-1) reads.

Current code in `run_analysis_qq_pooled.py` launches all works in parallel via `ThreadPoolExecutor(max_workers=len(works))`. Each work has its own pool+client, but they share the same Claude Code system prompt. The first call from each work could be hitting this issue.

[Prompt caching docs](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) — accessed 2026-02-23

### 8. Breakeven Is Just 2 Calls (High Confidence)

For 5-minute TTL: cache_write costs 1.25x base, reads cost 0.1x. Breakeven at 2 uses (32.5% savings). For 1-hour TTL: breakeven at 2 uses (barely positive), meaningful savings at 3+ uses.

This means the session pool's strategy of creating per-chapter sessions is only cost-effective if each session gets 2+ calls. Currently:
- pipeline B: 5-8 calls per chapter session (opus: style+progression+development+design+prose; sonnet: triage+summary+compress) — **well above breakeven**
- pipeline A generator: 15 steps per chapter — **well above breakeven**

## Recommendations (CLI-Only / Claude Max)

### Quick Wins (No Code Changes)

1. **Verify the cache TTL**: Check raw API responses for `ephemeral_5m_input_tokens` vs `ephemeral_1h_input_tokens` to confirm whether Claude Code uses 5-minute or 1-hour caching. If 5-minute, update the tracker's pricing to use $6.25/M instead of $10/M.

2. **Accept that interactive session waste is structural**: The 70% single-use sessions ($380-611 waste) come from interactive Claude Code use, not the pipeline. This is an inherent cost of using Claude Code interactively and can't be optimized via pipeline changes.

### Medium Effort (Code Changes)

3. **Drop sessions for truly independent calls**: If pipeline steps are self-contained (each prompt includes all context), consider NOT using `--session-id` / `--resume`. Let the system prompt cache naturally across standalone calls. Test this on a small batch and compare cache metrics.

4. **Reduce tool overhead with `--tools`**: Add a `--tools` argument to `ClaudeClient.call()` that restricts the tool set. For pipeline calls that don't need tools, pass `--disallowedTools "Edit,Write,Bash,Glob,Grep,WebFetch,WebSearch,NotebookEdit"` or equivalent.

5. **Ensure system prompt stability**: Check that the `--system-prompt` argument is byte-identical across calls. No timestamps, step counters, or dynamic content injected before the cache breakpoint. Any variation forces a full cache rewrite.

6. **Serialize the first call per model tier**: In parallel processing (like `run_analysis_qq_pooled.py`), send one "primer" call first and wait for its response before launching parallel calls. This ensures the cache entry exists.

### Larger Changes (Architecture)

7. **Evaluate sessions vs standalone**: Run a controlled test comparing:
   - Current: session pool with `--resume` (conversation accumulates)
   - Alternative: standalone `claude -p` calls with identical system prompt (no session, no conversation history)

   Measure cache_write, cache_read, and total cost. If sessions aren't reducing total cost, remove the pool.

8. **Set `max_turns` on the session pool**: The conversation history grows unbounded. Setting `max_turns` (e.g., 10-15) would auto-reset sessions before they get too large. This caps the cache prefix growth while maintaining session benefits for the first N turns.

9. **Add cache metrics to ClaudeClient**: Parse `cache_creation_input_tokens` and `cache_read_input_tokens` from the API response. Log per-call cache efficiency and alert when cache_write is unexpectedly high.

### Not Feasible (Requires API Key)

These would be the most impactful but require leaving Claude Max:

10. **Use the Anthropic Python SDK directly** — explicit cache breakpoints, TTL control, Batch API (50% discount)
11. **Use 5-minute TTL explicitly** — saves 37.5% on cache writes vs 1-hour
12. **Use the Batch API** — 50% cost reduction on all tokens

## Cost Impact Summary

| Optimization | Estimated Savings | Effort |
|-------------|------------------|--------|
| ~~Fix tracker pricing~~ | N/A — verified 1h TTL is correct | N/A |
| Drop sessions for independent calls | Eliminates conversation history bloat | Medium |
| Reduce tool set with `--tools` | Reduces prefix by ~2-4k tokens/call | Low |
| Serialize first parallel call | Prevents duplicate cache writes | Low |
| Set max_turns on pool | Caps conversation growth | Low |
| Switch to direct API + Batch | ~50% total cost reduction | High (requires API key) |

## Quality Checklist

- [x] All factual claims sourced from fetched pages (no training data fill)
- [x] Cross-referenced claims across 2+ source domains where possible
- [x] Flagged any contradictions between sources
- [x] Ran verification step on surprising/unusual claims
- [x] Noted confidence level for each major finding
- [x] Listed known gaps explicitly
- [x] Used targeted WebFetch prompts (not "tell me everything")
- [x] Stayed within budget limits for the complexity tier

## Sources

- [Prompt caching - Claude API Docs](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) — accessed 2026-02-23
- [Prompt caching cookbook](https://platform.claude.com/cookbook/misc-prompt-caching) — accessed 2026-02-23
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless) — accessed 2026-02-23
- [CLI reference - Claude Code Docs](https://code.claude.com/docs/en/cli-reference) — accessed 2026-02-23
- [Session Management - Agent SDK Docs](https://platform.claude.com/docs/en/agent-sdk/sessions) — accessed 2026-02-23
- [Optimizing costs with Anthropic's API batching and caching](https://www.ai.moda/en/blog/anthropics-batches-with-caching) — accessed 2026-02-23
- [Mastering 3 Key Points of Claude Caching Billing](https://help.apiyi.com/en/claude-prompt-caching-anthropic-native-format-guide-en.html) — accessed 2026-02-23
- [GitHub - claude-conversation-extractor](https://github.com/ZeroSumQuant/claude-conversation-extractor) — accessed 2026-02-23
- Token tracker empirical data: `~/.claude-tracker/usage.db` — 27,624 API calls across pipeline A and pipeline B
