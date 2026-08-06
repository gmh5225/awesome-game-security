---
title: cthash
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/hanickadot__cthash.md
updated: 2026-08-06
confidence: medium
---

# cthash

C++ library for **constexpr implementation of SHA-2 and SHA-3 family hashes**. Provides `hash_value` literals in namespace `cthash::literals` (parenthesis suffixes per hash function type), enabling digest precomputation at compile time instead of runtime crypto calls. Aimed at anti-cheat engineers and defensive security researchers in the Anti Cheat → Compile Time lane. (source: wiki/sources/descriptions/hanickadot__cthash.md)

Useful alongside compile-time string/constant protectors such as [[skcrypter]] / [[oxorany]] when building integrity checks, fingerprint tables, or constexpr-guarded constants without embedding runtime hash APIs. Not a string crypter or full obfuscation engine.

## Links

- Repo: https://github.com/hanickadot/cthash

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[skcrypter]] · [[oxorany]] · [[sbox]] · [[obfusk8]]
