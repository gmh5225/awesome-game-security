---
title: adaptive-boss-arena
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/Shadow-46__adaptive-boss-arena.md
updated: 2026-08-21
confidence: medium
---

# adaptive-boss-arena

**Adaptive Boss Arena** (Shadow-46) — Unity 6 C# arena combat demo where a boss learns player habits and adapts counters over a fight. Pure-C# learning stack covers behavior tracking, pattern recognition, combat memory, and counter-strategy selection, backed by extensive edit-mode and play-mode tests. Core anti-cheat design keeps the boss fair: compile-time assembly firewalls block AI and learning code from reading player input, while a delayed perception layer exposes only human-observable state on human reaction timescales. Also implements melee combat (weapons, parries, posture, phase-based boss attacks). Reference for adaptive AI, perception boundaries, and cheat-resistant boss design—not a commercial AC product. (source: wiki/sources/descriptions/Shadow-46__adaptive-boss-arena.md)

Useful beside Unity production samples such as [[fpssample]] when studying how assembly boundaries and perception delays constrain what server-side or AI logic can observe, complementing client attack-surface demos like [[unity-vulnerable-entrypoint]] on the offensive side.

## Links

- Repo: https://github.com/Shadow-46/adaptive-boss-arena

## Related

[[overviews/game-engine]] · [[overviews/anti-cheat]] · [[fpssample]] · [[unity-vulnerable-entrypoint]] · [[weird-anti-cheat-ideas]] · [[ghostbusters]]
