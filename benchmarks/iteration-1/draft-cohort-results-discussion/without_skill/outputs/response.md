I've written the Results (primary and secondary outcomes), the first two Discussion paragraphs and a Limitations paragraph, saved as **draft_sections.md**. Before you circulate it, one of your citations needs fixing.

**The Freedberg 2015 *Clin Infect Dis* paper doesn't support the recurrence claim.** I checked it in PubMed. That paper is a pediatric case-control study of acid suppression and *incident* CDI in infants and children ([doi:10.1093/cid/civ432](https://doi.org/10.1093/cid/civ432)). Freedberg's actual recurrent-CDI study is *Am J Gastroenterol* 2013, and it found **no** association between in-hospital PPI use and recurrence (HR, 0.82; 95% CI, 0.58-1.16) ([doi:10.1038/ajg.2013.333](https://doi.org/10.1038/ajg.2013.333)). In the draft I:
- cite the 2013 paper accurately, as a discordant result;
- support "PPIs are linked to recurrent CDI" with Kwok's pooled recurrence estimate (OR, 2.51) and McDonald et al 2015 *JAMA Intern Med* ([doi:10.1001/jamainternmed.2015.42](https://doi.org/10.1001/jamainternmed.2015.42)).

If your team meant a different Freedberg paper, send me the DOI and I'll revise.

I confirmed the Kwok 2012 meta-analysis in PubMed as you described it: OR, 1.74 (95% CI, 1.47-2.85) across 39 studies, with higher risk when PPIs and antibiotics are used together ([doi:10.1038/ajg.2012.108](https://doi.org/10.1038/ajg.2012.108)). The draft uses that antibiotic finding, since nearly every patient with CAP gets antibiotics. I also added the COMPASS randomized trial (Moayyedi 2019, *Gastroenterology*; [doi:10.1053/j.gastro.2019.05.056](https://doi.org/10.1053/j.gastro.2019.05.056)) because reviewers tend to bring it up. Both McDonald and COMPASS are optional.

**Other issues to fix before submission:**
1. **The exclusion percentage is off.** 312 is 5.0% of the 6214 analyzed patients, but the denominator should be everyone eligible (6526), which gives **4.8%**. Update Methods and the flow diagram.
2. **Competing risk of death.** With about 11% of patients dying within 90 days, reviewers will ask about it. I'd add a Fine-Gray or cumulative-incidence sensitivity analysis. The Limitations paragraph has a bracketed sentence ready for it.
3. **The sex subgroup is written conservatively on purpose.** The interaction P value is .14, so the text says the difference isn't significant and treats it as exploratory. It doesn't claim PPIs matter in men but not women.
4. **The null secondary outcomes don't mean "no effect".** The CIs allow up to about a 20% increase in mortality and readmission, and the text says so.

**Numbers I calculated or checked:**
- **Absolute difference:** 1.5 percentage points (95% CI, 0.6-2.4), from the crude proportions. Recompute it from your actual event counts.
- **E-value:** 2.32 (1.49 for the lower CI bound). It's an optional bracketed sentence.
- **Consistency check:** every HR and CI is internally consistent, and the interaction P value I recalculated (about .15) matches yours.

**Assumptions to confirm:**
- 4.1% and 2.6% are crude proportions, not Kaplan-Meier estimates.
- 90-day mortality is counted from discharge.
- The cohort is limited to patients discharged alive.
- Patients with prior CDI were excluded or adjusted for. If not, list it as a limitation.
- Event counts and subgroup sizes are left as [n] placeholders, because the rounded percentages don't pin down exact counts.
- Number formatting follows AMA/JAMA style (no comma in 4-digit numbers, no leading zero on P values), but the journal's copyeditors will have the final say.

Notes for you are marked as *Author note* blocks throughout the file; delete them before submission.

Sources: PubMed (DOIs above, plus [doi:10.7326/M16-2607](https://doi.org/10.7326/M16-2607) for the E-value method).
