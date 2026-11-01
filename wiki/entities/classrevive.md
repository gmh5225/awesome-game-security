---
title: ClassRevive
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/t1zzo__classrevive.md
  - wiki/sources/README-categories.md
updated: 2026-11-01
confidence: high
---

# ClassRevive

**Multi-engine Java decompiler workbench** (t1zzo; Gradle; Cheat / RE Tools). Recovers readable Java source from compiled bytecode and **measures structural correctness** of each candidate rather than trusting a single decompiler pass. Runs **CFR**, **Vineflower**, **Procyon**, and **JADX** in isolated worker JVMs, recompiles each output with **`javac`**, and selects the best result **per file and per method** using signature and round-trip checks against the original classes. Targets reverse engineers and security researchers who need **evidence-backed** decompilation of obfuscated or packaged Java—including game clients and protectors—**without executing** the analyzed code. (source: wiki/sources/descriptions/t1zzo__classrevive.md)

## Inputs and packaging

Accepts class files, JARs, multi-release archives, **Android APK/DEX**, and executables with embedded JARs. Optional **ProGuard/R8 mapping** restore can reinstate obfuscated names when mappings are available.

## Obfuscation handling

Profiles obfuscation characteristics on the input, applies automatic reversals for **Skidfuscator** and **Aidsfuscator**, and complements single-engine tools such as [[jadx]] and [[deobfuscator]] when JVM clients need graded recovery rather than one-shot decompile.

## Outputs

Swing desktop workbench and **CLI** produce **HTML/JSON confidence reports**, IDE project exports, and optional **native-library triage** with [[ghidra]]. Fits [[binary-evidence]] workflows where decompiler output must be corroborated before treating recovered logic as findings.

## Links

- Repo: https://github.com/t1zzo/classrevive

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[jadx]] · [[deobfuscator]] · [[binary-evidence]] · [[leaf-mod-analyzer]] · [[jaranalyzer]] · [[apktool]]
