---
title: External ImGui Android
kind: entity
topics: [mobile-security, graphics-api, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__External-ImGui-Android.md
updated: 2026-08-13
confidence: medium
---

# External ImGui Android

External **Dear ImGui** mod-menu scaffold for **Android games** using **OpenGL ES 3.0** rendering (gmh5225). Runs an overlay **outside the game process** via an Android **SurfaceView** overlay service and **NDK JNI** integration; includes **Unreal Engine** memory tools, math structures, and draw helpers. README tag: `[External Imgui Menu for Android]`. (source: wiki/sources/descriptions/gmh5225__External-ImGui-Android.md)

Contrasts with in-process GLES hooks ([[imgui-native-modmenu]], [[android-imgui-menu]], [[imgui-unity-android]]) and Zygisk-injected menus ([[zygisk-imgui-mod-menu]], [[imgui-zygisk-unity]]) by keeping UI rendering in a separate overlay service rather than inside the target app's GL context.

## Links

- Repo: https://github.com/gmh5225/External-ImGui-Android

## Related

[[imgui]] · [[imgui-unity-android]] · [[android-imgui-menu]] · [[imgui-native-modmenu]] · [[android-native-app-imgui]] · [[external-imgui-cheat-menu-example-2023]] · [[ue4dumper]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
