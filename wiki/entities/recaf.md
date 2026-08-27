---
title: Recaf
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/Col-E__Recaf.md
updated: 2026-08-27
confidence: medium
---

# Recaf

**Recaf** is a modern Java bytecode editing and reverse-engineering workstation for JVM and Android targets. Implemented in Java, it bundles multiple decompilers with bytecode assembly, recompilation support, and deep search across classes, constants, and instruction patterns. Deobfuscation-oriented workflows include automatic handling of malformed inputs, renaming assistance, and transformer utilities. Aimed at reverse engineers, security researchers, and developers analyzing or modifying compiled Java software. (source: wiki/sources/descriptions/Col-E__Recaf.md)

Complements multi-decompiler suites such as [[bytecode-viewer]] and static Android lanes ([[jadx]], [[apktool]]); pairs with bytecode tooling [[deobfuscator]] and [[raung]] when patching or deobfuscating JVM/DEX class files before recompilation.

## Links

- Repo: https://github.com/Col-E/Recaf

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[bytecode-viewer]] · [[jadx]] · [[apktool]] · [[deobfuscator]] · [[raung]] · [[proguard]]
