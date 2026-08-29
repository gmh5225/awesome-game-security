---
title: obfstr
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/CasualX__obfstr.md
updated: 2026-08-29
confidence: medium
---

# obfstr

Rust library for compile-time string obfuscation. Provides macros such as `obfstr!`, `obfcstr!`, `obfbytes!`, `wide!`, and `random!` to embed obfuscated constants and decode them locally at runtime. The implementation focuses on lightweight source-level integration and reproducible build-time randomness rather than strong secret protection. Useful for developers and reverse-engineering researchers who want to reduce obvious plaintext artifacts in binaries (Anti Cheat → String Crypter). (source: wiki/sources/descriptions/CasualX__obfstr.md)

Sits alongside other compile-time string crypters such as [[xorstr]] / [[malstring]] / [[crystr]] / [[static-string-obfuscation]] / [[rust-obfuscator]]. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/CasualX/obfstr

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[xorstr]] · [[malstring]] · [[crystr]] · [[static-string-obfuscation]] · [[rust-obfuscator]] · [[garble]]
