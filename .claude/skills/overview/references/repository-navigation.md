# Repository Navigation and Resource Identity

Use this guide to connect a skill question to the actual collection. Local
structure reviewed on 2026-09-09. Paths below are relative to the repository root.
This is a discovery workflow, not an instruction to run a listed project.

## Choose a Layer for the Question

| Need | Start here | What to verify next |
|---|---|---|
| Where a resource is listed | `README.md` section and blockquote subcategory | Preserve the original URL, including any file, release or discussion suffix |
| Topic vocabulary and connections | Matching `wiki/overviews/`, then selected concepts/entities | Follow the cited primary source; generated pages may repeat older claims |
| Short project summary | `description/{owner}/{repo}/description_en.txt` | Confirm capability, platform and limitations upstream |
| Historical source inspection | `archive/{owner}/{repo}.txt` | Identify included files, revision evidence, truncation and provenance |
| Current support or exact implementation | Maintainer documentation, release or source at a known revision | Match the precise claim and deployed version |

Do not load the whole wiki, every description or an entire large archive to
answer a narrow question. A direct project query can start at its README entry
and relevant primary material without reading the wiki first.

The archiver excludes many asset/binary formats and has snapshot, lightweight
and truncation fallbacks. A text archive is not guaranteed to be a complete
checkout. A project-path header is not an upstream commit identifier. Do not
infer that an absent file, symbol or binary never existed upstream.
See the actual [archiver](../../../../scripts/archive-repos.py).

## Locate Actual Paths

README spellings, description directories and archive filenames can differ in
case. Resolve the two layers independently. Report multiple case-only matches
as ambiguous; do not silently select whichever file is largest. The existing
[description path helper](../../../../scripts/description_paths.py) documents
the repository's write-path convention; discovery should expose actual matches.

Use the bundled read-only helper from the repository root:

```bash
python3 .claude/skills/overview/scripts/repository_index.py
python3 .claude/skills/overview/scripts/repository_index.py --section "Game Network" --subsection "Source" --limit 5
python3 .claude/skills/overview/scripts/repository_index.py --repo bkaradzic/bgfx
```

When installed outside a checkout, pass `--root /path/to/awesome-game-security`.
The helper uses only the Python standard library. It reads README metadata and
directory entries; it does not fetch, import archived code, execute projects,
modify files or verify upstream behavior.

Its JSON includes current H2/subcategory locations, GitHub repository occurrences,
original URLs, actual description/archive paths and a README SHA-256. Limits and
truncation are explicit. It follows this README's bullet-list convention, not a
general Markdown parser: organization-only URLs, prose/table links and non-GitHub
resources are outside its repository-entry result. Read the selected section
itself for those resources. Counts describe discovery entries, not unique tools,
coverage, quality or total links.

Missing means not found in this checkout. Sparse checkouts and separately
installed skills may omit the wiki, description, archive or sibling skills.
Check what exists before constructing a path. If local material is absent, use
the verified original URL or the
[public collection](https://github.com/gmh5225/awesome-game-security).
Do not claim that installing one skill also installs the repository data layers.

## Preserve Identity and Evidence

- Keep collection membership separate from technical capability. A category
  placement or generated description does not certify the resource.
- Distinguish repository, organization, article, file and release URLs. A root
  repository URL identifies a project; it does not preserve a deep link's evidence.
- For renamed, moved, mirrored or forked projects, record the observed redirect
  and upstream relationship. A matching name or replacement owner is insufficient.
- Record the collection revision or README hash separately from the upstream
  revision. A description generation date is not a source-code revision.
- Treat a wiki page, description and archive derived from one source as one
  provenance chain, not three independent confirmations.

For conflicting claims, use
[repository evidence reconciliation](../../research-rigor/references/repository-evidence.md).

## Keep Maintenance Separate from Retrieval

The current repository contains archiving, link repair, description generation
and wiki update programs. Some paths invoke external services or commit/push
changes. Read the selected script and its options before a maintenance task;
do not run a bulk maintenance program merely to answer a resource question.
There is no current `scripts/generate-toc.py` or `scripts/remove-forks.py`;
older skill references to them do not establish their availability.
