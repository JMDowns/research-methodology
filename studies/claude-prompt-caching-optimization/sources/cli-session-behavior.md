# Source: CLI Session Caching Behavior

**Agent**: Research subagent 2
**Sources**: Claude Code docs, Agent SDK docs, community analysis
**Date**: 2026-02-23

## Session Storage

Sessions saved as JSONL files at `~/.claude/projects/`, organized per project. Each session stores full message history (user messages, assistant responses, tool use blocks, tool results).

## --session-id vs --resume

- `--session-id UUID`: Sets session ID for a new conversation
- `--resume UUID`: Loads conversation history and sends full context to API
- The API is **stateless** — there is no server-side session state. Every call with `--resume` sends the ENTIRE conversation history in the `messages` array.

## How Sessions Map to API Caching

Claude Code **automatically enables prompt caching**. The multi-turn flow:

| Request | Cache Behavior |
|---------|---------------|
| Request 1 (new session) | Everything written to cache |
| Request 2 (resume) | Prior turns read from cache; new content written |
| Request 3 (resume) | Prior turns read from cache; new content written |

**5-minute TTL default**: If >5 minutes between calls, cache expires and next call pays full cache write cost. Claude Code uses **1-hour TTL** internally.

## CLI Overhead

- Claude Code injects its own system prompt (several thousand tokens)
- Tool definitions for ALL enabled built-in tools sent in every request
- Can reduce with `--tools "Bash,Read"` (restrict tool set)
- Auto-compaction and background summarization consume additional tokens

## Flags Affecting Caching

| Flag | Effect |
|------|--------|
| `--no-session-persistence` | Disables disk save, NOT API caching |
| `--tools` | Changes tool prefix = invalidates cache |
| `--system-prompt` | Changes system prefix = invalidates cache |
| `--model` | Different models = different cache entries |

**No CLI flag to control cache TTL or explicit breakpoints** — Claude Code manages internally.

## For Batch Workloads

Options ranked by control level:
1. **Messages API directly** — full cache control, Batch API (50% discount) — requires API key
2. **Agent SDK** — programmatic, structured outputs — requires API key
3. **claude -p with sessions** — automatic caching, no control over TTL/breakpoints — works with Claude Max

**Sources:**
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless) — accessed 2026-02-23
- [Prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — accessed 2026-02-23
- [CLI reference](https://code.claude.com/docs/en/cli-reference) — accessed 2026-02-23
- [Session Management - Agent SDK](https://platform.claude.com/docs/en/agent-sdk/sessions) — accessed 2026-02-23
