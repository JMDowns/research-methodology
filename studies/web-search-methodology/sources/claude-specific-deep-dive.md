# Claude Code WebSearch/WebFetch Deep Dive

**Surveyed**: 2026-02-22
**Search queries used**: ~10
**Sources found**: 20+

## 1. WebFetch Internals (3-Stage Pipeline)

### Architecture
- **Stage 1 — HTML Conversion**: Turndown library converts HTML to Markdown, stripping nav/scripts/CSS
- **Stage 2 — Smart Filtering**: Claude Haiku 3.5 processes Markdown against user's prompt, extracting only relevant sections
- **Stage 3 — Caching**: 15-minute TTL, LRU cache with 50MB limit

### Key Numbers
- Maximum fetch size: ~10 MB
- Markdown truncation: 100 KB of text
- URL max length: 250 characters (official) / 2,000 characters (observed)
- **125-character maximum for direct quotes** on untrusted sites
- Paraphrasing required outside quotation marks

### Trusted Sites Fast-Path
~80 documentation domains (Python docs, MDN, React, Kubernetes, AWS) bypass Haiku filtering step. Content-Type: text/markdown under 100k chars goes straight through. Trusted sites get more generous extraction — "relevant details, code examples and documentation excerpts." Untrusted sites get the strict 125-char quote limit.

### Security Model
- Claude cannot dynamically construct URLs — only fetch URLs provided by user or from prior WebSearch/WebFetch
- Domain validation via `https://claude.ai/api/web/domain_info`
- Deny-list maintained; robots.txt considered
- Cross-host redirects need explicit approval; same-host redirects auto-followed

**Sources**:
- [Inside Claude Code's Web Tools](https://mikhail.io/2025/10/claude-code-web-tools/) — accessed 2026-02-22
- [How Claude Code Eats the Web](https://giuseppegurgone.com/claude-webfetch) — accessed 2026-02-22
- [Anthropic Web Fetch Tool Docs](https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/web-fetch-tool) — accessed 2026-02-22

## 2. WebSearch Internals

- Returns only `title` and `url` (discards page_age, encrypted_content)
- To get content, must follow up with WebFetch
- Not available on Bedrock/Vertex
- Parameters: query (min 2 chars), allowed_domains[], blocked_domains[], max_uses, user_location
- **Pricing: $10 per 1,000 searches** + standard token costs
- **WebFetch: no additional charges** beyond token costs

**Source**: [Anthropic Web Search Tool Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) — accessed 2026-02-22

## 3. Dynamic Filtering (New 2026)

Tool versions `web_fetch_20260209` and `web_search_20260209` support dynamic filtering with Opus 4.6 and Sonnet 4.6. Claude writes and executes code to filter fetched content BEFORE it enters the context window. Requires code execution tool to be enabled.

Use cases: extracting specific sections from long docs, processing structured data, filtering PDFs, reducing tokens on large documents.

**Source**: [Anthropic Docs](https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/web-fetch-tool) — accessed 2026-02-22

## 4. Extended Thinking + Web Search

| Mode | Best For | Tool Calls |
|------|----------|------------|
| Web Search | Quick factual queries | 1-2 |
| Extended Thinking | Complex reasoning, no web | 0 |
| Research | Comprehensive synthesis | 5+, 1-3 min |

Research mode auto-enables extended thinking. **Interleaved thinking** (beta: `interleaved-thinking-2025-05-14`) enables reasoning between tool calls — evaluating results, identifying gaps, refining queries.

Key insight: Extended thinking helps NOT with formulating individual queries, but with **between-tool-call reasoning** — adapting strategy based on what's found.

**Sources**:
- [When to Use Web Search vs Thinking vs Research](https://support.claude.com/en/articles/11095361) — accessed 2026-02-22
- [Building with Extended Thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) — accessed 2026-02-22

## 5. Anthropic's Own Multi-Agent Research Architecture

Orchestrator-worker pattern:
1. Lead agent assesses complexity, determines subagent count, defines roles
2. Scaling: simple = 1 agent, 3-10 calls. Comparison = 2-4 subagents, 10-15 calls each. Complex = 10+ subagents
3. Subagents run in parallel (3+ simultaneously), use interleaved thinking after results
4. Start with **short broad queries, evaluate, then progressively narrow**
5. Lead agent saves plans to memory (context windows get truncated)

**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-02-22

## 6. Subagents for Research — Best Practices

- Each subagent gets its own **200k context window**
- Cannot nest subagents
- Parallelism caps ~10 concurrent
- `CLAUDE_CODE_SUBAGENT_MODEL` env var routes subagents to cheaper models
- Background execution keeps main thread free
- Context isolation: verbose output stays in subagent, only summary returns

Built-in agents: Explore (Haiku), Plan (inherits), General-purpose (inherits), Bash (inherits)

**Sources**:
- [Claude Code Sub-Agents Docs](https://code.claude.com/docs/en/sub-agents) — accessed 2026-02-22
- [Sub-Agent Best Practices](https://claudefa.st/blog/guide/agents/sub-agent-best-practices) — accessed 2026-02-22

## 8. WebFetch Prompt Engineering

The `prompt` parameter goes to **Haiku**, not to the main model. Effective patterns:
1. Be specific and extractive ("Extract all API endpoints, methods, params, return types")
2. Ask for structured output ("List each option with default value and data type")
3. Specify inclusions AND exclusions ("Extract pricing tiers. Ignore marketing copy")
4. Use enumeration ("List all 5 steps with code examples for each")
5. Remember the 125-char quote limit on untrusted sites

Anti-patterns:
- "Tell me everything about this page" — too broad for Haiku
- Expecting raw content — WebFetch always filters through Haiku
- Ignoring trusted-site distinction — prompts can be more generous for docs sites

**Takeaway**: Write prompts as if directing a fast junior researcher.

**Sources**:
- [Inside Claude Code's Web Tools](https://mikhail.io/2025/10/claude-code-web-tools/) — accessed 2026-02-22
- [WebFetch System Prompt](https://github.com/gregkonush/claude-system-prompts/blob/main/webfetch-tool-instructions.md) — accessed 2026-02-22

## 9. Token Costs

| Content Type | Size | ~Tokens |
|-------------|------|---------|
| Average web page | 10 KB | ~2,500 |
| Large docs page | 100 KB | ~25,000 |
| Research paper PDF | 500 KB | ~125,000 |

Optimization techniques:
1. Dynamic filtering (web_fetch_20260209)
2. Delegate research to subagents (isolate verbose output)
3. Prompt caching (cache_control breakpoints)
4. Leverage 15-min WebFetch cache (repeated access = free)
5. WebSearch: $10/1000 searches. WebFetch: no extra charge beyond tokens

**Source**: [Claude Code Cost Management](https://code.claude.com/docs/en/costs) — accessed 2026-02-22
