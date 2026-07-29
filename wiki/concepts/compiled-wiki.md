---
title: Compiled Wiki
kind: concept
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/AGENTS.md
updated: 2026-07-29
confidence: high
---

# Compiled Wiki

Karpathy-style **compiled knowledge wiki** under `wiki/`, maintained by `scripts/update-wiki-cli.py` (Cursor CLI in CI). It sits between immutable upstream sources (README, `.claude/skills/`, `description/**`) and raw archives, offering citation-aware synthesis for agents and humans. (source: wiki/sources/skills/overview.md) (source: wiki/AGENTS.md)

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

## Usage

For topical questions (DMA, EAC, Present hooks, HVCI, …): start at [[overviews/overview]] or `wiki/index.md`, then the matching overview and concept pages. Fall back to skills and `description/` summaries if a page is missing. Use [[research-rigor]] when elevating wiki or README text into security conclusions.

## Related

[[overviews/overview]] · [[research-rigor]] · [[AGENTS]] · [[index]]
