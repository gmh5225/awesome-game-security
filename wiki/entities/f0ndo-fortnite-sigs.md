---
title: fortnite-sigs (F0NDO)
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/F0NDO__fortnite-sigs.md
updated: 2026-08-25
confidence: medium
---

# fortnite-sigs (F0NDO)

Compact **Fortnite / Unreal Engine signature dump** (F0NDO; cheat / game:fortnite `[Signature]`). Plain-text byte patterns for locating key engine globals and game-specific routines—world pointers, name pools, event dispatching, visibility checks, and aiming-related functions—intended for manual refresh or scripted updater pipelines. Primary use case is keeping external or internal analysis tools synchronized when offsets churn faster than full SDK regen. (source: wiki/sources/descriptions/F0NDO__fortnite-sigs.md)

Distinct from the gmh5225 [[fortnite-sigs]] IDA-style pattern collection; scoped to F0NDO's lightweight text sig feed for fast offset maintenance.

## Links

- Repo: https://github.com/F0NDO/fortnite-sigs

## Related

[[fortnite-sigs]] · [[fortnite-sigs-updated-every-update]] · [[fortnite-offsets]] · [[fortnite-offsets-and-sigs]] · [[unreal-object-model]] · [[patternsleuth]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
