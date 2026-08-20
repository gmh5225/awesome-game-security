---
title: CS2Fixes
kind: entity
topics: [game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/Source2ZE__CS2Fixes.md
updated: 2026-08-20
confidence: medium
---

# CS2Fixes

**Metamod:Source plugin** for Counter-Strike 2 dedicated servers that adds gameplay fixes and server-side features, with strong emphasis on **zombie escape** community servers. (source: wiki/sources/descriptions/Source2ZE__CS2Fixes.md)

## Architecture

Hook-driven server logic with configuration systems, admin tooling, and bundled particle or sound assets consumed by the plugin at runtime.

## Developer reference

The codebase doubles as a practical reference for **Source 2 mod developers** who need common integration patterns and boilerplate for Metamod server plugins—complementing client-side SDK dumps such as [[source2gen]] and educational guides such as [[cs2-internals]]. (source: wiki/sources/descriptions/Source2ZE__CS2Fixes.md)

Primary use case: running and extending community CS2 servers with stable, configurable functionality. Sits in the server-authoritative community-host lane beside moderation plugins such as [[cs2-calladmin]] and behavioral AC such as [[cs2ac]], but focuses on gameplay fixes and custom server features rather than cheat detection.

## Links

- Repo: https://github.com/Source2ZE/CS2Fixes

## Related

[[overviews/game-engine]] · [[overviews/game-hacking]] · [[cs2ac]] · [[cs2-calladmin]] · [[source2gen]] · [[cs2-internals]] · [[cs2-sdk]]
