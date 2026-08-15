---
title: Android Native Surface
kind: entity
topics: [mobile-security, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Android_Native_Surface.md
updated: 2026-08-15
confidence: medium
---

# Android Native Surface

Demonstrates creating and rendering to a **native Android surface** from **C/C++** for game overlays on Android (gmh5225). Uses the Android NDK **`ANativeWindow`** API or **SurfaceFlinger** directly to create a **transparent overlay surface** above other apps, suitable for cheat menus or ESP-style draw. README tag: `[Android Native Overlay]`. (source: wiki/sources/descriptions/gmh5225__Android_Native_Surface.md)

Sits beside Java/SurfaceView external overlays ([[external-imgui-android]]), in-process GLES/Vulkan hooks ([[android-imgui-menu]], [[imgui-native-modmenu]]), and Zygisk-injected menus ([[zygisk-imgui-mod-menu]]) by drawing through a compositor-level native surface rather than hooking the target app's render chain.

## Links

- Repo: https://github.com/gmh5225/Android_Native_Surface

## Related

[[external-imgui-android]] · [[android-imgui-menu]] · [[imgui-native-modmenu]] · [[android-native-app-imgui]] · [[android-modmenu-semijni]] · [[present-hook]] · [[overviews/mobile-security]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
