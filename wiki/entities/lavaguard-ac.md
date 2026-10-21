---
title: LavaGuardAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/flameteamdev__LavaGuardAC.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: medium
---

# LavaGuardAC

Server-side anti-cheat plugin for **Bukkit** and **Spigot** Minecraft servers (Java; FlameTeam Studios). Implemented with the **Bukkit event API**, it runs configurable heuristics during normal gameplay to flag common client-side movement, combat, and world-interaction cheats. (source: wiki/sources/descriptions/flameteamdev__LavaGuardAC.md)

## Capabilities

- **Movement:** speed and bunnyhop, flight.
- **Combat:** extended reach, kill-aura-style patterns.
- **World:** fast break, nuker-style mining.
- **Enforcement:** detections roll into a violation counter; configurable threshold triggers **timed name bans**.
- **Staff:** in-game admin GUI; `lavaguard` commands (config reload; Polish or English messaging).
- **Alerts:** optional **Discord webhook** ban embeds posted asynchronously over HTTP.
- **Config:** YAML-driven settings and messages; **GPLv3**; no external AC service or license server.

## Architecture

Event-driven checks on server-authoritative Bukkit callbacks—no client mod install. Operators tune per-check sensitivity and ban duration in YAML; Discord delivery failures should be treated as notification health separate from detection hits (see [[detector-operations]]).

## Positioning

Aimed at **small-to-medium** survival or minigame hosts who want a lightweight, self-hosted cheat deterrent. Contrasts with PacketEvents-heavy Paper/Folia stacks ([[h-ac]], [[virgola-anticheat]]) and client injectors such as [[nocturne-client]] on the attacker side.

## Detection stack

Movement (speed/bhop/fly), combat (reach/kill aura), world (fast break/nuker); violation counter → timed bans; admin GUI + Discord alerts.

## Links

- Repo: https://github.com/flameteamdev/LavaGuardAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[h-ac]] · [[bs-anticheat]] · [[minecraft-anticheat-list]] · [[nocturne-client]]
