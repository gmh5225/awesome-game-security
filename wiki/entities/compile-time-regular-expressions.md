---
title: compile-time-regular-expressions
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/hanickadot__compile-time-regular-expressions.md
updated: 2026-08-06
confidence: medium
---

# compile-time-regular-expressions

C++ **Compile Time Regular Expression (CTRE)** library: regex patterns are parsed and matched at compile time via constexpr, avoiding runtime regex engines and keeping pattern logic out of hot paths. CMake projects can add the repo as a subdirectory and link against the `ctre` target. Aimed at anti-cheat engineers and defensive security researchers in the Anti Cheat → Compile Time lane. (source: wiki/sources/descriptions/hanickadot__compile-time-regular-expressions.md)

Useful alongside other hanickadot compile-time utilities such as [[cthash]] and string/constant protectors like [[skcrypter]] / [[oxorany]] when building constexpr parsers, signature tables, or static validation without embedding runtime regex APIs. Not a string crypter or full obfuscation engine.

## Links

- Repo: https://github.com/hanickadot/compile-time-regular-expressions

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[cthash]] · [[skcrypter]] · [[oxorany]] · [[obfusk8]]
