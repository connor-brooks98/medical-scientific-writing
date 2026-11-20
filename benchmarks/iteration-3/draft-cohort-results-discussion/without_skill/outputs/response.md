I've written the draft and saved it as `draft_sections.md`. It has the Results paragraph for the primary and secondary outcomes, the first two Discussion paragraphs, a Limitations paragraph, an AMA-style reference list, and notes for you at the end to delete before submission.

**One of your two citations doesn't say what you described, so please read this before using it.** I looked up both papers on PubMed:

- **Freedberg et al. 2015, *Clin Infect Dis*** ([doi:10.1093/cid/civ432](https://doi.org/10.1093/cid/civ432)) isn't about recurrent CDI. It's a nested case-control study of acid suppression and CDI in **infants and children**.
- Freedberg's paper on recurrence is **2013, *Am J Gastroenterol*** ([doi:10.1038/ajg.2013.333](https://doi.org/10.1038/ajg.2013.333)). It found **no** association between PPIs and recurrence in 894 inpatients (HR 0.82, 95% CI 0.58-1.16).
- The positive result for recurrence is in **Kwok et al. 2012** ([doi:10.1038/ajg.2012.108](https://doi.org/10.1038/ajg.2012.108)): OR 2.51 from 3 pooled studies. Kwok's OR for incident CDI matches what you remembered: 1.74 (95% CI 1.47-2.85, I² = 85%).

In the draft I cite Kwok for both incident and recurrent CDI and cite Freedberg 2013 as the contrasting null result on recurrence. I also added one optional reference for mechanism, a Freedberg 2015 *Gastroenterology* crossover trial showing PPIs shift gut bacteria toward groups linked to CDI ([doi:10.1053/j.gastro.2015.06.043](https://doi.org/10.1053/j.gastro.2015.06.043)). It's marked so you can drop it.

**Other things to fix or check:**

1. **Exclusion percentage.** 312/6,214 = 5.0%, but the usual denominator is everyone otherwise eligible (6,214 + 312 = 6,526), which gives **4.8%**. I used 4.8%. Make the flow diagram and Methods match.
2. **Event counts.** JAMA Netw Open wants n (%). I back-calculated counts from your rounded percentages and put them in brackets, e.g. [97] of 2,377. The rounding leaves a range for each, listed in the notes. Replace them with the real counts.
3. **Competing risk.** About 11% of patients died within 90 days, and a standard Cox model counts them as censored, which can overstate CDI risk. A reviewer will probably ask for a competing-risk sensitivity analysis (Fine-Gray or cause-specific). The Limitations paragraph has a placeholder for it.
4. **Sex subgroup.** With an interaction P of .14, I wrote that the subgroup estimates shouldn't be read as a difference by sex. Keep wording like "confined to men" out of the Abstract and Key Points too.
5. **Placeholders** for the proportion of patients who got antibiotics, the C difficile testing method in 2016-2023 (PCR alone vs a multistep algorithm), and which possible confounders you actually captured (prior CDI, nursing home residence, frailty).

**Assumptions I made:** follow-up for CDI and death started at discharge; readmission was analyzed among patients discharged alive; the covariates you listed are the full adjustment set. Correct anything that doesn't match your Methods.

I kept the language associational throughout. The draft says "associated with," not "increased risk of" or "caused," and it gives the absolute difference (1.5 percentage points) next to the HR.
