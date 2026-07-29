---
title: Research Rigor
kind: concept
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/sources/skills/game-engine.md
updated: 2026-07-29
confidence: high
---

# Research Rigor

Cross-cutting evidence discipline for factual synthesis, detector assessment, and consequential security claims in the awesome-game-security corpus. Pair the matching domain skill (e.g. [[overviews/anti-cheat]], [[overviews/dma-attack]]) with research-rigor when converting README listings, wiki prose, or archive snippets into actionable conclusions. (source: wiki/sources/skills/overview.md)

## Principles

- Treat README entries, generated descriptions, [[compiled-wiki]] pages, and archives as **discovery/provenance** layers—not automatic proof of embedded claims.
- Verify citation identity: confirm the source text supports the exact claim being stated.
- Separate **observation**, **finding**, **attribution**, and **action** in written output.
- Do not import fixed detection thresholds or confidence values without representative calibration and validation for the target environment.
- Narrow the conclusion or report it as inconclusive when evidence is missing or contradictory.

## When to apply

| Query type | Pair with |
|------------|-----------|
| Claim validation, citation checks | matching domain overview |
| Detector evaluation, false-positive rates | [[overviews/anti-cheat]] or relevant detection lane |
| Engine globals, offsets, SDK dumps | [[overviews/game-engine]] + [[unreal-object-model]] / [[il2cpp]] / [[source-netvars]] |
| Evidence conflicts across sources | domain skill + this page |

Engine globals, object layouts, metadata formats, and helper APIs vary by engine branch, build configuration, platform, and game modifications—verify the exact version and binary artifacts before generalizing signatures or offsets. (source: wiki/sources/skills/game-engine.md)

## Related

[[compiled-wiki]] · [[overviews/overview]] · [[AGENTS]]
