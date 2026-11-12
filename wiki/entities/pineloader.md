---
title: PineLoader
kind: entity
topics: [game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/EuroCent82__PineLoader.md
updated: 2026-11-12
confidence: medium
---

# PineLoader

**PineLoader** (EuroCent82/PineLoader) is a Windows mod loader for **Unreal Engine 5.8** titles that runs ahead of the game so mods attach without Steam launch options. It is built in **C#** on **.NET 10** with a **WinForms** shell and replaces the game's `Win64-Shipping` executable via a **hard link** while preserving the original game binary. Mods live as DLL plugins under a `Mods` folder, implement `IPineMod`, and receive an `IPineHost` API for logging, optional Java agents, and hooks on the running game process, with per-mod INI toggles and a cache layer for faster restarts. Failed mods are skipped individually so the game can still start—suited to mod developers, UE5.8 researchers, and anyone studying how a shipping executable can be redirected to inject managed extensions at launch. (source: wiki/sources/descriptions/EuroCent82__PineLoader.md)

Sits in the UE5 pre-launch mod-loader lane beside in-process frameworks such as [[re-ue4ss]] and [[unreal-mod-loader]].

## Links

- Repo: https://github.com/EuroCent82/PineLoader (Game Engine Plugins:Unreal)

## Related

[[re-ue4ss]] · [[unreal-mod-loader]] · [[ue4-base]] · [[unreal-object-model]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
