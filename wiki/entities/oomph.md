---
title: Oomph
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/oomph-ac__oomph.md
updated: 2026-07-26
confidence: medium
---

# Oomph

Interception-based anti-cheat proxy for Minecraft: Bedrock Edition that sits between clients and the game server and inspects traffic for cheating. Written primarily in Go; processes client and server packets and applies configurable detections for reach, hitbox abuse, aim assistance, autoclickers, kill aura, scaffolding, nukers, and malformed packets. (source: wiki/sources/descriptions/oomph-ac__oomph.md)

Features server-authoritative movement and combat with latency-aware position correction, entity rewind for attack validation, and raycast-based hit checks against common Bedrock cheats. Can run as a standalone Bedrock proxy or embed with Dragonfly, and integrates with backends such as PocketMine-MP. Aimed at Bedrock server operators in the same lightweight server/host AC lane as [[open.mp-anticheat]] and [[wellsanticheat]], rather than kernel products such as [[easy-anti-cheat]] or [[vanguard]].

## Links

- Repo: https://github.com/oomph-ac/oomph

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[open.mp-anticheat]] · [[wellsanticheat]] · [[certael]] · [[magnetite]]
