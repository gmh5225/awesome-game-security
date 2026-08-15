---
title: gatewarden-public
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/euuuuuuan__gatewarden-public.md
updated: 2026-08-15
confidence: medium
---

# gatewarden-public

Godot 4.7 low-poly 3D tower defense prototype where players place enemy spawn gates and sculpt the battlefield with walls before waves begin. Anti-abuse placement rules are published as a first-class system rather than hidden clamps: a **PathValidator** hypothetically blocks cells and runs scratch flow-field checks to reject maze-juggling or softlock layouts with stable machine-readable reason codes. (source: wiki/sources/descriptions/euuuuuuan__gatewarden-public.md)

GDScript implementation with a fixed 30 Hz deterministic simulation, Dijkstra flow-field pathfinding, and strict performance gates enforced by 59 GUT unit and integration tests including a headless bot that plays full runs. Serves as a reference for transparent, test-driven anti-cheat and validation systems in player-authored tower defense scenarios.

## Links

- Repo: https://github.com/euuuuuuan/gatewarden-public

## Related

[[godot]] · [[godot-sandbox]] · [[chessking]] · [[zombies-vs-plants]] · [[certael]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
