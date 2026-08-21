---
title: UnrealModLoader
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/RussellJerome__UnrealModLoader.md
updated: 2026-08-21
confidence: medium
---

# UnrealModLoader

**UnrealModLoader** (RussellJerome/UnrealModLoader) is a **mod loading framework** for **Unreal Engine 4** games that supports **Blueprint** and basic **SDK-based C++** mods. It combines native **hooking** and **event callback** systems with third-party components such as **MinHook** and **ImGui** to provide lifecycle hooks and in-game tooling interfaces. The codebase includes **injector** and **proxy DLL** loading paths to bootstrap mod modules into target processes. Primary audience: UE4 mod developers and researchers studying runtime extension and game instrumentation techniques. (source: wiki/sources/descriptions/RussellJerome__UnrealModLoader.md)

Sits in the UE4 in-process mod-loader lane beside live-scripting stacks such as [[re-ue4ss]], hook scaffolds such as [[ue4-base]], and dispatch instrumentation such as [[ue4-processevent-intercept]].

## Links

- Repo: https://github.com/RussellJerome/UnrealModLoader (Mod Loader)

## Related

[[unreal-object-model]] · [[re-ue4ss]] · [[ue4-base]] · [[ue4-injector]] · [[present-hook]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
