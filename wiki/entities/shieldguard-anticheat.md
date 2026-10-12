---
title: ShieldGuard AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Tobias1205__AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: high
---

# ShieldGuard AntiCheat

Paper **1.21.x** Minecraft server plugin (Tobias1205/AntiCheat; Java 21, Maven) that hardens survival multiplayer without client mods by rewriting outbound chunk and block packets per player via PacketEvents. It masks deep underground terrain against freecam, replaces ores with stone or deepslate until the player is within a configurable radius with clear line of sight, and hides storage blocks and related entities to block x-ray and storage ESP. Staff tooling includes in-game report commands, a management GUI, optional Discord webhooks, and permission-based bypass for testing. Primary audience: Paper server operators who want practical anti-cheat and moderation without client installs. (source: wiki/sources/descriptions/Tobias1205__AntiCheat.md)

## Mitigation stack

PacketEvents per-player outbound chunk/block rewriting; freecam terrain masking; proximity + LOS-gated ore reveal; storage-block and entity hiding for x-ray/ESP; report workflow + staff GUI + optional Discord webhooks.

## Operations

Player-facing report commands feed a staff management GUI; optional Discord webhooks extend alerts off-server. Permission-based bypass supports operator testing—separate bypass roles from production staff before go-live.

## Positioning

Broader packet-visibility bundle than freecam-only plugins such as [[petal-anti-freecam]] (adds ore masking and storage ESP hiding); complements statistical mining detectors such as [[xray-anticheat]] rather than replacing heuristic ore-vision scoring.

## Links

- Repo: https://github.com/Tobias1205/AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[petal-anti-freecam]] · [[xray-anticheat]] · [[serverguard]] · [[minecraft-anticheat-list]] · [[anticheat-qa]]
