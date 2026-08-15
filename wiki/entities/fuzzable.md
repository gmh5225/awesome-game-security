---
title: Fuzzable
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ex0dus-0x__fuzzable.md
updated: 2026-08-15
confidence: medium
---

# Fuzzable

**Fuzzable** is a framework that integrates with both C/C++ source code and binaries to help vulnerability researchers identify function targets that are viable for fuzzing. Aimed at game security researchers and reverse engineers studying offensive techniques in the cheat / Binary Ninja plugins lane — upstream target discovery before harness setup, not a coverage-guided fuzzer itself. (source: wiki/sources/descriptions/ex0dus-0x__fuzzable.md)

Sits beside coverage-guided Windows fuzzing ([[winafl]]), Intel-PT hypervisor fuzzing ([[qemu-nyx]]), and Binary Ninja automation ([[binary-ninja-mcp]]) in the Anti Cheat > Fuzzer research lane.

## Links

- Repo: https://github.com/ex0dus-0x/fuzzable (README tag: Fuzzer)

## Related

[[winafl]] · [[qemu-nyx]] · [[binary-ninja-mcp]] · [[ward]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
