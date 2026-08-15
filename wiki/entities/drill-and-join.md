---
title: DrillAndJoin
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/fvrmatteo__DrillAndJoin.md
updated: 2026-08-15
confidence: medium
---

# DrillAndJoin

C++17 header-only library implementing the **Drill & Join** synthesis algorithm for recovering simplified Boolean and bit-vector expressions from obfuscated predicates. Combines exact finite-domain synthesis over Algebraic Normal Form (ANF) with an SMT-backed workflow using **Bitwuzla** to soundly simplify 64-bit opaque predicates—including MBA-style obfuscation and point-function cases—without exhaustively searching the full 64-bit input space. (source: wiki/sources/descriptions/fvrmatteo__DrillAndJoin.md)

Pipeline: SMT-guided bit dependency reduction → Drill & Join on reduced support → accept replacements only when Bitwuzla proves equivalence under optional path constraints from concolic execution. Includes demos, trace examples, and a truth-table synthesis CLI for researchers deobfuscating opaque predicates, branch conditions, and MBA expressions in protected or game-related binaries.

Synthesis lane complementing algebraic MBA simplifiers such as [[cobra]] and IDA oracle-guided workflows such as [[qsynthesis]]; shares Bitwuzla/SMT backends with [[r2smt]] opaque-predicate tooling.

## Links

- Repo: https://github.com/fvrmatteo/DrillAndJoin

## Related

[[overviews/reverse-engineering]] · [[mixed-boolean-arithmetic]] · [[cobra]] · [[qsynthesis]] · [[stp]] · [[r2smt]] · [[opaque-predicates-detective]] · [[obfuscation-analysis]]
