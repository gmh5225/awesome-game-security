---
title: Amethyst
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/NaySurGithub__Amethyst.md
updated: 2026-08-30
confidence: medium
---

# Amethyst

Prediction-based anti-cheat plugin for PowerNukkitX Minecraft Bedrock servers. Written in Java, it replays each player's input every tick through a reimplementation of Bedrock physics and compares the simulated position to what the client reports, measuring movement the game's own rules cannot explain instead of relying on simple speed thresholds. Features authoritative movement and vehicle simulation, client-side world state tracking with acknowledgment gating, combat prediction with entity rewind, and checks for fly, reach, kill aura, scaffold, inventory abuse, backtrack, and malformed packets. Aimed at Bedrock server operators and plugin developers who need server-side cheat detection, movement correction, and violation alerting. (source: wiki/sources/descriptions/NaySurGithub__Amethyst.md)

## Detection stack

Per-tick Bedrock physics replay from player input; simulated vs client-reported position delta (not threshold-only speed checks); authoritative movement and vehicle simulation; client world-state tracking with acknowledgment gating; combat prediction with entity rewind; fly, reach, kill aura, scaffold, inventory abuse, backtrack, and malformed-packet checks; server-side movement correction and violation alerting.

## Links

- Repo: https://github.com/NaySurGithub/Amethyst

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[ghost-anticheat]] · [[astrox-anticheat]] · [[blarion-anticheat]] · [[paradox-anticheat]] · [[scythe-anticheat]] · [[minecraft-anticheat-list]] · [[grim]] · [[inertia]]
