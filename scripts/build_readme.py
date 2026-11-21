#!/usr/bin/env python3
"""Generate README.md from data/*.jsonl. Nothing about any entry is typed by hand.

Inputs  data/papers.jsonl  data/repos.jsonl  data/link_check.tsv (optional: entries whose URL returned 404 are dropped)
Outputs README.md  data/dropped.tsv (every repo or paper left out, with the reason)
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

PUSH_CUTOFF = "2025-06-01"          # repos with no push since this date are dropped
HIGH_STAR = 10_000                  # created-2026 repos at or above this need a harness-like description
HARNESS_WORDS = re.compile(
    r"harness|framework|\bsdk\b|\bcli\b|\btools?\b|toolkit|benchmark|\beval|runtime|sandbox|librar|platform|"
    r"server|protocol|memory|skills?\b|coding agents?|agent loop|orchestrat|infrastructure|assistant|browser|"
    r"scanner|optimi[sz]er|database|proxy|engine|manage agents|fleet of|knowledge graph|multi-agent|"
    r"agents? (?:os|team)|computer use|web agent|research|\bagents?\b(?!-)|auditing|claude\.md",
    re.I)

PARTS = [  # id, heading, one-line job (reference anatomy of the survey, paper/taxonomy.json)
    ("loop", "Control loop", "Runs the turn cycle: call the model, dispatch actions, decide when to stop."),
    ("context", "Context manager", "Builds what the model sees each turn: prompts, instruction files, retrieval, compaction."),
    ("action", "Action interface", "Tools and protocols through which the model acts: function calls, code, GUI, MCP."),
    ("environment", "Execution environment", "Where actions run: sandbox, container, VM, filesystem, network policy."),
    ("state", "State and memory", "What persists outside the context window: transcripts, checkpoints, memory, skills."),
    ("verification", "Verification and feedback", "Checks fed back into the loop: tests, critics, self-review, evaluators."),
    ("governance", "Governance", "Who may do what: permissions, approvals, guardrails, human oversight, audit."),
    ("orchestration", "Orchestration", "More than one loop: subagents, teams, workflows, agent-to-agent protocols."),
    ("observability", "Observability and extension", "Telemetry, traces, the human interface, hooks and plugins."),
]
PART_NAME = {p: n for p, n, _ in PARTS}
SECTION_PART = {"04a_loop": "loop", "04b_action": "action", "04c_context": "context", "04d_memory": "state",
                "04e_environment": "environment", "04f_verification": "verification",
                "04g_orchestration": "orchestration", "04h_observability": "observability"}
DOMAINS = {"software_engineering": "Software engineering", "web_computer_use": "Web and computer use",
           "science_research": "Science and research", "data_ml": "Data and ML engineering",
           "embodied_robotics": "Embodied agents and robotics", "enterprise_ops": "Enterprise and operations",
           "healthcare": "Healthcare", "education": "Education", "finance": "Finance",
           "creative_media": "Creative media", "security_ops": "Security operations",
           "general": "General and cross-domain"}
REPO_SECTION = {"evaluation harnesses and benchmarks": "bench", "safety, guardrails and red-teaming": "security",
                "educational and minimal harnesses": "courses"}
SURVEY_TITLE = re.compile(r"\bsurvey\b|taxonomy|\banatomy\b|systematic review|literature review|\boverview\b", re.I)


def read(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]


def anchor(text):
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")


def name(a):
    if "," in a:
        last, first = [s.strip() for s in a.split(",", 1)]
        return f"{first} {last}".strip()
    return a.strip()


def authors(lst):
    if not lst:
        return ""
    names = [name(a) for a in lst]
    return f"{names[0]} et al." if len(names) > 3 else ", ".join(names)


def md(text):
    return (text or "").replace("|", "\\|").replace("\n", " ").replace("[", "\\[").replace("]", "\\]").strip()


def paper_line(p):
    s = f"- [{md(p['title'])}]({p['url']})"
    a = authors(p["authors"])
    if a or p["year"]:
        s += " - " + a + (f" ({p['year']})" if p["year"] else "")
    s += "."
    if p.get("arxiv_id"):
        s += f" arXiv:{p['arxiv_id']}"
    elif p.get("doi"):
        s += f" doi:{p['doi']}"
    return s


def place(p):
    """(section, subsection) of a paper: from its coded views, or for uncoded cited papers from where the survey cites it."""
    secs = p["cited_in"]
    if p["type"] == "web" and ({"course", "education"} & set(p["tags"])):
        return "courses", None
    c = p["contribution"]
    if c == "conceptual" or "related_surveys" in p["master_topics"] or (c is None and SURVEY_TITLE.search(p["title"])):
        return "surveys", None
    if c == "security" or (c is None and secs[:1] == ["08_security"]):
        return "security", None
    if c == "benchmark" or (c is None and secs[:1] == ["07_evaluation"]):
        return "bench", None
    if c is not None:
        doms = [d for d in p["domains"] if d != "general"]
        parts = [x for x in p["parts"] if x in PART_NAME]
        if (c == "application" or p["relevance"] == "applied" or not parts) and doms:
            return "usecase", doms[0]
        if parts:
            return "part", parts[0]
        return "part", "whole"
    for s in secs:
        if s in SECTION_PART:
            return "part", SECTION_PART[s]
        if s == "06_usecases":
            return "usecase", "general"
        if s == "08_security":
            return "security", None
        if s == "07_evaluation":
            return "bench", None
    return "other", None


def human(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def repo_drop_reason(r):
    if r.get("archived"):
        return "archived"
    if r.get("is_fork"):
        return "fork"
    if r.get("is_mirror"):
        return "mirror"
    if (r.get("pushed_at") or "")[:10] < PUSH_CUTOFF:
        return f"no push since {PUSH_CUTOFF} (last {r.get('pushed_at', '')[:10]})"
    if "created-2026" in r.get("tags", []) and r["stars"] >= HIGH_STAR and not HARNESS_WORDS.search(r.get("description") or ""):
        return "created 2026 with high stars, description not about an agent harness, framework, tool or benchmark"
    return None


def repo_table(rows):
    out = ["| Repository | Stars | License | Last push | Description |", "|---|---:|---|---|---|"]
    for r in sorted(rows, key=lambda r: -r["stars"]):
        out.append(f"| [{r['full_name']}]({r['url']}) | {human(r['stars'])} | {r.get('license') or 'none'} | "
                   f"{(r.get('pushed_at') or '')[:10]} | {md(r.get('description'))} |")
    return out


def main():
    dead = set()
    lc = DATA / "link_check.tsv"
    if lc.exists():
        with open(lc, encoding="utf-8") as f:
            dead = {row["url"] for row in csv.DictReader(f, delimiter="\t") if row["status"] == "404"}

    dropped = []
    papers = []
    for p in read(DATA / "papers.jsonl"):
        if p["url"] in dead:
            dropped.append(("paper", p["key"] or p["arxiv_id"], p["url"], "", "link check returned 404"))
        else:
            papers.append(p)
    repos = []
    for r in read(DATA / "repos.jsonl"):
        why = "link check returned 404" if r["url"] in dead else repo_drop_reason(r)
        if why:
            dropped.append(("repo", r["full_name"], r["url"], r["stars"], why))
        else:
            repos.append(r)
    with open(DATA / "dropped.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["kind", "id", "url", "stars", "reason"])
        w.writerows(dropped)

    groups = {}
    for p in papers:
        groups.setdefault(place(p), []).append(p)
    for v in groups.values():
        v.sort(key=lambda p: (-(p["year"] or 0), p["title"].lower()))

    rcats = {}
    for r in repos:
        rcats.setdefault(r["category"], []).append(r)

    L = []
    L += ["# Awesome AI Harness", "",
          "An agent harness is the software around a language model that turns it into an agent: the loop that calls the "
          "model, the tools it acts through, the context it sees, where its actions run, what it remembers, and the checks, "
          "permissions and orchestration around it.",
          "This list is generated from the verified reference database of the survey *Agent Harnesses: Architecture, Measured Effects, "
          "and Design Trade-offs* (forthcoming on arXiv).",
          f"It holds {len(papers)} papers and resources the survey cites or codes as core harness work, and "
          f"{len(repos)} open-source repositories checked against the GitHub API.", "",
          "Entries are kept in [`data/`](data/) and the README is rebuilt by `python3 scripts/build_readme.py`; "
          "see [CONTRIBUTING.md](CONTRIBUTING.md).", ""]

    L += ["## Contents", "",
          "- [The nine-part anatomy](#the-nine-part-anatomy)",
          "- [Papers](#papers)",
          "  - [Surveys and anatomies](#surveys-and-anatomies)",
          "  - [By anatomy part](#by-anatomy-part)",
          "  - [By use case](#by-use-case)",
          "- [Harness repositories](#harness-repositories)",
          "- [Benchmarks and evaluation](#benchmarks-and-evaluation)",
          "- [Security](#security)",
          "- [Courses and learning](#courses-and-learning)", ""]

    L += ["## The nine-part anatomy", "", "| Part | What it does | Papers |", "|---|---|---:|"]
    for pid, pname, job in PARTS:
        L.append(f"| [{pname}](#{anchor(pname)}) | {job} | {len(groups.get(('part', pid), []))} |")
    L.append("")

    L += ["## Papers", "", "### Surveys and anatomies", ""]
    L += [paper_line(p) for p in groups.get(("surveys", None), [])] + [""]
    L += ["### By anatomy part", ""]
    for pid, pname, _ in PARTS + [("whole", "Whole-harness systems", "")]:
        rows = groups.get(("part", pid), [])
        if rows:
            L += [f"#### {pname}", ""] + [paper_line(p) for p in rows] + [""]
    L += ["### By use case", ""]
    for did, dname in DOMAINS.items():
        rows = groups.get(("usecase", did), [])
        if rows:
            L += [f"#### {dname}", ""] + [paper_line(p) for p in rows] + [""]
    rows = groups.get(("other", None), [])
    if rows:
        L += ["### Foundations and other cited work", ""] + [paper_line(p) for p in rows] + [""]

    L += ["## Harness repositories", "", "Sorted by stars within each category. Stars and last push from the GitHub API.", ""]
    for cat in sorted(rcats):
        if cat in REPO_SECTION:
            continue
        L += [f"### {cat[0].upper() + cat[1:]}", ""] + repo_table(rcats[cat]) + [""]

    for key, title in (("bench", "Benchmarks and evaluation"), ("security", "Security"), ("courses", "Courses and learning")):
        L += [f"## {title}", ""]
        rows = groups.get((key, None), [])
        if rows:
            L += ["### Papers and resources", ""] + [paper_line(p) for p in rows] + [""]
        for cat, sec in REPO_SECTION.items():
            if sec == key and rcats.get(cat):
                L += [f"### Repositories: {cat}", ""] + repo_table(rcats[cat]) + [""]

    L += ["## License", "", "[CC0 1.0](LICENSE). Repository descriptions are quoted from GitHub.", ""]
    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"papers {len(papers)}  repos {len(repos)}  dropped {len(dropped)} "
          f"(repos {sum(d[0] == 'repo' for d in dropped)}, papers {sum(d[0] == 'paper' for d in dropped)})")
    for k in sorted(groups, key=str):
        print(" ", k, len(groups[k]))


if __name__ == "__main__":
    main()
