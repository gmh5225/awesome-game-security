---
title: PEAK-mode AntiCheat Sentinel
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# PEAK-mode AntiCheat Sentinel

**Peak Sentinel** (DoomSalat/PEAK-mode-AntiCheat-Sentinel) is a prototype **BepInEx 5** host-side anti-cheat plugin for the multiplayer Unity title **PEAK**. Implemented in **C#** with **Harmony**, it hooks **Photon RPC execution** and network instantiation, attributing suspicious item spawns to the **Photon message sender** the server assigns (not client-spoofable). **RpcAudit** and **InstantiateAudit** rules cover spawn-in-hand cheats, forged pickups, inventory rewrites, clones, and suspicious creates; when the local player is host, configurable protection can refuse cheat/spawner-mod grants while allowing vanilla host flows such as airport passports. Reporting includes an **F6 manager window**, in-game connection-feed alerts, BepInEx logging, and optional debug trace files. (source: wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md)

Targets PEAK hosts who want lightweight **network-authoritative item integrity** without kernel or commercial AC stacks—beside other BepInEx host plugins such as [[among-us-anti-cheat]] and [[banmod]].

## Detection surfaces

- **Photon sender attribution** — tie item events to server-assigned network senders.
- **RpcAudit / InstantiateAudit** — spawn-in-hand, forged pickup, inventory rewrite, clone, and suspicious create rules.
- **Host-only enforcement** — optional block/refusal when local player is session host.
- **Operator UI** — F6 findings manager, connection-feed alerts, logs, optional trace file.

## Links

- Repo: https://github.com/DoomSalat/PEAK-mode-AntiCheat-Sentinel

## Related

[[bepinex]] · [[among-us-anti-cheat]] · [[banmod]] · [[detector-operations]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
