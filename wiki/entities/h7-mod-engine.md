---
title: H7 Mod Engine
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Whaileee__H7ModEngine.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# H7 Mod Engine

**Lua 5.4 modding engine** for the 64-bit Windows release of *Might & Magic Heroes VII* (v2.2.1). Targets single-player mod developers and UE3 researchers who want scriptable control and deep visibility into a commercial shipped build without patching game files or binaries. (source: wiki/sources/descriptions/Whaileee__H7ModEngine.md)

## Architecture

Ships as a **dinput8.dll proxy** beside the game executable. A **C++20** core discovers **Unreal Engine 3** internals in memory at runtime (signature scanning) rather than relying on modified game assets. (source: wiki/sources/descriptions/Whaileee__H7ModEngine.md)

## Mod developer surface

Exposes UE3 **reflection**, **function hooks**, and **Lua bindings** so mods can read/write game objects, call **UnrealScript** functions, intercept or override calls, and drive **events** and **timers** with **hot reload** plus an in-game **Mods** menu. Bundled example mods and documentation illustrate gameplay tweaks. (source: wiki/sources/descriptions/Whaileee__H7ModEngine.md)

## Research helpers

Reverse-engineering utilities include **object dumps** and **signature scanning** for exploring the shipped UE3 build. Sits in the same **proxy-DLL + in-engine scripting** lane as [[sr5-tweak-menu]] (Saints Row 2022 dinput8 Lua menu) but targets UE3 reflection/UnrealScript rather than a title-native Lua API surface.

## Links

- Repo: https://github.com/Whaileee/H7ModEngine

## Related

[[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[unreal-object-model]] · [[sr5-tweak-menu]] · [[smite-esp-aimbot]]
