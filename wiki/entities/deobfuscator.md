---
title: Deobfuscator
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/narumii__Deobfuscator.md
  - wiki/sources/descriptions/gmh5225__deobfuscator.md
updated: 2026-08-09
confidence: medium
---

# Deobfuscator

Two related Java bytecode deobfuscator projects share this name in the curated list. Both target obfuscated JVM class files—recovering readable structure from protected Java game clients, tooling, and Android APK/DEX surfaces alongside [[raung]] (bytecode asm/disasm) and [[jdbg]] (JDWP attach debug).

## gmh5225/deobfuscator

Java bytecode deobfuscator for reversing obfuscation from ProGuard, Allatori, ZKM, and other Java obfuscators. Applies transformation passes to remove string encryption, restore control flow, simplify opaque predicates, rename obfuscated identifiers, and clean up dead code in Java class files. Aimed at Java reverse engineers and malware analysts deobfuscating protected Java/Android applications. (source: wiki/sources/descriptions/gmh5225__deobfuscator.md)

## narumii/Deobfuscator

General Java bytecode deobfuscator (narumii/Deobfuscator). Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / RE tools lane—recovering readable Java class structure from obfuscated JVM clients and tooling. (source: wiki/sources/descriptions/narumii__Deobfuscator.md)

Scoped as JVM bytecode tooling rather than native OLLVM/VMP unpackers; pairs with mobile static lanes such as [[jadx]] and [[apktool]] when analyzing obfuscated Android APKs.

## Links

- Repo (gmh5225): https://github.com/gmh5225/deobfuscator
- Repo (narumii): https://github.com/narumii/Deobfuscator

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[raung]] · [[jdbg]] · [[deobf]] · [[obfuscar]] · [[jadx]] · [[apktool]]
