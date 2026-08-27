---
title: Obfuscapk
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/ClaudiuGeorgiu__Obfuscapk.md
updated: 2026-08-27
confidence: medium
---

# Obfuscapk

**Obfuscapk** is a modular Python tool for black-box obfuscation of Android applications. It decompiles APKs with [[apktool]], applies configurable obfuscation passes to smali code, resources, and manifests, and rebuilds functionally equivalent but harder-to-analyze outputs. The repository ships multiple obfuscator plugins, documentation, and early support for Android App Bundles through an external decompiler component. Mobile security researchers and developers use it to evaluate resilience against reverse engineering and signature-based detection. (source: wiki/sources/descriptions/ClaudiuGeorgiu__Obfuscapk.md)

Complements bytecode-level hardening such as [[black-obfuscator]] and [[proguard]], and pairs with decode/decompile/edit lanes ([[jadx]], [[recaf]], [[deobfuscator]]) when studying protected Android clients.

## Links

- Repo: https://github.com/ClaudiuGeorgiu/Obfuscapk

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apktool]] · [[black-obfuscator]] · [[proguard]] · [[jadx]] · [[recaf]] · [[deobfuscator]]
