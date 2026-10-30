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

Geode mod (MIT) for Geometry Dash 2.2081 that buffers early jump input: on a slightly early press, holds input until the first physics tick where an internal shadow simulation still treats the jump as safe—without autoplay or replacing manual play. C++23/CMake hooks via Geode; planner with trigger-world baking, buffer state machine, optional per-level learning, GDR replay import, and debug tooling (performance traces, dev evaluation lab). Cross-platform Geode module packaging (Windows primary). (source: wiki/sources/descriptions/ToldByNun__earlybuffering-gd.md)

## Links

- Repo: https://github.com/ToldByNun/earlybuffering-gd

## Related

[[level-hash]] · [[gd-internal]] · [[input-provenance]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
