---
title: UE4SS Launcher
kind: entity
topics: [game-engine, game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/T0PGLitch3r__UE4SS-Launcher.md
updated: 2026-11-16
confidence: medium
---

# UE4SS Launcher

**UE4SS Launcher** (T0PGLitch3r/UE4SS-Launcher) is a **Windows desktop application** with an integrated **in-game editor** for single-player **Unreal Engine 4 and 5** titles. It injects and manages [[re-ue4ss]] so **Lua and C++ mods** run inside a live game process. The stack is primarily **C++** with a **Dear ImGui** and **DirectX 11** UI, ships bundled UE4SS assets, a **LauncherBridge** Lua mod, and tooling for **launch**, **attach-injection**, per-game **signature and settings fixes**, and **mod toggling**. Beyond injection it exposes **free camera**, cheat and player tweaks, map and debug-menu discovery, Unreal-Editor-style **level editing** via in-game hotkeys, and **import or export of 3D assets** across common mesh formats including encrypted or **Oodle**-packed archives. The project targets mod developers, reverse engineers, and researchers who need a practical front end for UE4SS scripting, runtime object inspection, and hands-on experimentation on **offline** Unreal games rather than production multiplayer titles. (source: wiki/sources/descriptions/T0PGLitch3r__UE4SS-Launcher.md)

## Positioning

Listed under README **Cheat** as a Windows launcher and in-game UE4SS editor for single-player Unreal games (mods, freecam, cheat-manager unlock, level browser, GLB/FBX model import/export). Sits in the same UE4SS / mod-loader lane as [[unreal-mod-loader]], [[ue-live-bridge]], and [[ue4-freecam]]—a GUI orchestration layer on top of the [[re-ue4ss]] runtime.

## Links

- Repo: https://github.com/T0PGLitch3r/UE4SS-Launcher [Windows launcher and in-game UE4SS editor for single-player Unreal games: mods, freecam, cheat manager unlock, level browser, and GLB/FBX model import/export]

## Related

[[re-ue4ss]] · [[unreal-mod-loader]] · [[ue-live-bridge]] · [[ue4-freecam]] · [[ue4-base]] · [[dumper-7]] · [[unreal-object-model]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]