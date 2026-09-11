---
title: Compiled Wiki
kind: concept
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/AGENTS.md
updated: 2026-09-09
confidence: high
---

# Compiled Wiki

Karpathy-style **compiled knowledge wiki** under `wiki/`, maintained by `scripts/update-wiki-cli.py` (Cursor CLI in CI). It sits between immutable upstream sources (README, `.claude/skills/`, `description/**`) and raw archives, offering citation-aware synthesis for agents and humans. Generated wiki pages are discovery aids—follow their original citations before adopting technical claims. (source: wiki/sources/skills/overview.md) (source: wiki/AGENTS.md)

## Layout

| Need | Path |
|------|------|
| Catalog | `wiki/index.md` |
| Schema / conventions | `wiki/AGENTS.md` |
| Domain overviews | `wiki/overviews/<topic>.md` (aligned with skill topics) |
| Concepts | `wiki/concepts/<slug>.md` |
| Entities (tools/projects) | `wiki/entities/<slug>.md` |
| Activity log | `wiki/log.md` |
| Raw projections (regenerated) | `wiki/sources/**` |

Projections under `wiki/sources/` are gitignored placeholders regenerated each scan; agents read fresh copies at ingest time.

## Position in repository layers

The collection exposes four discovery layers (layer 0 is this wiki): (source: wiki/sources/skills/overview.md)

| Layer | Path | Role |
|-------|------|------|
| 0 — Compiled wiki | `wiki/` | Topical synthesis and cross-project connections |
| 1 — Resource index | `README.md` | Actual categories, subcategories, URLs, short descriptions |
| 2 — Descriptions | `description/{owner}/{repo}/description_en.txt` | Generated concise summaries (not independent verification) |
| 3 — Archives | `archive/{owner}/{repo}.txt` | Captured source trees (may exclude files or truncate) |

A direct project question can start with its README entry or description; reading the entire wiki is unnecessary. For exact capability claims, verify upstream documentation or source at a known revision. See [[resource-selection]] for provenance fields and [[research-rigor]] for evidence reconciliation when layers disagree.

## Usage

For topical questions (DMA, EAC, Present hooks, HVCI, …): start at [[overviews/overview]] or `wiki/index.md`, then the matching overview and concept pages. Fall back to skills and `description/` summaries if a page is missing. Not every skill has a matching wiki overview—check the catalog or skill directory first.

## Related

[[overviews/overview]] · [[resource-selection]] · [[research-rigor]] · [AGENTS](AGENTS.md)
