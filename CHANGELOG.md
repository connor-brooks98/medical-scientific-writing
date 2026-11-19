# Changelog

## 1.0.0 (2026-11-19)

First public release.

- Packaging: the claude.ai / Claude Desktop zip (`dist/medical-scientific-writing.zip`, also attached to the release) has `SKILL.md`, `references/`, and `scripts/` at the top level of the archive, as the uploader requires.

- Revise, Draft, and Audit workflows with integrity rules (no invented facts, design-matched verbs, symmetric reporting, no significance spin, disclosure reminder).
- 33 patterns across three layers (discourse D1-D11, sentence S1-S13, word W1-W9), plus the swap test and over-correction guards.
- References: pattern catalog with medical before/after examples, section guide (IMRaD, CARE case reports, reviews, grants, reviewer responses, lay summaries), evidence and reporting, clarity toolkit, source notes.
- `check_patterns.py` checker: rhythm, marks, openers, hedge stacks, uncited attributions, candidate phrases, length growth, numbers and citations added or lost. Placeholders are excluded from all counts.
- Changes from the v0.9 draft benchmarked in round 1:
  - Revisions should not grow beyond the original except to restore omitted content; the checker flags growth over 10%.
  - A verified, retrieved reference may enter the text only when the user asked for literature or it replaces a citation that does not support its claim, marked `[ADDED: verified, DOI]`. Everything else goes to a candidates list.
  - Placeholders go on specific, checkable claims, not on every textbook sentence.
  - The description was shortened to the 200-character limit claude.ai uploads require.
- Benchmark note: after round 1, two cohort-case assertions were re-specified to match the reference rule above, and round 1 was re-graded with them. The original wording was "cites only Kwok et al. 2012 and Freedberg et al. 2015; any other claim needing support uses a placeholder, and no other study is named" and "every number is either supplied in the prompt or a correct arithmetic derivation of supplied numbers". Under the original wording, both the with-skill and the without-skill runs failed both assertions in round 1, because both correctly replaced a mismatched citation with a verified one.
