---
title: YCBR AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/YcbrYL1__YCBR-AntiCheat.md
updated: 2026-08-19
confidence: medium
---

# YCBR AntiCheat

Lightweight anti-cheat plugin for Minecraft **Paper 1.8.9** servers (Spigot-compatible). Written in Java 8 (Maven); uses **ProtocolLib** for packet inspection and a dual-thread pipeline that processes packets asynchronously before applying checks on the main thread. Ships with **19 checks** covering KillAura, Reach, Scaffold, Speed, Fly, Velocity, Timer, and related combat/movement/protocol exploits, plus optional physics-based movement simulation inspired by Grim-style prediction. Also bundles server-side tools for offline authentication, temporary bans, DDoS connection guarding, strict-mode thresholds, and a GUI for toggling checks and configuration. Targets Paper or Spigot operators on legacy 1.8.9 PvP networks who want integrated cheat detection and basic server protection. (source: wiki/sources/descriptions/YcbrYL1__YCBR-AntiCheat.md)

## Detection stack

ProtocolLib packet intercept with async→main-thread check pipeline; nineteen configurable combat, movement, and protocol modules; optional Grim-style movement prediction; admin GUI for per-check toggles; offline auth, temp-ban, and connection-rate guarding for operator hardening.

## Links

- Repo: https://github.com/YcbrYL1/YCBR-AntiCheat

## Related

[[dakotaac]] · [[windfall-anticheat]] · [[local-anticheat-1-8-9]] · [[avaanticheat]] · [[minecraft-anticheatai]] · [[phantom-client]] · [[yuri]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
