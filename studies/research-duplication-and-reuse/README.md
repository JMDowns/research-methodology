---
title: "Research duplication and reuse"
category: methodology
status: complete
---

# Research duplication and reuse

This is a short summary of a study that measured repeated work across a large private set of studies. The corpus-level data stays private. `sources/` holds the literature notes on research waste and reuse.

- Whole-study duplication was rare: 0 duplicates among the 80 most similar study and proposal pairs.
- Repetition was in sources: 23.0% of study-URL pairs in source notes (4,917 of 21,370) were on URLs another study also used.
- Telling a researcher agent to reuse earlier notes saved only 3% of tokens, and it copied an earlier error into a headline. So research briefs should not include a "reuse repo notes" step.
- `scripts/find_prior.py` found the other half of a study and proposal pair in the top 5 for 70 of 78 queries. It found only 21 of 52 hand-listed prior studies across domains, so a person or agent should still search by hand.
