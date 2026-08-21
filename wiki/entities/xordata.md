---
title: XorData
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Sherman0236__XorData.md
updated: 2026-08-21
confidence: medium
---

# XorData

C++17 framework for compile-time and runtime-style obfuscation of constants, variables, and strings. Uses XOR-based data transformations to make static inspection of embedded values harder in compiled binaries. Includes example outputs and helper structures for integrating obfuscation patterns into normal application code. Primary use case is software hardening experiments and anti-analysis techniques in security-sensitive code (Anti Cheat → Compile Time / Obfuscation Engine). (source: wiki/sources/descriptions/Sherman0236__XorData.md)

Useful alongside compile-time string/constant crypters such as [[obfuscate]] / [[crystr]] / [[xorlit]] / [[skcrypter]] / [[mystic-xorstr]] / [[obfusheader-h]]. Broader than string-only crypters by covering variables and constants; not a full commercial protector or VM obfuscation engine.

## Links

- Repo: https://github.com/Sherman0236/XorData

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfuscate]] · [[crystr]] · [[xorlit]] · [[skcrypter]] · [[mystic-xorstr]] · [[obfusheader-h]] · [[obfuscxx]]
