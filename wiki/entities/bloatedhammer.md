---
title: BloatedHammer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/rad9800__BloatedHammer.md
updated: 2026-07-25
confidence: medium
---

# BloatedHammer

C++20 sample for **API hammering** implemented with fold expressions (avoiding explicit loops). Aimed at anti-cheat engineers and defensive researchers in the Anti Cheat → Compile Time lane—studying how compile-time metaprogramming can emit dense, loop-free API call sequences that bloat call volume / delay execution without classic loop patterns. (source: wiki/sources/descriptions/rad9800__BloatedHammer.md)

Complements other Compile Time references such as [[syscalls-cpp]] / [[obfusk8]] / [[skcrypter]] (stubs, obfuscation, string crypters) rather than a full protector or packer. Same author as early-boot [[bootexecute-edr]] research.

## Links

- Repo: https://github.com/rad9800/BloatedHammer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[syscalls-cpp]] · [[obfusk8]] · [[skcrypter]] · [[bootexecute-edr]]
