# Contributing

The README is generated. Do not edit `README.md` by hand.

1. Add or change an entry in `data/`:
   - a paper or other resource in `data/papers.jsonl` (fields: `title`, `authors`, `year`, `url`, `arxiv_id` or `doi`,
     and the codes `contribution`, `parts`, `domains` that place it in a section; see existing lines);
   - a repository in `data/repos.jsonl` (fields: `full_name`, `url`, `description`, `stars`, `license`, `pushed_at`,
     `archived`, `category`, `tags`).
2. Rebuild: `python3 scripts/build_readme.py`. Entries the quality pass leaves out are listed in `data/dropped.tsv`
   with the reason (archived, fork or mirror, no push since 2025-06-01, off-topic, or a dead link).
3. Check links: the `links` workflow runs [lychee](https://github.com/lycheeverse/lychee) on `README.md` and must pass.
   Locally: `lychee README.md`.
4. Commit `data/`, `README.md` and `data/dropped.tsv` together and open a pull request.

`scripts/export_data.py` regenerates `data/papers.jsonl` and `data/repos.jsonl` from the survey's reference database;
maintainers run it when the survey database changes.

By contributing you agree to release your contribution under [CC0 1.0](LICENSE).
