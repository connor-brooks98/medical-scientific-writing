#!/usr/bin/env python3
"""Over-editing and pattern metrics for revision cases.

Usage: python3 metrics3.py <iteration_dir> [...]  -> markdown table + JSON (metrics3.json in each iteration dir)
"""
import difflib, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EVALS = os.environ.get("EVALS", "/home/claude/repo/medical-scientific-writing/skills/medical-scientific-writing/evals")
CHECKER = os.environ.get("CHECKER", "/home/claude/repo/medical-scientific-writing/skills/medical-scientific-writing/scripts/check_patterns.py")
spec = importlib.util.spec_from_file_location("cp", CHECKER)
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

# case -> (output file, input file, how to slice the input)
CASES = {
    "revise-case-report-discussion": ("revised_discussion.md", "case_report_draft.md", "discussion"),
    "revise-intro-no-citations": ("intro_revised.txt", "intro_draft.txt", None),
    "preserve-clean-human-abstract": ("abstract_final.txt", "abstract.txt", None),
    "revise-discussion-staging-strawman": ("discussion_revised.md", "discussion.md", None),
    "revise-latex-file-mode": ("results.tex", "results.tex", None),
    "reviewer-response-lead-with-decision": ("response_revised.md", "response_draft.md", None),
    "author-sample-voice": ("new_paragraph_revised.txt", "new_paragraph.txt", None),
}
PH = re.compile(r"\[(?:[^\]]*(?:DATA NEEDED|CITATION|REF|AUTHOR|PLACEHOLDER|UNVERIFIED|VERIFY)[^\]]*|R\d+)\]", re.I)


def read(p):
    return open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else None


def prose(t):
    t = PH.sub("", t)
    t = re.sub(r"\\(?:label|ref|cite)\{[^}]*\}", "", t)
    t = re.sub(r"\\begin\{equation\}.*?\\end\{equation\}", "", t, flags=re.S)
    return t


def nwords(t):
    return sum(cp.word_count(s) for p in cp.paragraphs(t) for s in cp.sentences(p))


def hits(t):
    n = 0
    for regex, pid, label in cp.CANDIDATES:
        n += len(re.findall(regex, t, re.I | re.M))
    return n


def measure(out_text, in_text):
    po, pi = prose(out_text), prose(in_text)
    return {
        "words_in": nwords(pi),
        "words_out": nwords(po),
        "length_change_pct": round(100 * (nwords(po) - nwords(pi)) / max(1, nwords(pi))),
        "similarity": round(difflib.SequenceMatcher(None, in_text.strip(), out_text.strip(), autojunk=False).ratio(), 3),
        "pattern_hits_in": hits(pi),
        "pattern_hits_out": hits(po),
        "em_dashes_out": out_text.count("\u2014"),
        "placeholders_out": len(PH.findall(out_text)),
        "numbers_lost": sorted(set(cp.numbers(pi)) - set(cp.numbers(po))),
    }


def main(iters):
    rows = []
    for it in iters:
        tag = os.path.basename(it.rstrip("/"))
        res = {}
        for case, (fo, fi, sl) in CASES.items():
            src = read(f"{EVALS}/{case}/files/{fi}")
            if src is None:
                continue
            if sl == "discussion":
                src = "## Discussion" + src.split("## Discussion", 1)[1]
            for cfg in ("with_skill", "without_skill"):
                out = read(os.path.join(it, case, cfg, "outputs", fo))
                if out is None:
                    continue
                m = measure(out, src)
                res[f"{case}/{cfg}"] = m
                rows.append((tag, case, cfg, m))
        json.dump(res, open(os.path.join(it, "metrics3.json"), "w"), indent=1)
    print("| Round | Case | Config | Words in → out | Length change | Similarity to input | Pattern hits in → out | Placeholders | Numbers lost |")
    print("|---|---|---|---|---|---|---|---|---|")
    for tag, case, cfg, m in rows:
        print(f"| {tag} | {case} | {cfg} | {m['words_in']} → {m['words_out']} | {m['length_change_pct']:+d}% | {m['similarity']:.2f} | {m['pattern_hits_in']} → {m['pattern_hits_out']} | {m['placeholders_out']} | {len(m['numbers_lost'])} |")


if __name__ == "__main__":
    main(sys.argv[1:])
