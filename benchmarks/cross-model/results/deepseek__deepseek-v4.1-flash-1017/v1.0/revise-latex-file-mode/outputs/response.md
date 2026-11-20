[file returned: results.tex]

**What changed**

- *Discourse:* removed the editorial framing around the mortality result ("showed a similar pattern", "a testament to the overall safety of the strategy"). The HR with a CI spanning 1 cannot support a safety claim; the numbers now stand alone. Also dropped "the crucial role of early intervention", an interpretation that belongs in the Discussion if you keep it at all.
- *Sentences:* deleted the "It is important to note that" opener; replaced the "highlighting the robustness of the propensity-score matching approach" tail with the plain statement of what was observed (balance after matching); removed "underscoring" and "serves as a testament to".
- *Words:* removed "Notably", "Furthermore", "remarkably", "crucial", "robustness", "testament", and both em dashes (semicolon for the first, deletion for the second).
- LaTeX untouched: `\ref`, `\cite`, `\%`, `--` ranges, the `equation` block, `\text`, `\boldsymbol`, `\mathbf`, `^\top`, `_i`, and `\label` all render exactly as before.

**Fidelity:** all numbers (2,418; 142/11.7%; 198/16.4%; HR 0.69, 95% CI 0.56–0.86; p = 0.001; 7.9%; 8.6%; HR 0.92, 95% CI 0.70–1.21), both citations, and both figure/table references are preserved. The percentages are internally consistent with an approximately even two-group split of 2,418 (142/11.7% ≈ 198/16.4% ≈ 1,210 per group).

**Author queries**

1. "Consistent across all prespecified subgroups": if this rests on non-significant interaction tests, that is not evidence of consistency. Report the subgroup HRs with CIs, or the interaction p values, and note any subgroup where the direction or magnitude differed.
2. "Well balanced": standardized mean differences would let readers judge balance themselves. I read your sentence as balance *after* matching; confirm that is what Table~\ref{tab:baseline} shows.
3. Safety: if you have adverse-event data, report them here. All-cause mortality alone (HR 0.92, 95% CI 0.70–1.21) is compatible with harm as well as benefit.
4. Secondary outcomes: only mortality appears. Any other secondary outcomes, null ones included, belong in this paragraph.
5. Check your journal's style for italic *P* and for CI separators (en dash vs "to"); I left your `$p$` and `--` as written.

One housekeeping note: most journals and ICMJE require disclosure of AI-assisted writing, so add the statement your target journal asks for.
