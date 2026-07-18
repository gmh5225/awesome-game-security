---
title: GhidraMetrics
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/westfox-5__GhidraMetrics.md
updated: 2026-07-18
confidence: medium
---

# GhidraMetrics

Ghidra extension that computes native-code complexity metrics (cyclomatic complexity, function size, call depth, and related measures) for analyzed binaries. Supports batch runs via headless Ghidra scripts and exports JSON/reports—useful for triage and comparing complexity across game/client modules before deeper RE. (source: wiki/sources/descriptions/westfox-5__GhidraMetrics.md)

Not a decompiler or unpacker; scoped to metric collection on already-analyzed programs.

## Links

- Repo: https://github.com/westfox-5/GhidraMetrics

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idadeflat]] · [[xrefsext]]
