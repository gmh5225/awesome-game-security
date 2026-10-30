---
title: CS2 AntiCheat (mihaigsm2003)
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/mihaigsm2003__CS2-AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: medium
---

# CS2 AntiCheat (mihaigsm2003)

Server-side Metamod:Source plugin for Counter-Strike 2 dedicated hosts (mihaigsm2003). C++ against the Source 2 SDK with hooks, detours, movement analysis, and client cvar queries; Python/shell packaging via AMBuild for Linux and Windows. Eighteen configurable detection modules cover aim assistance, trigger and silent aim, bunnyhop and autostrafe, subtick manipulation, invalid cvars and inputs, suspicious DLL-related client events, and related rage behaviors. Server owners tune punishments, whitelists, and optional Discord or JSON webhook reporting through `AntiCheat.cfg` and console commands—no client install required. (source: wiki/sources/descriptions/mihaigsm2003__CS2-AntiCheat.md)

## Capabilities

- **Metamod:Source host** — dedicated CS2 Linux/Windows servers; evidence-driven in-game enforcement.
- **Broad detector set** — aim, movement, subtick, cvar/input integrity, and client-event heuristics.
- **Configurable enforcement** — punishments, whitelists, Discord/JSON webhook reporting.

Peers with [[anticheatsystem]], [[plugify-cs2ac]], [[cs2ac]], [[sac-the-server-anticheat]], and [[cs2-anticheat-by-chmonya]] in the Open Source Anti Cheat System lane.

## Links

- Repo: https://github.com/mihaigsm2003/CS2-AntiCheat

## Related

[[overviews/anti-cheat]] · [[detector-operations]] · [[input-provenance]] · [[anticheatsystem]] · [[plugify-cs2ac]] · [[cs2ac]] · [[sac-the-server-anticheat]] · [[cs2-anticheat-by-chmonya]] · [[aegis-ac-cs2]]
