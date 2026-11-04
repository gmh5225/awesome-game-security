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

**Lua 5.4 modding engine** for the 64-bit Windows release of *Might & Magic Heroes VII* (v2.2.1). Ships as a **dinput8.dll proxy** beside the game executable, discovers **Unreal Engine 3** internals at runtime via signature scanning, and exposes UE3 reflection, function hooks, and Lua bindings so mods can read/write objects, call UnrealScript, intercept calls, and use events/timers with **hot reload** and an in-game Mods menu—without patching shipped game files. Bundled example mods and RE helpers (object dumps, signature tooling) target single-player mod developers and UE3 researchers. (source: wiki/sources/descriptions/Whaileee__H7ModEngine.md)

Sits in the same **proxy-DLL + in-engine scripting** lane as [[sr5-tweak-menu]] (Saints Row 2022 dinput8 Lua menu) but targets UE3 reflection/UnrealScript rather than a title-native Lua API surface.

## Links

- Repo: https://github.com/Whaileee/H7ModEngine

## Related

[[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[unreal-object-model]] · [[sr5-tweak-menu]] · [[il2cpp]]
