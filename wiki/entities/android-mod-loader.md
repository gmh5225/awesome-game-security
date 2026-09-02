---
title: Android Mod Loader
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/AndroidModLoader__AndroidModLoader.md
updated: 2026-09-02
confidence: medium
---

# Android Mod Loader

Native **Android mod loader framework** for injecting and managing mods in games and applications. Primarily **C++** with **Android NDK** build scripts; bundles patching, memory writing, **function hooking**, and **interface-based mod APIs** for game mod developers and reverse engineers building runtime modifications on Android. (source: wiki/sources/descriptions/AndroidModLoader__AndroidModLoader.md)

Supporting components include **ARM hooking**, dependency handling, **IL2CPP-oriented utilities**, and mod template scaffolding — situating it in the same native inject/hook/mod-loader lane as [[kittymemory]], [[android-mod-menu]], and [[android-modding]] rather than as a standalone memory scanner or menu template.

## Links

- Repo: https://github.com/AndroidModLoader/AndroidModLoader (README tag: [Android Mod Loader])

## Related

[[kittymemory]] · [[and64-inline-hook]] · [[dobby]] · [[il2cpp]] · [[android-mod-menu]] · [[android-modding]] · [[android-mod-games-by-inject-zygote]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
