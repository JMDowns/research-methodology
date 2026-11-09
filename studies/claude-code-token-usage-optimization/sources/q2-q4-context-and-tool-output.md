# Q2 and Q4: main-thread context and tool output (researcher notes, 2026-11-07)

~25 tool calls. Everything below came from a page fetched or a search result seen today.
Claims from search snippets only are marked "(search snippet)". Local numbers come from
`local-usage-2026-11-05-to-07.md`.

## Q2 short answer (main-thread context)

- Anthropic's docs say long context costs usage on every turn, and tell users to `/clear`
  between unrelated tasks. They give no size at which a thread becomes worse at reasoning.
- Third-party research (Chroma, RULER, NoLiMa) shows quality falls as input grows, but
  mostly on retrieval-style tests, on older models, at 32k-113k tokens. None tests a 500k-900k
  Claude Code thread on Opus 5.5. So "worse at reasoning than a fresh 100k thread" is plausible
  but NOT directly shown. Anthropic itself says Opus 4.6 is "markedly better" at context rot
  than earlier models, without numbers for Opus 5.5.
- Anthropic's own best-practices page lists "manage the window aggressively" as old advice
  that is mostly outdated, but keeps `/clear` between tasks because "a focused context gets
  you better answers and costs less". This is a mild support for the owner's prior, and it is
  also a caution against over-claiming a quality win.
- Official handoff pattern exists: progress file + git log + init script, read at the start of a
  fresh session. Practitioners do the same with handoff files instead of `/compact`.
- Confidence: high on what the docs say; medium-low on "quality drops at 500k+ for current
  Opus". The local data cannot answer the quality question either.

## Q4 short answer (tool output)

- Bash: about 30,000 chars inline by default; a failing command gets only about 10,000 chars
  (head and tail). Larger valid output is saved to a file and Claude sees the path plus a
  2,000-char preview. Setting `bashOutputMaxChars` (v2.1.261+, up to 128,000) changes this.
  These caps are per call, so 36,768 Bash calls are not helped by them; the fix is smaller
  commands, not caps.
- Read: one call returns at most 25,000 tokens and refuses a whole file over 256 KB unless
  `allow_large: true`. So a `sed -n` slice is not cheaper than Read with offset/limit; the
  saving is in not reading the same file repeatedly.
- Images: tokens = ceil(w/28) x ceil(h/28). Opus 5.5 / Sonnet 5.5 are on the high-resolution
  tier (long edge up to 2,576 px, up to 4,784 tokens). Standard tier is 1,568 px / 1,568
  tokens. Docs: high-res can use about 3x the visual tokens, and say to downsample if you
  don't need the fidelity. A 1000x1000 image is 1,296 tokens; 1920x1080 is 2,691 on the
  high-res tier. This matches the local 2-7k-token estimate per screenshot.
- Images stay in context every later turn, and Claude Code drops the oldest images in batches
  when limits are hit, which causes a cache rebuild for those messages.
- No source says what resolution is enough to judge UI. That is a testable local question.
- Confidence: high for the numbers (official docs); medium that a ~1000 px screenshot is
  enough for UI checks (inference from token table, unverified for legibility).

## Evidence, Q2

### Official Claude Code guidance
- [Manage costs effectively](https://code.claude.com/docs/en/costs) — accessed 2026-11-07
  - "Clear between tasks: Use /clear to start fresh when switching to unrelated work. Stale
    context wastes tokens on every subsequent message."
  - "Claude Code sends your full conversation with every request ... a one-line question in a
    session that has been open all day still draws usage for the whole conversation."
  - Listed reasons usage climbs: long context, cache misses after a break longer than the cache
    lifetime, scheduled tasks, cross-session messages, goal check-ins, subagents (each sends its
    own requests on top of the main conversation's), compaction ("/compact reads the conversation
    it summarizes, so compacting a large context is itself a large request"; `/clear` costs
    nothing).
  - "Aim to keep CLAUDE.md under 200 lines" and move workflow-specific instructions to skills.
  - `/usage` on Pro/Max shows a breakdown by skill, subagent, plugin, MCP and flags long context
    and cache misses when they pass 10% of usage. Worth running before and after changes (Q6).
  - Sonnet for teammates/agents; "Use Sonnet for teammates"; `model: haiku` for simple subagents.
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) — accessed 2026-11-07
  - `/clear` between unrelated tasks "costs nothing, and it means the next task doesn't keep paying
    for the previous one's history". After two failed corrections, `/clear` and write a better
    prompt.
  - Note: "On the one-hour cache, a session past about 200K tokens that sits idle is compacted
    shortly before the cache expires ... If you don't need the history at all, a fresh session
    still costs less."
  - "Once SPEC.md exists, start a fresh session to build from it, so the build begins with a clean
    context and a written definition of done."
  - Section "old advice": "The context window is your main constraint, manage it aggressively" is
    listed as largely outdated (1M windows, auto-compaction), but "/clear between tasks is still
    worth doing, because a focused context gets you better answers and costs less."
  - Subagents: "every subagent sends its own requests and they count against the same usage as
    your main conversation"; a fresh subagent "has to gather context your conversation already
    had, so it can end up slower". Delegating does not give a better answer; a fresh reviewer does.
