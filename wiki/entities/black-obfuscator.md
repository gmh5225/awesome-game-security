---
title: BlackObfuscator
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/CodingGay__BlackObfuscator.md
updated: 2026-08-27
confidence: medium
---

# BlackObfuscator

**BlackObfuscator** is a DEX control-flow obfuscation tool for Android applications. Implemented mainly in Java, it uses a modified dex2jar pipeline to transform bytecode without changing app behavior. Configurable obfuscation depth, package targeting, and rule-based processing support selective hardening; companion GUI and Android Studio plugin integrations wrap build-time workflows. Intended for mobile application protection and reverse-engineering resistance research. (source: wiki/sources/descriptions/CodingGay__BlackObfuscator.md)

Complements symbol-oriented hardening such as [[proguard]] and bytecode edit/decompile lanes ([[dex2jar]], [[recaf]], [[jadx]], [[apktool]]) when studying or bypassing DEX control-flow obfuscation on protected Android clients.

## Links

- Repo: https://github.com/CodingGay/BlackObfuscator

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[proguard]] · [[dex2jar]] · [[recaf]] · [[jadx]] · [[apktool]] · [[deobfuscator]]
