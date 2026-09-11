---
title: Fusion AntiCheat
kind: entity
topics: [anti-cheat, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/irembo337__Fusion-AntiCheat.md
updated: 2026-09-11
confidence: medium
---

# Fusion AntiCheat

**FusionGuard** is a server-side anti-cheat and anti-crash protection mod for **LabFusion** multiplayer servers in **BONELAB**. Written in **C#** as a **MelonLoader** mod for **.NET 6**, it uses **Harmony** runtime patching to intercept and enforce policy on LabFusion network actions—item spawns and despawns, teleports, avatar changes, and message floods. (source: wiki/sources/descriptions/irembo337__Fusion-AntiCheat.md)

## Detection and enforcement

- **Crash and mod blocklists** — known crash barcodes and cheat mods
- **Rate limits** — flood and abuse throttling on network actions
- **Behavioral checks** — movement- and score-based cheat detection
- **Avatar allowlist enforcement** — restricts unauthorized avatar changes
- **SteamID lists** — configurable whitelist and blacklist
- **Operator tooling** — optional Discord webhook alerts and an in-game admin settings panel

Targets BONELAB server hosts and administrators who need practical protection against trainers, crashers, and griefers on LabFusion-hosted sessions—without kernel AC or client-side installs.

## Links

- Repo: https://github.com/irembo337/Fusion-AntiCheat

## Related

[[7dtd-anticheatmod]] · [[tshock]] · [[unityexplorer]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
