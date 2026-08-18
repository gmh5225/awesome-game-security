---
title: valorant-offsets
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/apekros__valorant_offsets.md
updated: 2026-08-18
confidence: medium
---

# valorant-offsets

Minimal Valorant **memory offset dump** repository (apekros; cheat / game:valorant `[Offset]`). Publishes updated address and structure offsets in a C++ header for direct integration into external tooling—focused on maintaining layout constants after client patches rather than providing a full SDK or dump framework. Used by reverse-engineering practitioners tracking Valorant memory layout under [[vanguard]]. (source: wiki/sources/descriptions/apekros__valorant_offsets.md)

Sits in the same per-title Valorant offset-feed lane as [[valorant-externals]] and beside dump tooling such as [[valorant-dumper]], but scoped to a lightweight header-only offset feed rather than live-process SDK generation or incremental external offset tables alone.

## Links

- Repo: https://github.com/apekros/valorant_offsets

## Related

[[vanguard]] · [[valorant-externals]] · [[valorant-dumper]] · [[valorant-dumper-tool]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
