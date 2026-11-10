---
title: "Type A Survey: Open-Source Deep Research Apps & Frameworks"
date: 2026-11-09
status: complete
bucket: A
parent_proposal: /home/jonathan/dev/research/research-method-benchmarking/research_proposals/01-github-research-methods-survey-2026-11-09.md
---

# Type A Survey: Open-Source Deep Research Apps & Frameworks

## Executive Summary

- **Scope & Coverage (14 Type A Repositories Inspected in Full):** We inspected the source code, prompt templates, configuration schemas, benchmark harnesses, and open/closed GitHub Issues across 14 major open-source Type A deep research applications and frameworks spanning **118,399+ combined GitHub stars**:
  1. [`assafelovic/gpt-researcher`](https://github.com/assafelovic/gpt-researcher) — 30,603★ (`Apache-2.0`, Python) — accessed 2026-11-09
  2. [`dzhng/deep-research`](https://github.com/dzhng/deep-research) — 19,885★ (`MIT`, TypeScript) — accessed 2026-11-09
  3. [`langchain-ai/open_deep_research`](https://github.com/langchain-ai/open_deep_research) — 12,677★ (`MIT`, Python/LangGraph) — accessed 2026-11-09
  4. [`LearningCircuit/local-deep-research`](https://github.com/LearningCircuit/local-deep-research) — 9,557★ (`MIT`, Python) — accessed 2026-11-09
  5. [`langchain-ai/local-deep-researcher`](https://github.com/langchain-ai/local-deep-researcher) — 9,409★ (`MIT`, Python/LangGraph) — accessed 2026-11-09
  6. [`zilliztech/deep-searcher`](https://github.com/zilliztech/deep-searcher) — 8,388★ (`Apache-2.0`, Python) — accessed 2026-11-09
  7. [`nickscamara/open-deep-research`](https://github.com/nickscamara/open-deep-research) — 6,298★ (`NOASSERTION`, TypeScript/Next.js) — accessed 2026-11-09
  8. [`jina-ai/node-DeepResearch`](https://github.com/jina-ai/node-DeepResearch) — 5,241★ (`Apache-2.0`, TypeScript) — accessed 2026-11-09
  9. [`u14app/deep-research`](https://github.com/u14app/deep-research) — 4,687★ (`MIT`, TypeScript/Next.js) — accessed 2026-11-09
  10. [`SkyworkAI/DeepResearchAgent`](https://github.com/SkyworkAI/DeepResearchAgent) — 3,573★ (`MIT`, Python) — accessed 2026-11-09
  11. [`mshumer/OpenDeepResearcher`](https://github.com/mshumer/OpenDeepResearcher) — 2,792★ (`MIT`, Python/Jupyter) — accessed 2026-11-09
  12. [`AnotiaWang/deep-research-web-ui`](https://github.com/AnotiaWang/deep-research-web-ui) — 2,226★ (`None`, TypeScript/Nuxt) — accessed 2026-11-09
  13. [`btahir/open-deep-research`](https://github.com/btahir/open-deep-research) — 2,139★ (`MIT`, TypeScript/Next.js) — accessed 2026-11-09
  14. [`SalesforceAIResearch/enterprise-deep-research`](https://github.com/SalesforceAIResearch/enterprise-deep-research) — 1,224★ (`Apache-2.0`, Python/LangGraph) — accessed 2026-11-09

- **Four Architectural Sub-Families of Type A Systems:**
  1. **A1 — Recursive Breadth×Depth Tree Explorers** (`dzhng/deep-research`, `assafelovic/gpt-researcher` [Deep mode], `AnotiaWang/deep-research-web-ui`, `nickscamara/open-deep-research`): Generate $B$ SERP queries at depth $D$, extract atomic "learnings" + follow-up questions per branch, halve breadth ($\lceil B/2 \rceil$) at each deeper level, and synthesize all deduplicated learnings and visited URLs in a single final report call.
  2. **A2 — Hierarchical Supervisor / Multi-Agent Graph Orchestrators** (`langchain-ai/open_deep_research`, `SalesforceAIResearch/enterprise-deep-research`, `SkyworkAI/DeepResearchAgent`, `assafelovic/gpt-researcher` [`multi_agents`]): Use a top-level supervisor or planning agent to decompose a research brief into parallel sub-agent tasks (each with isolated context windows), compress or review sub-agent findings, and synthesize a master report.
  3. **A3 — Iterative Search-Reflect-Refine Loops & Budgeted DeepSearch Engines** (`langchain-ai/local-deep-researcher`, `LearningCircuit/local-deep-research`, `jina-ai/node-DeepResearch`, `zilliztech/deep-searcher`, `mshumer/OpenDeepResearcher`): Execute sequential or hybrid parallel search rounds guided by explicit gap-analysis reflection, token budgets, or vector/RAG chunk routing.
  4. **A4 — Interactive Canvas / Split-Step Web UIs** (`u14app/deep-research`, `btahir/open-deep-research`, `AnotiaWang/deep-research-web-ui`): Expose human-editable report plans, ReactFlow node graphs, or knowledge-base sidebars in browser localStorage/IndexedDB.

- **Key Cross-Cutting Findings:**
  - **Verification & Anti-Hallucination:** Only **5 of 14** Type A frameworks implement active verification beyond prompt instructions (`assafelovic/gpt-researcher` via `FactCheckerAgent` and `SourceCurator`; `LearningCircuit/local-deep-research` via `EvidenceEvaluator`, `CrossEngineFilter`, and 4-tier `JournalReputationFilter` over ~217K OpenAlex/DOAJ venues; `jina-ai/node-DeepResearch` via post-hoc embedding cosine-similarity reference anchoring `buildReferences` + adversarial `evaluator.ts`; `AnotiaWang/deep-research-web-ui` via `assessSearchLearnings` relevance gating + bounded full-page source reading; `zilliztech/deep-searcher` via binary YES/NO LLM chunk reranking). The remaining 9 rely almost entirely on prompt-level citation rules (`[Title](URL)`), which frequently suffer from citation drift when sub-agent notes are compressed.
  - **Statelessness vs. Persistent Knowledge:** Most Type A systems are **session-ephemeral**—each run starts from a blank state and outputs a standalone Markdown/PDF report. Only `LearningCircuit/local-deep-research` (encrypted SQLCipher DB + local vector library + PR/Issue `#8472` Mem0-style research memories), `btahir/open-deep-research` (ReactFlow canvas + localStorage Knowledge Base with report consolidation), `u14app/deep-research` (IndexedDB history + local KB resources), and `SkyworkAI/DeepResearchAgent` (RSPL/SEPL versioned memory and self-evolving prompt/tool registry) persist cross-run knowledge.
  - **Dominant Real-World Failure Modes in GitHub Issues:**
    1. *Reasoning token starvation & structured output failures* (e.g., `gpt-5.4` or `DeepSeek-R1` consuming the entire `max_tokens=4000`/`4096` budget on hidden reasoning tokens and returning empty/unparseable JSON: `gpt-researcher` [#2251](https://github.com/assafelovic/gpt-researcher/issues/2251), `AnotiaWang` [#101](https://github.com/AnotiaWang/deep-research-web-ui/issues/101), `dzhng` [#141](https://github.com/dzhng/deep-research/issues/141), `jina-ai` [#110](https://github.com/jina-ai/node-DeepResearch/issues/110)).
    2. *Unbounded loops, ignored token budgets, and runaway API credit burn* (`jina-ai` [#118](https://github.com/jina-ai/node-DeepResearch/issues/118) & [#119](https://github.com/jina-ai/node-DeepResearch/issues/119), `mshumer` [#15](https://github.com/mshumer/OpenDeepResearcher/issues/15), `open_deep_research` [#269](https://github.com/langchain-ai/open_deep_research/issues/269), `gpt-researcher` [#2163](https://github.com/assafelovic/gpt-researcher/issues/2163)).
    3. *Context window overflow & destructive message truncation* (`open_deep_research` [#218](https://github.com/langchain-ai/open_deep_research/issues/218), [#252](https://github.com/langchain-ai/open_deep_research/issues/252), [#296](https://github.com/langchain-ai/open_deep_research/issues/296); `u14app` [#138](https://github.com/u14app/deep-research/issues/138)).
    4. *Scraper anti-bot blocks, junk domain injection, and duplicate paid scraping* (`LearningCircuit` [#8459](https://github.com/LearningCircuit/local-deep-research/issues/8459), `local-deep-researcher` [#87](https://github.com/langchain-ai/local-deep-researcher/issues/87) & [#105](https://github.com/langchain-ai/local-deep-researcher/issues/105), `SkyworkAI` [#84](https://github.com/SkyworkAI/DeepResearchAgent/issues/84), `gpt-researcher` [#2115](https://github.com/assafelovic/gpt-researcher/issues/2115) & [#2180](https://github.com/assafelovic/gpt-researcher/issues/2180)).
    5. *Silent multi-agent exception swallowing & concurrency state corruption* (`open_deep_research` [#283](https://github.com/langchain-ai/open_deep_research/issues/283) & [#284](https://github.com/langchain-ai/open_deep_research/issues/284), `SalesforceAIResearch` [#8](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/8)).
    6. *Server-Side Request Forgery (SSRF) and remote prompt injection via unvalidated crawlers* (`u14app` [#153](https://github.com/u14app/deep-research/issues/153), `zilliztech` [#278](https://github.com/zilliztech/deep-searcher/issues/278), `jina-ai` [#131](https://github.com/jina-ai/node-DeepResearch/issues/131), `SkyworkAI` [#98](https://github.com/SkyworkAI/DeepResearchAgent/issues/98)).

---

## Master Comparison Matrix (14 Type A Repositories)

| Repository | Stars / License | Primary Architecture | Claim Verification & Grounding | Persistent Knowledge / Reuse | Cost, Token & Loop Controls | Published Benchmarks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[`assafelovic/gpt-researcher`](https://github.com/assafelovic/gpt-researcher)** | 30,603★ Apache-2.0 | Multi-mode: Standard (plan→parallel scrape→curate→write), Deep Tree ($B \times D$), or LangGraph `multi_agents` | `SourceCurator` LLM ranking + `FactCheckerAgent` (up to 3 revision loops) + `hallucination_eval` & `quality_eval` | JSON `report_store.py` + local doc RAG (`my-docs/`); no cross-run wiki synthesis | `DEEP_RESEARCH_BREADTH=4`, `DEPTH=2`, `CONCURRENCY=2`, `MAX_FACT_CHECK_REVISIONS=3`, `add_costs` callback | **DeepResearch Bench**: RACE **0.512**, **35.2** verified citations/report (56.0% precision) |
| **[`dzhng/deep-research`](https://github.com/dzhng/deep-research)** | 19,885★ MIT | Recursive $B \times D$ tree (`deepResearch()`) with $\lceil B/2 \rceil$ decay per level (<500 LoC TS) | Prompt-only (`extract exact metrics/quotes/dates`); appends flat `visitedUrls` list at end of report | Stateless CLI (`output.md` / `answer.md`); no persistence ([Issue #135](https://github.com/dzhng/deep-research/issues/135)) | User-input `breadth` (4) & `depth` (2), `FIRECRAWL_CONCURRENCY=2`, `trimPrompt` to 128k context | None published ([Issue #159](https://github.com/dzhng/deep-research/issues/159) discusses lack of evals) |
| **[`langchain-ai/open_deep_research`](https://github.com/langchain-ai/open_deep_research)** | 12,677★ MIT | LangGraph Supervisor → parallel `researcher_subgraph` workers → `compress_research` → `final_report_generation` | Prompt-only inline citations `[Title](URL)` + optional Tavily LLM summarization; no post-hoc verifier | Stateless per LangGraph thread (`MemorySaver`); no cross-session KB | `max_researcher_iterations=6`, `max_react_tool_calls=10`, `max_concurrent_research_units=5`, token-limit truncation loop | **DeepResearch Bench**: **0.4344** overall (#6 on leaderboard, Aug 2025); built-in `tests/evaluators.py` |
| **[`LearningCircuit/local-deep-research`](https://github.com/LearningCircuit/local-deep-research)** | 9,557★ MIT | Strategy pattern (`SourceBased`, `FocusedIteration`, `BrowseComp`) with iterative parallel search & progressive exploration | `EvidenceEvaluator` (reliability weights 0.3–1.0) + `CrossEngineFilter` + 4-tier `JournalReputationFilter` (OpenAlex/DOAJ/predatory blacklist) | **Yes**: Encrypted SQLCipher DB, `FindingsRepository`, local RAG library, & `Research memories` ([#8472](https://github.com/LearningCircuit/local-deep-research/issues/8472)) | `search.iterations` (default 3–5), `questions_per_iteration` (3), `question_context_limit`, LLM journal scoring circuit breaker | **SimpleQA**: **~95%–96.51%** accuracy (`FocusedIterationStrategy`); **BrowseComp** runner included |
| **[`langchain-ai/local-deep-researcher`](https://github.com/langchain-ai/local-deep-researcher)** | 9,409★ MIT | 4-node sequential LangGraph (`generate_query` → `web_research` → `summarize_sources` → `reflect_on_summary`) | Prompt-only (`<REQUIREMENTS>` against hallucinated assumptions); deduplicates URLs per loop | Stateless per LangGraph thread; outputs single Markdown summary + deduplicated sources | `max_web_research_loops=3` (default), `MAX_TOKENS_PER_SOURCE=1000` (4,000 chars), `strip_thinking_tokens` | None published |
| **[`zilliztech/deep-searcher`](https://github.com/zilliztech/deep-searcher)** | 8,388★ Apache-2.0 | `RAGRouter` dispatching between `DeepSearch` (parallel sub-queries + reflection) and `ChainOfRAG` (sequential hop decomposition) over Milvus | Binary `YES`/`NO` LLM chunk reranker (`RERANK_PROMPT`) + strict anti-hallucination `INTERMEDIATE_ANSWER_PROMPT` | **Yes**: Persistent vector database collections (Milvus / Zilliz Cloud) with metadata routing | `max_iter: 3` in `config.yaml`, `deduplicate_results` by chunk text | Narrative comparison in README; no formal benchmark table in repo |
| **[`nickscamara/open-deep-research`](https://github.com/nickscamara/open-deep-research)** | 6,298★ NOASSERTION | Next.js AI SDK `deepResearch` tool loop (`search` → `extract` → `analyze` state machine) + reasoning model synthesis | Prompt-only (`analyze` step checks sufficiency of extracted findings; `maxSteps: maxDepth`) | Vercel Postgres (Neon) + Vercel Blob for chat/document artifacts; no cross-study synthesis ([Issue #55](https://github.com/nickscamara/open-deep-research/issues/55)) | `maxDepth=7` (`maxSteps` in `streamText`), `MAX_DURATION=300`s, Upstash Redis rate limiter | None published ([Issue #50](https://github.com/nickscamara/open-deep-research/issues/50) requests benchmarks) |
| **[`jina-ai/node-DeepResearch`](https://github.com/jina-ai/node-DeepResearch)** | 5,241★ Apache-2.0 | Iterative `Search → Read → Reason` loop (+ optional `planner.ts` orthogonal subproblems) until answer passes evaluation | Embedding cosine-similarity query dedup ($\ge 0.86$), ruthless `evaluator.ts` (`reject-all-answers`), & chunk-level `buildReferences` ($\ge 0.70$ sim) | Stateless per API call; returns concise answer or Markdown with anchored char-offset references | `tokenBudget` (`TokenTracker`), `maxBadAttempts=2`, `beastMode` forced final synthesis when budget expires | None in repo ([Issue #109](https://github.com/jina-ai/node-DeepResearch/issues/109) & [#120](https://github.com/jina-ai/node-DeepResearch/issues/120)) |
| **[`u14app/deep-research`](https://github.com/u14app/deep-research)** | 4,687★ MIT | Split-model (`thinkingModel` + `taskModel`) interactive plan → SERP task list → parallel search/crawl → final report | Prompt-only inline citations `[Title](URL)` + optional Gemini `useSearchGrounding: true` | Browser IndexedDB/Zustand store (`useHistoryStore`, `useKnowledgeStore`) + local file/crawler ingestion | Single-pass task list (or SSE API `maxResult=5`), `p-limit` concurrency | None published |
| **[`SkyworkAI/DeepResearchAgent`](https://github.com/SkyworkAI/DeepResearchAgent)** | 3,573★ MIT | 2-tier hierarchical `PlanningAgent` coordinating `deep_researcher_agent`, `deep_analyzer_agent`, `browser_use_agent` + SEPL/RSPL self-evolution | `deep_analyzer_agent` performs multi-step fact verification; `PersistMemory` records execution traces | **Yes**: RSPL/SEPL versioned resource registry + `PersistMemory` / `ContextMemory` in `workdir/` | `max_steps=20` (top-level), `max_steps=5` (`deep_researcher`), `max_steps=3` (`deep_analyzer`) | **GAIA**: **82.42** avg (validation), **73.33** (test); discussed in [#81](https://github.com/SkyworkAI/DeepResearchAgent/issues/81) & [#83](https://github.com/SkyworkAI/DeepResearchAgent/issues/83) |
| **[`mshumer/OpenDeepResearcher`](https://github.com/mshumer/OpenDeepResearcher)** | 2,792★ MIT | Async Python notebook loop: `generate_search_queries` (up to 4) → SERPAPI → Jina Reader → `is_page_useful` → `extract_relevant_context` → `get_new_search_queries` | Binary `Yes`/`No` page usefulness filter (`is_page_useful_async`) on first 20,000 chars of each Jina-fetched page | Stateless Colab/Gradio notebook; no persistence | User-set `iteration_limit` (default 2), 20,000-char page truncation, early stop when LLM returns `""` | None published |
| **[`AnotiaWang/deep-research-web-ui`](https://github.com/AnotiaWang/deep-research-web-ui)** | 2,226★ None | Recursive tree search (`deepResearch`) with structured `searchPlan` filters, query retry, and on-demand `readSource` | `assessSearchLearnings` (retries query once if insufficient), `createSourceReader` full-page verbatim quote extraction, `deduplicateLearnings`, citation excerpt inspection UI | Browser IndexedDB/localStorage session tree with interactive node follow-up & passage update | `breadth`, `depth`, `sourceReadLimits = { perNode: 2, perRun: 6, concurrency: 2, timeoutMs: 20_000 }`, `maxAttempt=2` | None published |
| **[`btahir/open-deep-research`](https://github.com/btahir/open-deep-research)** | 2,139★ MIT | Next.js visual canvas (`@xyflow/react`): search → `/api/analyze` selection → `/api/report` → `/api/question` branch nodes → `/api/consolidate` | `/api/analyze` LLM relevance scorer (`0.0–1.0`) + `/api/consolidate` deduplicated `[1..N]` source index | **Yes**: `localStorage` Knowledge Base (`useKnowledgeBase`) + visual multi-report canvas consolidation (`useFlowProjects`) | Upstash Redis rate limiting (`reportContentRatelimit`), search result cap (10–50), per-route `maxTokens` | None published |
| **[`SalesforceAIResearch/enterprise-deep-research`](https://github.com/SalesforceAIResearch/enterprise-deep-research)** | 1,224★ Apache-2.0 | LangGraph Master Planner + 4 domain search agents (General, Academic, GitHub, LinkedIn) + MCP/NL2SQL + `UserSteeringManager` | Prompt-enforced `[Title](URL)` inline attribution + cross-loop reflection gap analysis + human-in-the-loop `TodoItem` steering | Session-scoped SQLite/LangGraph state (`session_store.py`); no cross-session KB | `MAX_WEB_RESEARCH_LOOPS=10` (default; 5 in benchmarks), `--parallel-max 4`, circuit-breaker loop counter | **#1 on LiveResearchBench**; **DeepResearchBench** & **BrowseComp** (`arXiv:2510.17797`) |

---

## Detailed Repository Analyses

### 1. `assafelovic/gpt-researcher` (30,603★, Apache-2.0)

- **Repository:** [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  `gpt-researcher` provides three distinct execution pipelines ([Architecture Reference](https://github.com/assafelovic/gpt-researcher/blob/main/docs/docs/gpt-researcher/architecture.md) — accessed 2026-11-09):
  1. **Standard Single-Agent Pipeline (`gpt_researcher/agent.py`):**
     - *Agent & Role Selection:* Uses `STRATEGIC_LLM` (default `o3-mini`) to choose a domain persona and generate `MAX_SUBTOPICS` / sub-queries.
     - *Parallel Retrieval & Scraping:* Queries configured retrievers (`tavily`, `google`, `serper`, `exa`, `mcp`, or local docs) up to `MAX_SEARCH_RESULTS_PER_QUERY=5` and scrapes up to `MAX_URLS_TO_SCRAPE=10` pages via BeautifulSoup/Firecrawl/Tavily Extract.
     - *Context Compression (`ContextManager` in `gpt_researcher/skills/context_manager.py`):* Chunks scraped text, embeds chunks, and filters by vector cosine similarity (`SIMILARITY_THRESHOLD=0.42`) using `FAST_LLM` (`gpt-4o-mini`).
     - *Source Curation (`SourceCurator` in `gpt_researcher/skills/curator.py`):* Optionally invokes `SMART_LLM` (`temperature=0.2`, `max_tokens=8000`) to evaluate and rank sources by relevance, credibility, and reliability, recovering fenced JSON via `parse_json_markdown(..., parser=json_repair.loads)`.
     - *Report Generation (`ReportGenerator` in `gpt_researcher/skills/writer.py`):* Synthesizes the final report using `SMART_LLM` (`gpt-4o`).
  2. **Deep Research Tree Mode (`DeepResearchSkill` in [`gpt_researcher/skills/deep_research.py`](https://github.com/assafelovic/gpt-researcher/blob/main/gpt_researcher/skills/deep_research.py) — accessed 2026-11-09):**
     - Implements a `ResearchTimer` and recursive tree exploration (`deep_research()`): generates `breadth` (default 4) SERP queries via `generate_search_queries()`, runs parallel sub-researchers bounded by ` asyncio.Semaphore(self.concurrency_limit)` (default 2), extracts learnings and follow-up questions (`process_research_results()`), halves breadth at each recursion level (`new_breadth = int(math.ceil(breadth / 2))`), and decrements `depth` (default 2) until `depth == 0`, feeding accumulated `learnings`, `visited_urls`, and `context` into final synthesis.
  3. **LangGraph Multi-Agent Mode ([`multi_agents/`](https://github.com/assafelovic/gpt-researcher/tree/main/multi_agents) — accessed 2026-11-09):**
     - Orchestrated by `ChiefEditorAgent` (`multi_agents/agents/orchestrator.py`) coordinating 7 specialized nodes: `Browser` (initial research) → `Planner` (`EditorAgent` plans outline) → `Human` (optional human-in-the-loop plan approval) → `Researcher` (parallel section research) → `Writer` (`WriterAgent` compiles intro/conclusion/table of contents) ↔ `FactChecker` (`FactCheckerAgent`) and `Reviewer`/`Reviser` → `Publisher` (exports Markdown, PDF, DOCX).
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Active Multi-Agent Fact-Checking Loop:** [`multi_agents/agents/fact_checker.py`](https://github.com/assafelovic/gpt-researcher/blob/main/multi_agents/agents/fact_checker.py) and [`multi_agents/agents/utils/fact_check_review.py`](https://github.com/assafelovic/gpt-researcher/blob/main/multi_agents/agents/utils/fact_check_review.py) (accessed 2026-11-09) implement `FactCheckerAgent.check_facts(research_state)`, which audits draft sections against `research_data` + ` draft` for unsupported assertions or contradicted numbers. If issues are found, `route_fact_check()` routes back to the reviser up to `DEFAULT_MAX_FACT_CHECK_REVISIONS = 3` times before raising `MaxFactCheckRevisionsExceededError`.
  - **LLM Source Curation (`SourceCurator`):** Ranks scraped sources before synthesis.
  - **Post-Report Evaluation Suites (`evals/`):** Includes [`evals/hallucination_eval/evaluate.py`](https://github.com/assafelovic/gpt-researcher/blob/main/evals/hallucination_eval/evaluate.py) (using `HaluEvalDocumentSummaryNonFactual` from `judges`) and [`evals/quality_eval/`](https://github.com/assafelovic/gpt-researcher/blob/main/evals/quality_eval/README.md) (measuring RAGAS-aligned `unsupported_claim`, `subtopic_coverage`, `source_authority`, `source_diversity`, and ALCE-aligned `citation_faithfulness`) — accessed 2026-11-09.
- **Output Format & Knowledge Persistence:**
  - Outputs Markdown, PDF, DOCX, and JSON reports persisted via `backend/server/report_store.py`. Supports local corpus research (`REPORT_SOURCE=local` reading from `./my-docs`), but does not automatically accumulate a cross-session structured knowledge graph or reuse prior reports in future web runs.
- **Cost, Token & Loop Controls:**
  - `DEEP_RESEARCH_BREADTH=4`, `DEEP_RESEARCH_DEPTH=2`, `DEEP_RESEARCH_CONCURRENCY=2`, `MAX_SEARCH_RESULTS_PER_QUERY=5`, `MAX_URLS_TO_SCRAPE=10`, `MAX_TOKENS=4000`, `DEFAULT_MAX_FACT_CHECK_REVISIONS=3`, `max_plan_revisions`, and per-call `cost_callback=self.researcher.add_costs`.
- **Published Evaluation & Benchmark Evidence:**
  - Documented in [`benchmark/README.md`](https://github.com/assafelovic/gpt-researcher/blob/main/benchmark/README.md) and [`evals/README.md`](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) (accessed 2026-11-09):
    - **DeepResearch Bench (10 stratified English PhD tasks, `gpt-5.4`, recursion limit 60):** Comparing a stock LangChain `deepagents` harness (raw Tavily search) vs. `gpt-researcher` (`quick_search` + `deep_research`):
      - **RACE overall:** **0.512** vs. 0.503 baseline (+1.9%)
      - **Total citations per report:** **62.9** vs. 34.5 (+82%)
      - **Effective (verified) citations per report (FACT):** **35.2** vs. 18.6 (**+89%**, winning 7 of 10 tasks)
      - **Citation precision:** **56.0%** vs. 53.9% (+2.1 pts)
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Reasoning Token Exhaustion & Uncounted Retry Costs ([Issue #2251](https://github.com/assafelovic/gpt-researcher/issues/2251) — accessed 2026-11-09):** When running Deep Research with `gpt-5.4` (`max_tokens=4000` and `reasoning_effort=high`), the model consumes the entire 4,000-token output cap on hidden reasoning tokens and returns an empty string, triggering retries whose token costs are dropped from `add_costs`.
  - **Broken Shared URL Deduplication State ([Issue #2115](https://github.com/assafelovic/gpt-researcher/issues/2115) — accessed 2026-11-09):** In Python, `visited_urls = visited_urls or self.visited_urls` evaluates an explicitly passed empty `set()` as falsy, silently detaching the caller's shared deduplication set across recursive branches.
  - **Loss of Initial Planning Sources ([Issue #2144](https://github.com/assafelovic/gpt-researcher/issues/2144) — accessed 2026-11-09):** Initial planning sources are overwritten or lost when follow-up sub-queries return empty or disjoint search results.
  - **Duplicate Paid Scraping Across Parallel Researchers ([Issue #2180](https://github.com/assafelovic/gpt-researcher/issues/2180) — accessed 2026-11-09):** Parallel sub-agents in `multi_agents` and `DeepResearchSkill` independently scrape overlapping high-ranking URLs via paid scrapers (Firecrawl/Tavily) before deduplication occurs.
  - **Infinite Plan-Review Loop on Empty Console Reply ([Issue #2163](https://github.com/assafelovic/gpt-researcher/issues/2163) — accessed 2026-11-09):** In `multi_agents`, an empty console input during human plan review triggered re-planning without incrementing `max_plan_revisions`.

---

### 2. `langchain-ai/open_deep_research` (12,677★, MIT)

- **Repository:** [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  Implemented in [`src/open_deep_research/deep_researcher.py`](https://github.com/langchain-ai/open_deep_research/blob/main/src/open_deep_research/deep_researcher.py) (with legacy plan-and-execute and multi-agent graphs preserved in `src/legacy/graph.py` and `src/legacy/multi_agent.py` — accessed 2026-11-09), the primary architecture is a 3-stage hierarchical Supervisor-Subagent StateGraph:
  1. **Scope & Brief Generation (`clarify_with_user` → `write_research_brief`):**
     - `clarify_with_user` checks if `allow_clarification=True` and uses structured output (`ClarifyWithUser`) to either ask clarifying questions (`Command(goto=END)`) or proceed.
     - `write_research_brief` transforms the conversation history into a detailed `research_brief` string (`ResearchQuestion` schema) and initializes the supervisor's message state.
  2. **Supervisor Orchestration Loop (`supervisor_subgraph`: `supervisor` ↔ `supervisor_tools`):**
     - The supervisor (`research_model`, default `openai:gpt-4.1`) is bound to `lead_researcher_tools = [ConductResearch, ResearchComplete, think_tool]`.
     - Prompted by `lead_researcher_prompt` ([`src/open_deep_research/prompts.py`](https://github.com/langchain-ai/open_deep_research/blob/main/src/open_deep_research/prompts.py) — accessed 2026-11-09), the supervisor uses `think_tool` before and after every `ConductResearch` tool call to assess whether scaling requires single vs. parallel sub-agents (capped at `max_concurrent_research_units=5`).
     - `supervisor_tools` slices `conduct_research_calls[:max_concurrent_research_units]` and launches `researcher_subgraph.ainvoke()` in parallel via `asyncio.gather(*tasks)`.
  3. **Isolated Researcher Sub-Agents (`researcher_subgraph`: `researcher` ↔ `researcher_tools` → `compress_research`):**
     - Each sub-agent has an isolated context window, executes up to `max_react_tool_calls=10` searches across Tavily (`tavily_search`), native OpenAI/Anthropic web search, or configured MCP tools + `think_tool` reflection after each search.
     - Before returning to the supervisor, `compress_research` invokes `compression_model` (`openai:gpt-4.1`) with `compress_research_system_prompt` to clean and retain all verbatim statements and inline citations while stripping raw tool noise.
  4. **Final Report Synthesis (`final_report_generation`):**
     - Concatenates all compressed `notes`, clears sub-agent buffers, and calls `final_report_model` (`openai:gpt-4.1`, `max_tokens=10000`) with `final_report_generation_prompt`.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Prompt-Enforced Verbatim Compression & Citation Rules:** `compress_research_system_prompt` instructs the compression model to *"Clean up these findings: preserve ALL relevant statements and information that the researcher has gathered... Include inline citations for each source"* (`[Title](URL)`), and `final_report_generation_prompt` mandates numbered `[1] [Title](URL)` sources at the end of the report without duplicates.
  - **No Dedicated Verification Node:** Unlike `gpt-researcher` or `LearningCircuit`, there is no separate fact-checker node or deterministic URL/quote validator during execution (though `tests/evaluators.py` provides offline LLM-as-judge `GROUNDEDNESS_PROMPT` and `CORRECTNESS_PROMPT` evaluation).
- **Output Format & Knowledge Persistence:**
  - Returns a single comprehensive Markdown report (`final_report` in `AgentState`). State is ephemeral to the LangGraph thread; there is no persistent knowledge base across threads.
- **Cost, Token & Loop Controls:**
  - Configured in [`src/open_deep_research/configuration.py`](https://github.com/langchain-ai/open_deep_research/blob/main/src/open_deep_research/configuration.py) (accessed 2026-11-09):
    - `max_concurrent_research_units: int = 5` (excess `ConductResearch` calls receive a tool error message instructing the supervisor to wait).
    - `max_researcher_iterations: int = 6` (hard cap on supervisor delegation cycles).
    - `max_react_tool_calls: int = 10` (hard cap on per-subagent search tool calls).
    - `max_structured_output_retries: int = 3`.
    - Progressive context-window truncation loops (`max_attempts = 3`) in both `compress_research` and `final_report_generation` when `is_token_limit_exceeded(e, model_name)` triggers (reducing `findings_token_limit` by 10% per retry).
- **Published Evaluation & Benchmark Evidence:**
  - Achieved **#6 ranking on the Deep Research Bench Leaderboard** with an overall RACE score of **0.4344** (announced in [`README.md`](https://github.com/langchain-ai/open_deep_research/blob/main/README.md) on August 2, 2025 — accessed 2026-11-09).
  - Includes a built-in LangSmith benchmark harness ([`tests/evaluators.py`](https://github.com/langchain-ai/open_deep_research/blob/main/tests/evaluators.py) — accessed 2026-11-09) scoring reports on `OverallQualityScore` (6 criteria 1–5), `RelevanceScore`, `StructureScore`, `GroundednessScore` (claim-level `is_grounded: bool`), `CorrectnessScore`, and `CompletenessScore`.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Silent Sub-Agent Exception Swallowing ([Issue #283](https://github.com/langchain-ai/open_deep_research/issues/283) — accessed 2026-11-09):** In `supervisor_tools`, if *any* exception occurs inside the `try` block (e.g., a child `ConductResearch` task fails or times out), the `except Exception` handler routes directly to `Command(goto=END, update={"notes": get_notes_from_tool_calls(supervisor_messages)})`, silently terminating research and treating failed child tasks as complete.
  - **Destructive Recency Truncation in `compress_research` ([Issue #252](https://github.com/langchain-ai/open_deep_research/issues/252) & [Issue #218](https://github.com/langchain-ai/open_deep_research/issues/218) — accessed 2026-11-09):** When `compress_research` hits a token limit, `researcher_messages = remove_up_to_last_ai_message(researcher_messages)` removes the *most recent* AI/Tool messages from the end of the list rather than trimming oldest messages or truncating oversized tool payloads, causing `Maximum retries exceeded` or losing the final synthesis instructions.
  - **Token Bloat from Unfiltered Web Page Ingestion ([Issue #296](https://github.com/langchain-ai/open_deep_research/issues/296) — accessed 2026-11-09):** Sub-agents ingest massive raw web pages into `researcher_messages`, causing rapid context overflow before `compress_research` runs.
  - **Citation Format Contradiction in Prompts ([Issue #232](https://github.com/langchain-ai/open_deep_research/issues/232) — accessed 2026-11-09):** `compress_research_system_prompt` specifies inconsistent rules between `<Output Format>` and `<Citation Rules>` for formatting the `### Sources` section.
  - **Broken Evaluator Format String ([Issue #217](https://github.com/langchain-ai/open_deep_research/issues/217) — accessed 2026-11-09):** `CORRECTNESS_PROMPT` in `tests/prompts.py` omitted `{user_question}`, `{report}`, and `{answer}` placeholders, causing `eval_correctness` to judge an empty prompt.
  - **Legacy Multi-Agent Premature Termination & Unbounded Plan Revision Loop ([Issue #284](https://github.com/langchain-ai/open_deep_research/issues/284) & [Issue #269](https://github.com/langchain-ai/open_deep_research/issues/269) — accessed 2026-11-09):** `legacy/multi_agent.py` could mark partial section completion as full completion, and `legacy/graph.py` lacked a `max_revisions` counter on the `human_feedback ↔ generate_report_plan` cycle.

---

### 3. `langchain-ai/local-deep-researcher` (9,409★, MIT)

- **Repository:** [langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  Designed as a minimalist, single-agent IterDRAG-style loop for local LLMs (Ollama / LMStudio), implemented in [`src/ollama_deep_researcher/graph.py`](https://github.com/langchain-ai/local-deep-researcher/blob/main/src/ollama_deep_researcher/graph.py) (accessed 2026-11-09):
  1. **`generate_query`:** Prompts the local LLM with `query_writer_instructions` ([`src/ollama_deep_researcher/prompts.py`](https://github.com/langchain-ai/local-deep-researcher/blob/main/src/ollama_deep_researcher/prompts.py) — accessed 2026-11-09) using JSON mode (`format="json"`), structured outputs, or tool calling to emit `{"query": ..., "rationale": ...}`.
  2. **`web_research`:** Executes the query via `duckduckgo`, `searxng`, `tavily`, or `perplexity`, truncates each source's raw content to `MAX_TOKENS_PER_SOURCE = 1000` (`chars_per_token = 4` → 4,000 characters) via `deduplicate_and_format_sources()`, and increments `research_loop_count`.
  3. **`summarize_sources`:** Feeds `<User Input>`, `<Existing Summary>` (`state.running_summary`), and `<New Context>` to `summarizer_instructions` to iteratively extend or update the running Markdown summary, stripping `<think>...</think>` tags if `strip_thinking_tokens=True`.
  4. **`reflect_on_summary` & `route_research`:** Invokes `reflection_instructions` to identify a knowledge gap and output a `follow_up_query`. `route_research` loops back to `web_research` if `research_loop_count <= max_web_research_loops` (default 3); otherwise routes to `finalize_summary`, which deduplicates all gathered URLs and appends `### Sources:\n* title : url`.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Prompt-Only Constraints + Deterministic URL List Preservation:** `summarizer_instructions` instructs the model to *"Base your work strictly on the provided context — never make assumptions or extrapolate"*, while `finalize_summary` programmatically attaches the exact URLs returned by the search engine rather than letting the LLM generate bibliography URLs. However, inline claims within `running_summary` are not linked to individual source URLs.
- **Output Format & Knowledge Persistence:**
  - Outputs a single Markdown `running_summary` with a flat `### Sources:` bullet list at the bottom. Completely stateless across runs ([Issue #138](https://github.com/langchain-ai/local-deep-researcher/issues/138)).
- **Cost, Token & Loop Controls:**
  - Defined in [`src/ollama_deep_researcher/configuration.py`](https://github.com/langchain-ai/local-deep-researcher/blob/main/src/ollama_deep_researcher/configuration.py) (accessed 2026-11-09):
    - `max_web_research_loops: int = 3` (hard cycle cap).
    - `MAX_TOKENS_PER_SOURCE = 1000` (4,000-character hard truncation per scraped page in `graph.py`).
    - `fetch_full_page: bool = True` (optional full HTML scrape via DuckDuckGo/SearXNG).
    - `strip_thinking_tokens: bool = True` (prevents `<think>` blocks from polluting `running_summary`).
- **Published Evaluation & Benchmark Evidence:**
  - None published in the repository.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Running Summary Wiped Out / Empty Output ([Issue #92](https://github.com/langchain-ai/local-deep-researcher/issues/92) & [Issue #90](https://github.com/langchain-ai/local-deep-researcher/issues/90) — accessed 2026-11-09):** Because `summarize_sources` overwrites `running_summary = running_summary` on every loop iteration rather than appending section-by-section, small local models (or models whose `<think>` block consumes the output budget before closing `</think>`) overwrite the entire accumulated summary with an empty string or a truncated 1,000-token fragment on iteration 2 or 3.
  - **Junk/SEO Poisoning in Iterative Reflection ([Issue #105](https://github.com/langchain-ai/local-deep-researcher/issues/105) — accessed 2026-11-09):** Without domain filtering or source credibility scoring, searches repeatedly pull low-quality Zhihu/content-farm snippets into `running_summary`, which `reflect_on_summary` then uses to generate even more off-target follow-up queries.
  - **Default DuckDuckGo Rate-Limit Silent Failures ([Issue #87](https://github.com/langchain-ai/local-deep-researcher/issues/87) — accessed 2026-11-09):** Default `duckduckgo` search frequently returns zero results due to IP rate-limiting, causing the LLM to summarize empty context across all loops.
  - **Structured Output Parsing Failures on Local Inference Servers ([Issue #107](https://github.com/langchain-ai/local-deep-researcher/issues/107) — accessed 2026-11-09):** `llm.with_structured_output` fails probabilistically under concurrency when backed by Xinference/vLLM/Ollama models.

---

### 4. `dzhng/deep-research` (19,885★, MIT)

- **Repository:** [dzhng/deep-research](https://github.com/dzhng/deep-research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  Designed as a `<500 LoC` reference implementation of recursive breadth×depth tree research in TypeScript ([`src/deep-research.ts`](https://github.com/dzhng/deep-research/blob/main/src/deep-research.ts) — accessed 2026-11-09):
  1. **Pre-Research Clarification (`generateFeedback` in [`src/feedback.ts`](https://github.com/dzhng/deep-research/blob/main/src/feedback.ts) — accessed 2026-11-09):** Uses Vercel AI SDK `generateObject` to ask the user up to `numQuestions = 3` clarifying questions before starting the tree.
  2. **Recursive SERP Query Generation (`generateSerpQueries`):** Given `query` and accumulated `learnings`, calls `generateObject` to emit up to `numQueries = breadth` unique `{ query, researchGoal }` pairs.
  3. **Parallel Firecrawl Search + Scrape (`firecrawl.search`):** Bounded by `pLimit(ConcurrencyLimit)` (default `FIRECRAWL_CONCURRENCY = 2`), executes `firecrawl.search(serpQuery.query, { timeout: 15000, limit: 5, scrapeOptions: { formats: ['markdown'] } })` and trims each page's markdown to `25,000` characters.
  4. **Learning & Follow-Up Extraction (`processSerpResult`):** Calls `generateObject` (`timeout: 60_000`) to extract up to `numLearnings = 3` dense, entity/metric-rich factual learnings and `numFollowUpQuestions = Math.ceil(breadth / 2)` follow-up questions.
  5. **Recursive Branching (`deepResearch`):** Decrements `newDepth = depth - 1` and halves breadth (`newBreadth = Math.ceil(breadth / 2)`). If `newDepth > 0`, constructs `nextQuery` from `serpQuery.researchGoal` + `newLearnings.followUpQuestions` and recurses with `allLearnings` and `allUrls`.
  6. **Final Synthesis (`writeFinalReport` or `writeFinalAnswer`):** Deduplicates `learnings` and `visitedUrls` via `[...new Set(...)]`, calls `generateObject` to produce a comprehensive `>= 3 pages` Markdown report, and appends `\n\n## Sources\n\n- ${url}` at the end.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Prompt-Only Extraction + Unlinked Flat URL Footer:** `processSerpResult` prompts the model to *"Make sure each learning is... as detailed and information dense as possible. Make sure to include any entities... and any exact metrics, numbers, or dates."* However, `learnings` are stored as plain strings (`string[]`) completely detached from the URLs where they were found! In `writeFinalReport`, all `visitedUrls` are simply dumped at the bottom under `## Sources` without mapping which learning came from which URL.
- **Output Format & Knowledge Persistence:**
  - Writes `output.md` (report mode) or `answer.md` (short-answer mode) to disk. Completely stateless; cannot resume interrupted runs ([Issue #135](https://github.com/dzhng/deep-research/issues/135)).
- **Cost, Token & Loop Controls:**
  - User-specified `breadth` (default 4) and `depth` (default 2) with geometric breadth decay ($\lceil B/2 \rceil$ per depth level).
  - `ConcurrencyLimit = Number(process.env.FIRECRAWL_CONCURRENCY) || 2`.
  - `trimPrompt()` in `src/ai/providers.ts` using `RecursiveCharacterTextSplitter` (`src/ai/text-splitter.ts`) + `js-tiktoken` (`o200k_base`) to recursively trim prompts exceeding `contextSize = Number(process.env.CONTEXT_SIZE) || 128_000` down to a minimum chunk size of 140 chars.
- **Published Evaluation & Benchmark Evidence:**
  - None published; see maintainer/community discussion in [Issue #159](https://github.com/dzhng/deep-research/issues/159) (*"Are current benchmarks enough to measure research agents?"* — accessed 2026-11-09).
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Prompt Injection / Hallucinated Domain Drift from System Prompt Example ([Issue #132](https://github.com/dzhng/deep-research/issues/132) — accessed 2026-11-09):** Users reported that `dzhng/deep-research` frequently veered into researching "Metaverse and Blockchain" on unrelated queries because an early prompt/example or noisy SERP snippet contaminated the recursive `allLearnings` array passed down into every child branch (`learnings: allLearnings`).
  - **Zero Visited URLs on Self-Hosted Firecrawl ([Issue #126](https://github.com/dzhng/deep-research/issues/126) — accessed 2026-11-09):** Self-hosted Firecrawl instances lacking configured search/scrape backends or hitting the hard `timeout: 15000` ms limit in `firecrawl.search()` silently hit the `catch (e)` block and return `{ learnings: [], visitedUrls: [] }`, producing an ungrounded hallucinated report with `Visited URLs (0)`.
  - **`AI_NoObjectGeneratedError` on Non-OpenAI Models ([Issue #141](https://github.com/dzhng/deep-research/issues/141) — accessed 2026-11-09):** Because every single step (`generateFeedback`, `generateSerpQueries`, `processSerpResult`, `writeFinalReport`) relies on Vercel AI SDK's `generateObject()` with strict Zod schemas, OpenAI-compatible providers like GLM-4, DeepSeek, or local Ollama models fail with `NoObjectGeneratedError: could not parse the response`.
  - **No Checkpointing or Resumability ([Issue #135](https://github.com/dzhng/deep-research/issues/135) — accessed 2026-11-09):** If a deep run ($D=4, B=6$) fails at 90% completion due to a rate limit or network blip, all in-memory `learnings` are lost.


---

### 5. `LearningCircuit/local-deep-research` (9,557★, MIT)

- **Repository:** [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  `LearningCircuit/local-deep-research` (LDR) is the most heavily engineered local/hybrid research framework in Type A, built around a pluggable `BaseSearchStrategy` hierarchy in `src/local_deep_research/advanced_search_system/strategies/` ([`README.md`](https://github.com/LearningCircuit/local-deep-research/blob/main/README.md) — accessed 2026-11-09):
  1. **Strategy Selection (`AdvancedSearchSystem`):** Dispatches among multiple search strategies including:
     - **`SourceBasedSearchStrategy`** ([`source_based_strategy.py`](https://github.com/LearningCircuit/local-deep-research/blob/main/src/local_deep_research/advanced_search_system/strategies/source_based_strategy.py) — accessed 2026-11-09): Iterative question generation (`StandardQuestionGenerator` or `AtomicFactQuestionGenerator`) → parallel multi-engine search via `ThreadPoolExecutor` (`run_parallel_searches`) across 10+ engines (SearXNG, arXiv, PubMed, Semantic Scholar, OpenAlex, Wikipedia, Brave, Tavily, local library) → `CrossEngineFilter` → `CitationHandler` synthesis.
     - **`FocusedIterationStrategy`** ([`focused_iteration_strategy.py`](https://github.com/LearningCircuit/local-deep-research/blob/main/src/local_deep_research/advanced_search_system/strategies/focused_iteration_strategy.py) — accessed 2026-11-09): Hybrid strategy combining broad initial search with `ProgressiveExplorer` candidate exploration and `BrowseCompQuestionGenerator` adaptive refinement, achieving 96.51% on SimpleQA.
  2. **Context & Findings Management (`FindingsRepository`):** Tracks per-iteration search results, candidate entities, constraints, and cited sources across iterations (`CHECK_CONTEXT_ITERATION_START`, `CHECK_CONTEXT_POST_SEARCH`, `CHECK_CONTEXT_PRE_SYNTHESIS`).
- **Claim Verification & Anti-Hallucination Mechanisms:**
  LDR implements the richest verification and source-filtering stack among all 14 Type A repos:
  - **Multi-Tier Bibliometric & Predatory Venue Filtering (`JournalReputationFilter` in [`journal_reputation_filter.py`](https://github.com/LearningCircuit/local-deep-research/blob/main/src/local_deep_research/advanced_search_system/filters/journal_reputation_filter.py) — accessed 2026-11-09):** Scores academic sources 1–10 and automatically purges predatory venues using a 4-tier cascade:
    - *Tier 1 (Predatory Blacklist):* Auto-removes blacklisted predatory journals/publishers (with whitelist override for false positives).
    - *Tier 2 (Bundled OpenAlex Data):* Matches against ~217,000 bundled OpenAlex sources using h-index, quartile (Q1–Q4), and DOAJ status; lifts preprints via author institution affiliation lookup (Tier 3.5, capped at score 6).
    - *Tier 3 (DOAJ Floor):* Assigns a quality floor of 5 to listed Open Access journals.
    - *Tier 4 (Opt-in SearXNG + LLM Scoring):* Canonicalizes unmatched names via LLM and scores via SearXNG web lookup, protected by a circuit breaker that disables LLM scoring after 2 consecutive failures.
  - **Explicit Constraint-Based Evidence Scoring (`EvidenceEvaluator` in [`evidence_evaluator.py`](https://github.com/LearningCircuit/local-deep-research/blob/main/src/local_deep_research/advanced_search_system/evidence/evidence_evaluator.py) — accessed 2026-11-09):** Extracts structured `Evidence` objects (`direct_statement`, `official_record`, `research_finding`, `news_report`, `inference`, `speculation`) for each `(candidate, constraint)` pair and weights confidence by `source_reliability` (`official: 1.0`, `research: 0.95`, `news: 0.8`, `community: 0.6`, `inference: 0.5`, `speculation: 0.3`).
  - **Cross-Engine Relevance Filter (`CrossEngineFilter`) & `CitationHandler`:** Ranks and deduplicates results across engines and attaches numbered citations to synthesized claims.
- **Output Format & Knowledge Persistence:**
  - **Encrypted Local Persistence:** Stores research sessions, settings, cached journal scores, and downloaded full-text PDFs/chunks in an **SQLCipher-encrypted SQLite database** (`src/local_deep_research/database/`) and local vector RAG collections (`research_library`).
  - **Self-Updating Research Memories ([Issue #8472](https://github.com/LearningCircuit/local-deep-research/issues/8472) — accessed 2026-11-09):** Actively adding Mem0-style persistent user/research memory reconciliation across sessions.
- **Cost, Token & Loop Controls:**
  - Configurable `search.iterations` (default 3 in SimpleQA, 5 in `SourceBasedSearchStrategy`), `questions_per_iteration` (default 3–5), `search.question_context_limit` (limits accumulated search results passed to follow-up question generator to `[-N:]`), `snippets_only` mode, and circuit breakers on LLM journal analysis.
- **Published Evaluation & Benchmark Evidence:**
  - Documented in [`src/local_deep_research/benchmarks/README.md`](https://github.com/LearningCircuit/local-deep-research/blob/main/src/local_deep_research/benchmarks/README.md) and [`focused_iteration_strategy.py`](https://github.com/LearningCircuit/local-deep-research/blob/main/src/local_deep_research/advanced_search_system/strategies/focused_iteration_strategy.py) (accessed 2026-11-09):
    - **SimpleQA Benchmark:** Reports **~95% accuracy** in the repo header (e.g., `Qwen3.6-27B` locally on an RTX 3090) and **96.51% accuracy** using `FocusedIterationStrategy` (8 iterations × 5 questions per iteration).
    - **BrowseComp Benchmark:** Built-in CLI and programmatic runner (`python -m local_deep_research.benchmarks.cli.benchmark_commands browsecomp`).
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Header-less Anti-Bot Challenge Pages Ingested into Research Library & Shared Retry Exhaustion ([Issue #8459](https://github.com/LearningCircuit/local-deep-research/issues/8459) — accessed 2026-11-09):** When academic publishers return HTTP 200 challenge/CAPTCHA pages without standard bot headers, `research_library` publisher fallback ingests the challenge HTML as valid paper text and consumes shared extraction retry slots across concurrent users.
  - **Inability to Expand Cited Library Chunks to Full Stored Document Context ([Issue #8475](https://github.com/LearningCircuit/local-deep-research/issues/8475) — accessed 2026-11-09):** `fetch_content` cannot expand a local library chunk citation back into its surrounding stored document text during follow-up verification.
  - **$O(N^2)$ Full-Line Rescan in Citation Marker Processing ([Issue #8463](https://github.com/LearningCircuit/local-deep-research/issues/8463) — accessed 2026-11-09):** Citation marker post-processing rescans full lines per marker without cost tests catching the quadratic blowup on dense reports.
  - **Benchmark Harness Lacks Full-Report & Citation-Quality Metrics and Bypasses Live Lifecycle ([Issue #8477](https://github.com/LearningCircuit/local-deep-research/issues/8477) & [Issue #8517](https://github.com/LearningCircuit/local-deep-research/issues/8517) — accessed 2026-11-09):** Built-in benchmarks (`SimpleQA`, `BrowseComp`) only score short factual QA accuracy rather than long-form report quality or citation precision, and `BenchmarkService` bypasses the live web/DB research lifecycle.

---

### 6. `jina-ai/node-DeepResearch` (5,241★, Apache-2.0)

- **Repository:** [jina-ai/node-DeepResearch](https://github.com/jina-ai/node-DeepResearch) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  Explicitly designed for **deep iterative answer-finding** rather than long-form essay generation ([`README.md`](https://github.com/jina-ai/node-DeepResearch/blob/main/README.md) & [`src/agent.ts`](https://github.com/jina-ai/node-DeepResearch/blob/main/src/agent.ts) — accessed 2026-11-09):
  1. **Optional Multi-Agent Decomposition (`planner.ts` in [`src/tools/planner.ts`](https://github.com/jina-ai/node-DeepResearch/blob/main/src/tools/planner.ts) — accessed 2026-11-09):** When `teamSize > 1`, acts as a "Principal Research Lead" to decompose the query into `teamSize` (default 3) orthogonal subproblems with `<20%` overlap across distinct axes (temporal, methodological, stakeholder, technical layer).
  2. **Main `Search → Read → Reason` State Machine (`getResponse` in `src/agent.ts`):**
     - Maintains `gaps: string[]` (queue of unanswered questions), `allKnowledge: KnowledgeItem[]` (accumulated QA/side-info/url knowledge items), `allKeywords: string[]`, `visitedUrls`, and `badAttempts`.
     - At each step, prompts the reasoning LLM (`gemini-2.5-pro` or `o3-mini`) with `getPrompt()` to pick exactly one action from enabled flags (`allowSearch`, `allowRead`, `allowReflect`, `allowAnswer`, `allowCoding`):
       - **`search`:** Generates search queries, deduplicates them via embedding cosine similarity (`dedupQueries` in `src/tools/jina-dedup.ts`), searches via Jina Reader Search / Brave / Serper / DuckDuckGo, and stores snippet soundbites.
       - **`visit` (`Read`):** Fetches full markdown of selected URLs via Jina Reader (`r.jina.ai`), segments text into chunks, and adds to `allKnowledge`.
       - **`reflect`:** Generates orthogonal sub-questions (`dedupQueries` filtered) and pushes them onto `gaps`.
       - **`coding`:** Executes JavaScript snippets in a sandbox (`CodeSandbox`) to compute exact math/dates/transformations.
       - **`answer`:** Proposes a final answer when examining the original root question.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Adversarial Answer Evaluator (`evaluateAnswer` in [`src/tools/evaluator.ts`](https://github.com/jina-ai/node-DeepResearch/blob/main/src/tools/evaluator.ts) — accessed 2026-11-09):** Evaluates candidate answers across 6 specialized check types (`definitive`, `freshness`, `plurality`, `attribution`, `completeness`, `strict` / `reject-all-answers`). The `reject-all-answers` prompt instructs a "ruthless and picky answer evaluator trained to REJECT answers" to argue against the answer, argue for it, and return an improvement plan (`"For get a pass, you must..."`) if any detail is missing or unattributed. Failed evaluations increment `badAttempts`, push the critique into `diaryContext`, and re-enter the `Search → Read → Reason` loop.
  - **Embedding Cosine-Similarity Query Deduplication ([`src/tools/jina-dedup.ts`](https://github.com/jina-ai/node-DeepResearch/blob/main/src/tools/jina-dedup.ts) — accessed 2026-11-09):** Embeds candidate queries via `jina-embeddings-v3` and drops any query with cosine similarity $\ge 0.86$ (`SIMILARITY_THRESHOLD = 0.86`) against historical queries or earlier queries in the same batch.
  - **Post-Hoc Semantic Chunk-Level Reference Anchoring (`buildReferences` in [`src/tools/build-ref.ts`](https://github.com/jina-ai/node-DeepResearch/blob/main/src/tools/build-ref.ts) — accessed 2026-11-09):** Instead of trusting the LLM to place inline citation markers, `buildReferences` segments the final answer into text chunks (`chunkText`), segments all read web pages into chunks ($\ge 80$ chars), embeds both sets via `getEmbeddings()` (with `jaccardRank` fallback), and matches each answer chunk to the highest-similarity web chunk above `minRelScore = 0.70`, injecting exact character-range `[1..maxRef]` footnote markers and exact quote excerpts!
- **Output Format & Knowledge Persistence:**
  - Returns a structured JSON/Markdown response with `{ answer, references: [{ exactQuote, title, url, dateTime }], visitedURLs, readURLs, usage }` via CLI or OpenAI-compatible HTTP SSE server (`/v1/chat/completions`). Stateless across requests.
- **Cost, Token & Loop Controls:**
  - **Token Budget (`tokenBudget` via `TokenTracker`):** Tracks cumulative prompt + completion + embedding tokens across all LLM and Jina API calls.
  - **Max Bad Attempts (`maxBadAttempts = 2`):** Limits how many times `evaluateAnswer` can reject a final answer before forcing exit.
  - **Beast Mode (`beastMode`):** When `tokenTracker.getTotalUsage().totalTokens >= tokenBudget` or `badAttempts >= maxBadAttempts`, disables all search/read/reflect actions and forces a final synthesis from accumulated `allKnowledge`.
- **Published Evaluation & Benchmark Evidence:**
  - None published in the repository (users ask how to benchmark it in [Issue #109](https://github.com/jina-ai/node-DeepResearch/issues/109) and report poor output on official examples in [Issue #120](https://github.com/jina-ai/node-DeepResearch/issues/120) — accessed 2026-11-09).
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Potential Infinite Loop in `deepsearch` ([Issue #118](https://github.com/jina-ai/node-DeepResearch/issues/118) — accessed 2026-11-09):** When `gaps` keeps getting replenished or `allowAnswer` is blocked on non-root questions while `tokenBudget` tracking fails on custom OpenAI-compatible endpoints that omit `usage` metadata, the `while` loop in `src/agent.ts` spins indefinitely.
  - **Token Budget Ignored Until Overshoot ([Issue #119](https://github.com/jina-ai/node-DeepResearch/issues/119) — accessed 2026-11-09):** Because `tokenBudget` is checked only *after* parallel sub-steps, embeddings, and full-page reads complete, and `beastMode` still runs a massive final synthesis + `buildReferences` embedding pass, actual token consumption regularly overshoots `tokenBudget` by 2–4×.
  - **Remote Prompt Injection Triggering Server-Side Code Execution Effects ([Issue #131](https://github.com/jina-ai/node-DeepResearch/issues/131) — accessed 2026-11-09):** Malicious instructions embedded in scraped web pages are ingested into `allKnowledge` and can hijack the agent into invoking the `coding` action (`CodeSandbox`), creating a remote prompt-injection-to-code-execution vector.
  - **`No object generated: couldn't parse the response` ([Issue #110](https://github.com/jina-ai/node-DeepResearch/issues/110) — accessed 2026-11-09):** Complex nested union schemas in `ObjectGeneratorSafe` fail on OpenAI-compatible models that do not strictly enforce JSON schema outputs.

---

### 7. `zilliztech/deep-searcher` (8,388★, Apache-2.0)

- **Repository:** [zilliztech/deep-searcher](https://github.com/zilliztech/deep-searcher) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  `zilliztech/deep-searcher` is an enterprise private-data + hybrid web agentic RAG framework backed by Milvus / Zilliz Cloud ([`README.md`](https://github.com/zilliztech/deep-searcher/blob/master/README.md) — accessed 2026-11-09). Its pipeline uses a router-agent architecture:
  1. **Agent Routing (`RAGRouter` in [`deepsearcher/agent/rag_router.py`](https://github.com/zilliztech/deep-searcher/blob/master/deepsearcher/agent/rag_router.py) — accessed 2026-11-09):** Inspects the query and dispatches to one of two multi-step RAG agents:
  2. **Mode A — `DeepSearch` ([`deepsearcher/agent/deep_search.py`](https://github.com/zilliztech/deep-searcher/blob/master/deepsearcher/agent/deep_search.py) — accessed 2026-11-09):**
     - *Query Decomposition (`_generate_sub_queries`):* Uses `SUB_QUERY_PROMPT` to break the original question into up to 4 sub-questions as a Python list.
     - *Collection Routing & Vector Search (`_search_chunks_from_vectordb`):* `CollectionRouter` selects relevant Milvus collections (`route()`), embeds the sub-query, retrieves top-$K$ chunks per collection, and runs an async per-chunk LLM reranker (`RERANK_PROMPT`).
     - *Gap Reflection (`_generate_gap_queries`):* Up to `max_iter = 3` iterations (`config.yaml`), invokes `REFLECT_PROMPT` with the original query, all sub-queries, and accepted chunks to generate new gap-filling search queries if needed.
     - *Final Synthesis (`query`):* Deduplicates all accepted `RetrievalResult` chunks via `deduplicate_results()` and prompts `SUMMARY_PROMPT` to synthesize a comprehensive report.
  3. **Mode B — `ChainOfRAG` ([`deepsearcher/agent/chain_of_rag.py`](https://github.com/zilliztech/deep-searcher/blob/master/deepsearcher/agent/chain_of_rag.py) — accessed 2026-11-09):**
     - Sequential multi-hop decomposition (`max_iter = 4`): at each hop, generates one simple follow-up query (`FOLLOWUP_QUERY_PROMPT`) conditioned on `intermediate_context` (prior queries + answers), retrieves and filters chunks, synthesizes a grounded intermediate answer (`INTERMEDIATE_ANSWER_PROMPT`), checks `REFLECT_PROMPT` (`"Yes"` / `"No"` whether enough info is gathered), and finishes with `FINAL_ANSWER_PROMPT` + `GET_SUPPORTED_DOCS_PROMPT`.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Binary LLM Chunk Acceptance Filter (`RERANK_PROMPT` in `deep_search.py`):** Evaluates every retrieved vector chunk individually against the query and forces a strict `"YES"` or `"NO"` decision, discarding irrelevant vector neighbors before they reach the context window.
  - **Anti-Hallucination Intermediate Synthesis (`INTERMEDIATE_ANSWER_PROMPT` in `chain_of_rag.py`):** Explicitly mandates: *"DO NOT hallucinate any information, only use the provided documents to generate the answer. Respond 'No relevant information found' if the documents do not contain useful information."*
  - **Post-Answer Supporting Document Selection (`GET_SUPPORTED_DOCS_PROMPT` in `chain_of_rag.py`):** Selects the exact subset of retrieved documents that directly support the final answer.
- **Output Format & Knowledge Persistence:**
  - **Persistent Vector Database (`Milvus` / `Zilliz Cloud` / local Milvus Lite):** Unlike stateless web-only agents, `deep-searcher` ingests local PDFs, Markdown, Office docs, and Firecrawl/Jina/Crawl4AI web pages into persistent named Milvus collections with metadata schemas (`load_from_local_files`, `load_from_website`), enabling cumulative knowledge reuse across all future queries.
- **Cost, Token & Loop Controls:**
  - Configured in [`deepsearcher/config.yaml`](https://github.com/zilliztech/deep-searcher/blob/master/deepsearcher/config.yaml) (accessed 2026-11-09):
    - `max_iter: 3` (reflection loop cap).
    - `chunk_size: 1500`, `chunk_overlap: 100` during ingestion.
    - Tracks `total_tokens` across all router, sub-query, rerank, reflection, and synthesis calls.
- **Published Evaluation & Benchmark Evidence:**
  - Qualitative comparison vs. Naive RAG in `README.md`; no quantitative benchmark table published in the repository.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Critical Security Vulnerability: Unauthenticated FastAPI Server Allows Arbitrary Local File Read, SSRF, and Provider-Config Hijack ([Issue #278](https://github.com/zilliztech/deep-searcher/issues/278) — accessed 2026-11-09):** The FastAPI server (`main.py`) exposes `/load-files/`, `/load-website/`, and `/set-provider-config/` without authentication or path/URL validation, allowing remote attackers to ingest `/etc/passwd` or internal cloud metadata endpoints (`169.254.169.254`) into Milvus and exfiltrate them via `/query/`, or hijack the LLM base URL to steal API keys.
  - **Multi-Tenant Authorization Bypass in `CollectionRouter` ([Issue #267](https://github.com/zilliztech/deep-searcher/issues/267) — accessed 2026-11-09):** `CollectionRouter` routes queries across *all* collections registered in the vector database regardless of caller authorization context, leaking private collections across tenants.
  - **Fixed 1,500-Char Chunking Breaks Long-Document / Book-Scale Reasoning ([Issue #240](https://github.com/zilliztech/deep-searcher/issues/240) — accessed 2026-11-09):** Users indexing book-length texts (e.g., 950,000-character novels across 40 chapters) report that flat 1,500-char chunking with binary per-chunk `YES`/`NO` reranking loses cross-chapter narrative and structural context.
  - **Lack of Predefined Report Outlines & Interleaved Parallel Logs ([Issue #233](https://github.com/zilliztech/deep-searcher/issues/233) & [Issue #234](https://github.com/zilliztech/deep-searcher/issues/234) — accessed 2026-11-09):** `DeepSearch` cannot accept a structured report outline, and concurrent `asyncio.gather` sub-queries interleave global log state.

---

### 8. `nickscamara/open-deep-research` (6,298★, NOASSERTION)

- **Repository:** [nickscamara/open-deep-research](https://github.com/nickscamara/open-deep-research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  Built on Vercel's Next.js AI Chatbot template + Firecrawl (`search`, `extract`, `scrape`), the entire deep research engine lives inside a single Next.js API route ([`app/(chat)/api/chat/route.ts`](https://github.com/nickscamara/open-deep-research/blob/main/app/(chat)/api/chat/route.ts) — accessed 2026-11-09):
  1. **Primary Chat Stream (`streamText`):** When `experimental_deepResearch` is toggled on, the main chat model (`modelId`, default `gpt-4o`) is restricted to `experimental_activeTools = ['deepResearch']`.
  2. **Iterative `deepResearch` Tool Sub-Loop (`maxDepth = 7`):**
     - Maintains `researchState = { findings: Array<{ text, source }>, summaries: string[], nextSearchTopic, urlToSearch, currentDepth, failedAttempts, maxFailedAttempts: 3, completedSteps, totalExpectedSteps: maxDepth * 5 }`.
     - Runs a nested `streamText` call with `maxSteps: maxDepth` (7) where the agent must sequentially invoke three inner tools:
       - **`search`:** Calls `app.search(query, { limit: 5 })` via Firecrawl (`@mendable/firecrawl-js`) and appends `{ text: item.description, source: item.url }` to `researchState.findings`.
       - **`extract`:** Calls `app.scrapeUrl(url)` or structured Firecrawl extract on target URLs (`urls: string[]`, `prompt: string`) and appends extracted JSON/markdown to `researchState.findings`.
       - **`analyze`:** Invokes a separate reasoning model (`reasoningModelId`, e.g., `o1-mini`, `o3-mini`, or `deepseek-reasoner` configured in [`lib/ai/models.ts`](https://github.com/nickscamara/open-deep-research/blob/main/lib/ai/models.ts) — accessed 2026-11-09) via `generateObject` to critique all accumulated `findings`, output `{ analysis, nextSearchTopic, shouldContinue, gaps }`, and terminate early if `shouldContinue === false`.
  3. **Final Report Generation (`generateText` with `reasoningModel`):**
     - Once the `deepResearch` tool loop finishes (or hits `maxDepth = 7`), passes all `researchState.findings` and `summaries` to `reasoningModel` with a system prompt requiring a comprehensive, long-form Markdown report with inline citations.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Reasoning-Model Sufficiency Check (`analyze` tool):** Uses the secondary reasoning model to inspect accumulated `findings` and identify missing gaps (`gaps: string[]`) at each iteration, with `maxFailedAttempts: 3`. However, there is no post-generation claim-to-URL verification.
- **Output Format & Knowledge Persistence:**
  - Streams progress updates (`research-update` data stream deltas) to the Next.js UI and saves the final Markdown report as a chat message or Canvas artifact in **Vercel Postgres (Neon)** (`lib/db/queries.ts`) and **Vercel Blob**. Does not index or reuse prior reports across future research sessions ([Issue #55](https://github.com/nickscamara/open-deep-research/issues/55)).
- **Cost, Token & Loop Controls:**
  - `maxDepth = 7` (`maxSteps: maxDepth` in inner `streamText`, outer `maxSteps: 5`).
  - `maxFailedAttempts: 3` inside `researchState`.
  - `maxDuration = process.env.MAX_DURATION ? parseInt(process.env.MAX_DURATION) : 300` seconds (5-minute serverless route timeout).
  - Upstash Redis sliding-window rate limiter (`lib/rate-limit.ts`).
- **Published Evaluation & Benchmark Evidence:**
  - None published ([Issue #50](https://github.com/nickscamara/open-deep-research/issues/50) explicitly requests benchmarks — accessed 2026-11-09).
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Hard 300-Second Route Timeout Kills Deep Research Runs ([Issue #54](https://github.com/nickscamara/open-deep-research/issues/54) — accessed 2026-11-09):** Because the entire 7-step `search → extract → analyze` loop plus final reasoning-model synthesis runs synchronously inside a single Next.js `POST` handler (`app/(chat)/api/chat/route.ts`), multi-step Firecrawl extractions + `o1-mini`/`o3-mini` calls frequently exceed `maxDuration = 300` seconds or Vercel's serverless function timeout.
  - **Incomplete/Coupled Architecture Between Chat Template and Deep Research Engine ([Issue #66](https://github.com/nickscamara/open-deep-research/issues/66) & [Issue #67](https://github.com/nickscamara/open-deep-research/issues/67) — accessed 2026-11-09):** Open engineering issues document that the monolithic `route.ts` state machine mixes UI streaming, authentication, rate limiting, and recursive research state in a single 800-line handler without modular retry or checkpointing.
  - **No Offline / Private Document Database Support ([Issue #55](https://github.com/nickscamara/open-deep-research/issues/55) — accessed 2026-11-09):** Tightly coupled to live Firecrawl web APIs; cannot research local PDF/Markdown corpora.

---

### 9. `SkyworkAI/DeepResearchAgent` (3,573★, MIT)

- **Repository:** [SkyworkAI/DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  `SkyworkAI/DeepResearchAgent` has evolved across two major architectural generations in its codebase ([`README.md`](https://github.com/SkyworkAI/DeepResearchAgent/blob/main/README.md) — accessed 2026-11-09):
  1. **Hierarchical Multi-Agent Runtime:**
     - **Top-Level `PlanningAgent` ([`src/agent/planning_agent/planning_agent.py`](https://github.com/SkyworkAI/DeepResearchAgent/blob/main/src/agent/planning_agent/planning_agent.py) — accessed 2026-11-09):** Inherits from `InterCodeAgent` (`max_steps = 20`, `planning_interval`). Decomposes complex tasks into structured action plans (`update_plan`: `initial` vs. `update` based on `facts_survey`) and delegates subtasks to specialized lower-level managed agents wrapped as callable tools:
       - **`deep_researcher_agent` (`configs/agent/deep_researcher_agent.py`, `max_steps = 5`):** Performs multi-round web search (`web_searcher`), scraping, and synthesis via `DeepResearcherTool` ([`src/tool/workflow_tools/deep_researcher.py`](https://github.com/SkyworkAI/DeepResearchAgent/blob/main/src/tool/workflow_tools/deep_researcher.py) — accessed 2026-11-09).
       - **`deep_analyzer_agent` (`configs/agent/deep_analyzer_agent.py`, `max_steps = 3`):** Performs deep multi-model analysis, math/logic verification, and file inspection (`DeepAnalyzerTool`).
       - **`browser_use_agent` (`max_steps = 5`):** Drives an interactive Playwright headless browser for dynamic web interaction.
       - **`python_interpreter` (`local_python_executor`):** Executes Python code for data analysis and plotting.
  2. **RSPL / SEPL Self-Evolution Protocol Layer:**
     - **RSPL (Resource Substrate Protocol Layer):** Registers prompts (`src/prompt/`), tools (`src/tool/`), environments (`src/environment/`), and memory (`src/memory/`) as versioned resources (`src/version/`).
     - **SEPL (Self Evolution Protocol Layer, `src/optimizer/`):** Implements closed-loop `Act → Observe → Optimize → Remember` cycles using reflection, Reinforce++, or GRPO optimizers to update prompts and agent configurations across runs.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Fact-Survey Pre-Planning (`PlanningAgent.update_plan`):** Before revising a plan at `planning_interval`, `PlanningAgent` runs a dedicated `facts_survey` prompt (`planning_plan_update_facts`) that explicitly classifies what facts are *known/verified*, what facts must be *looked up*, and what facts must be *derived*, preventing the planner from hallucinating missing premises.
  - **Cross-Verification via `deep_analyzer_agent`:** Used to cross-check extracted claims, documents, and numerical calculations.
- **Output Format & Knowledge Persistence:**
  - **Persistent Memory & Versioned Artifacts:** Persists session/event traces (`src/tracer/`), `ContextMemory`, and `PersistMemory` (`src/memory/`) alongside versioned prompt/tool states in `workdir/`.
- **Cost, Token & Loop Controls:**
  - Strict hierarchical step caps: `PlanningAgent` (`max_steps = 20`, `max_len = 10000` observation truncation), `deep_researcher_agent` (`max_steps = 5`), `deep_analyzer_agent` (`max_steps = 3`), `browser_use_agent` (`max_steps = 5`), and `DeepResearcherTool` (`max_rounds = 3`, `num_Write = 3` parallel queries per round).
- **Published Evaluation & Benchmark Evidence:**
  - Evaluated on the **GAIA Benchmark** (reported in earlier README / documentation and discussed in [Issue #81](https://github.com/SkyworkAI/DeepResearchAgent/issues/81) & [Issue #83](https://github.com/SkyworkAI/DeepResearchAgent/issues/83) — accessed 2026-11-09), claiming **82.42%** average on GAIA validation and **73.33%** on GAIA test.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Severe Reproducibility Gap on GAIA Benchmark ([Issue #81](https://github.com/SkyworkAI/DeepResearchAgent/issues/81) & [Issue #83](https://github.com/SkyworkAI/DeepResearchAgent/issues/83) — accessed 2026-11-09):** Independent users running the open-source codebase against GAIA reported achieving only **~57%** on Level 1 (vs. the claimed >80%), noting that key prompt tuning, model routing, or environment states from the paper's evaluation were missing or altered in the public release.
  - **Copy-Pasted Sub-Agent Implementations ([Issue #78](https://github.com/SkyworkAI/DeepResearchAgent/issues/78) — accessed 2026-11-09):** Users inspecting `src/agent/` discovered that four distinct agent files shared identical code and prompts, differing only in class names while the actual differentiation lived inside the tool wrappers (`deep_researcher.py`, `deep_analyzer.py`).
  - **Playwright Browser Blocked by Anti-Bot CAPTCHAs ([Issue #84](https://github.com/SkyworkAI/DeepResearchAgent/issues/84) — accessed 2026-11-09):** `browser_use_agent` frequently stalls on Cloudflare/Google "verify you are human" challenges during live web browsing.
  - **`NoneType` Crash When LLM Returns `tool_calls=None` ([Issue #69](https://github.com/SkyworkAI/DeepResearchAgent/issues/69) — accessed 2026-11-09):** `ToolCallingAgent` and `PlanningAgent` crashed or failed to advance when a model responded with natural language text and `tool_calls=None` instead of invoking `final_answer`.
  - **Python Sandbox Executor Escape / Security Vulnerability ([Issue #98](https://github.com/SkyworkAI/DeepResearchAgent/issues/98) — accessed 2026-11-09):** Security researchers reported a sandbox vulnerability in the Python code executor (`local_python_executor`).


---

### 10. `SalesforceAIResearch/enterprise-deep-research` (1,224★, Apache-2.0)

- **Repository:** [SalesforceAIResearch/enterprise-deep-research](https://github.com/SalesforceAIResearch/enterprise-deep-research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  Accompanying the paper *Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics* (`arXiv:2510.17797`, accepted at AAAI Agentic AI Benchmarks and Applications Workshop; [`README.md`](https://github.com/SalesforceAIResearch/enterprise-deep-research/blob/main/README.md) — accessed 2026-11-09), EDR is a massive LangGraph workflow (`src/graph.py`, 231 KB, and `src/prompts.py`, 106 KB):
  1. **Master Planning & Decomposition (`master_planner` in [`src/graph.py`](https://github.com/SalesforceAIResearch/enterprise-deep-research/blob/main/src/graph.py) — accessed 2026-11-09):**
     - Analyzes the user query, uploaded files, and connected SQL databases (`_session_database_info`), generating an adaptive research plan and initializing a structured `TodoItem` checklist (`UserSteeringManager` in [`src/steering.py`](https://github.com/SalesforceAIResearch/enterprise-deep-research/blob/main/src/steering.py) — accessed 2026-11-09).
  2. **Specialized Multi-Agent Search & Enterprise Tool Execution:**
     - Routes sub-queries in parallel (`--parallel-search`, `--parallel-max 4`) across:
       - **Four Domain Web Search Agents:** General Web (`tavily`), Academic (scholarly/arXiv papers), GitHub (repositories/code), and LinkedIn (professional/company profiles).
       - **Enterprise MCP & NL2SQL Tools:** Queries enterprise relational databases via NL2SQL, analyzes local CSV/PDF/Excel documents, and invokes external MCP servers.
       - **Visualization Agent:** Generates charts and data-driven visual insights for quantitative queries.
  3. **Iterative Reflection & Live Human-in-the-Loop Steering (`reflection` & `steering.py`):**
     - After each research loop, evaluates knowledge gaps against the `TodoItem` list (`pending`, `in_progress`, `completed`, `cancelled`, `superseded`).
     - Processes real-time natural-language steering messages from the user (e.g., *"Focus on Q4 revenue in Europe"*, *"Stop researching X"*), converting them into `SteeringConstraint` mutations (`focus_only`, `exclude`, `prioritize`, `stop_searching`, `add_topic`) with monotonically increasing `plan_version` numbers.
  4. **Report Synthesis:** Compiles a structured executive/technical Markdown report with inline `[Title](URL)` citations.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Iterative Gap Reflection + Steerable Todo Verification (`src/steering.py` & `src/prompts.py`):** Tracks explicit task completion evidence per `TodoItem` and enforces strict source attribution in `src/prompts.py`. However, there is no separate automated fact-checking agent that re-fetches cited URLs post-synthesis.
- **Output Format & Knowledge Persistence:**
  - Outputs rich Markdown reports with embedded visualizations and JSON execution trajectories (`--collect-traj`). Persists session state via `session_store.py`, though cross-session knowledge graphs are not accumulated.
- **Cost, Token & Loop Controls:**
  - Configured in [`src/config.py`](https://github.com/SalesforceAIResearch/enterprise-deep-research/blob/main/src/config.py) (accessed 2026-11-09):
    - `MAX_WEB_RESEARCH_LOOPS = 10` (default in `.env`; set to `2`–`5` in [`benchmarks/README.md`](https://github.com/SalesforceAIResearch/enterprise-deep-research/blob/main/benchmarks/README.md) — accessed 2026-11-09).
    - `--parallel-max 4` concurrent search tasks per loop.
    - Explicit circuit-breaker loop checks in `src/graph.py` to prevent infinite planner-reflector oscillation.
- **Published Evaluation & Benchmark Evidence:**
  - **#1 Rank on LiveResearchBench Leaderboard** (announced Dec 12, 2025 in `README.md`).
  - Official entry on the **DeepResearchBench Leaderboard** (`muset-ai/DeepResearch-Bench-Leaderboard`) and evaluated on **BrowseComp** (`benchmarks/run_research_concurrent.py --benchmark drb`).
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Concurrency Race Condition Overwriting Database Connections Across Users ([Issue #8](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/8) — accessed 2026-11-09):** In `src/graph.py`, `_session_database_info` falls back to a shared `"__global__"` key when `session_id` is absent in non-streaming requests, causing concurrent requests to overwrite and leak each other's enterprise database connections.
  - **Benchmark Contamination / Leaked BrowseComp QA Pairs in Repo ([Issue #4](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/4) & [Issue #10](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/10) — accessed 2026-11-09):** Community members flagged that plaintext BrowseComp QA pairs were committed without the standard canary string or encryption, risking training-set contamination via web crawlers.
  - **Hardcoded Deprecated OpenAI Reasoning Models (`o3-mini` / `o4-mini`) ([Issue #14](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/14) — accessed 2026-11-09):** Default model configurations in `src/config.py` (`o3-mini`, `o4-mini`) broke when OpenAI sunset those endpoints on October 23, 2026.
  - **LangChain / LangGraph v1 Incompatibility ([Issue #1](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/1) — accessed 2026-11-09):** Pinned pre-v1 LangGraph dependencies prevent upgrading to LangGraph v1.

---

### 11. `AnotiaWang/deep-research-web-ui` (2,226★, No License)

- **Repository:** [AnotiaWang/deep-research-web-ui](https://github.com/AnotiaWang/deep-research-web-ui) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  A Nuxt 3 / TypeScript full-stack & client-mode deep research application that substantially extends the `dzhng` tree paradigm with **structured search plans, relevance assessment, query retry, and bounded on-demand full-page reading** ([`lib/core/deep-research.ts`](https://github.com/AnotiaWang/deep-research-web-ui/blob/main/lib/core/deep-research.ts) — accessed 2026-11-09):
  1. **Structured Query & Search Plan Generation (`generateSearchQueries` in `lib/core/search-queries.ts`):**
     - Uses plain-prompt streaming JSON (`parseStreamingJson` rather than provider-locked `generateObject`) so any OpenAI-compatible, DeepSeek, SiliconFlow, or Ollama model works.
     - Emits queries paired with a structured `SearchPlan` (`searchPlanSchema`) separating core query terms from time ranges and domain/source filters.
  2. **Search Execution & Snippet Extraction (`processSearchResult` in [`lib/core/extract-learnings.ts`](https://github.com/AnotiaWang/deep-research-web-ui/blob/main/lib/core/extract-learnings.ts) — accessed 2026-11-09):**
     - Searches via Tavily, Firecrawl, Exa, Bocha, SearXNG, or Jina.
     - Calls `processSearchResult` to extract structured `ResearchLearning` items (each retaining `sourceIndex`, `quote`, `confidence`, and `conflictsWith`) plus optional `readRequests: [{ sourceId, question }]` (max 2 per node) when snippets are insufficient.
  3. **Bounded On-Demand Full-Page Source Reading (`createSourceReader` in [`lib/core/read-source.ts`](https://github.com/AnotiaWang/deep-research-web-ui/blob/main/lib/core/read-source.ts) — accessed 2026-11-09):**
     - When `processSearchResult` requests full-page reads, `sourceReader.read()` fetches the full page via Jina/Firecrawl/local reader, caches normalized URLs across all recursive branches, and re-runs `processSearchResult` (`stage = 'after_source_read'`) to extract verbatim quotes.
  4. **Relevance Assessment & Single-Retry Loop (`assessSearchLearnings` in `shared/utils/search-assessment.ts`):**
     - Evaluates whether extracted learnings actually answer the node's `researchGoal`. If insufficient on `attempt === 1`, rewrites the query and retries once (`maxAttempt = 2`).
  5. **Deduplication & Recursive Tree Expansion (`deduplicateLearnings`):**
     - Deduplicates learnings while preserving source links, halves breadth (`Math.ceil(breadth / 2)`), decrements `depth`, and recurses.
  6. **Interactive Citation Inspection & Passage Follow-Up:**
     - Users can click any citation in the rendered report to inspect the exact extracted source excerpt, trigger a targeted follow-up search on a specific claim, and update the passage while preserving report version history.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Source-Linked Learnings with Conflict Detection:** Unlike `dzhng/deep-research` (which strips URLs from learnings), `AnotiaWang/deep-research-web-ui` binds every `ResearchLearning` to its exact `sourceIndex`, verbatim `quote`, and `conflictsWith` flags (`lib/core/extract-learnings.ts`).
  - **On-Demand Full-Page Verification (`readRequests`):** Specifically instructs the extractor to request full-page reads (`max(2)` per node) when search snippets lack verbatim proof, rather than guessing from a snippet.
  - **Query Sufficiency Gate (`assessSearchLearnings`):** Automatically retries low-yield queries with relaxed/rewritten constraints (implemented after [Issue #60](https://github.com/AnotiaWang/deep-research-web-ui/issues/60) — accessed 2026-11-09).
- **Output Format & Knowledge Persistence:**
  - Exports Markdown and PDF reports; persists full research session trees, source excerpts, and report revision history in browser storage so users can interactively branch or re-verify passages.
- **Cost, Token & Loop Controls:**
  - `breadth` and `depth` tree parameters.
  - **Shared Run-Wide Full-Page Read Budget (`sourceReadLimits` in `lib/core/read-source.ts`):** Hard-capped at `{ perNode: 2, perRun: 6, concurrency: 2, timeoutMs: 20_000 }` across the entire recursive tree!
  - `maxAttempt = 2` per search node.
  - Dynamic output token calculation via `getMaxOutputTokens(model)` (defaulting to 4,096 or higher for reasoning models).
- **Published Evaluation & Benchmark Evidence:**
  - None published.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Reasoning Models Exhausting 4,096 Output Token Cap Before Emitting JSON ([Issue #101](https://github.com/AnotiaWang/deep-research-web-ui/issues/101) — accessed 2026-11-09):** When using reasoning models (`DeepSeek-R1`, `QwQ`, `o3-mini`) that emit `reasoning_content`, `processSearchResult` hardcoded `maxOutputTokens: 4096`. Because providers count `reasoning_content` + `content` against `max_tokens`, the reasoning trace consumed all 4,096 tokens and truncated `content` mid-JSON, throwing `Invalid structured output`.
  - **UI Node Retry Crash from `structuredClone` on Vue Reactive Proxies ([Issue #103](https://github.com/AnotiaWang/deep-research-web-ui/issues/103) — accessed 2026-11-09):** Clicking the node "Retry" button in v1.3.0 threw `DataCloneError` inside `snapshotResearchGraph` because `structuredClone()` was called directly on Vue reactive Proxy objects containing non-cloneable state.
  - **Firecrawl Concurrency & Rate-Limit Contention ([Issue #73](https://github.com/AnotiaWang/deep-research-web-ui/issues/73) & [Issue #66](https://github.com/AnotiaWang/deep-research-web-ui/issues/66) — accessed 2026-11-09):** Parallel search branches hit Firecrawl HTTP 429 rate limits without backoff or per-provider error classification.
  - **Truncated / Shallow Final Reports on Large Trees ([Issue #69](https://github.com/AnotiaWang/deep-research-web-ui/issues/69) — accessed 2026-11-09):** Single-pass final report generation compresses large numbers of tree learnings too aggressively unless section-by-section writing is used.

---

### 12. `u14app/deep-research` (4,687★, MIT)

- **Repository:** [u14app/deep-research](https://github.com/u14app/deep-research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  A Next.js 15 / TypeScript multi-provider Web UI, SSE API, and MCP Server that introduces a **Dual-Model (`thinkingModel` + `taskModel`) Split Architecture** ([`src/utils/deep-research/index.ts`](https://github.com/u14app/deep-research/blob/main/src/utils/deep-research/index.ts) & [`src/hooks/useDeepResearch.ts`](https://github.com/u14app/deep-research/blob/main/src/hooks/useDeepResearch.ts) — accessed 2026-11-09):
  1. **Interactive Report Planning (`writeReportPlan`):**
     - Uses `thinkingModel` (e.g., `gemini-2.5-flash-thinking`, `deepseek-reasoner`, `o3-mini`) with `ThinkTagStreamProcessor` (which separates `<think>...</think>` blocks into a `reasoning` stream) and `writeReportPlanPrompt` ([`src/utils/deep-research/prompts.ts`](https://github.com/u14app/deep-research/blob/main/src/utils/deep-research/prompts.ts) — accessed 2026-11-09) to generate a structured report outline (`<report-plan>`), which the user can edit in the UI before execution.
  2. **SERP Task Decomposition (`generateSERPQuery`):**
     - Uses `thinkingModel` to convert the approved `reportPlan` into a JSON array of `{ query, researchGoal }` tasks (`getSERPQuerySchema`).
  3. **Parallel Search & Summarization (`runSearchTask`):**
     - For each task, executes either:
       - External search provider (`tavily`, `firecrawl`, `exa`, `bocha`, `searxng`, `jina`) + `taskModel` summarization (`processSearchResultPrompt`), or
       - Native model web search grounding (`useSearchGrounding: true` for Gemini networking models) via `processResultPrompt`.
     - Users can also trigger follow-up sub-queries on individual tasks in the UI (`useDeepResearch.ts`).
  4. **Final Report Compilation (`writeFinalReport`):**
     - Feeds `<report-plan>`, all `<learning>` blocks, external `<sources>`, `<images>`, and user-defined `<requirement>` guidelines to `thinkingModel` (`writeFinalReportPrompt`) to stream the final report, appending deduplicated footnote definitions `[1]: url "title"`.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Prompt-Only Footnote Citation Binding (`writeFinalReportPrompt`):** Instructs the model to cite sources using numbered Markdown footnote references (`[1]`, `[2]`) corresponding to the ordered `sourceList` appended after generation. No automated claim verification or post-synthesis fact checking.
- **Output Format & Knowledge Persistence:**
  - **Browser IndexedDB Persistence & Local Knowledge Base:** Persists research sessions (`useHistoryStore` via `storage.ts` IndexedDB) and includes a local Knowledge Base (`useKnowledgeStore` in `src/store/knowledge.ts`) allowing users to upload local files or crawl URLs (`/api/crawler`) and attach them as local resources to research runs.
  - Also exposes a programmatic `/api/sse` endpoint and `/api/mcp` Model Context Protocol server ([`docs/api-doc.md`](https://github.com/u14app/deep-research/blob/main/docs/api-doc.md) — accessed 2026-11-09).
- **Cost, Token & Loop Controls:**
  - Splits expensive reasoning calls (`thinkingModel` for planning, query generation, and final report) from high-volume search-result reading (`taskModel` for per-query summarization).
  - Bounded `maxResult = 5` search results per query; single-pass task list by default in `start()` unless the user manually triggers deeper node searches in the UI.
- **Published Evaluation & Benchmark Evidence:**
  - None published; `AGENTS.md` explicitly notes: *"Currently, there are no automated tests in the codebase."*
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Critical SSRF Vulnerability in `/api/crawler` ([Issue #153](https://github.com/u14app/deep-research/issues/153) — accessed 2026-11-09):** The server-side crawler endpoint (`src/app/api/crawler/route.ts`) accepts any user-supplied URL and fetches it directly from the server without IP blacklisting or scheme validation, allowing attackers to read AWS/GCP cloud metadata endpoints (`http://169.254.169.254/latest/meta-data/`) or scan internal VPC services.
  - **Local Knowledge-Base Resources Dropped from Final Report ([Issue #130](https://github.com/u14app/deep-research/issues/130) — accessed 2026-11-09):** Although users can attach local Knowledge Base documents to a research session, `writeFinalReport` in `useDeepResearch.ts` failed to include the local KB chunks in the final synthesis prompt, silently ignoring uploaded files.
  - **Final Report Generation Fails on Token Limit Exceeded ([Issue #138](https://github.com/u14app/deep-research/issues/138) — accessed 2026-11-09):** Concatenating all task `learnings` and full source contents into a single `writeFinalReport` prompt without token-budget truncation causes HTTP 429 / token-limit-exceeded failures on Gemini Free Tier and smaller context models.
  - **SSE Stream Content Duplication ([Issue #128](https://github.com/u14app/deep-research/issues/128) — accessed 2026-11-09):** Improper chunk buffering in the `/api/sse` stream processor caused duplicated text blocks in rendered reports.

---

### 13. `btahir/open-deep-research` (2,139★, MIT)

- **Repository:** [btahir/open-deep-research](https://github.com/btahir/open-deep-research) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  An interactive, **node-graph canvas** (`@xyflow/react`) Next.js application inspired by Gemini Deep Research where human curation and multi-branch visual exploration sit at the center of the loop ([`README.md`](https://github.com/btahir/open-deep-research/blob/main/README.md) & [`FLOW_PROJECTS.md`](https://github.com/btahir/open-deep-research/blob/main/FLOW_PROJECTS.md) — accessed 2026-11-09):
  1. **Prompt Optimization (`/api/optimize-research` in [`app/api/optimize-research/route.ts`](https://github.com/btahir/open-deep-research/blob/main/app/api/optimize-research/route.ts) — accessed 2026-11-09):**
     - Rewrites a raw user topic into an optimized research prompt and suggested search queries.
  2. **Web Search + Local Document Upload (`/api/search` & `DocumentUpload`):**
     - Fetches search results via Google Custom Search Engine (GSE) or Bing, and parses user-uploaded `TXT`, `PDF`, and `DOCX` files.
  3. **LLM Relevance Ranking (`/api/analyze` in [`app/api/analyze/route.ts`](https://github.com/btahir/open-deep-research/blob/main/app/api/analyze/route.ts) — accessed 2026-11-09):**
     - Ranks candidate search results (`0.0` to `1.0` relevance score + reasoning) and lets the user curate which sources to keep before fetching full content via Jina Reader (`/api/fetch-content`).
  4. **Initial Report & Visual Canvas Branching (`/api/report` & `/api/question`):**
     - [`app/api/report/route.ts`](https://github.com/btahir/open-deep-research/blob/main/app/api/report/route.ts) (accessed 2026-11-09) generates a structured JSON report (`{ title, summary, sections: [{ title, content }] }`) from the selected sources.
     - Rendered as a node on an infinite ReactFlow canvas (`components/flow/`), where users can spawn child `QuestionNode` or `SearchNode` branches to explore follow-up questions.
  5. **Multi-Report Consolidation (`/api/consolidate` in [`app/api/consolidate/route.ts`](https://github.com/btahir/open-deep-research/blob/main/app/api/consolidate/route.ts) — accessed 2026-11-09):**
     - Collects multiple branch reports from the canvas or Knowledge Base, builds a unified deduplicated `sourceIndex` (`[1] Source: name - url`), and synthesizes a master consolidated report with `[1..N]` inline citations.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Pre-Report Source Relevance Scoring (`/api/analyze`) + Human Selection Gate:** Scores every search snippet (`0.0–1.0`) and lets the user deselect noisy URLs before synthesis.
  - **Deduplicated Source Index in Consolidation (`/api/consolidate`):** Assigns deterministic `[1..N]` indices to unique source URLs across all child reports and instructs the consolidator to *"Use ONLY the source numbers provided in the source index"* (though initial single-node `/api/report` lacked clickable numbered citations, as noted in [Issue #28](https://github.com/btahir/open-deep-research/issues/28)).
- **Output Format & Knowledge Persistence:**
  - **Persistent Browser Knowledge Base & Visual Project Canvas:**
    - `useKnowledgeBase` hook stores generated reports and sources in `localStorage` with sidebar search (`[Enhancement] - KB Search Algorithm`, [Issue #23](https://github.com/btahir/open-deep-research/issues/23)).
    - `useFlowProjects` hook ([`FLOW_PROJECTS.md`](https://github.com/btahir/open-deep-research/blob/main/FLOW_PROJECTS.md) — accessed 2026-11-09) auto-saves full ReactFlow node/edge graphs to `localStorage` with JSON export/import and storage quota monitoring.
    - Exports final reports to PDF, Word (`.docx`), and Markdown.
- **Cost, Token & Loop Controls:**
  - Human-driven branching on the ReactFlow canvas prevents runaway autonomous loops.
  - Upstash Redis rate limiting (`reportContentRatelimit` in `lib/redis.ts`, bypassed when `platform === 'ollama'`).
  - Hard cap on search results per query (originally 10, raised to configurable 10–50 after [Issue #27](https://github.com/btahir/open-deep-research/issues/27)).
- **Published Evaluation & Benchmark Evidence:**
  - None published.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Google Custom Search Engine (GSE) Returning `totalResults: 0` on Valid LLM-Generated Queries ([Issue #30](https://github.com/btahir/open-deep-research/issues/30) — accessed 2026-11-09):** Overly long or complex boolean/quoted search queries generated by `/api/optimize-research` cause Google GSE to return `totalResults: 0`, stalling the pipeline before `/api/analyze`.
  - **Missing Clickable Inline Citations in Base Report Nodes ([Issue #28](https://github.com/btahir/open-deep-research/issues/28) — accessed 2026-11-09):** While `/api/consolidate` creates `[1..N]` citations, standard `/api/report` nodes output `{ title, summary, sections }` without mapping inline claims to clickable numbered `[1]` reference links.
  - **Low Default Search Result Cap (10 Results) Limiting Research Depth ([Issue #27](https://github.com/btahir/open-deep-research/issues/27) — accessed 2026-11-09):** Users noted that capping search at 10 results per query was too shallow for academic/literature reviews.
  - **Null-Reference Crash on Malformed LLM JSON Fields ([Issue #32](https://github.com/btahir/open-deep-research/issues/32) — accessed 2026-11-09):** Unvalidated LLM responses missing expected string fields triggered `undefined is not an object (evaluating 'e.toLowerCase')` in the frontend.

---

### 14. `mshumer/OpenDeepResearcher` (2,792★, MIT)

- **Repository:** [mshumer/OpenDeepResearcher](https://github.com/mshumer/OpenDeepResearcher) — accessed 2026-11-09
- **Architecture & Exact Pipeline Steps:**
  A single-cell (~280 LoC) asynchronous Python Jupyter/Colab notebook (`open_deep_researcher.ipynb` and `open_deep_researcher_gradio.ipynb`, [`mshumer_notebook.ipynb`](https://github.com/mshumer/OpenDeepResearcher/blob/main/open_deep_researcher.ipynb) — accessed 2026-11-09) chaining OpenRouter (`anthropic/claude-3.5-haiku` default), SerpAPI, and Jina Reader (`https://r.jina.ai/`):
  1. **Initial Query Decomposition (`generate_search_queries_async`):**
     - Prompts the LLM to emit up to 4 distinct search queries formatted as a Python list literal (`['query1', 'query2']`) and parses the raw LLM text using Python's built-in `eval(response)`!
  2. **Iterative Async Search-Scrape-Filter-Extract Loop (`while iteration < iteration_limit`):**
     - *Concurrent SERPAPI Search (`perform_search_async`):* Runs `asyncio.gather` across all search queries for the current round, extracting all `organic_results[].link` URLs (~10 links per query = up to 40 links per round) and deduplicating against `aggregated_links`.
     - *Concurrent Jina Webpage Fetch (`fetch_webpage_text_async`):* Fetches full markdown text for every unique link concurrently via `https://r.jina.ai/{url}`.
     - *Binary Page Usefulness Gate (`is_page_useful_async`):* Passes the `user_query` and the first `20,000` characters of `page_text` (`page_text[:20000]`) to the LLM, asking it to respond with `"Yes"` or `"No"`.
     - *Context Extraction (`extract_relevant_context_async`):* For every page judged `"Yes"`, calls the LLM again with `page_text[:20000]` to extract relevant facts into `all_contexts`.
     - *Gap Analysis & Follow-Up Query Generation (`get_new_search_queries_async`):* Sends `user_query`, `previous_search_queries`, and all accumulated `all_contexts` to the LLM. If the LLM returns `""`, the loop breaks early; otherwise it parses the returned Python list via `eval(response)` and starts the next iteration.
  3. **Final Report Generation (`generate_final_report_async`):**
     - Concatenates all extracted `all_contexts` and prompts the LLM to write a comprehensive report.
- **Claim Verification & Anti-Hallucination Mechanisms:**
  - **Binary LLM Page Filter (`is_page_useful_async`):** Filters out irrelevant scraped pages before context extraction.
  - **Complete Loss of Source Attribution in `all_contexts`:** Because `process_link` returns only the extracted string (`return context`) without attaching the source `url` or `title`, `all_contexts` is a flat list of anonymous text strings (`List[str]`). Consequently, `generate_final_report_async` has **zero access to the URLs or titles** of the pages it read and cannot produce grounded citations!
- **Output Format & Knowledge Persistence:**
  - Prints a plain Markdown report string to the Jupyter cell or Gradio textbox. Completely stateless.
- **Cost, Token & Loop Controls:**
  - User-input `iteration_limit` (default `2`), `page_text[:20000]` character truncation per page, and URL deduplication via `seen_links`.
  - **Zero Concurrency Semaphore or Per-Round Link Cap:** Every organic link returned by SerpAPI (~10 per query × 4 queries = 40 links per round) is fetched via Jina Reader and evaluated via 1–2 LLM calls (`is_page_useful_async` + `extract_relevant_context_async`) with unbounded `asyncio.gather` concurrency!
- **Published Evaluation & Benchmark Evidence:**
  - None published.
- **Real Issues & Failure Modes (from GitHub Issues):**
  - **Runaway API Credit Exhaustion ("WARNING!!! IT WILL CONSUME ALL YOUR CREDITS!") ([Issue #15](https://github.com/mshumer/OpenDeepResearcher/issues/15) & [Issue #16](https://github.com/mshumer/OpenDeepResearcher/issues/16) — accessed 2026-11-09):** Because each round fires 4 SerpAPI queries, fetches ~40 full webpages through Jina Reader API (`r.jina.ai`), and executes up to 80 OpenRouter LLM calls (40 usefulness checks + up to 40 context extractions, each up to 20,000 chars) with no `Semaphore`, max-links cap, or token budget, a single 3-iteration run can burn hundreds of thousands of Jina and OpenRouter tokens in seconds.
  - **Arbitrary Code Execution via `eval(response)` on LLM Output (`open_deep_researcher.ipynb` Cell 2):** Both `generate_search_queries_async` and `get_new_search_queries_async` parse LLM responses using raw Python `eval(response)` instead of `ast.literal_eval` or JSON parsing—meaning a prompt injection in a scraped webpage (`all_contexts` is fed directly into `get_new_search_queries_async`) can execute arbitrary Python code in the notebook kernel!
  - **Silent Final Report Failure in Gradio UI When Context Overflows ([Issue #4](https://github.com/mshumer/OpenDeepResearcher/issues/4) — accessed 2026-11-09):** When `all_contexts` accumulates dozens of multi-thousand-word page extractions, `generate_final_report_async` exceeds the model's context window on OpenRouter (`resp.status != 200`), returns `None`, and causes the Gradio app to finish without producing a final report.

---

## Cross-Cutting Synthesis: Type A Architecture vs. Real-World Failure Modes

### 1. The Verification Gap in Type A Frameworks
Across the 14 repositories, **retrieval breadth and orchestration complexity vastly outpace claim verification**:
- **Anonymous Learning Buffers Cause Citation Drift:** Early tree-based systems (`dzhng/deep-research`, `mshumer/OpenDeepResearcher`) decouple extracted `learnings: string[]` from `visitedUrls: string[]`. By the time the writer LLM sees the learnings, it either appends an unlinked URL dump (`dzhng`) or cannot cite sources at all (`mshumer`).
- **Four Notable Verification Patterns Worth Benchmarking:**
  1. **Post-Draft Multi-Agent Fact-Check Loop (`assafelovic/gpt-researcher`):** `FactCheckerAgent` (`multi_agents/agents/fact_checker.py`) audits draft claims against scraped context with up to 3 bounded revision loops (`DEFAULT_MAX_FACT_CHECK_REVISIONS = 3`), helping lift verified citation density by **+89%** on DeepResearch Bench.
  2. **Post-Hoc Embedding Chunk Alignment (`jina-ai/node-DeepResearch`):** `buildReferences` (`src/tools/build-ref.ts`) segments both the generated answer and all read webpages into chunks, embeds them with `jina-embeddings-v3`, and deterministically binds answer spans to source quotes at $\ge 0.70$ cosine similarity—eliminating LLM-hallucinated URLs.
  3. **Multi-Tier Bibliometric & Predatory Venue Filtering (`LearningCircuit/local-deep-research`):** `JournalReputationFilter` (`journal_reputation_filter.py`) deterministically filters academic sources against ~217K bundled OpenAlex venues, DOAJ, and predatory blacklists before synthesis, paired with `EvidenceEvaluator` source-reliability weights (`0.3`–`1.0`).
  4. **Snippet-to-Full-Page Escalation with Shared Read Budgets (`AnotiaWang/deep-research-web-ui`):** `extract-learnings.ts` binds each learning to a `sourceIndex`, verbatim `quote`, and `conflictsWith` array, and escalates to `read-source.ts` (`perNode: 2, perRun: 6`) when search snippets lack verbatim proof.

### 2. Six Systemic Failure Modes Documented Across Type A GitHub Issues

| Failure Category | Mechanism | Representative GitHub Issues (Accessed 2026-11-09) |
| :--- | :--- | :--- |
| **1. Reasoning Token Starvation** | Reasoning models (`gpt-5.4`, `DeepSeek-R1`, `o3-mini`) spend the entire `max_tokens=4000`/`4096` cap on hidden reasoning tokens and return empty strings or truncated JSON. | `gpt-researcher` [#2251](https://github.com/assafelovic/gpt-researcher/issues/2251), `AnotiaWang` [#101](https://github.com/AnotiaWang/deep-research-web-ui/issues/101), `local-deep-researcher` [#90](https://github.com/langchain-ai/local-deep-researcher/issues/90) & [#92](https://github.com/langchain-ai/local-deep-researcher/issues/92) |
| **2. Unbounded Loops & Credit Burn** | Missing `Semaphore`/link caps (`mshumer`), post-hoc token budget checks (`jina-ai`), or uncounted human-feedback revisions (`open_deep_research`, `gpt-researcher`). | `mshumer` [#15](https://github.com/mshumer/OpenDeepResearcher/issues/15), `jina-ai` [#118](https://github.com/jina-ai/node-DeepResearch/issues/118) & [#119](https://github.com/jina-ai/node-DeepResearch/issues/119), `open_deep_research` [#269](https://github.com/langchain-ai/open_deep_research/issues/269), `gpt-researcher` [#2163](https://github.com/assafelovic/gpt-researcher/issues/2163) |
| **3. Context Overflow & Destructive Truncation** | Raw webpage ingestion overflows sub-agent context; retry handlers pop recent messages instead of trimming oldest tool outputs. | `open_deep_research` [#218](https://github.com/langchain-ai/open_deep_research/issues/218), [#252](https://github.com/langchain-ai/open_deep_research/issues/252), [#296](https://github.com/langchain-ai/open_deep_research/issues/296); `u14app` [#138](https://github.com/u14app/deep-research/issues/138); `mshumer` [#4](https://github.com/mshumer/OpenDeepResearcher/issues/4) |
| **4. Scraper Anti-Bot Blocks & Junk Poisoning** | Challenge/CAPTCHA HTML ingested as valid source text (`LearningCircuit`), DuckDuckGo/Google GSE silent zero-result failures, or Zhihu/SEO farm poisoning (`local-deep-researcher`). | `LearningCircuit` [#8459](https://github.com/LearningCircuit/local-deep-research/issues/8459), `local-deep-researcher` [#87](https://github.com/langchain-ai/local-deep-researcher/issues/87) & [#105](https://github.com/langchain-ai/local-deep-researcher/issues/105), `SkyworkAI` [#84](https://github.com/SkyworkAI/DeepResearchAgent/issues/84), `btahir` [#30](https://github.com/btahir/open-deep-research/issues/30) |
| **5. Multi-Agent State & Exception Bugs** | Parent supervisor treats child `ConductResearch` exception as completion (`open_deep_research`), shared global DB fallback leaks across concurrent users (`SalesforceAIResearch`), or falsy empty `set()` breaks URL dedup (`gpt-researcher`). | `open_deep_research` [#283](https://github.com/langchain-ai/open_deep_research/issues/283) & [#284](https://github.com/langchain-ai/open_deep_research/issues/284), `SalesforceAIResearch` [#8](https://github.com/SalesforceAIResearch/enterprise-deep-research/issues/8), `gpt-researcher` [#2115](https://github.com/assafelovic/gpt-researcher/issues/2115) & [#2180](https://github.com/assafelovic/gpt-researcher/issues/2180) |
| **6. SSRF, Sandbox Escape & Prompt-Injection RCE** | Unvalidated server-side URL crawlers fetch cloud metadata (`169.254.169.254`), or scraped pages inject instructions into `CodeSandbox` / Python `eval()`. | `u14app` [#153](https://github.com/u14app/deep-research/issues/153), `zilliztech` [#278](https://github.com/zilliztech/deep-searcher/issues/278) & [#267](https://github.com/zilliztech/deep-searcher/issues/267), `jina-ai` [#131](https://github.com/jina-ai/node-DeepResearch/issues/131), `SkyworkAI` [#98](https://github.com/SkyworkAI/DeepResearchAgent/issues/98) |
