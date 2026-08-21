---
title: mordhau-simple-auto-block-cheat
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/Skengdo__mordhau-simple-auto-block-cheat.md
updated: 2026-08-21
confidence: medium
---

# mordhau-simple-auto-block-cheat

**mordhau-simple-auto-block-cheat** (Skengdo/mordhau-simple-auto-block-cheat) is an internal **C++ cheat module** for **Mordhau** focused on automated melee defense and response. It implements **auto-block** for swings and kicks plus optional **auto-stab** logic, and is intended to be **injected into the game process**. A very large **generated SDK** is bundled, showing heavy reliance on Unreal Engine class and function dump headers. Primary audience: game-hacking researchers exploring **combat automation** techniques and **internal module structure**. (source: wiki/sources/descriptions/Skengdo__mordhau-simple-auto-block-cheat.md)

Sits in the UE4 in-process combat-automation lane beside Skengdo [[ue4-processevent-intercept]] for dispatch instrumentation and generic internal scaffolds such as [[ue4-base]] atop generated SDK headers.

## Links

- Repo: https://github.com/Skengdo/mordhau-simple-auto-block-cheat

## Related

[[unreal-object-model]] · [[ue4-base]] · [[ue4-processevent-intercept]] · [[uedumper]] · [[ue4genny]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
