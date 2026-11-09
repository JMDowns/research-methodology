# Source: API-Level Caching Mechanics

**Agent**: Research subagent 1
**Sources**: Official Anthropic docs, Anthropic cookbook
**Date**: 2026-02-23

## What Gets Cached

Cache stores KV cache representations + cryptographic hashes (not raw text). Cacheable content: tool definitions, system messages, text messages (user+assistant), images, documents, tool use/results. Thinking blocks cannot be explicitly cached but ARE cached implicitly in tool-use loops.

Cache is **prefix-based**: `tools` -> `system` -> `messages`. Everything up to and including the `cache_control` block is cached as a contiguous prefix.

## Cache Hit/Miss Triggers

- **100% identical prefix** required for cache hit
- Backward sequential checking with 20-block lookback window
- Cache keys are cumulative: hash for each block depends on all prior content

### What Invalidates Cache

| Change | Impact |
|--------|--------|
| Tool definitions modified | Entire cache invalidated |
| Web search toggle | System + messages invalidated |
| Citations toggle | System + messages invalidated |
| Speed setting change | System + messages invalidated |
| tool_choice changed | Messages invalidated |
| Thinking parameters changed | Messages invalidated |
| Unstable JSON key ordering | Tools invalidated |

**Concurrency**: Cache entry only available after first response **begins**. Parallel requests before first response = multiple cache writes.

## TTL and Pricing

- Default: **5-minute TTL**, refreshed on each use (free)
- Extended: **1-hour TTL** at 2x base input price (not 1.25x)

| Token Type | Multiplier vs Base Input |
|-----------|-------------------------|
| 5-minute cache write | 1.25x |
| 1-hour cache write | 2.0x |
| Cache read (hit) | 0.1x |

For Opus 4.6 ($5/M base): 5m write = $6.25/M, 1h write = $10/M, read = $0.50/M

## Minimum Cacheable Sizes

| Model | Minimum |
|-------|---------|
| Opus 4.5/4.6, Haiku 4.5 | 4,096 tokens |
| Sonnet 4/4.5/4.6, Opus 4/4.1 | 1,024 tokens |
| Haiku 3/3.5 | 2,048 tokens |

## cache_control Parameter

- **Automatic mode**: `cache_control` at request body level -> breakpoint on last cacheable block, moves forward automatically
- **Explicit mode**: `cache_control` on individual content blocks (max 4 breakpoints)
- Only type: `"ephemeral"`, optional `ttl`: `"5m"` or `"1h"`

**Sources:**
- [Prompt caching - Claude API Docs](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) — accessed 2026-02-23
- [Prompt caching cookbook](https://platform.claude.com/cookbook/misc-prompt-caching) — accessed 2026-02-23
