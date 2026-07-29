---
title: obfuscation-detection
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrphrazer__obfuscation_detection.md
updated: 2026-07-29
confidence: medium
---

# obfuscation-detection

Binary Ninja plugin and script collection for pinpointing obfuscated code regions in binaries. Combines multiple heuristics: control-flow flattening detection via loop analysis and dominator trees, instruction-level complexity metrics, n-gram frequency analysis comparing basic blocks against a reference database, and statistical outlier detection. Includes batch-processing scripts for large-scale binary analysis campaigns. (source: wiki/sources/descriptions/mrphrazer__obfuscation_detection.md)

Detection-oriented complement to deobfuscation-focused Binary Ninja work (e.g. [[opaque-predicates-detective]]); scopes to locating suspect regions rather than simplifying them.

## Links

- Repo: https://github.com/mrphrazer/obfuscation_detection

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[opaque-predicates-detective]] · [[ariadne]] · [[idadeflat]] · [[d810-ng]]
