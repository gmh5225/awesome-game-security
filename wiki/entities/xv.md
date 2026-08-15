---
title: xv
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/emlinhax__xv.md
updated: 2026-08-15
confidence: medium
---

# xv

Single-header C++ pointer/value encryption library (`xv::xval<T>`) that hides scalars and pointers in-process so plaintext values are harder to find with memory scanners. Per-variable algorithm randomization is intended to complicate static analysis; no external dependencies. Listed under Anti Cheat → Encrypt Variable; useful for anti-cheat engineers and defensive researchers studying in-process value hiding. (source: wiki/sources/descriptions/emlinhax__xv.md)

Complements scalar encrypt libs such as [[encrypted-value]] and [[xor-float]], and compile-time variable obfuscation such as [[obfuscxx]]; pairs with engine-side static hiding like [[static-variables-obfuscator-ue4]]. Not a full obfuscation engine or packer.

## Links

- Repo: https://github.com/emlinhax/xv

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[encrypted-value]] · [[xor-float]] · [[obfuscxx]] · [[static-variables-obfuscator-ue4]]
