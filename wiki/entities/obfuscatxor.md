---
title: obfuscatxor
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/redskal__obfuscatxor.md
updated: 2026-07-24
confidence: medium
---

# obfuscatxor

Go string crypter that generates encrypted string variables for use in application code. Keeps plaintext literals out of static binaries—useful for anti-cheat engineers and defensive researchers in the Anti Cheat → Compile Time / String Crypter lane (Go counterpart to C++ xorstr-style tools). (source: wiki/sources/descriptions/redskal__obfuscatxor.md)

Useful alongside C++ compile-time string crypters such as [[skcrypter]] / [[mystic-xorstr]] / [[sbox]]; not a full obfuscation engine or packer.

## Links

- Repo: https://github.com/redskal/obfuscatxor

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[skcrypter]] · [[mystic-xorstr]] · [[sbox]] · [[obfusk8]] · [[encrypted-value]]
