---
title: Repository Navigation
kind: concept
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
updated: 2026-09-13
confidence: high
---

# Repository Navigation

Discovery workflow for connecting a question to the awesome-game-security collection: choose the right data layer, resolve actual paths (including case ambiguity), and preserve resource identity without conflating listing with capability. (source: wiki/sources/skills/overview.md)

## Choose a layer

| Need | Start here | Verify next |
|------|------------|-------------|
| Where a resource is listed | `README.md` section and blockquote subcategory | Preserve the original URL, including file/release/discussion suffixes |
| Topic vocabulary and connections | Matching `wiki/overviews/`, then concepts/entities | Follow cited primary sources; generated pages may repeat older claims |
| Short project summary | `description/{owner}/{repo}/description_en.txt` | Confirm capability, platform, and limitations upstream |
| Historical source inspection | `archive/{owner}/{repo}.txt` | Identify included files, revision evidence, truncation, provenance |
| Current support or exact implementation | Maintainer docs, release, or source at known revision | Match the precise claim and deployed version |

Do not load the whole wiki, every description, or an entire large archive for a narrow question. A direct project query can start at its README entry without reading the wiki first.

## Path lookup and case ambiguity

README spellings, description directories, and archive filenames can differ in case. Resolve the two layers independently. Report multiple case-only matches as ambiguous; do not silently select whichever file is largest. The archiver excludes many asset/binary formats and has snapshot/truncation fallbacks—a text archive is not a guaranteed complete checkout, and a project-path header is not an upstream commit identifier.

## Read-only repository index

Prefer the bundled indexer at `.claude/skills/overview/scripts/repository_index.py` for deterministic section and repo queries instead of loading the full README or archive tree. (source: wiki/sources/skills/overview.md)

```bash
python3 .claude/skills/overview/scripts/repository_index.py
python3 .claude/skills/overview/scripts/repository_index.py --section "Game Network" --subsection "Source" --limit 5
python3 .claude/skills/overview/scripts/repository_index.py --repo owner/repo
```

When installed outside a checkout, pass `--root /path/to/awesome-game-security`. The helper uses only the Python standard library: it reads README metadata and directory entries, returns JSON with H2/subcategory locations, GitHub occurrences, original URLs, actual description/archive paths, and a README SHA-256. It does not fetch upstream, import archived code, execute projects, or modify files. Limits and truncation are explicit. Organization-only URLs, prose/table links, and non-GitHub resources are outside its repository-entry results—read the selected section itself for those.

Missing means not found in this checkout. Sparse checkouts and separately installed skills may omit wiki, description, archive, or sibling skills. Do not claim that installing one skill also installs the repository data layers.

## Preserve identity and evidence

- Keep collection membership separate from technical capability.
- Distinguish repository, organization, article, file, and release URLs.
- For renamed, moved, mirrored, or forked projects, record the observed redirect and upstream relationship.
- Record collection revision or README hash separately from upstream revision.
- Treat wiki page, description, and archive derived from one source as one provenance chain—not three independent confirmations.

For conflicting claims, follow [[research-rigor]] evidence-reconciliation guidance.

## Maintenance vs retrieval

Archiving, link repair, description generation, and wiki update programs live under `scripts/`. Some invoke external services or commit/push changes. Read the selected script before a maintenance task; do not run bulk maintenance merely to answer a resource question.

## Related

[[resource-selection]] · [[compiled-wiki]] · [[research-rigor]] · [[overviews/overview]] · [AGENTS](AGENTS.md)
