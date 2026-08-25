---
title: ProGuard
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Guardsquare__proguard.md
updated: 2026-08-25
confidence: medium
---

# ProGuard

**Java bytecode shrinker, optimizer, obfuscator, and preverifier** for applications and libraries. Removes unused classes, fields, methods, and attributes to reduce package size and improve runtime efficiency; applies bytecode optimizations; and renames symbols to make reverse engineering harder while preserving behavior through configurable keep/rename rules. Implemented primarily in Java and commonly integrated through command-line workflows and Gradle builds for software protection and deployment hardening. (source: wiki/sources/descriptions/Guardsquare__proguard.md)

Upstream open-source obfuscator in the Guardsquare toolchain; Android builds often use R8 (ProGuard-compatible rules) while this repo remains the reference Java bytecode hardening lane. Pairs with RE tooling such as [[deobfuscator]], [[obfu-de-scate]], and [[apkid]] when analyzing obfuscated JVM/Android clients.

## Links

- Repo: https://github.com/Guardsquare/proguard

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[deobfuscator]] · [[obfu-de-scate]] · [[apkid]] · [[jadx]] · [[apktool]]
