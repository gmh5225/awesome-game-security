---
title: LinoAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/lino9999__LinoAC.md
  - wiki/sources/README-categories.md
updated: 2026-10-25
confidence: medium
---

# LinoAC

Experimental open-source **Spigot/Paper** Minecraft anti-cheat for **1.21.11–26.3** (Java). **PacketEvents** drives packet-rate and timing analysis alongside modular movement, combat, block, and inventory heuristics (speed, flight, reach, placement abuse, fast-break). Staff workflows include clickable alerts, violation profiles, punishment waves, audit logs, freeze/teleport tools, and a configurable per-check buffer pipeline; optional Discord webhooks, PlaceholderAPI, and a cancellable enforcement API. Targets operators wanting a lightweight, telemetry-free server-side alternative for survival and minigame hosts. (source: wiki/sources/descriptions/lino9999__LinoAC.md)

## Detection stack

PacketEvents + movement/combat/block modules; violation buffers → punishment waves; staff alerts and moderation tooling.

## Links

- Repo: https://github.com/lino9999/LinoAC

## Related

[[overviews/anti-cheat]] · [[virgola-anticheat]] · [[h-ac]] · [[novaguard]] · [[detector-operations]]
