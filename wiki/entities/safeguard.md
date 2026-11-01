---
title: SafeGuard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/BlaizerBrumo__SafeGuard.md
updated: 2026-11-01
confidence: medium
---

# SafeGuard

**SafeGuard** (BlaizerBrumo) is a **Minecraft Bedrock Edition** **behavior-pack add-on** that detects common client-side cheats and gives server owners in-world moderation tools without a separate backend service. It is implemented mainly in **JavaScript** using the Bedrock **Script API (Beta APIs)**, alongside mcfunction assets, JSON entity definitions, and an in-game **admin panel item** for toggling modules and editing settings. Targets Bedrock realm and dedicated-server operators who need lightweight, configurable anti-cheat and admin tooling. (source: wiki/sources/descriptions/BlaizerBrumo__SafeGuard.md)

## Detection

Combat abuse includes killaura, high CPS, no-swing attacks, FOV anomalies, auto-totem, auto-crystal, and combat logging. World and inventory abuse covers block nuking, scaffold and air-place placement, invalid equipment or durability, and name spoofing, with optional chat spam and packet protections.

## Staff tools

Ban and mute workflows, freeze and vanish, inventory inspection, world border control, device bans, ore mining alerts, and **AutoMod** escalation when players repeat violations.

## Links

- Repo: https://github.com/BlaizerBrumo/SafeGuard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[blarion-anticheat]] · [[scythe-anticheat]] · [[paradox-anticheat]] · [[minecraft-anticheat-list]]
