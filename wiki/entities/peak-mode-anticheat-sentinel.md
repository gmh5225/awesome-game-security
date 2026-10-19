---
title: PEAK-mode AntiCheat Sentinel
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: high
---

# PEAK-mode AntiCheat Sentinel

**Peak Sentinel** (DoomSalat/PEAK-mode-AntiCheat-Sentinel) is a prototype **BepInEx 5** host-side anti-cheat plugin for the multiplayer Unity title **PEAK**. Implemented in **C#** with **Harmony**, it hooks **Photon RPC execution** and network instantiation, attributing suspicious item spawns to the **Photon message sender** the server assigns (clients cannot spoof). **RpcAudit** and **InstantiateAudit** rules cover spawn-in-hand cheats, forged pickups, inventory rewrites, clones, and suspicious creates; when the local player is host, configurable protection can refuse cheat and spawner-mod requests while allowing vanilla grants such as airport passports and legitimate host spawns. Reporting includes an **F6 manager window** with scrollable findings, in-game connection-feed alerts, BepInEx logging, and an optional debug trace file. (source: wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md)

## Posture

Targets PEAK **hosts and mod users** who want lightweight **host-side game security** against item-spawn cheats—not kernel-level drivers or commercial anti-cheat stacks. Sender attribution treats Photon network identity as **server-assigned** evidence for RPC/instantiate events (see [[input-provenance]]). Complements other BepInEx host plugins such as [[among-us-anti-cheat]], [[au-anticheat]], and [[banmod]]. (source: wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md)

## Detection surfaces

- **Photon sender attribution** — tie item events to server-assigned network senders.
- **RpcAudit / InstantiateAudit** — spawn-in-hand, forged pickup, inventory rewrite, clone, and suspicious create rules.
- **Host-only enforcement** — optional block/refusal when local player is session host.
- **Operator UI** — F6 findings manager, connection-feed alerts, logs, optional trace file.

## Links

- Repo: https://github.com/DoomSalat/PEAK-mode-AntiCheat-Sentinel

## Related

[[bepinex]] · [[input-provenance]] · [[among-us-anti-cheat]] · [[au-anticheat]] · [[banmod]] · [[detector-operations]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
