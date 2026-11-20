#!/usr/bin/env python3
"""Grade the OpenRouter cross-model benchmark.

Usage: python3 analyze_or.py <results_dir> <out_dir>
  results_dir: or-bench/results from the Mac (results/<model>/<none|v1.0|v1.1>/<case>/...)
  out_dir:     per-model iteration dirs in the grade3 layout + summary.json + summary.md
A manual assertion passes only when both judges pass it.
"""
import contextlib, io, json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import grade3, metrics3

CFG = {"none": "without_skill", "v1.0": "old_skill", "v1.1": "with_skill"}
META = os.path.join(HERE, "iteration-3")


def main(res, out):
    os.makedirs(out, exist_ok=True)
    summary = {}
    agree = [0, 0]
    for model in sorted(m for m in os.listdir(res) if not m.startswith(".")):
        mdir = os.path.join(res, model)
        it = os.path.join(out, model)
        manual = {}
        for cfg, name in CFG.items():
            for case in sorted(c for c in os.listdir(os.path.join(mdir, cfg)) if not c.endswith('.attempt1')) if os.path.isdir(os.path.join(mdir, cfg)) else []:
                src = os.path.join(mdir, cfg, case)
                dst = os.path.join(it, case, name)
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                os.makedirs(dst)
                if os.path.isdir(os.path.join(src, "outputs")):
                    shutil.copytree(os.path.join(src, "outputs"), os.path.join(dst, "outputs"))
                for f in ("run.json", "error.txt"):
                    if os.path.exists(os.path.join(src, f)):
                        shutil.copy(os.path.join(src, f), dst)
                shutil.copy(os.path.join(META, case, "eval_metadata.json"), os.path.join(it, case))
                judges = [json.load(open(os.path.join(src, f))) for f in sorted(os.listdir(src)) if f.startswith("judge_")]
                if judges:
                    ent = {}
                    for k in judges[0]:
                        if k.startswith("_"):
                            continue
                        vs = [j.get(k, {}).get("passed") is True for j in judges]
                        if len(vs) == 2:
                            agree[0] += vs[0] == vs[1]
                            agree[1] += 1
                        ent[k] = [all(vs), " / ".join(f"{'P' if v else 'F'}: {j.get(k, {}).get('evidence', '')[:120]}" for v, j in zip(vs, judges))]
                    manual[f"{case}/{name}"] = ent
        json.dump(manual, open(os.path.join(it, "manual.json"), "w"), indent=1)
        with contextlib.redirect_stdout(io.StringIO()):
            grade3.main(it)
        # collect
        s = {}
        for case in sorted(os.listdir(it)):
            for name in CFG.values():
                d = os.path.join(it, case, name)
                if not os.path.isdir(d):
                    continue
                g = os.path.join(d, "grading.json")
                ent = {"passed": 0, "total": len(json.load(open(os.path.join(it, case, "eval_metadata.json")))["assertions"]), "failed": []}
                if os.path.exists(g):
                    gj = json.load(open(g))
                    ent["passed"] = gj["summary"]["passed"]
                    ent["failed"] = [e["text"][:90] + " :: " + e["evidence"][:160] for e in gj["expectations"] if not e["passed"]]
                else:
                    ent["failed"] = ["no output"]
                ent["retried"] = os.path.isdir(os.path.join(res, model, [k for k, v in CFG.items() if v == name][0], case + ".attempt1"))
                rj = os.path.join(d, "run.json")
                if os.path.exists(rj):
                    r = json.load(open(rj))
                    ent.update(cost=r.get("cost_usd"), seconds=r.get("seconds"), finish=r.get("finish_reason"), files=r.get("files_returned"))
                if case in metrics3.CASES:
                    fo, fi, sl = metrics3.CASES[case]
                    srct = metrics3.read(f"{metrics3.EVALS}/{case}/files/{fi}")
                    if sl == "discussion":
                        srct = "## Discussion" + srct.split("## Discussion", 1)[1]
                    o = metrics3.read(os.path.join(d, "outputs", fo))
                    if o:
                        ent["metrics"] = metrics3.measure(o, srct)
                s[f"{case}/{name}"] = ent
        summary[model] = s
    summary["_judge_agreement"] = {"agree": agree[0], "total": agree[1]}
    json.dump(summary, open(os.path.join(out, "summary.json"), "w"), indent=1)
    print(f"judge agreement {agree[0]}/{agree[1]}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
