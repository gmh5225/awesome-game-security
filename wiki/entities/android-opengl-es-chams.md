---
title: Android OpenGL ES Chams
kind: entity
topics: [mobile-security, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Android-OpenGL-ES-Chams.md
updated: 2026-08-15
confidence: medium
---

# Android OpenGL ES Chams

OpenGL ES chams research repo (gmh5225) focused on **chams** implementation for Android games. The main header includes descriptive comments to explain the GLES draw/shader hooking approach. README tag: `[Chams]`. Useful for game security researchers and reverse engineers studying offensive techniques in the cheat / render-draw lane on mobile OpenGL ES. (source: wiki/sources/descriptions/gmh5225__Android-OpenGL-ES-Chams.md)

Sits beside Android Unity/OpenGL cheat templates ([[android-cheat-template]]), in-process GLES ImGui hooks ([[android-imgui-menu]], [[imgui-native-modmenu]]), and desktop chams samples such as [[r6-chams-public]] by applying [[draw-call-hook]] patterns on mobile GLES instead of DirectX or external overlay surfaces.

## Links

- Repo: https://github.com/gmh5225/Android-OpenGL-ES-Chams

## Related

[[draw-call-hook]] · [[android-cheat-template]] · [[android-imgui-menu]] · [[imgui-native-modmenu]] · [[android-native-surface]] · [[r6-chams-public]] · [[overviews/mobile-security]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
