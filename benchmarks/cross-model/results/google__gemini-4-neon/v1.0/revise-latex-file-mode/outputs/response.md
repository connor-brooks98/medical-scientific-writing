I have revised `results.tex` in place while keeping all LaTeX commands, labels, cross-references, citations, math, and numeric formatting intact. I assumed this is an observational propensity-score matched cohort study based on the matching reference and Cox model.

[file returned: results.tex]

**What changed**
- **Discourse and evidence (D1, D3, D8):** Corrected the framing of all-cause mortality, which is a null finding (95\% CI 0.70--1.21 crosses 1.0) rather than a "similar pattern" to the primary outcome, and removed the unsupported claim that this null result demonstrates "overall safety." Removed interpretive commentary from Results ("crucial role of early intervention", praise of the matching approach).
- **Sentences (S1, S2, S6, S11):** Cut both `-ing` interpretive tails (", highlighting...", ", underscoring..."), removed the signposting opener ("It is important to note that"), replaced copula avoidance ("serves as a testament"), and changed "this effect" to "This association" to match the observational design.
- **Words and marks (W1, W3, W5, W6):** Removed AI-favored vocabulary and adverbs (`highlighting`, `robustness`, `remarkably`, `underscoring`, `crucial`, `testament`), cut unnecessary transition openers (`Notably,`, `Furthermore,`), and removed the prose dashes (`---` and `--`) while preserving LaTeX en-dashes (`--`) inside CI ranges.

**Fidelity**
All numbers, percentages, hazard ratios, confidence intervals, $p$ value, citations (`austin2011introduction`, `cox1972regression`, `therneau2000modeling`), figure/table references, and Equation `\ref{eq:cox}` are preserved unchanged.

**Author queries**
- **Model placement:** Equation `\ref{eq:cox}` (with `\cite{cox1972regression, therneau2000modeling}`) and the propensity-score matching citation (`\cite{austin2011introduction}`) were kept here so no labels or citations are lost, though most journals expect model specifications and methodological citations in Methods rather than Results.
- **Secondary outcomes:** The text refers to "secondary outcomes" (plural) but reports only all-cause mortality. Consider adding the remaining secondary outcomes with event counts, estimates, and 95\% CIs, or changing the opener to "All-cause mortality did not differ..." if it is the only secondary outcome reported here.
- **Completeness of reporting:** Consider adding the group sizes ($n$ per arm), the balance threshold for Table~\ref{tab:baseline} (for example, maximum standardized mean difference), event counts and the exact $p$ value for all-cause mortality, and interaction $p$ values for the prespecified subgroup analyses.
- **Safety claim:** If you plan to discuss safety in the Discussion, note that a 95\% CI of 0.70--1.21 is compatible with up to a 21\% relative increase in mortality and does not establish safety without a prespecified non-inferiority margin.
- **Disclosure:** If this manuscript is headed for journal submission, most journals and ICMJE guidelines require disclosing AI-assisted writing or editing.
