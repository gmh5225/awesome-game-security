---
title: EarlyBuffer (earlybuffering-gd)
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/ToldByNun__earlybuffering-gd.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: medium
---

# EarlyBuffer (earlybuffering-gd)

Geode mod (MIT) for **Geometry Dash 2.2081** that provides a **timing assist**: on a slightly early jump press, it holds input and releases on the first physics tick where an internal **shadow simulation** still treats the jump as safe—without autoplay or replacing manual play. Implemented in **C++23** with CMake; hooks the commercial client through **Geode**. Useful for studying client-side assist design, deterministic input validation, and mod hooking in a rhythm-game context. (source: wiki/sources/descriptions/ToldByNun__earlybuffering-gd.md)

## Mechanism

- **Planner** with trigger-world baking and a **buffer state machine** decides when held input may release safely against shadow physics.
- Optional **per-level learning**, **GDR replay import**, and debug tooling (performance traces, dev evaluation lab).
- Ships as standard Geode modules; **Windows** primary, with packaging paths for macOS, iOS, and Android.

## Security research angles

- **Input path**: outward jump timing is **client-reported**; assist logic runs entirely in-process—see [[input-provenance]] for telemetry labeling.
- **Determinism**: shadow tick validation is a reference pattern for “safe release” gates versus full autoplay or macro replay.
- **Integrity contrast**: pairs with Geode integrity mods such as [[level-hash]] (level digest UI) on the same title ecosystem.

## Links

- Repo: https://github.com/ToldByNun/earlybuffering-gd

## Related

[[level-hash]] · [[gd-internal]] · [[input-provenance]] · [[cheat-attack-surface]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
