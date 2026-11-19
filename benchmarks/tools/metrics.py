#!/usr/bin/env python3
"""Objective pattern metrics for benchmark outputs, using the skill's own checker lexicon.

Usage: python3 metrics.py <iteration_dir> [<iteration_dir> ...]  -> prints JSON + markdown table
"""
import importlib.util, json, os, re, sys

spec = importlib.util.spec_from_file_location("cp", os.path.join(os.path.dirname(__file__), "../../skills/medical-scientific-writing/scripts/check_patterns.py"))
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

EVALS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../skills/medical-scientific-writing/evals")
CASES = {
    "revise-case-report-discussion": ("revised_discussion.md", f"{EVALS}/revise-case-report-discussion/files/case_report_draft.md"),
    "draft-cohort-results-discussion": ("draft_sections.md", f"{EVALS}/draft-cohort-results-discussion/prompt.md"),
    "revise-intro-no-citations": ("intro_revised.txt", f"{EVALS}/revise-intro-no-citations/files/intro_draft.txt"),
}


def prose_only(text):
    """Drop reference lists, author-query/assumption sections, and author-note blocks."""
    text = re.split(r"\n#+\s*(?:References|Placeholders|Author queries|Assumptions|Candidates)\b", text, flags=re.I)[0]
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith(">"))
    return text


def measure(text, source):
    bare = cp.PLACEHOLDER.sub("", text)
    paras = cp.paragraphs(bare)
    sents = [s for p in paras for s in cp.sentences(p)]
    words = sum(cp.word_count(s) for s in sents)
    hits = {}
    for regex, pid, label in cp.CANDIDATES:
        n = len(re.findall(regex, bare, re.I | re.M))
        if n:
            hits[pid] = hits.get(pid, 0) + n
    discourse = sum(v for k, v in hits.items() if k.startswith("D") or k == "STAT")
    uniform = 0
    for p in paras:
        c = [cp.word_count(s) for s in cp.sentences(p)]
        if len(c) >= 3 and max(c) - min(c) <= 5:
            uniform += 1
    sents_full = [s for p in cp.paragraphs(text) for s in cp.sentences(p)]
    vague = sum(1 for s in sents_full if cp.VAGUE_ATTRIBUTION.search(s) and not cp.CITATION.search(s))
    added = sorted(set(cp.numbers(bare)) - set(cp.numbers(source))) if source is not None else []
    return {
        "words": words,
        "pattern_hits": sum(hits.values()),
        "discourse_hits": discourse,
        "em_dashes": text.count("—"),
        "uniform_paragraphs": uniform,
        "uncited_attributions": vague,
        "placeholders": len(re.findall(r"\[(?:[^\]]*(?:DATA NEEDED|CITATION|REF|AUTHOR|PLACEHOLDER|UNVERIFIED|VERIFY)[^\]]*|R\d+)\]", text, re.I)),
        "numbers_not_in_source": len(added),
        "by_pattern": hits,
    }


def discussion_of(draft):
    return draft.split("## Discussion", 1)[1] if "## Discussion" in draft else draft


def main(iters):
    rows = []
    # "Before" rows: the AI-styled inputs themselves
    cr = open(CASES["revise-case-report-discussion"][1]).read()
    rows.append(("revise-case-report-discussion", "input (AI draft)", measure(discussion_of(cr), cr)))
    intro = open(CASES["revise-intro-no-citations"][1]).read()
    rows.append(("revise-intro-no-citations", "input (AI draft)", measure(intro, intro)))
    for it in iters:
        tag = os.path.basename(it.rstrip("/"))
        for case, (fname, src) in CASES.items():
            source = open(src).read()
            for cfg in ("with_skill", "without_skill"):
                p = os.path.join(it, case, cfg, "outputs", fname)
                if os.path.exists(p):
                    rows.append((case, f"{tag}/{cfg}", measure(prose_only(open(p).read()), source)))
    print(json.dumps([{"case": c, "run": r, **m} for c, r, m in rows], indent=1))
    print("\n| Case | Run | Words | AI-pattern hits | Discourse-level hits | Em dashes | Uniform paragraphs | Uncited attributions | Placeholders |")
    print("|---|---|---|---|---|---|---|---|---|")
    for c, r, m in rows:
        print(f"| {c} | {r} | {m['words']} | {m['pattern_hits']} | {m['discourse_hits']} | {m['em_dashes']} | {m['uniform_paragraphs']} | {m['uncited_attributions']} | {m['placeholders']} |")


if __name__ == "__main__":
    main(sys.argv[1:])
