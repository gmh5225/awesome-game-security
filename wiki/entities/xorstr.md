---
title: xorstr
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/JustasMasiulis__xorstr.md
updated: 2026-08-24
confidence: medium
---

# xorstr

C++17 compile-time string encryption library. Uses vectorized SSE or AVX operations and inline decryption helpers to keep runtime usage lightweight. Design aims to keep string data out of normal read-only data sections and generate keys during compilation. Widely used for obfuscation in security tooling, reverse engineering challenges, and game security experiments (Anti Cheat → String Crypter). (source: wiki/sources/descriptions/JustasMasiulis__xorstr.md)

Canonical JM Xorstr implementation referenced by recovery tooling such as [[ida-jm-xorstr-decrypt-plugin]] and [[anti-xorstr]]. Useful alongside other compile-time string crypters such as [[skcrypter]] / [[mystic-xorstr]] / [[obfuscate]] / [[crystr]]. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/JustasMasiulis/xorstr

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[ida-jm-xorstr-decrypt-plugin]] · [[anti-xorstr]] · [[skcrypter]] · [[mystic-xorstr]] · [[obfuscate]] · [[crystr]]
