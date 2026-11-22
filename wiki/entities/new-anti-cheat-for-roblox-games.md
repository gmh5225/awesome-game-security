---
title: Shadow Nextbot Anti-Cheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/misteorecandy__New-anti-cheat-for-Roblox-games.md
updated: 2026-11-22
confidence: medium
---

# Shadow Nextbot Anti-Cheat

**Shadow Nextbot Anti-Cheat** (misteorecandy/New-anti-cheat-for-Roblox-games) is a Roblox Studio anti-cheat package that punishes suspected exploiters with a psychological horror chase instead of an immediate kick. It targets Roblox developers who want lightweight, server-authoritative cheat detection with an immersive deterrent. (source: wiki/sources/descriptions/misteorecandy__New-anti-cheat-for-Roblox-games.md)

## Detection surface

Paired **server** and **local** Luau scripts: the server monitors player movement on `RunService.Heartbeat` to flag **speed hacks** and **prolonged flight** against configurable thresholds (maximum speed, air time, and related limits). (source: wiki/sources/descriptions/misteorecandy__New-anti-cheat-for-Roblox-games.md)

## Punishment flow

On trigger, the server signals the offender via a **ReplicatedStorage** `RemoteEvent`. The client LocalScript dims lighting, spawns a wall-passing shadow **Nextbot**, plays whisper audio that escalates to a fullscreen jumpscare, then removes the player—an immersive client-side deterrent rather than a silent kick. (source: wiki/sources/descriptions/misteorecandy__New-anti-cheat-for-Roblox-games.md)

## Positioning

Movement-focused Studio drop-in beside instant-kick Luau server AC such as [[volcano-ac]], modular frameworks such as [[acf]], and strike-based packages such as [[encryptic-roblox-anti-cheat]]—distinct for its horror-themed client punishment choreography.

## Links

- Repo: https://github.com/misteorecandy/New-anti-cheat-for-Roblox-games

## Related

[[overviews/anti-cheat]] · [[volcano-ac]] · [[acf]] · [[encryptic-roblox-anti-cheat]] · [[anticheat-dashboard]] · [[roblox-speed-tester]]