# Literature Survey: Efficient Web Search Strategies for LLM Agents

**Surveyed**: 2026-02-22
**Search queries used**: ~12 across 6 topic areas
**Sources found**: 22+

## 1. Academic/Industry Research on LLM Web Search Agents

### Search-o1: Agentic Search-Enhanced Large Reasoning Models (Jan 2025)
- **URL**: [https://github.com/RUC-NLPIR/Search-o1](https://github.com/RUC-NLPIR/Search-o1)
- **Summary**: Integrates an agentic RAG mechanism into large reasoning models, allowing dynamic retrieval when uncertain. Includes "Reason-in-Documents" module that filters retrieved information to reduce noise.
- **Key takeaway**: Retrieve only when uncertain — and filter retrieved documents through a reasoning step before injecting into main chain.

### WebThinker: Deep Research Agent (NeurIPS 2025)
- **URL**: [https://arxiv.org/abs/2504.21776](https://arxiv.org/abs/2504.21776)
- **Summary**: Enables LRMs to autonomously search, navigate web pages, and draft reports within their thinking process. Uses "Autonomous Think-Search-and-Draft" strategy.
- **Key takeaway**: Interleaving reasoning with search is more effective than "search everything first, then reason."

### From Web Search towards Agentic Deep ReSearch (EMNLP 2024 Findings)
- **URL**: [https://arxiv.org/html/2506.18959v1](https://arxiv.org/html/2506.18959v1)
- **Summary**: Identifies tradeoff between reasoning (internal knowledge) and search (external knowledge). RL-based agents learn adaptive strategies through trial-and-error.
- **Key takeaway**: Task characteristics should determine reasoning vs. retrieval allocation.

### Survey of LLM-based Deep Search Agents (2025)
- **URL**: [https://arxiv.org/html/2508.05668v3](https://arxiv.org/html/2508.05668v3)
- **Summary**: Identifies three search structures: parallel, sequential, and hybrid. Hybrid structures preferred for non-fine-tuned agents.
- **Key takeaway**: For tool-using LLMs, combine parallel sub-query execution with sequential refinement.

## 2. Token Efficiency in LLM Web Retrieval

### Markdown vs. HTML Token Optimization
- **URL**: [https://www.searchcans.com/blog/markdown-vs-html-llm-context-optimization-2026/](https://www.searchcans.com/blog/markdown-vs-html-llm-context-optimization-2026/)
- **Summary**: HTML-to-Markdown reduces tokens 20-30%. Full content extraction saves 70-90%. Raw HTML wastes ~90% of tokens on non-content markup.
- **Key takeaway**: Never feed raw HTML. Markdown conversion is mandatory preprocessing.

### Scraper MCP: Context-Efficient Web Scraping
- **URL**: [https://github.com/cotdp/scraper-mcp](https://github.com/cotdp/scraper-mcp)
- **Summary**: MCP server reducing token usage 70-90% through server-side filtering, markdown conversion, CSS targeting. Three-tier caching with 60-80% hit rates.
- **Key takeaway**: Server-side content extraction before LLM consumption is the single biggest lever.

### Cost-Aware Retrieval (Dynamic Search-R1)
- **URL**: [https://arxiv.org/html/2510.15719v1](https://arxiv.org/html/2510.15719v1)
- **Summary**: Dynamic retrieval depth trained via RL. 16-20% latency reduction while improving quality 5%. Output generation 621% slower than input consumption.
- **Key takeaway**: Adaptive retrieval depth beats fixed. Output token reduction matters more than input reduction.

### LLM Token Optimization (Redis)
- **URL**: [https://redis.io/blog/llm-token-optimization-speed-up-apps/](https://redis.io/blog/llm-token-optimization-speed-up-apps/)
- **Summary**: Poor data serialization wastes 40-70% of tokens. CSV outperforms JSON by 40-50% for tabular data. Output tokens cost 3-5x input.
- **Key takeaway**: Format matters enormously. Constrain response length aggressively.

## 3. Quality vs. Cost Tradeoffs

### FLARE: Active Retrieval Augmented Generation
- **URL**: [https://arxiv.org/abs/2305.06983](https://arxiv.org/abs/2305.06983)
- **Summary**: Monitors token-level confidence; retrieves only when probability drops below threshold.
- **Key takeaway**: "Always retrieve" is wasteful. Selective retrieval maintains quality where it matters.

### Adaptive-RAG
- **URL**: [https://medium.com/@tuhinsharma121/understanding-adaptive-rag-smarter-faster-and-more-efficient-retrieval-augmented-generation-38490b6acf88](https://medium.com/@tuhinsharma121/understanding-adaptive-rag-smarter-faster-and-more-efficient-retrieval-augmented-generation-38490b6acf88)
- **Summary**: Routes simple queries to internal knowledge, complex queries through deeper retrieval chains.
- **Key takeaway**: Classify complexity first, allocate retrieval proportionally.

### Multi-LLM Collaborative Search
- **URL**: [https://arxiv.org/html/2502.18873v1](https://arxiv.org/html/2502.18873v1)
- **Summary**: Multi-step search outperforms single-step. Information overload degrades performance on complex tasks.
- **Key takeaway**: Multi-step favored for hard questions; single-step for simple ones.

## 4. Claude Code Specific

### Inside Claude Code's Web Tools
- **URL**: [https://mikhail.io/2025/10/claude-code-web-tools/](https://mikhail.io/2025/10/claude-code-web-tools/)
- **Summary**: Two-tool split: WebSearch (titles+URLs, lightweight), WebFetch (Haiku sub-model extraction, 100KB truncation, 15-min cache). Design philosophy: "lightweight search, targeted fetch."
- **Key takeaway**: WebFetch uses Haiku to pre-process content — a cheaper model extracts before expensive model reasons.

### Anthropic Multi-Agent Research System
- **URL**: [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Summary**: "Short, broad queries, evaluate, then narrow." Token usage explains 80% of quality variance. Multi-agent uses ~15x more tokens but outperforms single-agent 90.2%. Effort scaling rules in prompts prevent waste.
- **Key takeaway**: Broad-first, narrow-second. Embed effort scaling. Token spending should be *directed*, not just maximized.

## 5. Agentic Search Frameworks

### Perplexity AI
- **URL**: [https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api](https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api)
- **Summary**: Sub-document-level retrieval, hybrid ranking, plan-then-execute with sequential result accumulation.
- **Key takeaway**: Chunk-level extraction, not whole documents. Plan-then-execute is universal.

### Tavily
- **URL**: [https://docs.tavily.com/documentation/api-reference/endpoint/search](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- **Summary**: Pre-processed snippets optimized for RAG. Tunable depth, max_results, domain filtering.
- **Key takeaway**: Purpose-built LLM search APIs are fundamentally more token-efficient than raw search+fetch.

### OpenAI Deep Research
- **URL**: [https://openai.com/index/introducing-deep-research/](https://openai.com/index/introducing-deep-research/)
- **Summary**: Plan-Act-Observe loop. 30-60 query caps, 20-30 min time caps. Backtracking from dead ends.
- **Key takeaway**: Hard budget limits are universal. Decompose-then-narrow is standard.

### HuggingFace Open Deep Research
- **URL**: [https://huggingface.co/blog/open-deep-research](https://huggingface.co/blog/open-deep-research)
- **Summary**: Code-based agents 30% more token-efficient than JSON-based. Context overflow is a major challenge.
- **Key takeaway**: Action representation format matters for token efficiency.

## 6. Multi-step vs. Single-step

### Anthropic (empirical data)
- Multi-agent: ~15x tokens vs. chat, but 90.2% better quality
- Simple tasks: 1 agent, 3-10 tool calls
- Complex tasks: 10+ subagents, parallel execution cuts time 90%

### OpenAI Deep Research (empirical data)
- 72-73% accuracy vs. 63-67% for prior agents
- Biggest improvement on hardest questions (Level 3: 58%)
- 5-30 minutes, hundreds of sources typical
