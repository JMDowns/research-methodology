# Strand B: reuse of earlier notes and its effect on accuracy (Q2, Q3, Q5)

Gathered 2026-11-08. Facts come from fetched pages unless marked [S] (search snippet only). "(unverified)" means not confirmed on a fetched page.

## Headline findings

1. Citations misstate their source often. Across 28 studies, 25.4% of citations had an error (95% CI 19.5-32.4) and 11.9% had a major error (the source contradicts, fails to support, or is irrelevant to the claim). Major rate is unaffected by indirect references. (Jergas and Baethge 2015.)
2. Copying without reading is common. Simkin and Roychowdhury estimate about 20% of citers read the original. The 2015 review quotes a 70-90% "copied from other papers' reference lists" estimate. Both rest on misprint-propagation modelling, not direct observation.
3. Cached or remembered notes cut cost but spread errors. Caching with no invalidation saved 5-28% of tokens [S, preprint]. After the source changed, stale entries failed silently. Row-level invalidation recovered 29-33% of baseline token cost on 4 of 7 models. Naive table-level invalidation gave 0% first-try success after drift on 5 of 7 models.
4. AI citations are weak evidence of use. Deep-research tools had 12.5% to 97.5% unsupported statements and 50-79% citation accuracy (DeepTRACE). Up to 57% of RAG citations lacked faithfulness (post-rationalized: the model did not really rely on the cited document).
5. Review practice checks reuse by re-examining, not trusting. Cochrane update rules require reconsidering previously included studies and collecting more information if needed. Single extraction plus a second-person check had error rates close to double extraction (14.5% vs 17.7% in one trial [S]). Wikipedia's rule is one source of truth: merge duplicates, check for an existing page first.

## 1. Citation and quotation errors from secondary copying

**Jergas and Baethge 2015 (PeerJ, systematic review and meta-analysis)**, fetched at PMC:
- Pooled major errors 11.9% (95% CI 8.4-16.6; 27 studies).
- Pooled minor errors 11.5% (8.3-15.7); this includes indirect (secondary) references.
- Pooled total errors 25.4% (19.5-32.4; 28 studies). Heterogeneity is very high (I2 95-97%).
- Major error means the cited work "contradicted, failed to substantiate, or was irrelevant to" the claim (Luo 2013 definition quoted in the paper).
- Indirect references were under one sixth of all problems. Without them, minor errors are 8.5% and total errors 21.5% (17.4-26.2).
- The review did not measure copying in medicine. It cites Simkin and Roychowdhury for the copying estimate.
- A search snippet says a 2025 follow-up (46 studies, about 32,000 quotations) found no improvement over time (slope -0.002, p=0.85) [S].

**Simkin and Roychowdhury 2003, "Read before you cite!" (Complex Systems 14)**, abstract fetched from arXiv:
- Estimate: "only about 20% of citers read the original", from a stochastic model fitted to misprint distributions in citations.
- Snippet details [S]: in one heavily cited paper, 196 misprinted citations but only 45 distinct, the most common appearing 78 times. They admit the sample is not representative and that the method assumes non-copiers are readers.
- Caveat for us: this is a model-based estimate from physics citations. It shows the mechanism (a wrong detail copied forward repeats), not a rate for our repo.

Meaning for the repo: a note that repeats a number from an earlier note inherits that note's error, and the repeated string looks like independent confirmation.

## 2. Living systematic reviews and updates

What I could confirm:
- Elliott et al. 2017 (J Clin Epidemiol 91:23-30) is the standard LSR introduction. I only reached its citation details through search results, not the full text. Extraction-specific rules from it are (unverified).
- Cochrane/MECIR update standard U8, from a search snippet [S]: reconsider studies previously marked included, awaiting classification, ongoing or excluded, and collect more information from them if necessary. Check that exclusion reasons still match current criteria. Assess risk of bias for all new and previously included studies. Updated extraction forms must be piloted before use. Reports of the same study must be linked.
- Cochrane no longer demands routine two-year updates; update when new evidence or methods could change findings [S].
- The Cochrane update PDF could not be read by the fetch tool (binary), so none of this is page-confirmed.

