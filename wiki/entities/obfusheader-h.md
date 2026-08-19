---
title: obfusheader.h
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ac3ss0r__obfusheader.h.md
updated: 2026-08-19
confidence: medium
---

# obfusheader.h

Header-only C++ obfuscation library for hardening binaries against straightforward static analysis. Provides compile-time encryption for strings and constants, import and call hiding, control-flow mutation, and anti-decompiler oriented techniques. Targets C++14 and newer compilers across Windows and Unix-like environments. Primarily used in software protection and game security scenarios where developers want to increase reverse engineering cost (Anti Cheat → Obfuscation Engine / Compile Time). (source: wiki/sources/descriptions/ac3ss0r__obfusheader.h.md)

Broader than string-only crypters such as [[obfuscate]] / [[skcrypter]] / [[crystr]]; complements call-hiding libraries such as [[crycall]] and general compile-time toolkits such as [[obfusk8]]. Not a commercial packer or VM-based protector.

## Links

- Repo: https://github.com/ac3ss0r/obfusheader.h

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfuscate]] · [[crycall]] · [[obfusk8]] · [[obfuscxx]] · [[brkida]]
