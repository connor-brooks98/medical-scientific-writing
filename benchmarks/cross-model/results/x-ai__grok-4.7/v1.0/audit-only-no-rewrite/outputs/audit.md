# Audit: Introduction

Reading used: this is the opening of a prospective-study introduction, motivated by an institutional retrospective analysis. If it is the introduction to the 2,914-patient paper itself, the mortality result does not belong here, and the last sentence describes a different study.

Pattern IDs: D1 stated moral; D2 unnamed evidence; D3 tidy causal story; D4 study-as-hero; D5 promotional close; D6 generic opening; D7 uneven certainty; D8 advocacy; D9 restatement; S2 copula avoidance; S3 "not only...but also"; S6 verb or hedge miscalibration; S13 missing comparator or condition; W1 inflated vocabulary; W5 connective used as padding.

| Location | Quoted text | Pattern | Severity | Suggested fix |
|---|---|---|---|---|
| Paragraph 1, sentence 1 | "Sepsis remains a leading cause of death worldwide, representing a pivotal challenge in the evolving landscape of critical care." | D6, D1, S2, W1 | Major | Cut. The sentence could open any sepsis paper, and "representing" only restates "is." If a burden figure is needed, use one cited number and reach the timing question in the next sentence. |
| Paragraph 1, sentence 2 | "In recent years, there has been growing interest in the role of early vasopressor initiation." | D6 | Major | Cut. "Growing interest" is not a gap. Name the decision the study is about: when norepinephrine is started, compared with what, in whom. |
| Paragraph 1, sentence 3 | "Studies have shown that early norepinephrine improves survival in septic shock." | D2, S6 | Critical | Do not leave this as an unnamed consensus, and do not use "improves" unless the source is a randomized comparison of that endpoint. Name the study, design, population, and estimate, and cite it. If you do not have that source, mark the claim rather than assert it. |
| Paragraph 1, sentence 4 | "Furthermore, a growing body of evidence suggests that delayed vasopressor therapy may potentially be associated with worse outcomes in some patients." | D2, D9, S6, W5 | Major | Delete. This repeats the previous sentence in the other direction, cites nothing, and stacks hedges ("suggests," "may," "potentially," "in some patients") on an undefined outcome. |
| Paragraph 2, sentence 1 | "norepinephrine started within 1 hour of shock onset was associated with lower 28-day mortality (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)" | S13 | Major | Keep the verb "was associated with" and the estimate. Name the reference group and the covariates. If this analysis is published, cite it. If it is this paper's result, move it to Results. If it is unpublished preliminary data, label it as such. |
| Paragraph 2, sentence 2 | "Early norepinephrine therefore prevents death in septic shock." | S6, D3, D8 | Critical | Delete the causal leap. An adjusted retrospective association does not show that norepinephrine prevents death. State the association, then the main threat to that reading (confounding by indication, and how time zero and severity were handled). Do not give the favorable reading a stronger verb than the data. |
| Paragraph 2, sentence 3 | "To address this critical gap, we designed a comprehensive prospective study that will not only fill an important gap in the literature but also pave the way for improved outcomes." | D4, D5, S3, S13, W1 | Major | The gap is never defined, and a future study cannot yet have improved outcomes. Say what is unknown, then what the prospective study will compare, in whom, and on which primary outcome. Cut "critical gap," "not only...but also," "comprehensive," and "pave the way." |
| Whole introduction | "Studies have shown that early norepinephrine improves survival" followed by "To address this critical gap" | D4, D7 | Major | These contradict each other. If prior work has already shown a survival benefit, that is not the gap. Certainty should also match the design: the same question is first hedged into vagueness, then upgraded to prevention. |

Leave the association sentence's verb and the odds ratio with its confidence interval as they are. Those are the parts that already match the design. No unfavorable or null result was in the source text, so none was judged missing. No citation in the draft could be checked, because there are none.

## Five revisions that would help most

1. Remove "therefore prevents death," and do not use "improves" unless a cited randomized comparison supports it.
2. Replace "studies have shown" and "a growing body of evidence" with named, quantified, cited sources, or mark those claims as needing citations.
3. Open on the timing question, not on sepsis as a worldwide cause of death.
4. Define the unresolved question and the prospective comparison, population, and primary outcome. Cut the closing promise.
5. Delete the delayed-therapy restatement. On the institutional analysis, specify the reference group and the covariates, and say whether that analysis is prior work, preliminary data, or this paper's result.
