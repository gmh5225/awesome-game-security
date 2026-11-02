---
title: BedrockGuard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/TheMax98000__BedrockGuard.md
  - wiki/sources/README-categories.md
updated: 2026-11-02
confidence: medium
---

# BedrockGuard

**BedrockGuard** (TheMax98000/BedrockGuard) is a **Paper/Spigot/Folia** server plugin that provides anti-cheat detection tuned for **Minecraft Bedrock Edition** players on **Geyser** and **Floodgate** cross-play Java servers. It runs **alongside** conventional Java anti-cheats and applies checks **only** to Floodgate-linked Bedrock clients, whose touch/controller movement and packet timing differ enough that Java-centric plugins often exempt them or flag false positives. Depends on **Floodgate**, **PacketEvents**, and **Geyser** (on-server or behind Velocity/BungeeCord). (source: wiki/sources/descriptions/TheMax98000__BedrockGuard.md)

## Detection stack

Timer, speed, fly, reach, nuker, scaffold, autoclicker, bad packets, velocity, and kill aura checks with **violation levels** that decay over time. Staff receive in-game alerts; optional **Discord webhooks** and configurable punishments.

## Operator API

Exposes a developer API to **cancel or observe** violations for custom moderation flows.

## Links

- Repo: https://github.com/TheMax98000/BedrockGuard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[astrox-anticheat]] · [[fox-addition]] · [[windfall-anticheat]] · [[vanticheat]] · [[oomph]] · [[minecraft-anticheat-list]]
