---
title: FFS Explorer
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/KlasScripts__FFS-Explorer.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# FFS Explorer

Cross-platform **PySide6** desktop viewer for iOS and Android **full file system (FFS)** extractions packaged as ZIP archives from GrayKey and Cellebrite UFED workflows. Streams and seeks inside archives without unpacking entire images, reconstructs vendor metadata (including Cellebrite MessagePack sidecars and GrayKey ZIP extra fields), and exposes SQLite/WAL preview, plist/LevelDB parsers, keyword search, and declarative per-app artifact shortcuts for mobile examiners. (source: wiki/sources/descriptions/KlasScripts__FFS-Explorer.md)

## Role in game security

Supports **mobile cheat and integrity investigations** when reviewers need to validate what commercial suites report against raw on-disk app data—complementary to static APK analyzers such as [[mobsentry]] and consensual PC-check workflows, not a live anti-cheat product.

## Related

[[mobsentry]] · [[jaranalyzer]] · [[alibi]] · [[dexcheck]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]]
