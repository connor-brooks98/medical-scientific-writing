#!/usr/bin/env python3
"""Programmatic grading for iteration runs. Manual verdicts come from manual.json.

Usage: python3 grade.py <iteration_dir>
manual.json (in the iteration dir): {"<case>/<config>": {"<assertion prefix>": [passed_bool, "evidence"]}}
"""
import json, os, re, sys, glob

EVALS = "/home/claude/medical-scientific-writing/evals"
NUM = re.compile(r"(?<![A-Za-z])\d+(?:[.,]\d+)*")


def nums(t):
    out = set()
    for m in NUM.finditer(t):
        tok = m.group(0).rstrip(".,")
        if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", tok):
            tok = tok.replace(",", "")
        for x in tok.split(","):
            if x:
                out.add(x)
    return out


def words(t):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-.,%]*", t))


def read(p):
    return open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""


def absent(text, phrases):
    hits = [p for p in phrases if p.lower() in text.lower()]
    return (not hits, f"found: {hits}" if hits else "none of the phrases found")


def grade_case1(out):
    t = read(os.path.join(out, "revised_discussion.md"))
    src = read(f"{EVALS}/revise-case-report-discussion/files/case_report_draft.md")
    r = {}
    n = t.count("—")
    r["01"] = (n == 0, f"{n} em dashes")
    extra = sorted(nums(t) - nums(src))
    r["02"] = (not extra, f"numbers not in draft: {extra}")
    fda = "FDA" in t or "Food and Drug Administration" in t
    ok = "[5]" in t and re.search(r"\b3\b|three", t) is not None and fda
    r["03"] = (ok, f"[5] present: {'[5]' in t}; FDA present: {fda}")
    m = re.search(r"[^.]*three-fold[^.]*\.?", t, re.I)
    r["04"] = (None, f"three-fold sentence: {m.group(0).strip() if m else 'removed'}")
    r["05"] = (None, f"ileus mentioned: {'ileus' in t.lower()}; opioid mentioned: {'opioid' in t.lower()}")
    r["06"] = absent(t, ["highlights the importance", "valuable reminder", "further research is needed",
                         "high index of suspicion", "evolving landscape", "revolutionized"])
    r["07"] = (None, f"'demonstrat' occurrences: {[s.strip() for s in re.findall(r'[^.]*demonstrat[^.]*', t, re.I)]}")
    return r


def grade_case2(out):
    t = read(os.path.join(out, "draft_sections.md"))
    r = {}
    need = ["1.48", "1.12", "1.96", "1.03", "0.88", "1.21", "1.06", "0.94", "1.20", "1.81", "1.24", "2.64", "0.81", "1.80", "0.14"]
    miss = [x for x in need if x not in t and not (x.startswith("0.") and re.search(r"(?<![0-9])"+re.escape(x[1:]), t))]
    r["01"] = (not miss, f"missing: {miss}" if miss else "all 15 values present")
    r["02"] = (None, "manual")
    causal = re.findall(r"[^.]*\bPPIs?\b[^.]*\b(?:increase[sd]?|cause[sd]?|raise[sd]?|leads? to|elevate[sd]?)\b[^.]*", t)
    r["03"] = (None, f"sentences with PPI + causal verb: {[c.strip()[:160] for c in causal]}")
    names = set(re.findall(r"\b([A-Z][a-z]+) et al", t))
    other = sorted(n for n in names if n not in {"Kwok", "Freedberg"})
    years = sorted(set(re.findall(r"\b(?:19|20)\d{2}\b", t)) - {"2012", "2015", "2016", "2023"})
    r["04"] = (not other and not years, f"other 'et al' names: {other}; other years: {years}")
    low = t.lower()
    checks = {"admission-only exposure": "admission" in low,
              "within-system ascertainment": ("within" in low and "system" in low) or "outside" in low,
              "single system": "single" in low or "1 academic" in low or "one academic" in low,
              "312 excluded": "312" in t}
    r["05"] = (all(checks.values()), str(checks))
    r["06"] = (None, "manual")
    n = t.count("—")
    ok, ev = absent(t, ["further research", "more research is needed", "highlights the importance", "underscore", "pave the way"])
    r["07"] = (ok and n == 0, f"{n} em dashes; {ev}")
    prompt = read(f"{EVALS}/draft-cohort-results-discussion/prompt.md")
    extra = sorted(nums(t) - nums(prompt))
    r["08"] = (None, f"numbers not in prompt (check derivations): {extra}")
    return r


