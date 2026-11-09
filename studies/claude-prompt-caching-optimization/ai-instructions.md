# AI Instructions: Prompt Caching Optimization

These instructions describe how to optimize Claude prompt caching in `claude -p` pipeline workloads (Claude Max / CLI-only).

## Decision: When to Use Sessions

```
Does this pipeline step reference prior turns in the conversation?
    │
    ├── YES → Use sessions (--session-id / --resume)
    │         Session accumulates context that later turns build on.
    │
    └── NO → Consider standalone calls (no session)
             Each call is self-contained with its own prompt + context.
             System prompt caching still works across standalone calls.
```

**Current state**: Both pipeline A and pipeline B use sessions for ALL calls, but the calls are self-contained (each prompt includes all context). This means conversation history accumulates uselessly, increasing cache_write per turn.

## When Sessions ARE Worth It

Sessions break even at **2 calls** (5-minute TTL) or **2-3 calls** (1-hour TTL). Use sessions when:

- The session will get 3+ calls within the cache TTL
- Steps genuinely build on each other (later prompts reference earlier responses)
- The system prompt + context is large (>4,096 tokens for Opus) and identical across calls

## Reducing Cache Overhead (CLI-Only)

### 1. Restrict Tool Definitions

Add to `ClaudeClient.call()`:
```python
cmd = ["claude", "-p", "--output-format", "json", "--model", model]
# For pipeline calls that don't use tools:
cmd.extend(["--disallowedTools", "Edit,Write,Bash,Glob,Grep,WebFetch,WebSearch,NotebookEdit,Task"])
```

This removes tool definitions from the cache prefix, reducing cache_write on first call and cache_read on subsequent calls.

### 2. Keep System Prompts Byte-Identical

Any variation in the `--system-prompt` argument invalidates the cache. Do NOT include:
- Timestamps or dates
- Step names or phase counters
- Request IDs or random values
- Dynamic content that changes per call

Put all dynamic content in the **user message** (after the cache prefix), not in the system prompt.

### 3. Serialize First Parallel Call

When launching parallel calls (e.g., ThreadPoolExecutor):

```python
# WRONG: All workers start simultaneously → multiple cache writes
with ThreadPoolExecutor(max_workers=N) as ex:
    futures = [ex.submit(call, work) for work in works]

# RIGHT: Prime the cache first, then parallelize
first_result = call(works[0])  # This creates the cache entry
with ThreadPoolExecutor(max_workers=N-1) as ex:
    futures = [ex.submit(call, work) for work in works[1:]]
```

### 4. Cap Session Length

Set `max_turns` on SessionPool to prevent unbounded conversation growth:

```python
pool = SessionPool(state_dir=output_dir / "pool_state", max_turns=15)
```

After 15 turns, the session auto-resets. This caps the cache prefix size while maintaining benefits for the first N turns.

### 5. Add Cache Metrics to ClaudeClient

Parse cache fields from the JSON response:

```python
usage = data.get("usage", {})
cache_read = usage.get("cache_read_input_tokens", 0)
cache_write = usage.get("cache_creation_input_tokens", 0)
# Also check TTL breakdown:
cache_creation = usage.get("cache_creation", {})
tokens_5m = cache_creation.get("ephemeral_5m_input_tokens", 0)
tokens_1h = cache_creation.get("ephemeral_1h_input_tokens", 0)
```

Log these per call and compute read:write ratios per pipeline run. Target ratio: (N_steps - 1):1.

## Testing the Impact

To verify whether dropping sessions helps:

1. Run the same pipeline on the same input with sessions (current behavior)
2. Run again without sessions (remove `session_id` / `is_new_session` from calls)
3. Compare:
   - Total cache_write tokens
   - Total cache_read tokens
   - Total cost
   - Quality of output (should be identical)

If standalone calls are cheaper, remove the session pool entirely.

## Reference: Cache Pricing

| Model | Base Input | 5m Write | 1h Write | Read |
|-------|-----------|----------|----------|------|
| Opus 4.5/4.6 | $5/M | $6.25/M | $10/M | $0.50/M |
| Sonnet 4/4.5/4.6 | $3/M | $3.75/M | $6/M | $0.30/M |
| Haiku 4.5 | $1/M | $1.25/M | $2/M | $0.10/M |

## Reference: What Breaks the Cache

| Change | Impact |
|--------|--------|
| Different tool definitions | Entire cache invalidated |
| Different system prompt | System + messages invalidated |
| Different model | Different cache entry |
| Toggle web search/citations | System + messages invalidated |
| Change thinking parameters | Messages invalidated |
| Non-deterministic JSON key ordering | Tools invalidated |
