#!/usr/bin/env python3
"""OpenRouter benchmark for the medical-scientific-writing skill.

Runs every case under payload/cases against each model in three configurations:
  none  - no skill
  v1.0  - skill v1.0.0 (SKILL.md + references) as the system prompt
  v1.1  - skill v1.1.0 (SKILL.md + references) as the system prompt

The API key is read from the OPENROUTER_API_KEY environment variable or from
~/.config/openrouter/api_key. It is never printed or written to disk.

Usage:
  python3 run.py                 # all models, all configs, all cases (skips finished runs)
  python3 run.py --smoke         # one cheap call to check the key and the protocol
  python3 run.py --models a,b    # subset
Stdlib only.
"""
import argparse, concurrent.futures as cf, json, os, pathlib, re, sys, threading, time, urllib.error, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
PAYLOAD = HERE / "payload"
OUT = HERE / "results"
MODELS = [
    "openai/gpt-6.2-sol",
    "openai/gpt-6.2-astra",
    "openai/gpt-6.1-terra",
    "google/gemini-4-neon",
    "x-ai/grok-4.7",
    "deepseek/deepseek-v4.1-flash-1017",
    "qwen/qwen3.8-27b",
    "qwen/qwen4-max",
]
CONFIGS = ["none", "v1.0", "v1.1"]
API = "https://openrouter.ai/api/v1/chat/completions"
LOCK = threading.Lock()

PROTOCOL = """
---
How to return your work (this environment has no file tools, so files are exchanged as text):

- The input files are attached below, each between <<<FILE: name>>> and <<<END FILE>>>.
- Return every file you create or edit the same way: a line <<<FILE: filename>>>, the complete file content, then a line <<<END FILE>>>. Always return the complete file, never a diff or an excerpt.
- Outside the file blocks, write the message you would send me in chat.
"""

SKILL_PREAMBLE = """You have the following skill installed. Follow it for this task.

Environment note: you cannot run scripts or open files in this environment. All of the skill's reference files are included below, so do not try to load them. Where the skill says to run scripts/check_patterns.py, do those checks yourself by reading the text. You also have no literature-search tool.

"""


def key():
    k = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not k:
        p = pathlib.Path.home() / ".config" / "openrouter" / "api_key"
        if p.exists():
            k = p.read_text().strip()
    if not k:
        sys.exit("No key: set OPENROUTER_API_KEY or create ~/.config/openrouter/api_key")
    return k


def skill_text(version):
    d = PAYLOAD / "skills" / version
    parts = [SKILL_PREAMBLE, "=== SKILL.md ===\n", (d / "SKILL.md").read_text()]
    for ref in sorted((d / "references").glob("*.md")):
        parts += [f"\n\n=== references/{ref.name} ===\n", ref.read_text()]
    return "".join(parts)


def user_text(case):
    d = PAYLOAD / "cases" / case
    msg = (d / "prompt.md").read_text().strip() + "\n" + PROTOCOL
    fdir = d / "files"
    if fdir.exists():
        for f in sorted(fdir.iterdir()):
            msg += f"\n<<<FILE: {f.name}>>>\n{f.read_text()}\n<<<END FILE>>>\n"
    return msg


# Lenient: accepts >>>END FILE<<<, <<<END_FILE>>>, or an unterminated last block.
BLOCK = re.compile(r"<<<\s*FILE:\s*([^>\n]+?)\s*>>>[ \t]*\n?(.*?)(?:\n?(?:<<<|>>>)\s*END[ _]FILE\s*(?:>>>|<<<)|(?=\n<<<\s*FILE:)|\Z)", re.S)
EXPECTED = {
    "revise-case-report-discussion": "revised_discussion.md", "draft-cohort-results-discussion": "draft_sections.md",
    "revise-intro-no-citations": "intro_revised.txt", "preserve-clean-human-abstract": "abstract_final.txt",
    "revise-discussion-staging-strawman": "discussion_revised.md", "revise-latex-file-mode": "results.tex",
    "reviewer-response-lead-with-decision": "response_revised.md", "author-sample-voice": "new_paragraph_revised.txt",
    "audit-only-no-rewrite": "audit.md",
}


def parse(text):
    files = {}
    for name, body in BLOCK.findall(text):
        name = os.path.basename(name.strip())
        if body.strip():
            files[name] = body.rstrip("\n") + "\n"
    response = BLOCK.sub(lambda m: f"[file returned: {os.path.basename(m.group(1).strip())}]", text).strip()
    return files, response


