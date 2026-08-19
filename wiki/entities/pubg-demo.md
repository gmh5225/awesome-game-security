---
title: Pubg-demo
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/a0yark__Pubg-demo.md
updated: 2026-08-19
confidence: medium
---

# Pubg-demo

External cheat demo for PUBG (a0yark) built in **C++** with the **Unreal Engine SDK**. Ships a dumped **CppSDK** with generated class headers, **bone helper** utilities for skeleton rendering, an **ESP and aimbot** framework, and an **ImGui-based DirectX 11** overlay. A **DLL-injected** cheat module handles game memory reads while visual overlays run through a **separate rendering pipeline**—a common split when keeping draw calls out of the game's swap path. (source: wiki/sources/descriptions/a0yark__Pubg-demo.md)

Useful for game security researchers studying Unreal Engine SDK-based cheat architectures and external overlay techniques on desktop PUBG—complementing simpler external samples such as [[pubg-external-cheat]], SDK dumpers such as [[pubg-dumper]], and internal references such as [[pubg-internal]].

## Links

- Repo: https://github.com/a0yark/Pubg-demo

## Related

[[unreal-object-model]] · [[world-to-screen]] · [[imgui-standalone]] · [[pubg-external-cheat]] · [[pubg-internal]] · [[pubg-dumper]] · [[pubg-dump-offset]] · [[pubg-dx]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
