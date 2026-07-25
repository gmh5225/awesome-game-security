---
title: dex2jar
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/pxb1988__dex2jar.md
updated: 2026-07-25
confidence: medium
---

# dex2jar

Java toolset for converting Android DEX bytecode to Java class files (JAR) and back. Converted JARs feed standard Java decompilers (JD-GUI, CFR). Also ships `d2j-baksmali` disassembly plus APK signing and DEX manipulation utilities. Aimed at Android reverse engineers and security analysts who prefer Java-class analysis workflows over direct DEX tooling. (source: wiki/sources/descriptions/pxb1988__dex2jar.md)

Classic DEX↔JAR bridge beside direct DEX→Java decompilers such as [[jadx]], agent-facing wraps ([[delamain]], [[apktool-mcp-server]]), and packer/obfuscator triage ([[apkid]]).

## Links

- Repo: https://github.com/pxb1988/dex2jar

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[jadx]] · [[delamain]] · [[apktool-mcp-server]] · [[apkid]] · [[obfu-de-scate]] · [[android-unpacker]] · [[r2garlic]]
