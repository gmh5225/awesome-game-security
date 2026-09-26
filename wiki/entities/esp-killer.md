---
title: esp-killer
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/kroshtan__esp-killer.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# esp-killer

**esp-killer** (kroshtan/esp-killer) is a **server-side ESP / wallhack detection system** for **The Isle: Evrima** multiplayer servers. Written in Python, it analyzes player movement patterns alone—never touching the game client—because Evrima ships with Easy Anti-Cheat and offers no modding API. (source: wiki/sources/descriptions/kroshtan__esp-killer.md)

README category: Anti Cheat / Detection:ESP.

## Detection surface

Movement heuristics flag behavior that only makes sense if a player can see through walls:

- Heading directly toward distant hidden players.
- Arriving at locations implausibly fast relative to server-visible position snapshots.

Alerts route to server admins for **human review** rather than automatic bans.

## Architecture

- **Read-only agent** — deploys beside the game server; polls player positions through the Evrima **RCON** protocol.
- **FastAPI backend** — receives position snapshots; **SQLite** storage with API key management.
- **Clean-room RCON client** — on-disk upload queue with retry logic for resilient telemetry ingest.
- **Dev tooling** — fake RCON server and movement simulator for pipeline testing without a live game host. (source: wiki/sources/descriptions/kroshtan__esp-killer.md)

## Positioning

Sits in the **Detection:ESP** lane beside server-side terrain/occlusion mitigations such as [[petal-anti-freecam]] and [[serverguard]], and movement-replay backends such as [[blastscale]]. Complements EAC-protected titles where client instrumentation is unavailable by inferring wallhack use from **RCON position telemetry** alone—closer to heuristic server-side review stacks such as [[osanticheat]] than packet-layer visibility masking.

## Peers

[[petal-anti-freecam]] · [[serverguard]] · [[osanticheat]] · [[corner-culling]] · [[blastscale]]

## Links

- Repo: https://github.com/kroshtan/esp-killer

## Related

[[easy-anti-cheat]] · [[overviews/anti-cheat]] · [[concepts/detector-operations]]
