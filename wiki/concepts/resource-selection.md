---
title: Resource Selection
kind: concept
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
updated: 2026-09-09
confidence: high
---

# Resource Selection

Workflow for connecting a concrete question to the awesome-game-security collection: start from the question's object and desired output, select the relevant domain skill, then only the resource layers needed to answer it. (source: wiki/sources/skills/overview.md)

## Principles

- **Repository membership is discovery, not proof.** Listing in a category does not guarantee capability, endorsement, or compatibility.
- **Route before diving.** Use [[overviews/overview]] skill-routing table to pick the domain; do not force security review onto ordinary graphics or gamedev questions.
- **Layer appropriately.** Prefer [[compiled-wiki]] synthesis; descend to descriptions, archives, or upstream only when the question needs repo-specific detail.
- **Pair with [[research-rigor]]** when elevating README, wiki, or archive text into consequential security conclusions.

## Selection output fields

For each chosen resource, document:

| Field | Purpose |
|-------|---------|
| Original identity/URL | Canonical upstream link from README |
| README location | Category and subcategory for provenance |
| Fit reason | Why this resource matches the task |
| Expected artifact | What the user should inspect (source file, doc section, dump) |
| Version/platform scope | Engine, OS, or build constraints |
| Material limitation | Truncated archive, generated summary, stale fork, etc. |

Use a small comparative table when alternatives serve different roles (e.g. DMA firmware vs analysis backend vs HID bridge). Distinguish collection-listed resources from supplemental upstream sources discovered during verification.

## Data layer order

1. Wiki entity/concept/overview ([[index]])
2. `description/{owner}/{repo}/description_en.txt`
3. `archive/{owner}/{repo}.txt` (scoped inspection; not a guaranteed complete checkout)
4. README category bullet

Resolve path casing before constructing local or raw URLs. Extract owner/repo from the GitHub URL, omitting a `.git` suffix.

## Maintenance (when requested)

Before adding entries: check duplicates, fork relationships, and category placement. Preserve deep links and document meaningful redirects—changing owner alone does not establish equivalent source identity. README bullet convention:

```markdown
## Category
> Subcategory
- https://github.com/owner/project [Purpose; platform/scope; distinctive value or limitation]
```

## Related

[[compiled-wiki]] · [[research-rigor]] · [[overviews/overview]] · [[AGENTS]]
