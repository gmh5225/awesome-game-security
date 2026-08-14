---
title: CheatIt
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__CheatIt.md
updated: 2026-08-14
confidence: medium
---

# CheatIt

Unreal Engine **multi-title internal cheat** (gmh5225) targeting **Witch It** and **POLYGON**. Uses **signature scanning** to locate UObject arrays and other engine structures, then applies in-game modifications with **configurable pattern matching** so one codebase can switch between game targets. (source: wiki/sources/descriptions/gmh5225__CheatIt.md)

Illustrates the [[unreal-object-model]] address-discovery lane—pattern-scan `GObjects`/globals before SDK consumption—beside title-specific POLYGON samples such as [[polygon-ue5]] and other UE demo/title offensive repos ([[shootergame-hack]], [[remnant-esp]]).

## Technique summary

| Mechanism | Role |
|-----------|------|
| Signature / pattern scan | Resolve UObject arrays and UE globals per build |
| Configurable patterns | Retarget Witch It vs POLYGON without separate binaries |
| In-game modifications | Gameplay/feature hooks once engine structures are located |

## Links

- Repo: https://github.com/gmh5225/CheatIt

## Related

[[polygon-ue5]] · [[shootergame-hack]] · [[patternsleuth]] · [[unreal-object-model]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
