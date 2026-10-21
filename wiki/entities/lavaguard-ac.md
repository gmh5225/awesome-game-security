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

Open-source **Bukkit/Spigot** Minecraft server anti-cheat plugin (Java; FlameTeam Studios). Configurable Bukkit event checks cover speed and bunnyhop, flight, extended reach and kill-aura-style combat, and fast break or nuker mining; violations accumulate toward timed name bans after a threshold. Staff workflows use an in-game admin GUI and `lavaguard` commands (reload; Polish or English messaging). Optional Discord webhooks post ban embeds asynchronously. YAML-driven settings and messages ship under GPLv3 for small-to-medium survival or minigame hosts wanting self-hosted cheat deterrence without external AC services. (source: wiki/sources/descriptions/flameteamdev__LavaGuardAC.md)

## Detection stack

Movement (speed/bhop/fly), combat (reach/kill aura), world (fast break/nuker); violation counter → timed bans; admin GUI + Discord alerts.

## Links

- Repo: https://github.com/flameteamdev/LavaGuardAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[h-ac]] · [[bs-anticheat]] · [[minecraft-anticheat-list]]
