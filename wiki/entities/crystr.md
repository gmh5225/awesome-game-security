---
title: crystr
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/android1337__crystr.md
updated: 2026-08-18
confidence: medium
---

# crystr

C++20 compile-time string and numeric constant obfuscation library. XOR-encrypts literals using keys derived from compile-time math, timestamps, and counters; decrypts at runtime via inline or virtual paths. Macros cover strings and numeric constants with per-character and per-value key variation to reduce static pattern readability. Aimed at anti-reversing and game security hardening where cleartext constants are easy extraction targets (Anti Cheat → Compile Time / String Crypter). (source: wiki/sources/descriptions/android1337__crystr.md)

Useful alongside xorstr-style compile-time crypters such as [[skcrypter]] / [[mystic-xorstr]] / [[xorlit]] / [[obfuscxx]] / [[sbox]]; sibling call-site obfuscation via [[crycall]] from the same author. Recovery-side counterpart [[ida-jm-xorstr-decrypt-plugin]] targets JM Xorstr-style strings in IDA. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/android1337/crystr

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[crycall]] · [[skcrypter]] · [[mystic-xorstr]] · [[xorlit]] · [[obfuscxx]] · [[sbox]] · [[oxorany]]
