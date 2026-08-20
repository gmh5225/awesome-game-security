---
title: Android Native Surface
kind: entity
topics: [mobile-security, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Android_Native_Surface.md
  - wiki/sources/descriptions/SsageParuders__Android_Native_Surface.md
updated: 2026-08-20
confidence: medium
---

# Android Native Surface

Native **Android surface rendering library** for creating **overlay surfaces without app-level permissions** from **C/C++**, aimed at game-security researchers and overlay developers studying compositor-level draw across Android versions. README tag: `[Android Native Overlay]`.

**gmh5225** fork demonstrates **`ANativeWindow`** or **SurfaceFlinger** transparent overlay surfaces above other apps—suitable for cheat menus or ESP-style draw. (source: wiki/sources/descriptions/gmh5225__Android_Native_Surface.md)

**SsageParuders** fork ships **AOSP-compatible** sources for **Android 10–14**, supporting native **surface rendering** and **screen recording** through standard Android APIs. (source: wiki/sources/descriptions/SsageParuders__Android_Native_Surface.md)

Sits beside Java/SurfaceView external overlays ([[external-imgui-android]]), in-process GLES/Vulkan hooks ([[android-imgui-menu]], [[imgui-native-modmenu]]), and Zygisk-injected menus ([[zygisk-imgui-mod-menu]]) by drawing through a compositor-level native surface rather than hooking the target app's render chain.

## Links

- Repo (gmh5225): https://github.com/gmh5225/Android_Native_Surface
- Repo (SsageParuders): https://github.com/SsageParuders/Android_Native_Surface

## Related

[[external-imgui-android]] · [[android-imgui-menu]] · [[imgui-native-modmenu]] · [[android-native-app-imgui]] · [[android-modmenu-semijni]] · [[cheat-unity-games]] · [[present-hook]] · [[overviews/mobile-security]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
