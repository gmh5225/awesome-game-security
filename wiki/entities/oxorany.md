---
title: oxorany
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/llxiaoyuan__oxorany.md
updated: 2026-07-31
confidence: medium
---

# oxorany

C/C++ header library for **obfuscated compile-time encryption of arbitrary constants** on any platform. Values are encrypted at build time and decrypted at runtime, hiding literals (strings, integers, and other constexpr data) from static analysis and memory scanners. Aimed at anti-cheat engineers and defensive security researchers in the Anti Cheat → Compile Time lane. (source: wiki/sources/descriptions/llxiaoyuan__oxorany.md)

Sits alongside platform-agnostic xorstr-style crypters such as [[mystic-xorstr]] / [[obfuscxx]] / [[skcrypter]] / [[sbox]] / [[obfusk8]], and scalar Encrypt Variable samples such as [[encrypted-value]]. Not a full obfuscation engine, packer, or commercial protector.

## Links

- Repo: https://github.com/llxiaoyuan/oxorany

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[mystic-xorstr]] · [[obfuscxx]] · [[skcrypter]] · [[sbox]] · [[obfusk8]] · [[encrypted-value]]
