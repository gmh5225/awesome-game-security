---
title: Obfuscate
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/adamyaxley__Obfuscate.md
updated: 2026-08-19
confidence: medium
---

# Obfuscate

Header-only C++14 library for compile-time string literal obfuscation. Encrypts literals with `constexpr` logic and randomized keys, then decrypts them at runtime when needed. The API is intentionally simple: wrap strings with a macro for minimal integration into existing code. Main use case is reducing trivial string extraction during reverse engineering of game-security-related binaries (Anti Cheat → String Crypter). (source: wiki/sources/descriptions/adamyaxley__Obfuscate.md)

Useful alongside other compile-time string crypters such as [[skcrypter]] / [[crystr]] / [[mystic-xorstr]] / [[xorlit]] / [[obfuscatxor]]. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/adamyaxley/Obfuscate

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[skcrypter]] · [[crystr]] · [[mystic-xorstr]] · [[xorlit]] · [[obfuscatxor]] · [[oxorany]]
