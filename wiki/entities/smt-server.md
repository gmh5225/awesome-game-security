---
title: smt-server
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/LLVMParty__smt-server.md
updated: 2026-08-23
confidence: medium
---

# smt-server

Rust-based SMT solver server for QF_BV (quantifier-free bitvector) logic. Parses SMT-LIB 2 formulas, bit-blasts to SAT, and exposes C++/Python client libraries for integration with binary analysis and deobfuscation pipelines. Sits in the Cheat Mixed boolean-arithmetic / constraint-solver lane beside standalone solvers such as [[stp]] and radare2-integrated tools like [[r2smt]]. (source: wiki/sources/descriptions/LLVMParty__smt-server.md)

## Links

- Repo: https://github.com/LLVMParty/smt-server

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[stp]] · [[r2smt]] · [[cobra]] · [[drill-and-join]] · [[obfuscation-analysis]]
