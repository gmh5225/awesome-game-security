---
title: obfuscation-analysis
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrphrazer__obfuscation_analysis.md
updated: 2026-07-29
confidence: medium
---

# obfuscation-analysis

Binary Ninja plugin for analyzing and simplifying obfuscated code. Features MBA (Mixed Boolean-Arithmetic) expression simplification via backward slicing and oracle-based lookup (msynth), opaque-predicate detection through dataflow analysis, and automated deobfuscation workflows. Translates BNIL expressions to Z3-compatible forms for semantic verification of simplification correctness. (source: wiki/sources/descriptions/mrphrazer__obfuscation_analysis.md)

Deobfuscation-oriented complement to detection-focused Binary Ninja work from the same author (e.g. [[obfuscation-detection]]); scopes to simplifying expressions and predicates rather than pinpointing suspect regions.

## Links

- Repo: https://github.com/mrphrazer/obfuscation_analysis

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[obfuscation-detection]] · [[opaque-predicates-detective]] · [[cobra]] · [[mutaben]] · [[idadeflat]]