def grade_case3(out):
    t = read(os.path.join(out, "intro_revised.txt"))
    src = read(f"{EVALS}/revise-intro-no-citations/files/intro_draft.txt")
    r = {}
    n = t.count("—")
    r["01"] = (n == 0, f"{n} em dashes")
    etal = re.findall(r"et al", t)
    yrs = re.findall(r"\b(?:19|20)\d{2}\b", t)
    numcites = re.findall(r"\[\d+(?:[-,]\d+)*\]", t)
    r["02"] = (not etal and not yrs and not numcites, f"et al: {len(etal)}, years: {yrs}, numbered cites: {numcites} (check named studies manually)")
    ph = re.findall(r"\[(?:[^\]]*(?:CITATION|REF|DATA)[^\]]*|R\d+)\]", t, re.I)
    r["03"] = (len(ph) >= 2, f"{len(ph)} placeholders")
    extra = sorted(nums(re.sub(r"\[[^\]]*\]", "", t)) - nums(src))
    r["04"] = (not extra, f"numbers not in draft (outside brackets): {extra}")
    low = t.lower()
    checks = {"prospective": "prospective" in low, "75": "75" in t, "smartwatch": "smartwatch" in low,
              "14-day": "14-day" in low or "14 day" in low, "patch": "patch" in low}
    r["05"] = (all(checks.values()), str(checks))
    ok, ev = absent(t, ["millions of individuals", "in recent years"])
    first = re.split(r"(?<=[.!?])\s", t.replace("Introduction", "", 1).strip(), maxsplit=1)[0]
    r["06"] = (ok, f"{ev}; first sentence: {first[:200]}")
    r["07"] = absent(t, ["promising", "transform", "landscape", "fills an important gap", "pave the way", "critical gap", "comprehensive"])
    paras = [p for p in re.split(r"\n\s*\n", t.strip()) if p.strip() and p.strip().lower() != "introduction"]
    tw = words(re.sub(r"\[[^\]]*\]", "", t))
    r["08"] = (tw < words(src) and len(paras) <= 3, f"words excluding [placeholders] {tw} vs {words(src)}; paragraphs {len(paras)}")
    return r


GRADERS = {"revise-case-report-discussion": grade_case1,
           "draft-cohort-results-discussion": grade_case2,
           "revise-intro-no-citations": grade_case3}


def main(it):
    manual_path = os.path.join(it, "manual.json")
    manual = json.load(open(manual_path)) if os.path.exists(manual_path) else {}
    for case, fn in GRADERS.items():
        meta = json.load(open(os.path.join(it, case, "eval_metadata.json")))
        texts = meta["assertions"]
        for cfg in ("with_skill", "without_skill", "old_skill"):
            run = os.path.join(it, case, cfg)
            if not os.path.isdir(run):
                continue
            res = fn(os.path.join(run, "outputs"))
            man = manual.get(f"{case}/{cfg}", {})
            exps = []
            keys = sorted(res)
            for k, text in zip(keys, texts):
                passed, ev = res[k]
                if k in man:
                    passed, mev = man[k]
                    ev = f"{mev} | auto: {ev}"
                exps.append({"text": text, "passed": bool(passed) if passed is not None else False,
                             "evidence": ev if passed is not None else f"UNGRADED (manual needed): {ev}"})
            p = sum(e["passed"] for e in exps)
            g = {"expectations": exps, "summary": {"passed": p, "failed": len(exps) - p, "total": len(exps),
                                                   "pass_rate": round(p / len(exps), 2)}}
            json.dump(g, open(os.path.join(run, "grading.json"), "w"), indent=2)
            print(f"{case}/{cfg}: {p}/{len(exps)}")
            for e in exps:
                print(f"   [{'PASS' if e['passed'] else 'FAIL'}] {e['text'][:70]} :: {e['evidence'][:220]}")


if __name__ == "__main__":
    main(sys.argv[1])
