[file returned: results.tex]

**What changed**

- *Discourse:* deleted the closing interpretation in the last paragraph ("a finding that serves as a testament to the overall safety of the strategy"). An HR of 0.92 with a CI spanning 0.70 to 1.21 does not support a safety claim; argued in Results is also the wrong place for it.
- *Sentences:* removed the two -ing tails ("highlighting the robustness of…", "underscoring the crucial role of early intervention"), which restated the data as conclusions. Folded the propensity-score attribution into the sentence about balance so the citation still sits on the claim it supports.
- *Words and marks:* removed "It is important to note that", "Notably", "Furthermore", "remarkably", "crucial", "testament"; replaced the two em dashes (`---`, `--`) with a period and parentheses.
- *Rhythm:* sentence lengths in paragraph 1 now run 15 and 17 words rather than three near-equal clauses.

**Fidelity**

All numbers, the equation, and every `\ref`, `\label`, and `\cite` key are unchanged and in the same order (I left the space in `\cite{cox1972regression, therneau2000modeling}` exactly as written). The one datum deleted with its sentence is the word "safe", which was an evaluation, not a result. The revised file is shorter than the original.

**Author queries**

1. **Mortality.** I ended the last paragraph at the confidence interval rather than supplying a replacement verdict. If you want the mortality result interpreted, the honest statement is that the CI includes no difference (0.70 to 1.21).
2. **"Consistent across all prespecified subgroups."** I kept your wording, but a per-subgroup description is not a test. If no treatment-by-subgroup interaction test was run, an editor will ask for one; if one was run and any subgroup was null, say so here rather than in the Discussion.
3. **"Well balanced."** No balance statistics (standardized mean differences) accompany the claim. If you have them, one number would carry it better than the adjective.
4. **Model sentence.** "The adjusted model was specified as" appears before any unadjusted result; if the primary analysis was unadjusted or if both were fitted, a half-sentence saying which model produced the HR in paragraph 2 would remove the ambiguity.

If this is going to a journal: most journals and ICMJE require disclosure of AI-assisted writing in the cover letter or a dedicated statement. One mention there is enough.
