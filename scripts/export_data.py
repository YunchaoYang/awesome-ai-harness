#!/usr/bin/env python3
"""Export slim data files from the survey project into data/ (run once per survey release).

  data/papers.jsonl  papers cited by the survey or coded relevance=core, with their codes and citing sections
  data/repos.jsonl   GitHub repos of the survey's repo census, joined with fork/mirror flags (data/repo_flags.json)

Usage: python3 scripts/export_data.py [/path/to/agent-harness-survey]
"""
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SURVEY = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/yangy78/work/agent-harness-survey")
sys.path.insert(0, str(SURVEY / "scripts"))
import corpus  # noqa: E402  (survey's single corpus reader)

CITE = re.compile(r"\\(?:cite[a-z]*|nocite)\*?(?:\[[^\]]*\])*\{([^}]*)\}")


def read(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]


def cite_map():
    out = {}
    for f in sorted(glob.glob(str(SURVEY / "paper/sections/*.tex"))):
        sec = Path(f).stem
        for m in CITE.finditer(Path(f).read_text(encoding="utf-8")):
            for k in m.group(1).split(","):
                k = k.strip()
                if k:
                    out.setdefault(k, [])
                    if sec not in out[k]:
                        out[k].append(sec)
    return out


def main():
    master = read(SURVEY / "refs/master.jsonl")
    by_key = {r["key"]: r for r in master}
    by_ax = {r["arxiv_id"]: r for r in master if r.get("arxiv_id")}
    coded = {r["arxiv_id"]: r for r in corpus.load_coded()}
    abstracts = {r["arxiv_id"]: r for r in corpus.load_abstracts()}
    cites = cite_map()

    keep = {}  # key or arxiv id -> record
    for k, secs in cites.items():
        r = by_key[k]
        keep[k] = (r, secs)
    for ax, c in coded.items():
        if c["relevance"] != "core":
            continue
        r = by_ax.get(ax)
        if r is not None:
            keep.setdefault(r["key"], (r, cites.get(r["key"], [])))
        else:
            a = abstracts[ax]
            keep.setdefault("arXiv:" + ax, ({"key": None, "type": "paper", "title": a["title"], "authors": a["authors"],
                                             "year": a["year"], "arxiv_id": ax, "doi": None,
                                             "url": f"https://arxiv.org/abs/{ax}"}, []))
    # the Berkeley Advanced LLM Agents course is listed even though the survey text does not cite it
    keep.setdefault("song2025advanced", (by_key["song2025advanced"], cites.get("song2025advanced", [])))

    rows = []
    for _, (r, secs) in keep.items():
        c = coded.get(r.get("arxiv_id")) or {}
        rows.append({
            "key": r.get("key"), "type": r.get("type"), "title": r["title"], "authors": r.get("authors") or [],
            "year": r.get("year"), "arxiv_id": r.get("arxiv_id"), "doi": r.get("doi"), "url": r.get("url"),
            "venue": r.get("venue"), "tags": r.get("tags") or [], "master_topics": r.get("topics") or [],
            "cited_in": secs, "relevance": c.get("relevance"), "contribution": c.get("V2_contribution"),
            "parts": c.get("V1_component", []), "domains": c.get("V3_domain", []),
        })
    rows.sort(key=lambda x: (-(x["year"] or 0), x["title"].lower()))
    with open(HERE / "data/papers.jsonl", "w", encoding="utf-8") as f:
        for x in rows:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")

    flags = json.loads((HERE / "data/repo_flags.json").read_text())
    with open(HERE / "data/repos.jsonl", "w", encoding="utf-8") as f:
        for r in read(SURVEY / "awesome/repos.jsonl"):
            fl = flags.get(r["full_name"]) or {}
            r["is_fork"] = bool(fl.get("isFork"))
            r["is_mirror"] = bool(fl.get("isMirror"))
            r["archived"] = bool(r.get("archived") or fl.get("isArchived"))
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"papers {len(rows)}  repos {len(flags)}")


if __name__ == "__main__":
    main()
