---
title: Android Inline Hook ARM64
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/GToad__Android_Inline_Hook_ARM64.md
updated: 2026-08-25
confidence: medium
---

# Android Inline Hook ARM64

Native **ARM64 Android inline hooking framework** for building shared libraries that patch target code paths at runtime. C, C++, and ARM64 assembly with Android NDK build scripts and stub logic for inline trampoline handling. Emphasizes **pure inline hooking** (not PLT hooking) and includes examples for register-level control inside hook handlers. Primary use case: mobile reverse engineering and game security experimentation where native function interception is required. (source: wiki/sources/descriptions/GToad__Android_Inline_Hook_ARM64.md)

Sits in the native Android hook lane beside [[and64-inline-hook]], [[dobby]], [[adbi]], and [[pyasm-patch]].

## Links

- Repo: https://github.com/GToad/Android_Inline_Hook_ARM64

## Related

[[and64-inline-hook]] · [[dobby]] · [[adbi]] · [[pyasm-patch]] · [[kittymemory]] · [[qbdi-tracer-android]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
