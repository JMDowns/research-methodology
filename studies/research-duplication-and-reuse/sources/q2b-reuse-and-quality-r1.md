# Q2b strand B: reuse of earlier notes and what happens to quality (round 1)

Gathered 2026-11-08. [F] = read on a fetched page. [S] = search snippet only. "(unverified)" = not confirmed.
Several sites blocked the fetch tool (PubMed, PMC, Springer, Nature: cookie or captcha walls), so some numbers are snippet-only.

## Headline findings

1. Citing without checking the source is common and measurable. A meta-analysis of 28 studies found 25.4% of citations had a quotation error (95% CI 19.5-32.4), and 11.9% were major (the source contradicts, fails to support, or is irrelevant to the claim) [F]. Single studies ranged from 6.7% to 83%.
2. Copying propagates errors. Simkin and Roychowdhury estimate only about 20% of citers read the original, because identical misprints spread through reference lists [F abstract]. Jergas and Baethge repeat this as "70-90% copied" for physics, with no medical estimate [F].
3. Extraction by one person is error-prone even with a check. Single extraction made more errors than double extraction (14.5% vs 17.7% in one trial; 21.7% relative difference, P=0.019) [S]. A methodological review found extraction error rates "up to 50%" [S]. A later trial found no big difference between double extraction and single extraction plus verification (15% vs 16%) [S]. So a second check on reused data helps, but is not perfect.
4. AI agents that reuse their own memory without quality filtering get worse. In a memory study, adding every past record ("add-all") lowered accuracy versus a small fixed memory on 2 of 3 tasks (EHRAgent 13.04 vs 16.89; AgentDriver 32.48 vs 40.53), while adding only checked-correct records raised it (38.86; 50.94) [F]. Errors in stored records spread to later tasks.
5. Citations can look right and still not be faithful. Deep-research tools had citation accuracy of 31-79% and unsupported-statement rates of 12.5-97.5% in one audit [F]. Up to 57% of RAG citations were "post-rationalized" (the model cited a document it did not actually rely on) [F, abstract only]. Web sources also decay: about 1 in 5 scholarly articles has reference rot, and about 50% of Supreme Court-opinion links no longer showed the cited material [F]. So cached notes need a fetch date and a re-check rule.

## 1. Citation and quotation errors from copying secondary sources

### Jergas and Baethge 2015 (PeerJ) [F, PMC copy]
- 28 studies in the main analysis. The text says 7,321 references; Table 2 says 7,171. The paper does not reconcile these.
- Pooled total quotation error rate: 25.4% (95% CI 19.5-32.4), I-squared 97%. Study range 6.7% to 83.0%, median 22.5%.
- Major errors: 11.9% (95% CI 8.4-16.6). Minor errors (including indirect references): 11.5% (8.3-15.7).
- Major = the cited reference contradicts, fails to support, or is irrelevant to the author's claim. Formal errors such as wrong page numbers were excluded.
- Indirect (secondary) references were under one sixth of all problems. Without them: minor 8.5%, total 21.5% (17.4-26.2).
- They cite Simkin and Roychowdhury (2005): roughly 70-90% of physics citations copied from other papers' reference lists, originals unread. Authors say it is plausible in medicine but give no estimate.
- A 2025 update by the same authors found no improvement over time (slope -0.002, 95% CI -0.03 to 0.02, p=0.85) [S, from a search summary; not opened].

### Simkin and Roychowdhury 2003 "Read before you cite!" [F abstract only]
- Abstract: "Our estimate is only about 20% of citers read the original." Method: stochastic model of the citation process; misprints in citations follow a Zipf law.
- A search summary said ~4,300 citations, ~196 with misprints, 45 distinct, top misprint repeated 78 times [S]. The PDF was compressed and could not be read, so those counts are (unverified).

### Lesson for this repo
Copying a claim from a note without re-reading the page is the same behaviour these studies measure. The risk is highest for the claims that get repeated most.

## 2. Living reviews and review updates: what is re-checked

Thin evidence. I did not reach a primary page that states a re-verification rule. What I have:
- Cochrane training text: reviews should be assessed periodically; update if the question still matters and new data or methods could change findings [S].
- A COVID-era living-review guide advises documenting and justifying protocol changes before each update [S].
- Extraction quality evidence (used by reviews for new data):
  - Buscemi 2006 randomised pilot: single extraction had more errors than double (21.7% relative difference, P=0.019; 14.5% double vs 17.7% single-with-verification) [S].
  - Li 2018: double extraction vs single plus verification, 15% vs 16%, no substantial difference [S].
  - Tang crossover trial: double extraction cut errors but the rate "remained high" [S].
  - Mathes, Klassen, Pieper 2017 methodological review: error rates up to 50%; errors often changed effect estimates; evidence base only six studies, "weak" [S].
  - A semi-automation study (SWAR 28) notes a checker can change a correct extraction into a wrong one [S].
