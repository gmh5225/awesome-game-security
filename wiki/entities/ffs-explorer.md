---
title: FFS Explorer
kind: entity
topics: [anti-cheat, mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/KlasScripts__FFS-Explorer.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# FFS Explorer

Cross-platform **PySide6** desktop application for browsing **iOS and Android full file system (FFS)** extractions packaged as ZIP archives from common mobile forensic vendors—**without unpacking the image first**. Implemented in Python; reads archives via direct offset seeks, including vendor-specific handling of **Cellebrite MessagePack** sidecar metadata and **GrayKey** ZIP extra-field timestamps and attributes. (source: wiki/sources/descriptions/KlasScripts__FFS-Explorer.md)

## Capabilities

| Area | Coverage |
|------|----------|
| Archive access | Stream-browse ZIP FFS dumps; seek by offset (no full unpack) |
| Vendor metadata | Cellebrite MessagePack sidecars; GrayKey ZIP extra fields |
| Built-in viewers | SQLite (+ WAL diff and carving), property lists, LevelDB / IndexedDB, SEGB logs, hex dumps |
| Media recovery | Embedded media from BLOBs and plists |
| Artifact framework | Declarative per-app parsers (messaging, browser, system) on iOS and Android |
| Search / typing | Keyword search; header-based file typing |
| Reporting | Optional AI-assisted reporting for examiners |

## Role in game security

Targets **digital forensics practitioners and researchers** who need extraction layout inspection, validation of what mainstream suites report against raw on-disk files, and study of how mobile app data is stored. Supports **mobile cheat and integrity investigations** when reviewers must reconcile commercial tool output with raw app artifacts—complementary to static APK analyzers such as [[mobsentry]] and consensual PC-check workflows, not a live anti-cheat product.

## Links

- Repo: https://github.com/klasscripts/ffs-explorer

## Related

[[mobsentry]] · [[bagbak]] · [[jaranalyzer]] · [[alibi]] · [[dexcheck]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]]
