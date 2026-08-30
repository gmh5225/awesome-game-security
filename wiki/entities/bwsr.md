---
title: BWSR
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/BossKoopa__BWSR.md
updated: 2026-08-30
confidence: medium
---

# BWSR

Cross-platform **inline hooking library** for **Arm64** and **Arm64e** devices. Implemented in **C**, it targets **iOS**, **Android**, **Linux**, and **macOS** for runtime native code interception. The project focuses on low-level patching primitives and ships build paths for multiple mobile and desktop platforms. Intended for security researchers and systems developers who need portable hook-based instrumentation in native binaries. (source: wiki/sources/descriptions/BossKoopa__BWSR.md)

Sits in the AArch64 native inline-hook lane beside [[and64-inline-hook]], [[android-inline-hook-arm64]], and [[dobby]], but spans iOS and desktop Unix targets in addition to Android.

## Links

- Repo: https://github.com/BossKoopa/BWSR

## Related

[[and64-inline-hook]] · [[android-inline-hook-arm64]] · [[dobby]] · [[adbi]] · [[kittymemory]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
