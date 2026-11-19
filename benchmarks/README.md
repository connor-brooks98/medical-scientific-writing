# Benchmarks

Every run behind the numbers in the top-level README.

| Folder | Skill version | Model | Runs |
|---|---|---|---|
| `iteration-1/` | v0.9 (first draft) | Claude Opus 5.5 | 3 cases × (with skill, without skill) |
| `iteration-2/` | v1.0 | Claude Opus 5.5 | 3 cases × (with skill, without skill) |
| `iteration-2-haiku/` | v1.0 | Claude Haiku 5.5 | 3 cases × (with skill, without skill) |

Each run folder holds:
- `outputs/`: the file the task asked for, plus `response.md`, the model's full reply to the user.
- `grading.json`: each assertion with pass/fail and evidence.
- `timing.json`: tokens and wall-clock time.

`benchmark.json` and `benchmark.md` aggregate each round. `manual.json` holds the verdicts for assertions that need reading rather than a regex, with the quoted evidence. `metrics.txt` holds the pattern counts and word counts for every output and for the AI-styled inputs.

Each run was a fresh agent session given the same user prompt. "With skill" runs were told to read `SKILL.md` first; "without skill" runs were told not to use any skill. Runs could use web and PubMed tools. Several of them checked the cohort case's supplied references, and every one found that one of them doesn't support the claim the prompt makes about it.

## Reproduce the grading

```bash
python3 benchmarks/tools/grade.py benchmarks/iteration-2      # writes grading.json per run
python3 benchmarks/tools/metrics.py benchmarks/iteration-1 benchmarks/iteration-2 benchmarks/iteration-2-haiku
```

## Rerun the test cases

With Claude Code (billed model runs):

```bash
cd skills/medical-scientific-writing
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

## Limitations

- **Small sample:** three cases, one run per configuration per round.
- **Same author:** the assertions and the pattern lexicon were written by the skill's author.
- **Near ceiling:** for a strong model, the assertions mostly pass with or without the skill.
- **No human rating:** no blinded human rating has been done.

Additional cases are welcome, especially real (de-identified) AI-assisted drafts, as are blinded editor ratings.
