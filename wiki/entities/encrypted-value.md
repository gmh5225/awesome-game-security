---
title: encrypted_value
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/serge-14__encrypted_value.md
updated: 2026-07-23
confidence: medium
---

# encrypted_value

Simple header-only C++ library for encrypting scalar values in-process so plaintext integers/floats are harder to find with memory scanners. Aimed at anti-cheat engineers and defensive researchers in the Anti Cheat → Encrypt Variable lane. (source: wiki/sources/descriptions/serge-14__encrypted_value.md)

Complements compile-time string/integer crypters such as [[skcrypter]] / [[mystic-xorstr]] / [[sbox]] (those focus more on literals at compile time); pairs with engine-side static hiding like [[static-variables-obfuscator-ue4]]. Not a full obfuscation engine or packer.

## Links

- Repo: https://github.com/serge-14/encrypted_value

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[skcrypter]] · [[mystic-xorstr]] · [[sbox]] · [[obfusk8]] · [[static-variables-obfuscator-ue4]]
