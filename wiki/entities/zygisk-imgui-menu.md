---
title: Zygisk-ImGui-Menu
kind: entity
topics: [mobile-security, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/fedes1to__Zygisk-ImGui-Menu.md
updated: 2026-08-15
confidence: medium
---

# Zygisk-ImGui-Menu

**ImGui menu using Zygisk** — a Magisk Zygisk module sample that injects a Dear ImGui overlay into Android game processes. Builds on **cURL** and ImGui; primary hook logic lives in `hook.cpp`. Adjust `module.gradle` before publishing. Useful for game security researchers and reverse engineers studying offensive cheat / render-draw techniques on rooted Android. (source: wiki/sources/descriptions/fedes1to__Zygisk-ImGui-Menu.md)

Peers other Zygisk ImGui templates ([[zygisk-imgui-mod-menu]], [[zygisk-imgui-modmenu]]) and complements non-Zygisk GLES menus ([[imgui-native-modmenu]], [[android-imgui-menu]]) in the Magisk ([[magisk]]) / [[zygisk]] overlay lane.

## Links

- Repo: https://github.com/fedes1to/Zygisk-ImGui-Menu

## Related

[[zygisk]] · [[magisk]] · [[zygisk-imgui-mod-menu]] · [[zygisk-imgui-modmenu]] · [[imgui-native-modmenu]] · [[android-imgui-menu]] · [[overviews/mobile-security]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