def call(k, model, system, user, max_tokens=24000, tries=4):
    msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = json.dumps({"model": model, "messages": msgs, "max_tokens": max_tokens, "usage": {"include": True}}).encode()
    last = None
    for i in range(tries):
        req = urllib.request.Request(API, data=body, headers={
            "Authorization": f"Bearer {k}", "Content-Type": "application/json",
            "X-Title": "medical-scientific-writing benchmark"})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                data = json.loads(r.read())
            if "choices" not in data:
                raise RuntimeError(json.dumps(data.get("error", data))[:400])
            return data, time.time() - t0
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read()[:400].decode(errors='replace')}"
            if e.code in (400, 401, 402, 403, 404):
                break
        except Exception as e:  # network, timeout, malformed
            last = f"{type(e).__name__}: {str(e)[:400]}"
        time.sleep(5 * 2 ** i)
    raise RuntimeError(last)


def slug(model):
    return model.replace("/", "__")


def run_one(k, model, cfg, case, systems):
    d = OUT / slug(model) / cfg / case
    if (d / "run.json").exists():
        return "skip"
    d.mkdir(parents=True, exist_ok=True)
    try:
        data, secs = call(k, model, systems[cfg], user_text(case))
    except Exception as e:
        (d / "error.txt").write_text(str(e))
        with LOCK:
            print(f"FAIL {model} {cfg} {case}: {str(e)[:160]}", flush=True)
        return "fail"
    text = data["choices"][0]["message"].get("content") or ""
    files, response = parse(text)
    od = d / "outputs"
    od.mkdir(exist_ok=True)
    for n, body in files.items():
        (od / n).write_text(body)
    (od / "response.md").write_text(response + "\n")
    (d / "raw.txt").write_text(text)
    u = data.get("usage", {}) or {}
    meta = {"model": model, "provider_model": data.get("model"), "config": cfg, "case": case,
            "seconds": round(secs, 1), "prompt_tokens": u.get("prompt_tokens"),
            "completion_tokens": u.get("completion_tokens"), "cost_usd": u.get("cost"),
            "finish_reason": data["choices"][0].get("finish_reason"), "files_returned": sorted(files)}
    (d / "run.json").write_text(json.dumps(meta, indent=1))
    with LOCK:
        print(f"ok   {model} {cfg} {case}  {secs:.0f}s  files={sorted(files)}  ${u.get('cost') or 0:.4f}", flush=True)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--configs", default=",".join(CONFIGS))
    ap.add_argument("--cases", default="")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--retry-missing", action="store_true",
                    help="re-parse finished runs leniently; rerun once any run whose expected file is still missing")
    a = ap.parse_args()
    k = key()
    if a.smoke:
        data, secs = call(k, "qwen/qwen3.8-27b", None,
                          "Reply with exactly:\n<<<FILE: t.txt>>>\nhello\n<<<END FILE>>>\ndone", max_tokens=2000)
        files, resp = parse(data["choices"][0]["message"].get("content") or "")
        print("smoke ok" if files.get("t.txt", "").strip() == "hello" else "smoke: protocol not followed",
              f"({secs:.1f}s, cost ${(data.get('usage') or {}).get('cost') or 0:.5f})")
        return
    if a.retry_missing:
        n = 0
        for rj in OUT.glob("*/*/*/run.json"):
            d = rj.parent
            if d.name.endswith(".attempt1") or (d.parent / (d.name + ".attempt1")).exists():
                continue
            files, response = parse((d / "raw.txt").read_text())
            if EXPECTED[d.name] in files:
                od = d / "outputs"
                for nme, body in files.items():
                    (od / nme).write_text(body)
                (od / "response.md").write_text(response + "\n")
                meta = json.loads(rj.read_text()); meta["files_returned"] = sorted(files)
                rj.write_text(json.dumps(meta, indent=1))
            else:
                d.rename(d.parent / (d.name + ".attempt1")); n += 1
        print(f"{n} runs moved to .attempt1 for a second try")
    systems = {"none": None, "v1.0": skill_text("v1.0"), "v1.1": skill_text("v1.1")}
    cases = a.cases.split(",") if a.cases else sorted(p.name for p in (PAYLOAD / "cases").iterdir())
    jobs = [(m, c, cs) for m in a.models.split(",") for c in a.configs.split(",") for cs in cases]
    print(f"{len(jobs)} runs", flush=True)
    with cf.ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(lambda j: run_one(k, *j, systems), jobs))
    print({s: res.count(s) for s in set(res)})
    tot = 0.0
    for p in OUT.glob("*/*/*/run.json"):
        tot += json.loads(p.read_text()).get("cost_usd") or 0
    print(f"total cost so far: ${tot:.2f}")


if __name__ == "__main__":
    main()
