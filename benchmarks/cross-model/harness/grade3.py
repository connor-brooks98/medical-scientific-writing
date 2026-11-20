#!/usr/bin/env python3
"""Programmatic grading for all 9 cases (iteration 3+). Manual verdicts come from manual.json.

Usage: python3 grade3.py <iteration_dir>
manual.json: {"<case>/<config>": {"<NN>": [passed_bool, "evidence"]}}
"""
import collections, difflib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import grade as g1  # cases 1-3 and helpers (nums, words, read, absent)

EVALS = os.environ.get("EVALS", "/home/claude/repo/medical-scientific-writing/skills/medical-scientific-writing/evals")
g1.EVALS = EVALS
nums, words, read, absent = g1.nums, g1.words, g1.read, g1.absent


def src(case, name):
    return read(f"{EVALS}/{case}/files/{name}")


def sim(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def num_equal(out, orig):
    lost = sorted(nums(orig) - nums(out))
    added = sorted(nums(out) - nums(orig))
    return (not lost and not added), f"lost {lost}; added {added}"


def grade_clean_abstract(out):
    t = read(os.path.join(out, "abstract_final.txt"))
    o = src("preserve-clean-human-abstract", "abstract.txt")
    r = {}
    s = sim(o.strip(), t.strip())
    r["01"] = (s >= 0.85, f"similarity {s:.3f}")
    wo, wt = words(o), words(t)
    r["02"] = (abs(wt - wo) <= 0.10 * wo, f"words {wt} vs {wo}")
    r["03"] = num_equal(t, o)
    co, ct = o.lower().count("associated with"), t.lower().count("associated with")
    r["04"] = (ct >= co, f"'associated with' {ct} vs {co}")
    rng = ["1.08–1.54", "0.86–1.33", "0.98–1.42"]
    miss = [x for x in rng if x not in t]
    r["05"] = (not miss, f"missing {miss}" if miss else "all three present")
    ph = re.findall(r"\[(?:CITATION|DATA|REF)[^\]]*\]", t, re.I)
    r["06"] = (not ph, f"{len(ph)} placeholders")
    r["07"] = (None, "manual: response says abstract was largely clean")
    return r


def grade_staging(out):
    t = read(os.path.join(out, "discussion_revised.md"))
    o = src("revise-discussion-staging-strawman", "discussion.md")
    low = t.lower()
    r = {}
    r["01"] = absent(t, ["at its core", "central question", "currency of", "the key point is"])
    r["02"] = absent(t, ["this is not to say", "one might argue"])
    m = re.search(r"does not mean[^.]*\.\s+It means", t)
    r["03"] = (m is None, f"found: {m.group(0)[:80]}" if m else "absent")
    closers = re.findall(r"(?:^|[.!?]\s+)Overall,", t) + re.findall(r"This illustrates", t)
    r["04"] = (not closers, f"found {closers}" if closers else "absent")
    bad = [p for p in ["likely nonambulatory", "suggesting that these patients"] if p in low]
    r["05"] = (not bad, f"found {bad}" if bad else "no inference about missing ambulatory status")
    r["06"] = absent(t, ["table below compares"])
    r["07"] = num_equal(t, o)
    sent = [s for s in re.split(r"(?<=[.!?])\s+", t) if "mortality" in s.lower()]
    assoc = any("associated with" in s.lower() for s in sent)
    causal = [s[:120] for s in sent if re.search(r"\b(reduced|lowered|prevented|decreased)\b[^.]*mortality", s, re.I)]
    r["08"] = (assoc and not causal, f"assoc={assoc}; causal={causal}")
    return r


def latex_cmds(t):
    return collections.Counter(re.findall(r"\\(?:label|ref|cite)\{[^}]*\}", t))


def grade_latex(out):
    t = read(os.path.join(out, "results.tex"))
    o = src("revise-latex-file-mode", "results.tex")
    r = {}
    lo, lt = latex_cmds(o), latex_cmds(t)
    r["01"] = (lo == lt, f"missing {dict(lo - lt)}; extra {dict(lt - lo)}")
    eq = re.search(r"\\begin\{equation\}.*?\\end\{equation\}", o, re.S).group(0)
    r["02"] = (eq in t, "equation byte-identical" if eq in t else "equation changed")
    rng = ["0.56--0.86", "0.70--1.21"]
    miss = [x for x in rng if x not in t]
    r["03"] = (not miss, f"missing {miss}" if miss else "ranges kept")
    spaced = re.findall(r"\s---?\s", t)
    r["04"] = (not spaced, f"{len(spaced)} spaced dashes")
    r["05"] = absent(t, ["It is important to note", "highlighting", "underscoring", "remarkably", "crucial", "serves as a testament", "Furthermore"])
    lost = sorted(nums(o) - nums(t))
    r["06"] = (not lost, f"lost {lost}")
    bal = t.count("{") == t.count("}")
    be = collections.Counter(re.findall(r"\\(begin|end)\{(\w+)\}", t)) == collections.Counter(re.findall(r"\\(begin|end)\{(\w+)\}", o))
    r["07"] = (bal and be, f"braces balanced={bal}; begin/end same={be}")
    return r


def norm_dash(s):
    return s.replace("–", "-").replace("—", "-")


def grade_reviewer(out):
    t = read(os.path.join(out, "response_revised.md"))
    o = src("reviewer-response-lead-with-decision", "response_draft.md")
    r = {}
    wo, wt = words(o), words(t)
    r["01"] = (wt <= 0.75 * wo, f"words {wt} vs {wo} ({(1 - wt / wo) * 100:.0f}% shorter)")
    refs = ["182-184", "121-125", "301-306", "322-325", "Figure 1"]
    nt = norm_dash(t)
    miss = [x for x in refs if x not in nt]
    r["02"] = (not miss, f"missing {miss}" if miss else "all refs kept")
    need = ["14", "4.1", "17", "5.0"]
    missn = [x for x in need if x not in nums(t)]
    r["03"] = (not missn, f"missing {missn}" if missn else "kept")
    r["04"] = absent(t, ["insightful", "thought-provoking", "excellent", "sincerely thank", "grateful"])
    r["05"] = (None, "manual: first sentence of each response")
    r["06"] = (None, "manual: no invented changes")
    return r


def grade_voice(out):
    t = read(os.path.join(out, "new_paragraph_revised.txt"))
    o = src("author-sample-voice", "new_paragraph.txt")
    r = {}
    n = t.count("—")
    r["01"] = (n >= 1, f"{n} em dashes")
    r["02"] = absent(t, ["Notably", "highlight", "crucial", "underscoring", "pivotal", "paradigm shift", "testament", "Furthermore", "Interestingly"])
    r["03"] = num_equal(t, o)
    r["04"] = absent(t, ["not only"])
    hedged = re.search(r"may have reduced|might have reduced|could have reduced|appeared to reduce", t, re.I)
    r["05"] = (hedged is None, f"hedged: {hedged.group(0)}" if hedged else "primary result not over-hedged")
    return r


def grade_audit(out):
    t = read(os.path.join(out, "audit.md"))
    r = {k: (None, "manual") for k in ["01", "02", "03", "04", "05", "06", "07"]}
    r["02"] = (None, f"manual; 'prevents death' mentioned: {'prevents death' in t}")
    return r


GRADERS = {
    "revise-case-report-discussion": g1.grade_case1,
    "draft-cohort-results-discussion": g1.grade_case2,
    "revise-intro-no-citations": g1.grade_case3,
    "preserve-clean-human-abstract": grade_clean_abstract,
    "revise-discussion-staging-strawman": grade_staging,
    "revise-latex-file-mode": grade_latex,
    "reviewer-response-lead-with-decision": grade_reviewer,
    "author-sample-voice": grade_voice,
    "audit-only-no-rewrite": grade_audit,
}


def main(it):
    mp = os.path.join(it, "manual.json")
    manual = json.load(open(mp)) if os.path.exists(mp) else {}
    for case, fn in GRADERS.items():
        mpath = os.path.join(it, case, "eval_metadata.json")
        if not os.path.exists(mpath):
            continue
        texts = json.load(open(mpath))["assertions"]
        for cfg in ("with_skill", "without_skill", "old_skill"):
            run = os.path.join(it, case, cfg)
            if not os.path.isdir(os.path.join(run, "outputs")):
                continue
            res = fn(os.path.join(run, "outputs"))
            man = manual.get(f"{case}/{cfg}", {})
            exps = []
            for k, text in zip(sorted(res), texts):
                passed, ev = res[k]
                if k in man:
                    passed, mev = man[k]
                    ev = f"{mev} | auto: {ev}"
                exps.append({"text": text, "passed": bool(passed) if passed is not None else False,
                             "evidence": ev if passed is not None else f"UNGRADED (manual needed): {ev}"})
            p = sum(e["passed"] for e in exps)
            json.dump({"expectations": exps, "summary": {"passed": p, "failed": len(exps) - p, "total": len(exps),
                       "pass_rate": round(p / len(exps), 2)}}, open(os.path.join(run, "grading.json"), "w"), indent=2)
            print(f"{case}/{cfg}: {p}/{len(exps)}")
            for e in exps:
                if not e["passed"]:
                    print(f"   [FAIL] {e['text'][:70]} :: {e['evidence'][:240]}")


if __name__ == "__main__":
    main(sys.argv[1])
