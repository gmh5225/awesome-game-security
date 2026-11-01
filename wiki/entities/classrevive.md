---
title: ClassRevive
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/t1zzo__classrevive.md
updated: 2026-11-01
confidence: medium
---

# ClassRevive

Gradle-based Java application that runs CFR, Vineflower, Procyon, and JADX in isolated worker JVMs, recompiles each candidate with `javac`, and picks the best output per file and per method using signature and round-trip checks against original bytecode. Accepts class files, JARs, multi-release archives, Android APK/DEX, and executables with embedded JARs; profiles obfuscation, applies automatic reversals for Skidfuscator and Aidsfuscator, and can restore names from ProGuard/R8 mappings. Swing workbench and CLI emit HTML/JSON confidence reports, IDE project exports, and optional native-library triage with Ghidra—aimed at evidence-backed decompilation of obfuscated Java game clients without executing analyzed code. (source: wiki/sources/descriptions/t1zzo__classrevive.md)

Listed under README **Cheat** / RE Tools beside [[deobfuscator]] and [[jadx]] JVM bytecode lanes; see [[overviews/reverse-engineering]] and [[overviews/game-hacking]].

## Links

- Repo: https://github.com/t1zzo/classrevive
