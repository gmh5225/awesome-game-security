---
title: Ghost Anti-Cheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/GhostNgEnd__Ghost-AntiCheat.md
updated: 2026-08-25
confidence: medium
---

# Ghost Anti-Cheat

Prediction-based anti-cheat plugin for Minecraft: Bedrock Edition servers running on Nukkit. Written in Java and built with Gradle, it simulates Bedrock Dedicated Server movement, collision, and physics on the server using an entity-component-system architecture to compare client-reported motion against expected outcomes. The plugin monitors network packets with latency compensation and runs checks for movement exploits such as phase, no-slow, and anti-knockback, as well as combat reach and hitbox abuse, invalid block breaking, elytra flight anomalies, bad packets, and multi-action violations. Aimed at Bedrock server operators and game-security practitioners who need server-side cheat detection rather than client-side enforcement. (source: wiki/sources/descriptions/GhostNgEnd__Ghost-AntiCheat.md)

## Detection stack

ECS-based BDS movement/collision/physics simulation; latency-compensated packet monitoring; phase, no-slow, and anti-knockback movement checks; reach and hitbox combat validation; invalid block breaking; elytra flight anomaly detection; bad-packet and multi-action violation checks.

## Links

- Repo: https://github.com/GhostNgEnd/Ghost-AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[oomph]] · [[paradox-anticheat]] · [[scythe-anticheat]] · [[minecraft-anticheat-list]] · [[grim]] · [[windfall-anticheat]]
