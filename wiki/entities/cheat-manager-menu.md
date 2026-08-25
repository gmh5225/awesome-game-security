---
title: Cheat Manager Menu
kind: entity
topics: [game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/Ghostleadie__CheatManagerMenu.md
updated: 2026-08-25
confidence: medium
---

# Cheat Manager Menu

Unreal Engine 5.8 plugin (Win64, C++) that automatically builds an in-game cheat menu by reflecting over the local player's `UCheatManager` and any registered cheat manager extensions. At runtime it discovers native `Exec` functions and `BlueprintCallable` cheat extensions, then presents them with parameter-aware controls—checkboxes, dropdowns, sliders, and text fields—rendered through the experimental SlateIM UI layer. Supports keyboard, mouse, and gamepad input; filtering, favorites, category grouping from `UFUNCTION` metadata, tooltips from doc comments, and optional confirmation dialogs for destructive cheats. Compiled out of Shipping builds; intended for developers and testers who need a zero-maintenance debug interface during development, play-in-editor, and packaged Development or Test builds. (source: wiki/sources/descriptions/Ghostleadie__CheatManagerMenu.md)

Sits in the legitimate Unreal debug / cheat-command lane beside ImGui tooling such as [[unreal-imgui-tools]] and engine-literacy samples such as [[unrealcpp]]—not an external memory cheat or anti-cheat bypass. Understanding `UCheatManager` reflection surfaces is relevant when studying which dev-only cheat commands may remain reachable in non-Shipping builds.

## Links

- Repo: https://github.com/Ghostleadie/CheatManagerMenu (README: UE 5.8 plugin that auto-builds an in-game cheat menu by reflecting UCheatManager and registered cheat extensions)

## Related

[[overviews/game-engine]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[unreal-imgui-tools]] · [[unrealcpp]] · [[unreal-mod-loader]]