- [How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching) — accessed 2026-11-07
  - Compaction invalidates the conversation cache layer. With a warm cache, `/compact` "costs a
    fraction of what the context size suggests"; after a break longer than the TTL the
    summarization request reprocesses all history uncached, so compacting an old resumed session
    "costs the most". Advice: run `/compact` at natural breaks between tasks.
  - TTL: main conversation 1 hour on a subscription within plan usage; 5 minutes for
    subagents, workflows, compaction ("everything else") unless `subagentPromptCacheTtl` is set.
    This matters for the owner's 220-subagent session (feeds Q1/Q3).
  - Sessions are cached per machine and directory; subagent first requests do not read the
    parent's cache; a fork does.
  - Idle compaction: a long conversation on the 1-hour TTL can be compacted when left idle
    (`idleCompaction` setting, v2.1.290+).
- [Explore the context window](https://code.claude.com/docs/en/context-window) — accessed 2026-11-07
  - Survives compaction: root CLAUDE.md, auto memory, up to 5 recently read files (files over
    5,000 tokens come back as path only), invoked skill bodies (5,000/25,000 token caps).
    Instructions given only in conversation are lost, and nested CLAUDE.md / path-scoped rules are
    summarized away. Background commands and subagents keep running.
  - `/autocompact 500k` sets how full the window gets before auto-compaction; `/compact focus on X`
    steers the summary; `/rewind` > "Summarize from here" compacts part of the thread.
- [How Claude remembers your project](https://code.claude.com/docs/en/memory) — accessed 2026-11-07
  - CLAUDE.md: "target under 200 lines per CLAUDE.md file. Longer files consume more context and
    reduce adherence." Auto memory: first 200 lines or 25KB of MEMORY.md loaded each session; the
    rest is not loaded.
  - Owner's `~/.claude/CLAUDE.md` is ~60 lines but includes long sections; MEMORY.md has ~22 index
    lines, so both are within limits (my line count of the pasted index, not measured).

### Anthropic engineering
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — accessed 2026-11-07
  - Recall degrades as context grows; context is a finite "attention budget" with "diminishing
    marginal returns". Compaction keeps decisions, unresolved bugs, implementation details and
    drops redundant tool output. Tool result clearing is "one of the safest lightest touch forms of
    compaction". Structured note-taking outside the window; sub-agents with clean windows return
    "often 1,000-2,000 tokens" to the lead.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — accessed 2026-11-07
  - Pattern across many context windows: an initializer session creates `init.sh`, a progress log
    and a git commit; each later session reads git log + progress files, picks one feature, runs a
    health check, and ends with a commit and progress update. JSON feature list as a scope guard.
    This is the closest official model for the owner's "fresh orchestrator from a handoff file".
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) — accessed 2026-11-07
  - MRCR v2 8-needle at 1M: Opus 4.6 76% vs Sonnet 4.5 18.5%. Says context rot is "a common
    complaint" and Opus 4.6 "performs markedly better than its predecessors", no numbers. Vendor
    claim; retrieval benchmark, not reasoning in an agent loop. Nothing found for Opus 5.5.

### Independent long-context evidence
- [Context Rot (Chroma)](https://www.trychroma.com/research/context-rot) — accessed 2026-11-07
  - 18 LLMs incl. Claude Opus 4 / Sonnet 4: "Across all experiments, model performance
    consistently degrades with increasing input length." On LongMemEval, focused prompts (~300
    tokens) beat full prompts (~113k) with Claude showing the largest gap, which the authors say
    is largely abstentions. Claude had the lowest hallucination rate with distractors. Tasks are
    simple (retrieval, repeated words), models are 2025 generation.
- [RULER (arXiv 2404.06654)](https://arxiv.org/abs/2404.06654) — accessed 2026-11-07
  - 17 models, 13 tasks; all claim 32k+, "only half of them can maintain satisfactory performance
    at the length of 32K". Old models.
- [NoLiMa (arXiv 2502.05167)](https://arxiv.org/abs/2502.05167) — accessed 2026-11-07
  - 13 models claiming 128k+: "At 32K ... 11 models drop below 50% of their strong short-length
    baselines"; reasoning/CoT models also degrade. Old models, no Claude 5.x.
- Fiction.liveBench: the fiction.live page returned no data to WebFetch, and the search found no
  Claude 5.x numbers. Not verified.
- Same-domain note: Chroma, RULER and NoLiMa agree with Anthropic's own "context rot" wording, so
  the direction (worse with length) is cross-checked. The size of the effect for Opus 5.5 at 500k+
  is not.

### Practitioners (weak evidence)
- (search snippet) Several blogs advise a written handoff file + fresh session over `/compact` for
  long sessions, because the compact summary is opaque and lossy: e.g.
  [claude-auto-handoff wiki](https://github.com/alexknowshtml/claude-auto-handoff/wiki),
  [MindStudio on context rot and handoffs](https://www.mindstudio.ai/blog/context-rot-ai-agents-session-handoff-fix-2/),
  [mejba.me handoff skill](https://www.mejba.me/blog/handoff-skill-claude-code-multi-session)
  — accessed 2026-11-07 (search results only, pages not fetched).
- Claims of a "~120k smart zone" come from an unnamed source in a blog (unverified).

## Evidence, Q4

- [Tools reference, Bash output limits and Read](https://code.claude.com/docs/en/tools-reference) — accessed 2026-11-07
  - Bash: valid result inline up to ~30,000 chars by default; beyond that the file path plus a
    preview of up to the first 2,000 chars, Claude reads/searches the file for the rest. Failure:
    inline up to ~10,000 chars, head-and-tail excerpt, no path. `BASH_MAX_OUTPUT_LENGTH` default
    30,000, ceiling 150,000. `bashOutputMaxChars` up to 128,000, v2.1.261+, makes
    `BASH_MAX_OUTPUT_LENGTH` ignored.
  - Read: one call returns at most 25,000 tokens (`CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`),
    refuses a whole file over 256 KB; `allow_large: true` (v2.1.296+) reads more. Images (PNG,
    JPEG, GIF, WebP) come back as visual content; Claude Code "resizes and recompresses large
    images ... so Claude may see a downscaled version".
  - Glob results capped at 100 files, with a truncation flag. Grep has `count` and `head_limit`.
  - Cross-check on a second domain (third party, search snippet only): [claudeissues.com #19901](https://claudeissues.com/issue/19901-docs-missing-documentation-on-bash-tool-output-limits-30k-characters-and-truncat)
    and [claudelog](https://claudelog.com/faqs/what-is-bash-output-max-chars-in-claude-code/) also
    give 30,000 chars default; claudelog says clamp 4,000-128,000.
- [Vision docs](https://platform.claude.com/docs/en/build-with-claude/vision) — accessed 2026-11-07
  - Cost = ceil(w/28) x ceil(h/28). Tiers: Claude 4.7 and later: max long edge 2,576 px, 4,784
    tokens; others 1,568 px / 1,568 tokens. Examples (standard / high-res tokens): 200x200 = 64 /
    64; 1000x1000 = 1,296 / 1,296; 1092x1092 = 1,521 / 1,521; 1920x1080 = 1,560 / 2,691;
    2000x1500 = 1,564 / 3,888; 3840x2160 = 1,560 / 4,784.
  - "High-resolution images can use up to roughly three times more visual tokens ... If you don't
    need the additional fidelity ... downsample images before sending." Images under ~200 px are
    unreliable. Over 20 images in a request triggers a stricter limit (3,000 px per side, or keep
    to 20 images). Resizing may make text less legible.
  - Only one domain (Anthropic). Local data (2.1k median, 6.7k p90 per screenshot) agrees.
- [Manage costs: offload processing to hooks](https://code.claude.com/docs/en/costs) — accessed 2026-11-07
  - A PreToolUse hook can rewrite test commands to `| grep -A 5 -E '(FAIL|ERROR|error:)' | head -100`;
    "reducing context from tens of thousands of tokens to hundreds". Code intelligence (LSP) plugins
    replace grep + multi-file reads. Delegate verbose operations (tests, logs, docs) to a subagent
    so only a summary returns.
- Prompt-caching page: accumulating many images triggers batch removal of oldest images and a
  partial cache rebuild (see Q2 link).

## Implications for the owner's workflow (inference, not sourced)
- 322 background-agent notices each at ~0.5M context: docs support the cost side (full context is
  re-read every turn, 1h TTL on main thread, subagents 5 min). Cheapest lever: fresh orchestrator
  from a handoff file when it passes ~200-300k, or `/autocompact` at a lower value.
- A cold-cache `/compact` on a 900k thread is the most expensive form of compaction per docs;
  compact while warm or start fresh instead of resuming a month-old session.
- Cap screenshots at about 1000-1300 px long edge unless detail is needed; do not re-read the same
  PNG. Prefer cropped regions.
- Replace repeated `sed -n` slices with one Read of the needed range, or a script that prints a
  summary. The 30k-char Bash cap means one big dump is up to ~7-8k tokens.

## Open questions
1. Is there any measurement of Opus 5.5 / Sonnet 5.5 quality at 500k-900k in an agent loop?
   Not found. Could be tested locally by comparing owner corrections and redo agents against
   context size (Q6).
2. What does a plan-usage window count for cache reads? Belongs to Q1.
3. What screenshot size is legible enough for the owner's UI checks? Needs a small local test.
4. Does `/autocompact N` lower the threshold below the default, and what is the default for Opus
   5.5? Docs link to model-config "Default auto-compact thresholds", not fetched.
5. Fiction.liveBench / newer long-context numbers for Claude 5.x: not retrieved.
