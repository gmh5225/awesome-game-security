---
title: mixed-boolean-transform
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/mizt0__mixed-boolean-transform.md
updated: 2026-07-29
confidence: medium
---

# mixed-boolean-transform

Source-to-source C++ obfuscation tool that replaces integer constants and arithmetic expressions with semantically equivalent mixed boolean-arithmetic (MBA) expressions. Uses Z3 SMT verification to prove equivalence; builds large polynomial MBA identities over bitwise operators (`&`, `|`, `^`, `~`) with Eigen3 linear algebra and GMP arbitrary-precision integers. (source: wiki/sources/descriptions/mizt0__mixed-boolean-transform.md)

Compile-time / source-level MBA transform in the Cheat Mixed boolean-arithmetic lane — complements sample generators ([[mutaben]], [[mba-obfuscator]]) and simplifiers ([[cobra]]) for obfuscation–deobfuscation RE pipelines.

## Links

- Repo: https://github.com/mizt0/mixed-boolean-transform

## Related

[[mixed-boolean-arithmetic]] · [[overviews/reverse-engineering]] · [[mutaben]] · [[mba-obfuscator]] · [[cobra]] · [[stp]]
