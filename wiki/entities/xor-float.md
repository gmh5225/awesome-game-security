---
title: xor-float
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/obama-gaming__xor-float.md
updated: 2026-07-27
confidence: medium
---

# xor-float

C++ project focused on XOR-based float (and related scalar) value encryption so plaintext floats are harder to find with memory scanners. Listed under Anti Cheat → Encrypt Variable; useful for anti-cheat engineers and defensive researchers studying in-process value hiding. (source: wiki/sources/descriptions/obama-gaming__xor-float.md)

Complements scalar encrypt libs such as [[encrypted-value]] and compile-time string/integer crypters like [[skcrypter]] / [[mystic-xorstr]]; pairs with engine-side static hiding like [[static-variables-obfuscator-ue4]]. Not a full obfuscation engine or packer.

## Links

- Repo: https://github.com/obama-gaming/xor-float

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[encrypted-value]] · [[skcrypter]] · [[mystic-xorstr]] · [[static-variables-obfuscator-ue4]]
