---
title: Provenance Elite Force II decomp (Android/Linux)
kind: entity
topics: [reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/imjustadudegamer__Provenance-Elite-Force-II-decomp-Android-linux.md
updated: 2026-11-06
confidence: medium
---

# Provenance Elite Force II decomp (Android/Linux)

Unofficial **decompiled, rebuildable** source tree for *Star Trek: Voyager — Elite Force II* (de-MOHAAd **id Tech 3** lineage), organized to build on **Linux** and **Android**. The stack is mostly **C/C++** with **CMake** for native engine and game code and **Gradle** wrapping JNI plus game assets; it wires SDL, OpenAL, zlib, and common media libraries, and exposes **GLES3**- and **Vulkan**-oriented renderer configuration alongside classic Quake-family **client**, **server**, **cgame**, and **bot AI** modules. Packaging helpers cover Android APKs, Linux **AppImage** layout, and **PK3**-style assets, with provenance and third-party license documentation. **No game data** ships in the repository—aimed at reverse engineering, porting, and preservation with repeatable builds rather than anti-cheat or multiplayer security tooling. (source: wiki/sources/descriptions/imjustadudegamer__Provenance-Elite-Force-II-decomp-Android-linux.md)

README lane: unofficial Android/Linux port; de-MOHAAd id Tech 3; GLES 3.2/Vulkan; **no game data**.

## Links

- Repo: https://github.com/imjustadudegamer/Provenance-Elite-Force-II-decomp-Android-linux

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/mobile-security]]
