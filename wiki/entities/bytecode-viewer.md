---
title: Bytecode Viewer
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/gmh5225__bytecode-viewer.md
updated: 2026-08-09
confidence: medium
---

# Bytecode Viewer

**Bytecode Viewer** is a Java/Android APK reverse engineering suite that integrates multiple decompilers—CFR, Procyon, FernFlower, JD-GUI, and Krakatau—into a single tabbed interface. It supports viewing Java bytecode, decompiled source, and Smali simultaneously for JAR, class, DEX, and APK inputs, with search, string extraction, and plugin support. Aimed at Java and Android reverse engineers who want to compare decompiler outputs and analyze bytecode in one unified environment. (source: wiki/sources/descriptions/gmh5225__bytecode-viewer.md)

Complements decode/decompile lanes ([[apktool]], [[jadx]], [[dex2jar]]) and structural triage via [[android-classyshark]]; pairs with JVM bytecode tooling such as [[deobfuscator]] and [[raung]] when comparing recovered source against raw bytecode or smali.

## Links

- Repo: https://github.com/gmh5225/bytecode-viewer

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[apktool]] · [[jadx]] · [[android-classyshark]] · [[dex2jar]] · [[deobfuscator]] · [[raung]]
