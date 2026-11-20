import json, sys, statistics as st
s = json.load(open(sys.argv[1]))
CF = ["without_skill", "old_skill", "with_skill"]
LBL = {"without_skill": "none", "old_skill": "v1.0", "with_skill": "v1.1"}
auto_only = "--auto" in sys.argv
print("| Model | none | v1.0 | v1.1 |"); print("|---|---|---|---|")
tot = {c: [0, 0] for c in CF}
for m, v in s.items():
    if m.startswith("_"): continue
    row = []
    for cfg in CF:
        p = t = 0
        for k, e in v.items():
            if not k.endswith("/" + cfg): continue
            ung = sum("UNGRADED" in f for f in e["failed"]) if auto_only else 0
            t += e["total"] - ung; p += e["total"] - ung - (len(e["failed"]) - ung)
        row.append(f"{p}/{t}"); tot[cfg][0] += p; tot[cfg][1] += t
    print(f"| {m.split('__')[1]} | " + " | ".join(row) + " |")
print("| **All** | " + " | ".join(f"**{tot[c][0]}/{tot[c][1]} ({100*tot[c][0]/tot[c][1]:.0f}%)**" for c in CF) + " |")
# metrics
print("\nMedian length change on the 7 revision cases (words), and residual pattern hits")
print("| Model | none | v1.0 | v1.1 | hits none/v1.0/v1.1 | clean abstract similarity none/v1.0/v1.1 |"); print("|---|---|---|---|---|---|")
for m, v in s.items():
    if m.startswith("_"): continue
    lc, hits, simab = [], [], []
    for cfg in CF:
        ms = [e["metrics"] for k, e in v.items() if k.endswith("/" + cfg) and "metrics" in e and not k.startswith("preserve")]
        lc.append(f"{st.median(x['length_change_pct'] for x in ms):+.0f}%" if ms else "-")
        hits.append(str(sum(x["pattern_hits_out"] for x in ms)))
        a = v.get(f"preserve-clean-human-abstract/{cfg}", {}).get("metrics")
        simab.append(f"{a['similarity']:.2f}" if a else "-")
    print(f"| {m.split('__')[1]} | " + " | ".join(lc) + " | " + "/".join(hits) + " | " + "/".join(simab) + " |")