Extraction error evidence (search snippets only [S]; the PubMed page was blocked):
- Buscemi 2006: single extraction had more errors than double extraction (relative difference 21.7%, P=.019). A later protocol quotes 14.5% (double) vs 17.7% (single plus verification).
- Li 2018 as described in the same protocol: 15% vs 16%, no substantial difference between double extraction and single extraction plus verification.
- Mathes 2017 methodological review: extraction errors up to 50% in some studies, moderate effect of method.
Reading: a second look at extracted data catches a meaningful share of errors, and a verifier is almost as good as a second full extractor. Not confirmed on the primary pages.

## 3. LLM and agent side

**DeepTRACE (Microsoft/Salesforce, arXiv 2509.04499, snapshot 2025-08-27)**, fetched:
| System | Unsupported statements | Citation accuracy | Citation thoroughness |
|---|---|---|---|
| GPT-5 deep research | 12.5% | 79.1% | 87.5% |
| YouChat DR | 74.6% | 72.3% | 83.5% |
| Perplexity DR | 97.5% | 58.0% | 9.1% |
| Gemini DR | 53.6% | 50.3% (text says 40.3%) | 27.1% |
| GPT-5 web search | 58.9% | 31.4% | 17.9% |
Judge agreement with humans was moderate: r=0.62 for factual support, r=0.72 for answer confidence (100 items each). The paper is inconsistent on the judge model (GPT-5 vs GPT-4). Treat the numbers as approximate.

**Wallat et al., "Correctness is not Faithfulness in RAG Attributions" (arXiv 2412.18004)**, abstract fetched: "up to 57 percent of the citations" lack faithfulness, i.e. post-rationalization. The abstract does not give the models or setup. A snippet says Command-R+ on adversarial cases [S, unverified]. Meaning: a citation that supports a claim does not prove the claim came from that page. For us, a note that cites a URL does not prove the page was read.

**Xiong et al. 2025, "How Memory Management Impacts LLM Agents" (arXiv 2505.16067)**, abstract fetched: stored mistakes "compound and degrade future performance"; some seemingly correct past runs "provide limited or even misleading value". No numbers in the abstract. They report that evaluator feedback helps [S].

**Invalidation contracts for cross-episode agent memory (arXiv 2609.00243)**, abstract page fetched; one preprint, not peer reviewed:
- About 9,400 episodes, 7 models, 2 domains.
- Cached fixes fail silently after the underlying data changes; re-deriving every time gives the saving back.
- Row-level invalidation: +0 to +66.7 points first-try compliance, and recovers 29-33% of baseline token cost on 4 of 7 models.
- Table-level invalidation drops post-drift first-try rate to 0% on 5 of 7 models.
- The "5-28% token savings" for naive memory comes from a search snippet only [S].

**Compliance Trap (arXiv 2607.10608)**: abstract says agents adopt conflicting memory at the first exposure even when it is task-wrong, repeated exposure amplifies it, and recovery is weak. Numbers (63-72% adoption, 17-31% success after compliance, -20.8 points for one model) came from a third-party overview on the page, not the abstract. (unverified)

**Fabricated references (Walters and Wilder 2023)**: could not fetch (blocked). Not recorded.

No study found that measures prompt-caching cost savings and research accuracy together. Practitioner blog claims (e.g. "40-60% of savings unrealized") are unsupported [S].

## 4. Knowledge-management practice

- Wikipedia "Content forking" policy (fetched): duplicate pages on the same scope can drift into "different and possibly even conflicting facts"; they multiply maintenance work. Prefers a single source of truth. Remedies: merge the newer into the main article; split into a subarticle with a neutral summary left in the parent; check for an existing article before creating one. The page does not name redirects, and does not use the words "stale" or "unmaintained".
- Wikipedia verifiability studies [S]: the Dartmouth 2016 study (5,000 articles, 295,800 citations) measured whether citations let a reader check a claim, not whether they support it. A SIDE paper (Nature Mach Intell 2023) reports annotator agreement of only kappa 0.11 on whether citations support claims. No authoritative failed-citation rate found.
- Zettelkasten/evergreen notes [S]: no empirical study found. Only practitioner accounts. One user with over 1,000 notes reports repeatedly creating a note and finding a near-identical one. Andy Matuschak notes that most users write about others' ideas. Treat as anecdote.

