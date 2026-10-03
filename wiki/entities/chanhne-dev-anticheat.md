---
title: Chanhne-dev AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Chanhne-dev__AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# Chanhne-dev AntiCheat

**AntiCheat** (Chanhne-dev/AntiCheat) is a **Java** Minecraft **Paper/Folia** server plugin that detects and blocks common client-side cheating without requiring player installs. It targets **Minecraft server operators** who need **server-side** anti-cheat rather than kernel-level drivers or commercial game protection. (source: wiki/sources/descriptions/Chanhne-dev__AntiCheat.md)

README category: Anti Cheat / Open Source Anti Cheat System / game:minecraft.

## Detection

- **Periodic scan tasks** — scheduled movement and behavior checks (fly detection) plus illegal-item inventory scanning.
- **Client-mod modules** — targeted detectors for **Meteor Client**, **TrouserStreak**, and **NoraTweaks**.
- **Anti-ESP integration** — optional entity-culling logic that hides entities outside a player's line of sight.

## Operations

Violation tracking, configurable enforcement actions, **Discord webhook** alerts, and optional movement logging for staff review.

## Positioning

Paper/Folia server-side AC for operators who want client-mod fingerprinting (Meteor/TrouserStreak/NoraTweaks) and illegal-item enforcement beside heuristic plugins such as [[bs-anticheat]], starter frameworks such as [[nova-anticheat]], and survival plugins such as [[ultimate-meteor-anticheat]].

## Peers

[[h-ac]] · [[nova-anticheat]] · [[ultimate-meteor-anticheat]] · [[larping-anti-cheat]] · [[key-value-checker]] · [[minecraft-anticheat-list]]

## Links

- Repo: https://github.com/Chanhne-dev/AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]]
