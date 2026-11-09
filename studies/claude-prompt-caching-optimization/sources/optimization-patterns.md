# Source: Caching Optimization Patterns

**Agent**: Research subagent 3 (partial — WebFetch denied for non-Anthropic domains)
**Sources**: Official Anthropic docs, search snippets from optimization articles
**Date**: 2026-02-23

## Core Principle: Prefix Stability

Cache works on exact prefix matching. Put static content first, dynamic content last.

## Breakeven Analysis (5-minute TTL)

| Uses (N) | Without Cache | With Cache | Savings |
|----------|--------------|------------|---------|
| 1 | 1.00x | 1.25x | -25% (loss) |
| 2 | 2.00x | 1.35x | 32.5% |
| 3 | 3.00x | 1.45x | 51.7% |
| 5 | 5.00x | 1.65x | 67.0% |
| 10 | 10.00x | 2.15x | 78.5% |

**Breakeven at N=2 for 5-minute TTL.** For 1-hour TTL (2.0x write): breakeven at ~N=2 (barely).

## Anti-Patterns

1. **Slightly varying prompts** — timestamps/IDs injected before cache breakpoint
2. **Too many short independent sessions** — each creates a cache write
3. **Changing tool definitions** between calls
4. **Dynamic content before static content** in system prompt
5. **Prompts below minimum cacheable length** (4096 for Opus)
6. **Concurrent first requests** — multiple writes instead of 1 write + N reads

## Session Structuring for Pipelines

### Long sessions (multi-turn)
Best when steps build on each other. Cache grows incrementally — max cache_read, minimal delta writes. But context grows and eventually hits limits.

### Independent calls with shared prefix
Best when steps don't reference prior turns. Cache system prompt once, each call's unique content is regular input. First call writes, subsequent calls read.

**Critical**: Serialize the first call. Wait for response before parallel calls.

## Monitoring

API response includes `cache_creation_input_tokens` and `cache_read_input_tokens`. Track read:write ratio per pipeline run. Target: (N_steps - 1):1 for N steps sharing a prefix.

**Sources:**
- [Prompt caching - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — accessed 2026-02-23
- [Optimizing costs with Anthropic's API batching and caching](https://www.ai.moda/en/blog/anthropics-batches-with-caching) — accessed 2026-02-23
- [Mastering 3 Key Points of Claude Caching Billing](https://help.apiyi.com/en/claude-prompt-caching-anthropic-native-format-guide-en.html) — accessed 2026-02-23
