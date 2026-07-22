---
title: skCrypter
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/skadro-official__skCrypter.md
updated: 2026-07-22
confidence: medium
---

# skCrypter

Header-only C++ compile-time string encryption library: XOR-encodes string literals at compile time via constexpr and template metaprogramming, decrypts at runtime through a simple macro API. Keeps plaintext strings out of static binary analysis and signature scanners. Aimed at cheat developers and software-protection researchers in the Anti Cheat → Compile Time / String Crypter lane. (source: wiki/sources/descriptions/skadro-official__skCrypter.md)

Useful as a lightweight xorstr-style compile-time string crypter alongside [[mystic-xorstr]] / [[sbox]] / [[obfusk8]]; recovery-side counterpart [[ida-jm-xorstr-decrypt-plugin]] targets JM Xorstr-style strings in IDA. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/skadro-official/skCrypter

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[mystic-xorstr]] · [[sbox]] · [[obfusk8]] · [[ida-jm-xorstr-decrypt-plugin]] · [[obfcoder]]
