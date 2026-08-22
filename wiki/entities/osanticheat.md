---
title: OSAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Pintuzoft__OSAntiCheat.md
updated: 2026-08-22
confidence: medium
---

# OSAntiCheat

Experimental **server-side heuristic anti-cheat** for Counter-Strike 2, implemented as a **CounterStrikeSharp** plugin in C# (.NET). It observes only **server-visible data**—player positions, view angles, shots, and timing—then applies statistical detectors for spinbot, aimbot snaps, triggerbot, and several wallhack signals including tracking, gaze, and a McNemar null test. (source: wiki/sources/descriptions/Pintuzoft__OSAntiCheat.md)

## Detection model

Independent detector outputs feed a **fusion suspicion engine** that grades confidence with decay and corroboration, producing **Watch/Review tiers** rather than automatic kicks or bans. The project targets CS2 server operators and researchers who want **log-only, probability-based cheat flagging** during calibration against real demos and live server data.

## Positioning

Sits in the server-authoritative community-host lane beside [[cs2ac]] and [[cs2-calladmin]], but emphasizes heuristic statistical fusion and review tiers over automated punishments—closer to calibration-oriented research than production ban enforcement.

## Links

- Repo: https://github.com/Pintuzoft/OSAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cs2ac]] · [[cs2-calladmin]] · [[aimbot-detection-prototype]] · [[cs2-hybrid-anticheat-proposal]]
