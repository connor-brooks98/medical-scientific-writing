[file returned: results.tex]

Edited in place; only prose changed. All LaTeX is untouched: `\section`, `\label`, the `equation` environment and its contents, every `\ref`, `\cite` key, escaped `\%`, math mode `$p = 0.001$`, and the `--` en dashes in CI ranges.

**What changed**

- **Discourse:** removed the two interpretation sentences that belong in the Discussion, not Results ("underscoring the crucial role of early intervention"; mortality as "a testament to the overall safety"). The mortality estimate has a CI spanning 1, so it is now reported as no difference rather than as evidence of safety or as "a similar pattern" to the significant primary outcome.
- **Discourse:** "the groups were well balanced, highlighting the robustness of the propensity-score matching approach" became a plain statement of balance; the Austin citation is retained at the matching clause.
- **Sentences:** deleted the ", highlighting..." tail and the "It is important to note that" opener; "serves as a testament to" removed.
- **Words/marks:** dropped Notably, remarkably, crucial, robustness, Furthermore; replaced the `---` and `--` used as dashes with sentence structure. Kept "prespecified", all group labels, and the [HR] definition as you had them.

**Fidelity:** every number, percentage, HR, CI, p value, citation, and cross-reference in the original appears unchanged in the revision; nothing was added. The revision is shorter (about 130 vs 175 words of prose).

**Author queries**

1. Balance is asserted without a statistic. If Table 1 reports standardized mean differences, give the range (e.g. all <0.10) here; otherwise "balanced" is a judgment an editor will query.
2. `\cite{austin2011introduction}` is a methods tutorial. It supports the matching procedure, not the claim that your groups balanced. Consider moving it to Methods and citing your own Table 1 here.
3. "Estimates were similar across the prespecified subgroups" has no numbers behind it. Add the subgroup HRs or the interaction p value, or state that no formal interaction test was done; the forest plot alone will not satisfy a reviewer.
4. You wrote "secondary outcomes" (plural) but report only mortality. The other secondary outcomes, including null ones, need to appear here with estimates and CIs.
5. Mortality is given without a p value or event counts; add the numerator/denominator per group if the journal expects them.
6. No multiplicity statement for the secondary outcomes. If none was applied, say so in Methods and label these analyses as exploratory if that is what they were.

One reminder for submission: most journals and ICMJE require disclosure of AI-assisted writing, so note this editing help in the appropriate statement.