- A 2024 preprint used two LLMs as two "reviewers" with cross-critique for living-review extraction; provisional [S].
- Gap: Cochrane Handbook / MECIR text on re-checking old extractions was not found. Next step: fetch the Handbook living-review chapter directly.

## 3. LLM and agent side

### Memory quality (Xiong et al., arXiv 2505.16067) [F]
- Tasks: EHRAgent (2,392 tasks), AgentDriver (2,000), CIC-IoT (1,200); mostly GPT-4o-mini.
- Final accuracy (memory size):

| Strategy | EHRAgent | AgentDriver | CIC-IoT |
|---|---|---|---|
| Fixed small memory | 16.89 (100) | 40.53 (180) | 60.25 (100) |
| Add-all | 13.04 (2411) | 32.48 (2125) | 60.00 (1300) |
| Coarse judge (LLM) | 31.35 | 37.03 | 60.67 |
| Strict (ground-truth check) | 38.86 (1012) | 50.94 (1178) | 63.33 (860) |

- Errors in retrieved records influence the current task and, once stored, propagate to later tasks ("experience-following"). Add-all and coarse judging widened the gap over time; strict addition closed it.
- Selective add plus delete: average absolute gain of 10% versus naive growth (abstract). Deletion with a weak (LLM) judge mostly did not help.
- Table 1 and Table 2 differ slightly for EHRAgent strict (38.86 vs 38.89).
- Meaning: reusing everything is worse than reusing only verified items; the quality of the filter matters.

### Other memory papers [S]
- "More Memory, Worse Agents" (arXiv 2610.27406): errors regenerated through abstraction and re-abstraction cycles. AMA-Bench: many memory designs underperform plain long context because compression and retrieval errors compound. Not opened.

### Citation audit of deep-research tools (DeepTRACE, arXiv 2509.04499) [F]
- 303 queries; 9 systems per design (10 configurations in tables); LLM judge, human agreement Pearson r 0.62 on factual support (moderate).
- Citation accuracy: GPT-5 DR 79.1%, YouChat DR 72.3%, PPLX DR 58.0%, Gemini DR 50.3%, GPT-5 web search 31.4%. Unsupported statements: GPT-5 DR 12.5%, Gemini DR 53.6%, YouChat DR 74.6%, Copilot 90.2%, PPLX DR 97.5%.
- The paper has internal inconsistencies (Gemini 40.3 vs 50.3; judge model named GPT-5 in one place, GPT-4 in another). Treat figures as approximate.

### Post-rationalized citations (Wallat et al., arXiv 2412.18004) [F, abstract only]
- Correct citation is not the same as faithful citation. "Up to 57 percent of the citations" lacked faithfulness. Model and conditions not stated on the abstract page; a search summary said Command-R+ in adversarial cases [S]. Treat 57% as an upper bound.

### Fabricated references (Walters and Wilder 2023, Sci Rep) [S, page blocked]
- ChatGPT-written reviews, 636 citations: 55% of GPT-3.5 citations fabricated, 18% for GPT-4; of the real ones, 43% (GPT-3.5) and 24% (GPT-4) had substantive errors.

### Cost savings from caching [S]
- Regmi and Pun, GPT Semantic Cache (arXiv 2411.05276): up to 68.8% fewer API calls, hit rates 61.6-68.8%, positive-hit accuracy above 97% (their data: customer-style queries, ~8,000 Q&A pairs, 0.8 similarity threshold per a secondary summary). This is call reduction, not dollars, one dataset, no replication found. Weak analogy: this repo's reuse is of research notes, not repeated chat queries.
- No study found that measures token savings from reusing earlier research notes in a research agent.

## 4. Knowledge-management practice

