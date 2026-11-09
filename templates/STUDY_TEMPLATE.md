---
title: "[Study Title]"
date: YYYY-MM-DD
status: in_progress        # complete | in_progress
confidence: medium         # high | medium | low
confidence_reason: "[brief justification]"
completeness: 0            # integer 0-100
completeness_reason: "[what's covered vs missing]"
category: methodology      # methodology | (add new as needed)
tier: 2                    # 1 | 2 | 3 (research complexity)
objective: "[What this study answers]"
summary: "[One line: what this research produced / concluded]"
why: "[Why we're doing it — which pipeline decision/feature it informs]"
blockers:
  - "[What's blocking completion, or what this blocks — omit / [] if none]"
source_count: 0
known_gaps:
  - "[What's missing or uncertain]"
next_steps:
  - "[Actionable continuation step]"
quality_checklist:
  sourced_claims: false
  cross_referenced: false
  flagged_contradictions: false
  verified_surprising: false
  noted_confidence: false
  listed_gaps: false
  targeted_prompts: false
  within_budget: false
---

# [Study Title]

## Question / Objective

[What is this study trying to answer or accomplish?]

## Known Gaps

- [What's missing or uncertain]

## Findings

[Synthesized results go here — only from fetched sources]

## Quality Checklist

- [ ] All factual claims sourced from fetched pages (no training data fill)
- [ ] Cross-referenced claims across 2+ source domains where possible
- [ ] Flagged any contradictions between sources
- [ ] Ran verification step on surprising/unusual claims
- [ ] Noted confidence level for each major finding
- [ ] Listed known gaps explicitly
- [ ] Used targeted WebFetch prompts (not "tell me everything")
- [ ] Stayed within budget limits for the complexity tier

## Sources

[All citations collected here]
- [Description](URL) — accessed YYYY-MM-DD
