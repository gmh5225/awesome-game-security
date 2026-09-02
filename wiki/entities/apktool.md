---
title: Apktool
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/iBotPeaches__Apktool.md
updated: 2026-09-02
confidence: medium
---

# Apktool

Java tool for reverse engineering Android APK files. Decodes resources to nearly original form (layouts, strings, assets), disassembles DEX to smali and reassembles after edits, decodes resource tables, parses `AndroidManifest.xml`, and repackages APKs with proper resource compilation — enabling inspection and modification without original source. Listed in the README under **[Apk]**. Aimed at Android reverse engineers, modders, and security researchers. (source: wiki/sources/descriptions/iBotPeaches__Apktool.md)

Core static APK decode/rebuild lane before DEX→Java decompilers such as [[jadx]]; Windows GUI wrapper [[apktoolgui]] bundles apktool, signapk, zipalign, and baksmali for drag-and-drop packaging workflows; agent-facing wrappers such as [[apktool-mcp-server]] expose the same workflows to MCP clients.

## Links

- Repo: https://github.com/iBotPeaches/Apktool
- Site: https://apktool.org/

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[jadx]] · [[apktoolgui]] · [[apktool-mcp-server]] · [[dex2jar]] · [[dalvikus]] · [[frida]] · [[il2cpp]]
