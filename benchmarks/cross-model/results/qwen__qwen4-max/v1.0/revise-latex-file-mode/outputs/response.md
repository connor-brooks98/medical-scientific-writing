[file returned: results.tex]

Here's the cleaned-up section. All LaTeX is untouched: `\label`s, `\ref`s, `\cite` keys, the `equation` environment, math, and escaped `\%` are exactly as you had them. The two placeholders are LaTeX comments, so the file still compiles and nothing extra prints.

**What changed**

- **Discourse:** removed the interpretation that doesn't belong in Results — "underscoring the crucial role of early intervention" and the claim that a null mortality result is "a testament to the overall safety of the strategy." A CI spanning 1.0 supports "did not reach statistical significance," not a safety claim (that would need adverse-event data). Also dropped "highlighting the robustness of the propensity-score matching approach," which is self-evaluation, not a result.
- **Sentences:** cut "It is important to note that"; deleted the two -ing tails; replaced "serves as a testament" and the vague "secondary outcomes showed a similar pattern" with the actual numbers and their group labels.
- **Words/marks:** removed "Notably," "remarkably," "crucial," "robustness," "Furthermore"; replaced the prose em dashes (`---`, `--`) with a period and a comma. The en dashes in the CI ranges (`0.56--0.86`, `0.70--1.21`) are numeric ranges and stay.
- **Calibration:** "this effect was consistent" became "the association was similar," since a propensity-score-matched cohort is observational.

**Fidelity:** every number, percentage, HR, CI, p value, citation, and cross-reference is preserved, and both outcomes (primary and the null mortality result) still appear with the same prominence. The revision is shorter than the original.

**Placeholders and queries**

1. `[DATA NEEDED: standardized mean differences before and after matching]` — "well balanced" was an unsupported assertion; I softened it to "similar," but a reviewer will want the SMDs (or a statement that all were <0.1).
2. `[DATA NEEDED: subgroup HRs with 95% CIs and p values for interaction]` — "consistent across all prespecified subgroups" needs the interaction tests behind it, or at least a pointer to the forest plot values.
3. The Austin citation now sits on the matching method rather than on a claim about your own balance; check that placement matches your intent.
4. If you have adverse-event or harm data, that belongs here as its own sentence — it, not the mortality CI, is what would support a safety statement.
5. One note for submission: most journals and ICMJE require disclosure of AI-assisted writing.
