# Cross-model benchmark (skill v1.0 vs v1.1 vs no skill)

Eight models from four providers, accessed through OpenRouter, each ran the 9 eval cases in three configurations: no skill, skill v1.0.0, and skill v1.1.0. That is 216 runs. Run on 2026-11-20.

## Method

- **How the skill was given:** these models cannot load Claude skills, so the harness (`harness/run.py`) sent SKILL.md and every reference file as the system prompt. Input files went in the user message, and models returned files between text markers. The models had no tools, so they could not run `scripts/check_patterns.py` or search the literature. This is a one-shot test, harder than the agentic Claude runs.
- **Automatic checks:** 45 of the 63 assertions per configuration are graded by script (`harness/grade3.py`). One grader was loosened after the run: the case-report check for the FDA recommendation now accepts "US Food and Drug Administration" as well as "FDA". GPT-6.2 Sol spelled it out in all three configurations and had been failed for it.
- **Judged checks:** the other 18 need reading. Two blind judges from different providers, Claude Opus 5.5 and GPT-6.2 Sol, graded them (`harness/judge.py`). Judges saw the task, the inputs and the output, never the model or configuration. An assertion passes only if both judges pass it. The judges agreed on 417 of 432 verdicts (96.5%); most disagreements were GPT-6.2 Sol failing responses that open with "We agree." before stating the change.
- **Retries:** four runs did not return their output file on the first try and got one retry each. Their first attempts are kept as `*.attempt1`:
  - Grok 4.7 omitted the file twice: no skill, cohort; v1.1, case report.
  - Qwen 3.8 27B hit the 24k-token output cap twice: v1.1, case report and staging.

## Assertions passed (of 63 per model and configuration)

| Model | No skill | v1.0 | v1.1 |
|---|---|---|---|
| deepseek-v4.1-flash-1017 | 51 | 60 | 60 |
| gemini-4-neon | 57 | 62 | 62 |
| gpt-6.1-terra | 54 | 58 | 61 |
| gpt-6.2-astra | 52 | 56 | 60 |
| gpt-6.2-sol | 53 | 57 | 60 |
| qwen3.8-27b | 51 | 58 | 61 |
| qwen4-max | 51 | 56 | 62 |
| grok-4.7 | 52 | 61 | 62 |
| **All** | **421/504 (84%)** | **468/504 (93%)** | **488/504 (97%)** |

## By case (all 8 models)

| Case | No skill | v1.0 | v1.1 |
|---|---|---|---|
| audit-only-no-rewrite | 47/56 | 54/56 | 56/56 |
| author-sample-voice | 34/40 | 34/40 | 38/40 |
| draft-cohort-results-discussion | 57/64 | 61/64 | 62/64 |
| preserve-clean-human-abstract | 38/56 | 47/56 | 50/56 |
| reviewer-response-lead-with-decision | 39/48 | 40/48 | 44/48 |
| revise-case-report-discussion | 44/56 | 55/56 | 56/56 |
| revise-discussion-staging-strawman | 57/64 | 57/64 | 63/64 |
| revise-intro-no-citations | 51/64 | 64/64 | 63/64 |
| revise-latex-file-mode | 54/56 | 56/56 | 56/56 |

The v1.1 gains are on the cases that test the rules added in v1.1:

- **Staging and strawman** (new S14/S15 patterns): 57 → 63.
- **Reviewer reply leads with the decision:** 40 → 44.
- **Author's own em dashes kept:** 34 → 38.

## Length, leftover patterns and over-editing

Median word change across the 7 revision cases; leftover pattern-catalog phrases summed over those cases; difflib similarity of the clean human abstract to the original (1.00 = untouched).

| Model | Length: none | v1.0 | v1.1 | Leftover hits none/v1.0/v1.1 | Clean-abstract similarity none/v1.0/v1.1 |
|---|---|---|---|---|---|
| deepseek-v4.1-flash-1017 | -2% | -18% | -19% | 12/0/1 | 0.98/0.93/0.97 |
| gemini-4-neon | -18% | -33% | -32% | 2/2/1 | 1.00/1.00/1.00 |
| gpt-6.1-terra | -29% | -33% | -36% | 5/2/0 | 0.93/0.95/0.96 |
| gpt-6.2-astra | -19% | -25% | -32% | 0/2/0 | 0.78/0.80/0.80 |
| gpt-6.2-sol | -22% | -31% | -31% | 1/0/0 | 0.77/0.80/0.79 |
| qwen3.8-27b | +10% | -30% | -30% | 15/5/2 | 0.91/1.00/0.97 |
| qwen4-max | +82% | -22% | -26% | 6/0/0 | 0.84/0.88/0.88 |
| grok-4.7 | 0% | -40% | -29% | 4/2/0 | 0.85/1.00/0.98 |

The GPT-6.2 models rewrote the clean abstract (similarity about 0.8) with or without the skill, so the skill does not fully stop over-editing in those models.

## Limits

- **One run per cell:** a one- or two-assertion difference for a single model is within noise. The totals and the per-case patterns are the more reliable signal.
- **The skill author wrote the assertions,** and one judge (Claude) is from the same family as the model that helped write the skill. The script-graded checks alone show the same ordering (313/360, 339/360, 350/360: 87% → 94% → 97%).
- **Cost:** $18.58 in total ($15.42 for runs, $3.16 for judging).
