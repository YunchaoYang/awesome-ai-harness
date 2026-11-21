#!/usr/bin/env python3
"""Check a seeded random sample of entry URLs with curl and write data/link_check.tsv (url, status, kind, id).

A HEAD request first (curl -sI -L); if it fails or returns 403/405, a GET. build_readme.py drops entries whose status is 404.
Usage: python3 scripts/link_sample.py [N=60] [SEED=0]
"""
import csv
import json
import random
import subprocess
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def status(url, head=True):
    cmd = ["curl", "-s", "-o", "/dev/null", "-L", "--max-time", "20", "-A", "Mozilla/5.0 (link-check)",
           "-w", "%{http_code}"] + (["-I"] if head else []) + [url]
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip() or "000"


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    items = [("paper", p["key"] or p["arxiv_id"], p["url"]) for p in map(json.loads, open(DATA / "papers.jsonl"))]
    items += [("repo", r["full_name"], r["url"]) for r in map(json.loads, open(DATA / "repos.jsonl"))]
    sample = random.Random(seed).sample(items, n)
    rows = []
    for kind, i, url in sample:
        s = status(url)
        if s in ("000", "403", "405"):
            s = status(url, head=False)
        rows.append({"url": url, "status": s, "kind": kind, "id": i})
        print(s, url, flush=True)
    with open(DATA / "link_check.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["url", "status", "kind", "id"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    bad = [r for r in rows if r["status"] not in ("200", "206")]
    print(f"checked {len(rows)}, not 200: {len(bad)}, 404: {sum(r['status'] == '404' for r in rows)}")


if __name__ == "__main__":
    main()