## 5. Safeguards and their evidence

| Safeguard | Evidence | Strength |
|---|---|---|
| Re-check headline claims against the primary page | Quotation error 11.9% major; Cochrane updates re-examine earlier studies | Strong rationale, indirect |
| Verifier on extracted data (single extraction plus check) | 14.5% vs 17.7% and 15% vs 16% error rates [S] | Moderate, snippets only |
| Record provenance (page, fetch date, what was extracted) | Faithfulness gap (up to 57%) and copied misprints show citations alone do not prove reading | Rationale, no direct trial |
| Expiry or invalidation for notes | Invalidation preprint: silent failure after drift, 29-33% token recovery with row-level invalidation | Single preprint |
| Independent checking by a fresh agent | DeepTRACE judge-human r=0.62-0.72 shows judge checking is useful but imperfect | Moderate |
| Single source of truth, merge duplicates | Wikipedia policy | Policy, no measured effect |

Gaps: no study directly compares re-fetching with reusing notes for accuracy. No primary-page confirmation for Elliott 2017 update rules, MECIR U8, Buscemi, Li or Mathes numbers. Walters and Wilder not read.

## Sources

- [Jergas and Baethge 2015, Quotation accuracy in medical journal articles (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627914) — accessed 2026-11-08
- [Simkin and Roychowdhury, Read before you cite (arXiv cond-mat/0212043)](https://arxiv.org/abs/cond-mat/0212043) — accessed 2026-11-08
- [Simkin and Roychowdhury, Read before you cite (search result with misprint details)](https://arxiv.org/pdf/cond-mat/0212043) — accessed 2026-11-08 [S]
- [DeepTRACE, auditing deep research systems (arXiv 2509.04499)](https://arxiv.org/html/2509.04499v1) — accessed 2026-11-08
- [Wallat et al., Correctness is not Faithfulness in RAG Attributions (arXiv 2412.18004)](https://arxiv.org/abs/2412.18004) — accessed 2026-11-08
- [Xiong et al., How Memory Management Impacts LLM Agents (arXiv 2505.16067)](https://arxiv.org/abs/2505.16067) — accessed 2026-11-08
- [Invalidation Contracts for Cross-Episode Agent Memory (arXiv 2609.00243)](https://arxiv.org/abs/2609.00243) — accessed 2026-11-08
- [The Compliance Trap, conflicting agent memory (arXiv 2607.10608)](https://www.alphaxiv.org/abs/2607.10608v1) — accessed 2026-11-08
- [Wikipedia, Content forking policy](https://en.wikipedia.org/wiki/Wikipedia:Content_forking) — accessed 2026-11-08 (wiki)
- [Elliott et al. 2017, Living systematic review 1 (citation details)](https://discovery-pp.ucl.ac.uk/id/eprint/10025041) — accessed 2026-11-08 [S]
- [Cochrane instructions for updating an intervention review (MECIR U8 via search result)](https://ec.cochrane.org/sites/ec.cochrane.org/files/uploads/carg_ec_detailed_instructions_for_updating_an_intervention_review_april_2020.pdf) — accessed 2026-11-08 [S]
- [Buscemi 2006 single vs double extraction (PubMed)](https://pubmed.ncbi.nlm.nih.gov/16765272/) — accessed 2026-11-08 [S]
- [Extraction error trial protocol quoting Buscemi and Li (medRxiv)](https://medrxiv.org/content/10.1101/2023.10.16.23297056v1.full.pdf) — accessed 2026-11-08 [S]
- [Improving Wikipedia Verifiability with AI (arXiv 2207.06220)](https://arxiv.org/pdf/2207.06220) — accessed 2026-11-08 [S]
- [Andy Matuschak, evergreen notes vs Zettelkasten](https://notes.andymatuschak.org/zQvwwb95vzcHcpow3GWy5Wi) — accessed 2026-11-08 [S]
