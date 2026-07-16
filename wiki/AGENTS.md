# Awesome Game Security — LLM Wiki Schema

This directory is a **compiled knowledge wiki** for the curated game-security resource list.
It follows the [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern:

1. **Raw sources** (immutable projections under `wiki/sources/`) — derived from `README.md`, `.claude/skills/`, and selected `description/**/description_en.txt`.
2. **Wiki** (this tree) — LLM-owned markdown: overviews, concepts, entities, index, log.
3. **Schema** (this file) — conventions the maintainer agent must follow.

Do **not** treat `archive/` as a wiki source. Archives are huge; use `description/` summaries instead.

Orchestrator: `scripts/update-wiki-cli.py`. CI: `.github/workflows/update-wiki-cli.yml`.

---

## Layout

```
wiki/
  AGENTS.md           # this schema (human + agent contract)
  index.md            # catalog of pages
  log.md              # chronological ingest / lint / skill-sync entries
  concepts/           # durable concept pages (DMA, EAC, HVCI, …)
  entities/           # tool / product / project pages (when warranted)
  overviews/          # one page per skill topic (anti-cheat, dma-attack, …)
  sources/            # read-only projections written by the orchestrator at runtime
    README-categories.md
    skills/<name>.md
    descriptions/<owner>__<repo>.md
  .state.json         # hashes, last run, pending queue (orchestrator-owned)
```

`wiki/sources/**` projections are **gitignored** (regenerated every scan/ingest). Only `.gitkeep` placeholders are tracked. Agents and CI always project fresh copies before compile.

---

## Page kinds

| Kind | Path | Purpose |
|------|------|---------|
| overview | `overviews/<topic>.md` | Domain synthesis aligned with a skill (`anti-cheat`, `dma-attack`, …) |
| concept | `concepts/<slug>.md` | Shared technical concept (cross-cutting) |
| entity | `entities/<slug>.md` | Specific tool, AC product, or notable repo |
| index | `index.md` | TOC with links to all active pages |
| log | `log.md` | Append-only activity journal |

### Naming

- Filenames: lowercase kebab-case ASCII (`easy-anti-cheat.md`, `present-hook.md`).
- Titles: human-readable H1 matching the topic.
- Prefer updating an existing page over creating duplicates. Before creating, search `index.md` and the target directory.

### Frontmatter (required on overview / concept / entity)

```yaml
---
title: Easy Anti-Cheat
kind: concept          # overview | concept | entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
updated: 2026-07-16
confidence: medium     # high | medium | low
---
```

---

## Linking and citations

- Cross-link with Obsidian-style wikilinks: `[[easy-anti-cheat]]` or `[[concepts/easy-anti-cheat]]`.
- When a claim comes from a projected source, cite it inline, e.g. `(source: wiki/sources/descriptions/ufrisk__pcileech.md)`.
- Prefer citing `description/` / skill / README projections — never paste large archive dumps into wiki pages.
- Keep pages focused: prefer 1–3 screenfuls; split if a page grows past ~200 lines.

---

## Operations

### Bootstrap

Create skeleton overviews for all skill topics and a small set of core concepts extracted from skills + README category map. Do not ingest the full description corpus.

### Ingest

Given one or more projected sources under `wiki/sources/`:

1. Read this schema and `index.md`.
2. Read the new/changed source projection(s).
3. Update or create a **small** set of pages (typically 1 overview and/or 1–3 concepts/entities).
4. Refresh `index.md` entries for touched pages.
5. Append one dated bullet block to `log.md`.
6. Print `Done: <summary>` when finished.

Hard limits per ingest task:

- Touch at most **8** wiki markdown files (excluding `log.md` / `index.md` bookkeeping).
- Do not rewrite unrelated pages.
- Do not delete pages unless they are empty stubs or clear duplicates.

If `wiki/overviews/` is empty, the orchestrator runs **bootstrap** before ingest.

Description ingest is incremental only:

- Hash-changed descriptions already in `wiki/.state.json`
- Up to **5** never-tracked `description/**/description_en.txt` per scan (newest first)
- Explicit `--repos` / PR path filters / `--repos-env`

### Lint

1. Scan `index.md` vs files on disk; fix missing/orphan entries.
2. Check for obvious broken wikilinks among recently touched pages.
3. Flag contradictions only when both claims are in-wiki and clearly incompatible; note in `log.md`.
4. Repair high-priority broken links; leave speculative rewrites alone.

### Skill sync

After wiki pages for a topic exist, optionally strengthen `.claude/skills/<topic>/SKILL.md`:

- Add missing cross-references to `wiki/overviews/<topic>.md` and key concepts.
- Fill clear gaps or correct outdated one-liners **only when** the wiki page has higher confidence.
- Do **not** change YAML frontmatter `name`.
- Do **not** expand a skill into a full textbook (cap: ~30 new lines per skill per run).
- Do **not** modify any path outside the allowlisted skill file.

---

## Topics (skill alignment)

| Topic slug | Skill path | Overview page |
|------------|------------|---------------|
| overview | `.claude/skills/overview/SKILL.md` | `overviews/overview.md` |
| anti-cheat | `.claude/skills/anti-cheat/SKILL.md` | `overviews/anti-cheat.md` |
| dma-attack | `.claude/skills/dma-attack/SKILL.md` | `overviews/dma-attack.md` |
| game-engine | `.claude/skills/game-engine/SKILL.md` | `overviews/game-engine.md` |
| game-hacking | `.claude/skills/game-hacking/SKILL.md` | `overviews/game-hacking.md` |
| graphics-api | `.claude/skills/graphics-api/SKILL.md` | `overviews/graphics-api.md` |
| mobile-security | `.claude/skills/mobile-security/SKILL.md` | `overviews/mobile-security.md` |
| reverse-engineering | `.claude/skills/reverse-engineering/SKILL.md` | `overviews/reverse-engineering.md` |
| windows-kernel | `.claude/skills/windows-kernel/SKILL.md` | `overviews/windows-kernel.md` |

---

## Forbidden

- Reading or embedding `archive/**` content into wiki pages.
- Full-corpus description ingest in a single run.
- Committing secrets, API keys, or personal paths.
- Rewriting `README.md` or `description/` from the wiki agent (those are upstream sources).
- Using `llm-wiki-compiler` / external wiki compilers in this repo — maintenance is via `scripts/update-wiki-cli.py` only.

---

## Local / CI usage

```bash
# Scan pending deltas (no agent)
python3 scripts/update-wiki-cli.py --list-pending

# Dry-run bootstrap prompt
python3 scripts/update-wiki-cli.py --mode bootstrap --dry-run

# Bootstrap overviews from skills + README categories
export CURSOR_API_KEY=...
python3 scripts/update-wiki-cli.py --mode bootstrap --commit-every 1

# Ingest pending description / skill / README deltas
python3 scripts/update-wiki-cli.py --mode ingest --limit 5 --commit-every 1

# Daily health pass
python3 scripts/update-wiki-cli.py --mode lint --commit-every 1

# Strengthen skills from wiki overviews
python3 scripts/update-wiki-cli.py --mode skill-sync --topics anti-cheat --commit-every 1
```

GitHub Actions (`.github/workflows/update-wiki-cli.yml`):

- **schedule** — daily auto (bootstrap if empty, else ingest pending incl. ≤5 new descriptions, else lint)
- **workflow_dispatch** — manual mode / limit / topics / repos / sync_skills
- **pull_request** — same-repo only; path filters on README, descriptions, skills; bootstrap-if-empty then ingest; pushes wiki updates to the PR head branch

Requires repository secret `CURSOR_API_KEY`. Forks never receive secrets.