- Evergreen notes / Zettelkasten [S]: only practitioner writing found (Matuschak notes, Fabric guide, CASRAI). Claims: concept-oriented atomic notes, revised over time; value from link density. No measured outcomes on reuse quality or staleness. Evidence level: none.
- Wikipedia content forks [F, en.wikipedia.org]: a second page on the same subject and same page type is a "redundant content fork", unacceptable. Reasons given: redundant or conflicting articles, copies drift apart, preference for a "single source of truth". Remedy: merge the newer article into the main one. No sync procedure is given for acceptable forks, only "should not contradict each other". Policy text, not a measurement.
- Reference rot as a staleness measure:
  - Klein et al. 2014 (PLoS ONE) [F]: over 1 million web references in 3.5 million articles (arXiv, Elsevier, PMC; 1997-2012). About 1 in 5 articles suffers reference rot; about 7 in 10 among articles that have web references. Link rot rises with age.
  - Zittrain et al. 2014 (Harvard Law Review Forum) [F]: law journals: 65.8-73.2% of spot-checked links lost the cited material (link rot 33-40%; HLR 5,911 links, HRJ 2,358, JOLT 5,428). Supreme Court opinions, 555 links: 36.4% link rot, 49.9% reference rot (the paper's own counts would imply 50.1%).
  - Meaning: a source note taken from a web page may not match the page later. Record the fetch date and keep the extracted text.

## 5. Safeguards and the evidence behind them

| Safeguard | Evidence found | Strength |
|---|---|---|
| Check against ground truth before a note is reused (strict filter) | Memory study: strict add +10 to +22 pts vs fixed on 2 of 3 tasks; add-all lowered 2 of 3 [F] | Medium (3 tasks, one backbone) |
| Do not trust an LLM judge as the only filter | Coarse LLM-judge addition did much worse than strict on AgentDriver (37.03 vs 50.94); DeepTRACE judge agreement r 0.62 [F] | Medium |
| Second reader on extracted data | Double vs single extraction: fewer errors [S]; but single plus verification about as good (15% vs 16%) [S]; checker can introduce errors [S] | Medium, mixed |
| Re-read the primary source for claims that get repeated | Copying studies show errors spread through unread reference lists [F]; quotation error rate 25.4% [F] | Indirect (observational) |
| Record provenance: page, fetch date, text extracted | Reference rot 20-70% depending on corpus [F]; citation-faithfulness gap up to 57% [F abstract] | Indirect |
| Expiry or age check on notes | Link rot rises with age [F]; no study of expiry intervals for notes | Weak |
| Single canonical page, merge duplicates | Wikipedia policy [F]; no measurement | Policy only |

Not found: any study testing "re-verify headline claims" as an intervention in a note library, or any measured expiry interval.

## Gaps for round 2
- Primary text for Cochrane/MECIR/living-review re-check rules; Elliott 2017 LSR series full text.
- Mathes 2017 full table of error rates; Buscemi 2006 and Li 2018 abstracts (PubMed blocked).
- Walters and Wilder abstract (Nature blocked), Simkin counts, "More Memory, Worse Agents" and AMA-Bench contents.
- Any measurement of cost savings from reusing retrieved web pages in agent research.

## Sources
- [Jergas and Baethge 2015, Quotation accuracy in medical journal articles (PMC copy)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627914) — accessed 2026-11-08
- [Jergas and Baethge 2015, PeerJ page (search snippet only; fetch 403)](https://peerj.com/articles/1364) — accessed 2026-11-08
- [Simkin and Roychowdhury, Read before you cite! (arXiv abstract)](https://arxiv.org/abs/cond-mat/0212043) — accessed 2026-11-08
- [Simkin and Roychowdhury, Complex Systems 14 (snippet only)](https://www.complex-systems.com/abstracts/v14_i03_a05/) — accessed 2026-11-08
- [Mathes, Klassen, Pieper 2017, Frequency of data extraction errors (snippet only)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5704562) — accessed 2026-11-08
- [Buscemi 2006, single vs double data extraction (snippet only)](https://www.pubmed.ncbi.nlm.nih.gov/16765272/) — accessed 2026-11-08
- [Elliott et al., Living systematic reviews 1 and 2 (search results only)](https://read.qxmd.com/read/28912003/living-systematic-reviews-2-combining-human-and-machine-effort) — accessed 2026-11-08
- [Xiong et al., How Memory Management Impacts LLM Agents (arXiv 2505.16067)](https://arxiv.org/html/2505.16067v1) — accessed 2026-11-08
- [DeepTRACE: Auditing Deep Research AI Systems (arXiv 2509.04499)](https://arxiv.org/html/2509.04499v1) — accessed 2026-11-08
- [Wallat et al., Correctness is not Faithfulness in RAG Attributions (arXiv abstract)](https://arxiv.org/abs/2412.18004) — accessed 2026-11-08
- [Walters and Wilder 2023, fabricated citations by ChatGPT (search result only)](https://doaj.org/article/fc88ea07ec994a7c8a144f8516c48cbf) — accessed 2026-11-08
- [Regmi and Pun, GPT Semantic Cache (search result only)](https://arxiv.org/abs/2411.05276v3) — accessed 2026-11-08
- [Wikipedia: Content forks](https://en.wikipedia.org/wiki/Wikipedia:Content_forks) — accessed 2026-11-08 (wiki policy page)
- [Klein et al. 2014, One in Five Articles Suffers from Reference Rot (PLoS ONE)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253) — accessed 2026-11-08
- [Zittrain, Albert, Lessig 2014, Perma (Harvard Law Review Forum)](https://harvardlawreview.org/2014/03/perma-scoping-and-addressing-the-problem-of-link-and-reference-rot-in-legal-citations/) — accessed 2026-11-08
- [Matuschak, Evergreen notes should be concept-oriented (practitioner notes, snippet only)](https://notes.andymatuschak.org/Evergreen_notes_should_be_concept-oriented) — accessed 2026-11-08
