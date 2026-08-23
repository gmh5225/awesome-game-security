---
title: FortConsole
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Makk5__FortConsole.md
updated: 2026-08-23
confidence: medium
---

# FortConsole

Injected x64 Windows C++ DLL that re-enables the Unreal Engine in-game console interface in a specific Fortnite build context. Uses pattern scanning and engine object construction logic to locate and initialize console-related structures at runtime; ships low-level Unreal object enums and memory helpers for internal injection workflows. Primary use case is Unreal Engine internals exploration and game security research in controlled, anti-cheat-disabled environments—not a packaged combat-cheat feature set. (source: wiki/sources/descriptions/Makk5__FortConsole.md)

## Links

- Repo: https://github.com/Makk5/FortConsole

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[unreal-object-model]] · [[fortkit]] · [[basic-fortnite-cheat-source-internal]] · [[re-ue4ss]] · [[easy-anti-cheat]]
