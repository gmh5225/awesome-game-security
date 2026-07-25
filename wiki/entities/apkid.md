---
title: APKiD
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/rednaga__APKiD.md
updated: 2026-07-24
confidence: medium
---

# APKiD

Android application identifier (“PEiD for Android”) that fingerprints compilers, packers, obfuscators, and anti-analysis techniques in APK/DEX files via YARA rules. Covers ProGuard, DexGuard, Bangcle, Ijiami, and many other commercial/custom protectors; Python CLI reports detections and versions for initial triage before deeper RE. (source: wiki/sources/descriptions/rednaga__APKiD.md)

Complements decode/decompile lanes ([[jadx]], [[apktool-mcp-server]], [[delamain]]), ProGuard/R8 name recovery ([[obfu-de-scate]]), and packed-sample unpackers ([[android-unpacker]]); peer to desktop packer/compiler ID such as [[die-engine-web]].

## Links

- Repo: https://github.com/rednaga/APKiD

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[jadx]] · [[apktool-mcp-server]] · [[delamain]] · [[obfu-de-scate]] · [[android-unpacker]] · [[die-engine-web]]
