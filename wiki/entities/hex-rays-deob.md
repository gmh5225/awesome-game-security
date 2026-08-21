---
title: HexRaysDeob
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/RolfRolles__HexRaysDeob.md
updated: 2026-08-21
confidence: medium
---

# HexRaysDeob

**HexRaysDeob** (RolfRolles) is a **Hex-Rays microcode plugin** for deobfuscating protected binaries. Written in C++ against the IDA and Hex-Rays SDK, it applies pattern-based simplification passes to obfuscated expressions and implements **control-flow unflattening** that reconstructs dispatcher-driven flattened regions and cleans up unreachable blocks. Intended for reverse-engineering workflows on obfuscated game and malware code. (source: wiki/sources/descriptions/RolfRolles__HexRaysDeob.md)

Complements decompiler-time CFF recovery tools such as [[d810-ng]] and microcode-oriented plugins like [[genmc]] in the Hex-Rays Microcode lane.

## Links

- Repo: https://github.com/RolfRolles/HexRaysDeob

## Related

[[d810-ng]] · [[ollvm-unflattener]] · [[idadeflat]] · [[genmc]] · [[control-flow-flattening]] · [[obfuscation-analysis]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
