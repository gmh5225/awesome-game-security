---
title: opaque-predicate-patcher
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Vector35__OpaquePredicatePatcher.md
updated: 2026-08-19
confidence: medium
---

# opaque-predicate-patcher

Binary Ninja plugin that **automatically removes opaque predicates** from obfuscated binaries (Vector35). Implemented in Python, it analyzes MLIL branch conditions to detect constant true or false paths, patches branch instructions to always or never branch, and re-runs analysis in iterative passes. Target audience: reverse engineers who need faster deobfuscation of protected or intentionally confusing code. (source: wiki/sources/descriptions/Vector35__OpaquePredicatePatcher.md)

Complements detection-oriented [[opaque-predicates-detective]] and SMT-backed tooling such as [[r2smt]] and [[drill-and-join]]; pairs with other Vector35 BN plugins such as [[tanto]] and [[obfuscation-analysis]].

## Links

- Repo: https://github.com/Vector35/OpaquePredicatePatcher

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[opaque-predicates-detective]] · [[obfuscation-analysis]] · [[drill-and-join]] · [[r2smt]] · [[tanto]] · [[official-plugins]] · [[community-plugins]]
