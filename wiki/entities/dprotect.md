---
title: dProtect
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/open-obfuscator__dProtect.md
updated: 2026-07-26
confidence: medium
---

# dProtect

Android/iOS native-code obfuscator built on the LLVM obfuscator framework. C++ IR-level passes apply control-flow flattening, instruction substitution, string encryption, opaque predicates, and mixed boolean-arithmetic transformations—architecture-independent via the LLVM pipeline. Aimed at mobile developers and software-protection researchers hardening native mobile app code. (source: wiki/sources/descriptions/open-obfuscator__dProtect.md)

Useful as a mobile-oriented OLLVM-style Obfuscation Engine reference alongside [[kagura]] and lighter IR pass tools such as [[the-poor-mans-obfuscator]]; complementary to Swift identifier/string tools [[swiftshield]] / [[swift-string-obfuscator]].

## Links

- Repo: https://github.com/open-obfuscator/dProtect

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[kagura]] · [[the-poor-mans-obfuscator]] · [[swiftshield]] · [[swift-string-obfuscator]] · [[obfu-de-scate]]
