---
title: fortnite-offsets (Trydos)
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/Trydos__fortnite-offsets.md
updated: 2026-08-20
confidence: medium
---

# fortnite-offsets (Trydos)

Lightweight Fortnite **offset database** published as a **JSON file** (Trydos; cheat / game:fortnite `[Offset]`). Stores key memory offsets for engine pointers, entity structures, camera data, and weapon-related fields—data only, no application logic—so external cheat or research tooling can stay synchronized with current game memory layouts after patches. (source: wiki/sources/descriptions/Trydos__fortnite-offsets.md)

Distinct from the gmh5225 [[fortnite-offsets]] UE4 SDK structure tables and from combined offset+signature maintenance repos such as [[fortnite-offsets-and-sigs]]; scoped to a minimal JSON offset feed for easy consumption by downstream tools.

## Links

- Repo: https://github.com/Trydos/fortnite-offsets

## Related

[[fortnite-offsets]] · [[fortnite-offsets-and-sigs]] · [[fortnite-sigs]] · [[fortnite-offset-dumper]] · [[unreal-object-model]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
