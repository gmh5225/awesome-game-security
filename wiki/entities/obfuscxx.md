---
title: obfuscxx
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/nevergiveup-c__obfuscxx.md
updated: 2026-07-28
confidence: medium
---

# obfuscxx

Header-only compile-time variables obfuscation library for C++20 and later. Runtime decryption uses SIMD (AVX2 / SSE2 / NEON), which complicates static analysis of protected literals and values. Compiler support: MSVC (+WDM), LLVM, GCC; architectures: x86-64 and ARM. Aimed at anti-cheat engineers and defensive researchers in the Anti Cheat → Encrypt Variable / Compile Time lane. (source: wiki/sources/descriptions/nevergiveup-c__obfuscxx.md)

Sits alongside SIMD xorstr-style crypters such as [[mystic-xorstr]] / [[skcrypter]] / [[sbox]] / [[obfusk8]], and scalar Encrypt Variable samples such as [[encrypted-value]] / [[xor-float]]. Not a full obfuscation engine, packer, or commercial protector.

## Links

- Repo: https://github.com/nevergiveup-c/obfuscxx

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[mystic-xorstr]] · [[skcrypter]] · [[sbox]] · [[obfusk8]] · [[encrypted-value]] · [[xor-float]]
