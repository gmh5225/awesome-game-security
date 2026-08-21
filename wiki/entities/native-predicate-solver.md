---
title: native-predicate-solver
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ScriptWare-Software__native-predicate-solver.md
updated: 2026-08-21
confidence: medium
---

# native-predicate-solver

Native **Binary Ninja plugin** for removing opaque predicates from obfuscated binaries (ScriptWare-Software). Implemented in modern C++, it analyzes MLIL conditional branches to detect always-true or always-false conditions. Supports single-function and whole-binary passes with configurable limits and multithreaded processing for large programs. Target audience: reverse engineers who need faster deobfuscation workflows during malware analysis or protected binary research. (source: wiki/sources/descriptions/ScriptWare-Software__native-predicate-solver.md)

Complements Python [[opaque-predicate-patcher]] (Vector35; iterative branch patching) and detection-oriented [[opaque-predicates-detective]]; pairs with SMT-backed [[drill-and-join]] and [[r2smt]] plus BN obfuscation tooling such as [[obfuscation-analysis]].

## Links

- Repo: https://github.com/ScriptWare-Software/native-predicate-solver

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[opaque-predicate-patcher]] · [[opaque-predicates-detective]] · [[obfuscation-analysis]] · [[drill-and-join]] · [[r2smt]] · [[official-plugins]] · [[community-plugins]]
