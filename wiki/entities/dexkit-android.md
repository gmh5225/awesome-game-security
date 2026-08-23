---
title: DexKit-Android
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/LuckyPray__DexKit-Android.md
updated: 2026-08-23
confidence: medium
---

# DexKit-Android

High-performance **Android DEX deobfuscation library** from LuckyPray for native-assisted code discovery. Combines **C++ NDK** components with **JNI** and **Kotlin-facing** integration to search classes and methods by **strings**, **relations**, and **opcode patterns**. Ships **Gradle** distribution, **prefab** packaging, and **CMake** linking for embedding in Android projects. Commonly used in Android reverse engineering for app analysis, hook-point discovery, and navigating obfuscated bytecode. (source: wiki/sources/descriptions/LuckyPray__DexKit-Android.md)

Complements static decode lanes ([[jadx]], [[apktool]], [[dex2jar]]) with programmatic in-process or embedded DEX query when analysts need pattern-driven discovery rather than manual GUI search.

## Links

- Repo: https://github.com/LuckyPray/DexKit-Android (README tag: [dex deobfuscator])

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[jadx]] · [[dex2jar]] · [[obfu-de-scate]] · [[deobfuscator]] · [[frida]] · [[glass]]
