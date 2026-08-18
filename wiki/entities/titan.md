---
title: Titan
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/archercreat__titan.md
updated: 2026-08-18
confidence: medium
---

# Titan

VMProtect devirtualizer that lifts virtualized code into analyzable LLVM-oriented output. Uses Triton for emulation and symbolic execution, identifies VM handlers through AST pattern matching, and reconstructs control-flow structure from virtual execution. The toolchain includes custom optimization passes and workflows around intrinsics and virtual entry-point analysis. Intended for reverse engineering research on protected binaries, including anti-cheat and software protection studies. (source: wiki/sources/descriptions/archercreat__titan.md)

Companion surface to [[novmp]] (static VTIL lift) and [[novmpy]] (Python/Triton symbolic handler recovery): LLVM-oriented lift with AST-based handler identification and CFG reconstruction rather than VTIL static devirt or trace-only recovery.

## Links

- Repo: https://github.com/archercreat/titan

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[novmp]] · [[novmpy]] · [[rumba]] · [[vmattack]] · [[vmp-devirtualization-lab]]
