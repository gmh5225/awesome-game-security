---
title: xorlit
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/igozdev__xorlit.md
updated: 2026-08-04
confidence: medium
---

# xorlit

String crypter that encrypts string literals for compile-time / build-time protection. When invoked with a single argument, the encryption key defaults to `xorlit::seed`. Aimed at anti-cheat engineers and defensive security researchers in the Anti Cheat → Compile Time / String Crypter lane. (source: wiki/sources/descriptions/igozdev__xorlit.md)

Useful as a lightweight compile-time string crypter alongside [[skcrypter]] / [[mystic-xorstr]] / [[sbox]] / [[obfuscatxor]]; recovery-side counterpart [[ida-jm-xorstr-decrypt-plugin]] targets JM Xorstr-style strings in IDA. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/igozdev/xorlit

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[skcrypter]] · [[mystic-xorstr]] · [[sbox]] · [[obfuscatxor]] · [[obfusk8]] · [[ida-jm-xorstr-decrypt-plugin]]
