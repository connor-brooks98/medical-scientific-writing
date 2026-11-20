I edited `results.tex` in place and changed only the prose. Every `\ref`, `\label`, `\cite` key, `~` tie, `\%`, numeric `--` range, and the whole `equation` block is the same as before, character for character. The file also compiles cleanly inside a minimal `article` wrapper.

I treated this as a propensity-score-matched observational cohort, based on the matching citation, so I used associational wording rather than causal wording.

```latex
\section{Results}
\label{sec:results}

A total of 2,418 patients met the inclusion criteria (Figure~\ref{fig:flow}). After propensity-score matching \cite{austin2011introduction}, baseline characteristics were well balanced between the groups (Table~\ref{tab:baseline}).

The primary outcome occurred in 142 patients (11.7\%) in the intervention group and 198 patients (16.4\%) in the control group (hazard ratio [HR] 0.69; 95\% CI 0.56--0.86; $p = 0.001$). The association was consistent across all prespecified subgroups (Figure~\ref{fig:forest}).

The adjusted model was specified as
\begin{equation}
  \log h_i(t) = \log h_0(t) + \beta_1 \text{Treatment}_i + \boldsymbol{\gamma}^\top \mathbf{x}_i ,
  \label{eq:cox}
\end{equation}
where $\mathbf{x}_i$ denotes the vector of baseline covariates listed in Table~\ref{tab:baseline} \cite{cox1972regression, therneau2000modeling}.

All-cause mortality, a secondary outcome, did not differ significantly between the groups (7.9\% versus 8.6\%; HR 0.92; 95\% CI 0.70--1.21). [DATA NEEDED: results for any other secondary outcomes]
```

**What changed**
- **Interpretation in Results:** I cut three sentences that told the reader what to conclude:
  - "highlighting the robustness of the propensity-score matching approach": balance on measured covariates doesn't show robustness.
  - "underscoring the crucial role of early intervention": a matched cohort can't establish a causal role.
  - "serves as a testament to the overall safety of the strategy": a null mortality result doesn't establish safety.
- **Mortality result:** the old sentence said secondary outcomes "showed a similar pattern". But the mortality CI (0.70–1.21) includes 1, unlike the primary outcome's. I now report mortality as the null result it is, written as plainly as the primary result.
- **Causal wording:** "this effect" is now "the association", to fit the observational design.
- **Filler and connectives:** I cut "It is important to note that", "Notably", "Furthermore", and "remarkably".
- **Dashes:** I removed the `---` em dash and the spaced ` -- ` used as a dash. The `--` in the numeric ranges (0.56--0.86, 0.70--1.21) is correct en-dash typography, so it stays.
- **First paragraph:** the matching citation now sits on the matching itself, and the table reference moved into parentheses after the finding.
- **Length:** 147 words, down from 182.

**Fidelity:** I checked every number, percentage, HR, CI, p value, citation key, and cross-reference against the original with `check_patterns.py --original`. Nothing was lost or added, and the equation block is identical.

**Placeholders and author queries**
- `[DATA NEEDED: results for any other secondary outcomes]`: the original said "secondary outcomes" (plural) but reported only mortality. Add the others, or delete the placeholder if mortality was the only one. It's inline text, so it will show in the PDF until you deal with it.
- **What does 2,418 count?** 142/11.7% and 198/16.4% each work out to about 1,209 patients per arm, and 2 × 1,209 = 2,418. So 2,418 looks like the *matched* cohort, not the number who met the inclusion criteria. If more patients were eligible before matching, report both numbers (e.g., "X patients met the inclusion criteria, of whom 2,418 were matched").
- **"Well balanced":** consider giving the criterion, e.g., all standardized mean differences < 0.1, if Table~\ref{tab:baseline} reports them.
- **"Consistent across all prespecified subgroups":** I kept your claim. If you ran interaction tests, a p-for-interaction range would support it better than the forest plot alone.
- **The model specification** (the equation and its covariates) usually belongs in Methods. I left it where it is because moving it was outside the scope of a prose cleanup.
- Most journals and ICMJE require you to disclose AI-assisted editing at submission.
