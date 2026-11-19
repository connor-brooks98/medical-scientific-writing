I wrote the Results paragraph, the first two Discussion paragraphs and the Limitations paragraph, and saved them in `draft_sections.md`. Bold brackets mark data or choices only you can fill in. The text follows AMA style (for example, "aHR, 1.48; 95% CI, 1.12-1.96" and "*P* = .14 for interaction"). Citations are author-year placeholders until your references are numbered.

## The Freedberg citation doesn't match what you described

I checked both references in PubMed. Kwok et al. 2012 is correct: a pooled OR of 1.74 (95% CI, 1.47-2.85) for incident CDI across 42 observational studies ([DOI](https://doi.org/10.1038/ajg.2012.108)).

The Freedberg paper isn't what you described:

- **Freedberg et al. 2015, *Clin Infect Dis*** is a nested case-control study of infants and children. It looks at acid suppression and *incident* CDI, not recurrence ([DOI](https://doi.org/10.1093/cid/civ432)). It doesn't fit an older-adult cohort.
- **Freedberg et al.'s recurrent-CDI paper** is *Am J Gastroenterol* 2013. It found **no** association between PPIs and recurrence among 894 inpatients (HR, 0.82; 95% CI, 0.58-1.16) ([DOI](https://doi.org/10.1038/ajg.2013.333)).

In the draft I cite the 2013 paper accurately, as contrasting evidence on recurrence. The positive recurrence finding comes from Kwok's pooled analysis of 3 studies (OR, 2.51). If you don't want to discuss recurrence at all, those two sentences can be cut cleanly.

## Things to fix or confirm before submission

1. **The exclusion percentage is wrong.** 312/6,214 is 5.0%, but that uses the analytic cohort as the denominator. The eligible population is 6,214 + 312 = 6,526, which gives **4.8%**. The draft uses 4.8%, so please confirm the eligible count.
2. **Event counts are missing.** JAMA Network Open expects n (%) for every outcome. Based on your percentages, expect about 97-98 CDI events in PPI users vs 98-101 in nonusers; 280-281 vs 428-431 deaths; and 425-426 vs 628-631 readmissions. Use your actual numbers.
3. **Absolute risk difference.** I added the crude difference of 1.5 percentage points, because the journal and its reviewers expect absolute measures. A rough CI from your percentages is about 0.6 to 2.4 percentage points, but calculate it from the real counts. An adjusted risk difference would be better if you can get one.
4. **Competing risk of death.** About 11% of patients died within 90 days. Your Cox model gives a cause-specific HR, and reviewers will likely ask for a Fine-Gray sensitivity analysis. I left a placeholder sentence in the Limitations.
5. **Sex subgroup.** With an interaction P of .14, the draft says the association does *not* differ significantly by sex. Please don't frame it as a finding in men. If you want a stronger statement, you'd need a different analysis, not different wording.
6. **Residual confounding.** Your adjustment set is fairly limited. An E-value is easy to add and reviewers like it. For aHR 1.48 it is about **2.32**, and for the lower CI bound of 1.12 it is about **1.49**. This would need a line in Methods.

## Assumptions I made

- The 6,214 patients are the analytic cohort after the 312 exclusions (2,377 + 3,837 = 6,214).
- Patients with CDI during the index stay or prior CDI were excluded, so the outcome is incident post-discharge CDI. Please confirm.
- Nearly all patients got antibiotics during the index stay. The second Discussion paragraph builds on Kwok's PPI-antibiotic synergy finding because of this.
- The CDI assay isn't specified (PCR vs toxin), so there is a placeholder for it in the Limitations.
- Sex was the only prespecified subgroup.

## Optional references to consider (found in PubMed)

- Howell et al., *Arch Intern Med* 2010: a dose-response relationship between acid suppression and hospital-onset CDI in 101,796 discharges ([DOI](https://doi.org/10.1001/archinternmed.2010.89)). This would strengthen the second Discussion paragraph.
- Dial et al., *JAMA* 2005: PPIs and community-acquired CDI, adjusted rate ratio 2.9 ([DOI](https://doi.org/10.1001/jama.294.23.2989)).
- Freedberg et al., *Gastroenterology* 2015: PPIs shift gut microbial taxa associated with CDI ([DOI](https://doi.org/10.1053/j.gastro.2015.06.043)). This supports the optional sentence on mechanism.
- You'll still need a reference on PPI deprescribing for the sentence about reassessing PPIs; there's a placeholder for it.
