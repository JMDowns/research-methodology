# Source: Empirical Usage Analysis

**Source**: Token tracker database (`~/.claude-tracker/usage.db`)
**Date**: 2026-02-23
**Scope**: 27,624 API calls across pipeline A and pipeline B

## Overall Token Breakdown by Model

| Model | Input | Output | Cache Read | Cache Write | Cost | Calls |
|-------|-------|--------|-----------|-------------|------|-------|
| claude-opus-4-6 | 334,354 | 1,222,703 | 807,388,151 | 45,759,105 | $893.52 | 10,196 |
| claude-opus-4-5-20251101 | 63,025 | 116,575 | 191,219,548 | 59,937,792 | $698.22 | 8,519 |
| claude-sonnet-4-20250514 | 24,525 | 15,517 | 100,384,189 | 42,906,851 | $287.86 | 5,421 |
| claude-sonnet-4-6 | 1,270 | 43,674 | 37,642,086 | 4,115,043 | $36.64 | 646 |
| claude-haiku-4-5-20251001 | 12,507 | 4,017 | 25,353,477 | 9,404,851 | $21.38 | 1,418 |
| claude-3-haiku-20240307 | 3,225 | 2,910 | 27,104,336 | 6,288,368 | $3.96 | 1,318 |
| **TOTAL** | **439,223** | **2,376,216** | **1,192,463,610** | **170,433,570** | **$1,980.17** | **27,624** |

## Session Length Distribution

| Bucket | Sessions | Total Calls | Avg Turns |
|--------|----------|-------------|-----------|
| 1 call (no reuse) | 7,386 | 7,386 | 1.0 |
| 2-3 calls | 2,518 | 5,564 | 2.2 |
| 4-10 calls | 426 | 2,363 | 5.5 |
| 11-50 calls | 154 | 2,815 | 18.3 |
| 51-100 calls | 19 | 1,359 | 71.5 |
| 100+ calls | 41 | 8,137 | 198.5 |

**Total distinct sessions: 10,544**

## 1-Call Session Analysis (Waste)

7,386 sessions (70%) have only 1 call — cache written but never read.

| Source | Count | Cache Write | Wasted $ (Opus rate) |
|--------|-------|-------------|---------------------|
| Unlabeled (interactive) | 7,384 | 61,134,378 | ~$611 |
| Labeled (pipeline) | 2 | 13,699 | ~$0.14 |

**Key finding**: Nearly all waste comes from interactive sessions, not the pipeline.

By model (1-call sessions only):
- pipeline B opus-4-5: 2,852 sessions, 27.1M cache_write
- pipeline B sonnet-4: 2,692 sessions, 20.4M cache_write
- pipeline A haiku-3: 923 sessions, 5.0M cache_write
- pipeline A sonnet-4: 522 sessions, 5.4M cache_write

## Multi-Call Session Value

| Session Length | Sessions | CR:CW Ratio | Net $ Savings (Opus) |
|---------------|----------|-------------|---------------------|
| 2-3 turns | 2,518 | 2.5:1 | $57.33 |
| 4-10 turns | 426 | 5.2:1 | $136.70 |
| 11-50 turns | 154 | 5.3:1 | $240.79 |
| 50+ turns | 60 | 20.7:1 | $3,286.15 |
| **Total** | **3,158** | | **$3,720.97** |

## Cache Write Per-Call Distribution

| Bucket | Calls | Total Write | Avg Read/Call |
|--------|-------|-------------|---------------|
| 0 (pure cache hit) | 528 | 0 | 28,856 |
| 1-999 | 7,912 | 2,731,487 | 72,696 |
| 1k-5k | 6,189 | 19,089,585 | 48,444 |
| 5k-20k | 11,747 | 104,610,392 | 22,742 |
| 20k-50k | 1,063 | 29,225,279 | 29,789 |
| 50k-100k | 150 | 10,533,723 | 19,145 |
| 100k+ | 35 | 4,243,104 | 15,725 |

The 5k-20k bucket is the largest: 42.5% of calls, 61% of all cache_write.

## Top Sessions by Cache Efficiency

Best sessions (50+ turns) achieve 20-41x cache_read:write ratios with $54.77 average net savings per session.

Worst sessions (1-call) waste $0.05-0.10 each on average, but there are 7,386 of them.
