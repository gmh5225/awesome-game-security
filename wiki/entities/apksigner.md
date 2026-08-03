---
title: apksigner
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/jixiaoyong__ApkSigner.md
updated: 2026-08-03
confidence: medium
---

# apksigner

Standalone Android APK signing tool ([jixiaoyong/ApkSigner](https://github.com/jixiaoyong/ApkSigner)). The current version’s functions are relatively stable and cover basic signing needs for repack/mod workflows after decode–patch–rebuild steps (apktool, smali edits, native `.so` swaps). Aimed at game security researchers and reverse engineers working in cheat / RE tooling lanes. (source: wiki/sources/descriptions/jixiaoyong__ApkSigner.md)

Complements signature-transplant research via [[apksigcopier]] and APK signature-crack study via [[asctool]]—here the focus is straightforward re-signing with a key, not copying existing Signing Blocks or cracking verification helpers.

## Links

- Repo: https://github.com/jixiaoyong/ApkSigner

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apksigcopier]] · [[asctool]] · [[dex2jar]] · [[apktool-mcp-server]]
