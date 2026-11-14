---
title: Among Us 3D VR AntiCheat
kind: entity
topics: [anti-cheat, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/Jolynes-Mods__Among-Us-3D-VR-AntiCheat.md
updated: 2026-11-14
confidence: medium
---

# Among Us 3D VR AntiCheat

Open-source **MelonLoader** mod that adds **host-side** anti-cheat for **Among Us 3D** and **VR** sessions. Implemented in **C#** for **.NET 6**, it applies **Harmony** runtime patches against the game's **Il2Cpp** and **Photon Fusion** assemblies to validate networked actions—kills, meetings, votes, tasks, vents, power-ups, cosmetics, movement speed, and related RPC paths. (source: wiki/sources/descriptions/Jolynes-Mods__Among-Us-3D-VR-AntiCheat.md)

## Operator tooling

Configurable in-game GUI, per-room whitelist and blacklist management, a fetched global cheat blacklist, automatic release updates, and kicks designed to bypass common anti-kick cheats. Targets streamers, room hosts, and communities that want practical client-side game security on Unity VR titles and a reference for mod-based defenses on Fusion-backed multiplayer.

## Posture

Runs on the **session host** with MelonLoader (not kernel AC or a dedicated headless server). Complements classic Among Us BepInEx stacks such as [[among-us-anti-cheat]], [[au-anticheat]], and [[banmod]], and other Unity host-moderation mods such as [[crewtools]] and [[fusion-anti-cheat]].

## Links

- Repo: https://github.com/Jolynes-Mods/Among-Us-3D-VR-AntiCheat

## Related

[[among-us-anti-cheat]] · [[au-anticheat]] · [[banmod]] · [[il2cpp]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]