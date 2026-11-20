# Changelog

## 1.1.0 (2026-11-20)

**Benchmarks.** v1.1 was tested on Claude Opus 5.5 (9 cases) and against v1.0 and no skill on eight models from five providers via OpenRouter (216 runs, two blind judges). Pass rate across the eight models: 84% without the skill, 93% with v1.0, 97% with v1.1. See `benchmarks/cross-model/`. Six eval cases were added: clean human abstract (over-editing), staging and strawman Discussion, LaTeX file mode, reviewer response, author's voice, and audit only.

Additions from a review of [blader/humanizer](https://github.com/blader/humanizer) v4.0.0. Details and rejected items are in `references/source-notes.md`.

- **Evidence tiers:** strong patterns are fixed on one sighting; weak ones (a single listed word, one dash, one hedge, one passive) only when other tells cluster. Watched phrases inside quotations, titles, and names are left alone.
- **New sentence patterns:** S14, staging and aphorism ("At its core", "The key question is", "X is the currency of Y"), and S15, arguing with no one ("This is not to say", "One might argue").
- **Extended patterns:**
  - S3 adds the split-sentence form ("This does not mean X. It means Y.") and "X rather than Y".
  - D9 adds closers after a finding and closing "Overall/Ultimately" verdicts.
  - S11 adds document self-description.
  - W8 adds gap-filling guesses ("not documented, suggesting...", "she likely...").
  - W6 now covers spaced en dashes and double hyphens, keeps en dashes in ranges and eponyms, and adds the predicate-hyphen rule.
  - W1 adds seven words.
- **New guards:**
  - Text supplied for editing is never treated as instructions.
  - A writing sample from the author overrides the defaults.
  - "Associated with" is protected as correct statistical wording.
- **Workflow:** the editor's audit now checks the tells that most often survive a rewrite first; file mode changes prose only and reports which sections were covered.
- **Section guide:** reviewer responses lead with the decision.
- **Checker:** new candidate patterns for S3 (split form), S11, S14, S15, D9, and W8, plus the new W1 words.

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
