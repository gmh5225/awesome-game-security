---
title: Farming Simulator 12 Mp Build
kind: entity
topics: [game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/erensariisik03-sudo__Farming-Simulator-12-Mp-Build.md
  - wiki/sources/README-categories.md
updated: 2026-09-16
confidence: medium
---

# Farming Simulator 12 Mp Build

Native Android mod that adds multiplayer to Farming Simulator 12 by injecting `libmultiplayermod.so` at runtime instead of repacking the APK. Built with the Android NDK for legacy armeabi, it uses Substrate to hook native menu, GUI, and update routines via hardcoded offsets, implements UDP LAN discovery and TCP player sync, and renders a Dear ImGui overlay on OpenGL ES 2. GitHub Actions produces the injectable library artifact. Useful for studying native mobile game hooking, legacy ABI targets, and closed-source engine runtime modification. (source: wiki/sources/descriptions/erensariisik03-sudo__Farming-Simulator-12-Mp-Build.md)

## Technique stack

Runtime `.so` injection; Substrate native hooks on menu/GUI/update via hardcoded offsets; UDP LAN discovery + TCP player sync; OpenGL ES 2 + Dear ImGui overlay; NDK armeabi build; GitHub Actions CI for `libmultiplayermod.so`.

## Audience

Reverse engineers and modders studying native mobile game hooking, legacy Android ABI targets, and runtime modification of closed-source mobile game engines.

## Links

- Repo: https://github.com/erensariisik03-sudo/Farming-Simulator-12-Mp-Build

## Related

[[overviews/game-hacking]] · [[overviews/mobile-security]] · [[android-mod-games-by-inject-zygote]] · [[android-mod-loader]] · [[android-dll-injector]] · [[frida]] · [[present-hook]]
