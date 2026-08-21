---
title: OpenSw
kind: entity
topics: [mobile-security, game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/RemiPelloux__OpenSw.md
updated: 2026-08-21
confidence: medium
---

# OpenSw

Standalone Android Nintendo Switch emulator derived from the Eden and yuzu codebases. Targets generic ARM64 devices with an optional AYN Thor optimization profile. C++ core with dynarmic ARM JIT recompilation, Vulkan and OpenGL rendering, and a Kotlin Android frontend. OpenSw-specific tooling includes build-ID-aware cheat import from Atmosphere and Eden formats, an in-game Cockpit panel, performance diagnostics with session snapshots, a dmnt-style cheat engine, per-game configuration profiles, and a Profile build variant with an automation bridge for lab testing. Aimed at Switch researchers, emulator developers, and users investigating game behavior, cheats, and Android-side Switch emulation. (source: wiki/sources/descriptions/RemiPelloux__OpenSw.md)

Adjacent to [[yuzu-android]] (yuzu Android port) and [[nuzu]] (desktop yuzu fork), but adds live cheat import, per-game profiles, and lab automation on top of the Eden/yuzu lineage.

## Links

- Repo: https://github.com/RemiPelloux/OpenSw

## Related

[[yuzu-android]] · [[nuzu]] · [[se-tools]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
