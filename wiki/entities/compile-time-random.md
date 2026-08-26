---
title: compile-time-random
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Deniskore__CompileTimeRandom.md
updated: 2026-08-26
confidence: medium
---

# compile-time-random

C++11 header-only compile-time random number utility. Uses `constexpr` hashing and generator logic—including FNV and Murmur3-style operations—to produce deterministic values during compilation. Exposes macros for 32-bit and 64-bit compile-time random constants without runtime RNG calls. Mainly useful for low-level tooling, lightweight obfuscation patterns, and game-security research code that benefits from compile-time value generation (Anti Cheat → Compile Time). (source: wiki/sources/descriptions/Deniskore__CompileTimeRandom.md)

Complements string/constant protectors such as [[xorstr]] / [[obfuscate]] / [[crystr]] / [[oxorany]] and other compile-time utilities like [[compile-time-regular-expressions]] when per-build randomized keys, salts, or opaque constants are needed without pulling in runtime entropy APIs. Not a string crypter or full obfuscation engine.

## Links

- Repo: https://github.com/Deniskore/CompileTimeRandom

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[xorstr]] · [[obfuscate]] · [[crystr]] · [[oxorany]] · [[compile-time-regular-expressions]] · [[skcrypter]]
