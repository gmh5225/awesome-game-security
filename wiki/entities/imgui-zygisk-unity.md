---
title: ImGUI-Zygisk-Unity
kind: entity
topics: [mobile-security, graphics-api, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/lbertitoyt__ImGUI-Zygisk-Unity.md
updated: 2026-08-01
confidence: medium
---

# ImGUI-Zygisk-Unity

Zygisk module template for injecting Dear ImGui overlays into Unity-based Android games. Loads native C++ via Magisk [[zygisk]] at process startup, hooks the Unity rendering pipeline, and draws an ImGui mod menu with OpenGL ES context sharing and touch-input translation—aimed at Android Unity modders on rooted devices. (source: wiki/sources/descriptions/lbertitoyt__ImGUI-Zygisk-Unity.md)

Complements direct-inject Unity ImGui templates ([[imgui-unity]], [[imgui-unity-with-layout]]), generic Zygisk ImGui samples ([[zygisk-imgui-mod-menu]]), and native GLES menus ([[imgui-native-modmenu]]) in the Magisk ([[magisk]]) / Unity-on-Android lane.

## Links

- Repo: https://github.com/lbertitoyt/ImGUI-Zygisk-Unity

## Related

[[imgui-unity]] · [[imgui-unity-with-layout]] · [[zygisk-imgui-mod-menu]] · [[imgui-native-modmenu]] · [[android-native-app-imgui]] · [[zygisk]] · [[magisk]] · [[il2cpp]] · [[overviews/mobile-security]] · [[overviews/graphics-api]] · [[overviews/game-engine]]
