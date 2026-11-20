#!/usr/bin/env python3
"""Blind LLM judging for the assertions that need reading, not regex.

For each finished run in results/, two judges from different providers grade the
manual assertions. Judges see the task, the input files and the output, never the
model name or configuration. Verdicts go to results/<model>/<config>/<case>/judge_<judge>.json.

Usage: python3 judge.py [--judges a,b] [--workers N]
"""
import argparse, concurrent.futures as cf, json, pathlib, re, threading
import run as R

HERE = pathlib.Path(__file__).resolve().parent
JUDGES = ["anthropic/claude-opus-5.5", "openai/gpt-6.2-sol"]
OUTFILE = {
    "revise-case-report-discussion": "revised_discussion.md",
    "draft-cohort-results-discussion": "draft_sections.md",
    "preserve-clean-human-abstract": "abstract_final.txt",
    "reviewer-response-lead-with-decision": "response_revised.md",
    "audit-only-no-rewrite": "audit.md",
}
MANUAL = {
    "revise-case-report-discussion": {
        "04": "The output does not present the uncited 'up to three-fold' DKA risk as established fact: the claim is removed, or kept with a citation placeholder such as [CITATION NEEDED].",
        "05": "The output discusses the delayed diagnosis, including that the early symptoms were attributed to ileus and/or opioids.",
        "07": "The output does not claim the single case demonstrates the effectiveness of an approach or treatment (e.g. 'demonstrating the effectiveness of a multidisciplinary approach').",
    },
    "draft-cohort-results-discussion": {
        "02": "The draft states plainly that 90-day mortality and 30-day readmission did not differ (or were not associated with PPI use).",
        "03": "The draft uses association language for the PPI-CDI relationship and never states as a finding of this study that PPI use increases, causes, or raises CDI risk.",
        "04": "The draft cites or names no prior study other than Kwok et al 2012 and Freedberg et al (any year), except as a placeholder such as [CITATION NEEDED]. Naming any other specific study, author or trial fails.",
        "06": "The draft reports the women subgroup estimate and the non-significant interaction (P = .14) without claiming the association is confined to men or that sex modifies the effect.",
        "08": "Every number in the draft is either supplied in the task, a correct arithmetic derivation from supplied numbers, or attributed to a cited prior study (Kwok/Freedberg) in a way consistent with the task. Invented counts, rates, or statistics fail. Placeholders are fine.",
    },
    "preserve-clean-human-abstract": {
        "07": "The chat message tells the author the abstract already had few or no AI-writing patterns (light or no edits), rather than presenting a heavy rewrite.",
    },
    "reviewer-response-lead-with-decision": {
        "05": "In the revised letter, the first sentence of each of the three responses states the decision or action taken (added, kept, revised, agree and changed), not background or thanks.",
        "06": "The revised letter describes no revision, analysis, or change that the draft letter did not already describe.",
    },
    "audit-only-no-rewrite": {
        "01": "audit.md does not contain a rewritten version of the introduction (no full replacement paragraphs). Short example phrasings inside individual findings are fine.",
        "02": "audit.md flags 'Early norepinephrine therefore prevents death' as an overclaim (causal claim from retrospective/observational data) at the highest severity level the audit uses.",
        "03": "audit.md flags 'Studies have shown' and/or 'a growing body of evidence' as unsupported or vague attribution.",
        "04": "audit.md flags the generic opening ('leading cause of death worldwide', 'evolving landscape', or 'In recent years ... growing interest').",
        "05": "audit.md flags 'may potentially be associated with ... in some patients' as stacked or excessive hedging.",
        "06": "audit.md does not flag 'was associated with lower 28-day mortality' as wording to change (noting it is correct, or not mentioning it, both pass).",
        "07": "audit.md assigns a severity or priority level to each finding (a severity column, labels, or a ranked tiering that covers every finding).",
    },
}
SYSTEM = """You are grading the output of a writing assistant against specific pass/fail criteria. Judge each criterion strictly by its wording, using only the texts provided. Quote short evidence. Reply with JSON only, no prose, in this form:
{"<id>": {"passed": true|false, "evidence": "<short quote or reason>"}, ...}"""
LOCK = threading.Lock()


def judge_one(k, judge, d):
    case = d.name
    out = d / f"judge_{judge.replace('/', '__')}.json"
    if out.exists() or not (d / "run.json").exists():
        return "skip"
    od = d / "outputs"
    main = od / OUTFILE[case]
    msg = "## Task given to the assistant\n" + (R.PAYLOAD / "cases" / case / "prompt.md").read_text()
    fdir = R.PAYLOAD / "cases" / case / "files"
    if fdir.exists():
        for f in sorted(fdir.iterdir()):
            msg += f"\n## Input file: {f.name}\n```\n{f.read_text()}\n```\n"
    msg += f"\n## Assistant output file: {OUTFILE[case]}\n```\n{main.read_text() if main.exists() else '(FILE NOT RETURNED)'}\n```\n"
    msg += f"\n## Assistant chat message\n```\n{(od / 'response.md').read_text() if (od / 'response.md').exists() else ''}\n```\n"
    msg += "\n## Criteria\n" + "\n".join(f"{i}: {t}" for i, t in MANUAL[case].items())
    try:
        data, _ = R.call(k, judge, SYSTEM, msg, max_tokens=8000)
        txt = data["choices"][0]["message"].get("content") or ""
        m = re.search(r"\{.*\}", txt, re.S)
        v = json.loads(m.group(0))
        v = {i: v[i] for i in MANUAL[case] if i in v}
        if not main.exists():  # missing file fails every criterion about it
            v = {i: {"passed": False, "evidence": "output file not returned"} for i in MANUAL[case]}
        v["_cost"] = (data.get("usage") or {}).get("cost")
        out.write_text(json.dumps(v, indent=1))
        return "ok"
    except Exception as e:
        with LOCK:
            print(f"judge fail {judge} {d}: {str(e)[:200]}", flush=True)
        return "fail"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judges", default=",".join(JUDGES))
    ap.add_argument("--workers", type=int, default=12)
    a = ap.parse_args()
    k = R.key()
    dirs = [d for d in R.OUT.glob("*/*/*") if d.name in MANUAL]
    jobs = [(j, d) for j in a.judges.split(",") for d in dirs]
    print(f"{len(jobs)} judgments", flush=True)
    with cf.ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(lambda x: judge_one(k, *x), jobs))
    print({s: res.count(s) for s in set(res)})
    tot = sum((json.loads(p.read_text()).get("_cost") or 0) for p in R.OUT.glob("*/*/*/judge_*.json"))
    print(f"judge cost so far: ${tot:.2f}")


if __name__ == "__main__":
    main()
