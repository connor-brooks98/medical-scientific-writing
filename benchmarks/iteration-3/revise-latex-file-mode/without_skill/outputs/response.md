I edited `results.tex` in place. Only the prose in three paragraphs changed. The equation block, every `\ref`, every `\cite`, the inline math, `\%` escapes, `~` ties and `--` number ranges are exactly as you had them.

**What changed**

1. **Paragraph 1:** Took out "It is important to note that". Rewrote "highlighting the robustness of the propensity-score matching approach" to say only that the groups were balanced after matching. Balance tells you the matching worked on the measured covariates. It doesn't show the approach is robust. I also replaced the `---` em dash with a semicolon.
2. **Paragraph 2:** Cut "Notably," "remarkably" and "underscoring the crucial role of early intervention." Consistent subgroup effects don't show that *timing* matters, so that's a Discussion point at best. It now reads: "The effect was consistent across all prespecified subgroups (Figure~\ref{fig:forest})."
3. **Last paragraph:** Took out "Furthermore," "showed a similar pattern" and "a testament to the overall safety of the strategy." The mortality CI (0.70–1.21) includes 1, so the result can't support a safety claim. The en dash `--` in that sentence was also doing an em dash's job, which is wrong, so it's gone. It now reads: "Among secondary outcomes, all-cause mortality was 7.9\% versus 8.6\% (HR 0.92; 95\% CI 0.70--1.21)."

**How I checked it:** The `\ref`/`\cite` keys, `$` count, environment count and brace balance are the same as in the original. I also ran the file through `pdflatex` inside a minimal wrapper (amsmath + bm). It compiled with no errors. The only warnings were the expected undefined-reference ones, since the labels and bib entries live elsewhere in your project.

**Things to check (I didn't change these):**
- **Mortality sentence:** I assumed 7.9% is intervention and 8.6% is control, the same order as the primary outcome. You may want to add "in the intervention and control groups, respectively" or give the n's as you did for the primary outcome. A p value would also match the primary-outcome sentence.
- **"Secondary outcomes":** The original said "secondary outcomes" (plural) but reported only mortality. If there are others, report them here.
- **"all prespecified subgroups":** I kept "all" because I can't see the forest plot. Make sure no subgroup's interaction p value or CI weakens it.
- **Model equation:** The Cox equation and the "adjusted model was specified as" text are Methods content. Consider moving them to Methods and referring back with `Equation~\eqref{eq:cox}`.
