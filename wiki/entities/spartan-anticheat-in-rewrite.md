---
title: Spartan AntiCheat in Rewrite
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/Vagdedes__Spartan-AntiCheat-In-Rewrite.md
  - wiki/sources/README-categories.md
updated: 2026-11-12
confidence: medium
---

# Spartan AntiCheat in Rewrite

Work-in-progress **Java/Maven** rewrite of the long-running **Spartan** Minecraft server anti-cheat for **Spigot**, **Paper**, and **Folia**. Centers on a modular check framework with runners, per-detection violation tracking, and configurable punishments and staff commands.

Distinguishes Java and Bedrock clients, supports Bukkit- and packet-oriented detection modes, and integrates Floodgate, ViaVersion, Discord webhooks, and multi-version server scheduling. Aimed at server operators and plugin developers building modern server-side cheat detection. (source: wiki/sources/descriptions/Vagdedes__Spartan-AntiCheat-In-Rewrite.md)

## Detection stack

Modular check runners; violation counters; staff/punishment commands; Java vs Bedrock client paths; Bukkit and packet checks; Floodgate/ViaVersion bridges; Discord webhook alerts.

## Links

- Repo: https://github.com/Vagdedes/Spartan-AntiCheat-In-Rewrite (README: Java/Maven rewrite of Spartan Minecraft server AC)

## Related

[[minecraft-anti-cheat]] · [[vulcan-anticheat-built]] · [[shieldguard-anticheat]] · [[nexora-anticheat]] · [[overviews/anti-cheat]] · [[overviews/game-engine]]
