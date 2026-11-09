# AI Instructions: Web Search Methodology

These instructions tell Claude Code how to perform web research efficiently. Reference this file at the start of any research session.

## Decision Flowchart

```
User asks a research question
    │
    ├── Can I answer confidently from training data?
    │   ├── YES → Answer directly, cite training knowledge, flag uncertainty
    │   └── NO → Continue to web search
    │
    ├── Is this a simple factual lookup? (1-2 facts needed)
    │   ├── YES → TIER 1: Single search + snippets
    │   └── NO → Continue
    │
    ├── Is this a moderate question? (single topic, few sources needed)
    │   ├── YES → TIER 2: Search + selective fetch
    │   └── NO → Continue
    │
    └── This is a complex research task
        └── TIER 3: Parallel subagents + deep research
```

## Tier 1: Simple Factual Lookup

```
1. WebSearch("concise factual query")
2. Read snippets from results
3. If snippets answer the question → done
4. If not → upgrade to Tier 2
```

**Budget**: 1-2 WebSearch, 0-1 WebFetch
**Example**: "What year was Python 3.10 released?"

## Tier 2: Search + Selective Fetch

```
1. WebSearch("broad topic query")
2. Read snippets, identify 2-3 most promising URLs
3. WebFetch(best_url, prompt="Extract [specific data needed]. Format as [table/list/etc].")
4. Assess: Do I have what I need?
   - YES → Go to step 6
   - NO → Identify gap, do ONE more targeted WebSearch
5. WebFetch(new_best_url, prompt="Extract [missing data]")
6. VERIFY: Fetch 1-2 more pages to cross-check key claims (prerequisites, counts, names)
   - Use a DIFFERENT source than step 3 for verification
7. Synthesize
```

**Budget**: 1-3 WebSearch, 3-5 WebFetch (do NOT stop at 1-2 fetches — our A/B test showed that stopping too early misses critical details, dropping quality from ~93% to ~86%)

**Critical Rules** (from R3 A/B testing — violating these caused 7.1% quality drop):
1. **NEVER state something as fact unless it came from a fetched source** — do not fill gaps from training data. If you can't verify it, mark it "(unverified)" or fetch another source.
2. **Verify counts and prerequisites explicitly** — when a source says "requires X vocations", fetch and confirm the exact list. Don't assume from memory.
3. **Cross-reference across 2+ source domains** — different wikis/sites contain different errors. Using only one source propagates its mistakes.

**Example**: "What are the configuration options for pytest's conftest.py?"

## Tier 3: Deep Research with Subagents

```
1. Decompose the question into 2-5 sub-questions
2. For each sub-question, launch a Task subagent:
   - subagent_type: "general-purpose"
   - run_in_background: true
   - prompt: Specific sub-question + Tier 2 instructions
3. Wait for all subagents to complete
4. Synthesize results in main context
5. Identify gaps across all subagent results
6. If needed, launch 1-2 more targeted subagents
```

**Budget**: 3-5 subagents, each with Tier 2 budget (3-9 tool calls each)
**Example**: "Comprehensive overview of Dragon Quest VII's plot, characters, and gameplay systems"

## WebFetch Prompt Templates

### For extracting lists/tables:
```
"Extract all [items] from this page. For each item, include: [field1], [field2], [field3]. Format as a markdown table. Ignore navigation, ads, and unrelated content."
```

### For extracting procedures/steps:
```
"Extract the step-by-step process for [task]. Include any code examples or commands. Number each step."
```

### For extracting factual claims:
```
"Extract all factual claims about [topic] from this page. For each claim, note the specific detail and any caveats mentioned."
```

### For extracting structured data:
```
"Extract [data type] as structured data. Use this format for each entry:
- Name: ...
- Property 1: ...
- Property 2: ...
Ignore [irrelevant sections]."
```

## Citation Format

Every factual claim from web sources must include:
```
[Brief description](URL) — accessed YYYY-MM-DD
```

## Verification Step (Learned from A/B Testing)

Snippet-only searches can produce "plausible but wrong" facts (e.g., confusing PS1 localization names with 3DS vocations). Before finalizing, do a verification pass:

1. **Flag surprising or unusual claims** — anything that seems unlikely, uses unfamiliar terminology, or contradicts other findings
2. **Verify flagged claims with a targeted WebFetch** — fetch the most authoritative source and ask specifically about the claim
3. **If WebFetch is unavailable**, do a targeted confirmation search: `"exact claim" site:authoritative-source.com`
4. **Mark unverified claims** with a confidence qualifier: "(unverified)" or "(from snippets only)"

This step adds 1-2 tool calls but prevents the fabrication errors observed in our A/B test (34% efficiency gain was partially offset by 3 factual errors that would have been caught with verification).

## Quality Checklist

Before finalizing research:
- [ ] Cross-referenced claims across 2+ sources where possible
- [ ] Flagged any contradictions between sources
- [ ] **Ran verification step on surprising/unusual claims**
- [ ] Noted confidence level (High/Medium/Low) for each major finding
- [ ] Listed known gaps explicitly
- [ ] Preferred primary sources over secondary summaries
- [ ] Used targeted WebFetch prompts (not "tell me everything")
- [ ] Stayed within budget limits for the complexity tier

## Anti-Patterns to Avoid

1. **Fetching every search result** — evaluate snippets first
2. **Vague WebFetch prompts** — "summarize this page" wastes Haiku's extraction capacity
3. **Not using subagents for complex research** — main context fills up fast
4. **Over-searching simple questions** — if snippets answer it, stop
5. **Ignoring cached results** — WebFetch caches 15 min, don't re-fetch
6. **No reasoning between searches** — pause to assess what you've learned
7. **Not decomposing complex questions** — one giant search rarely works
8. **Trusting snippets for specifics** — snippets are good for discovery, bad for precision. Verify specific claims with WebFetch.
