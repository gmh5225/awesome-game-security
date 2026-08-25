---
title: BanMod
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/GiannBart__BanMod.md
updated: 2026-08-25
confidence: medium
---

# BanMod

BepInEx moderation and anti-cheat plugin for Among Us that helps hosts protect lobbies from cheaters, teamers, and disruptive players. Written in C# with Harmony runtime patches on Unity IL2CPP; syncs server-backed ban, cheater, and teamer lists, runs in-game detectors for AFK behavior, camera abuse, following, and other suspicious activity, and exposes moderator UI for kicks, bans, warnings, and player reporting. (source: wiki/sources/descriptions/GiannBart__BanMod.md)

## Features

- **Host-side AntiCheat module** — RPC/task abuse, crashers, and lobby-integrity checks at the lobby host.
- **Synced moderation lists** — server-backed ban, cheater, and teamer rosters shared across sessions.
- **Behavior detectors** — AFK, camera abuse, following, and related suspicious-activity heuristics.
- **Moderator tooling** — in-game UI for kicks, bans, warnings, and player reports; chat and meeting controls.
- **Lobby extras** — custom roles, lobby discovery, optional premium features via remote API, multi-language support.

Targets Among Us hosts and community moderators who want integrated anti-cheat enforcement and lobby management rather than manual moderation alone. Sits beside lightweight host plugins such as [[wellsanticheat]]; distinct from kernel or server-authoritative products such as [[easy-anti-cheat]], [[certael]], or [[magnetite]].

## Links

- Repo: https://github.com/GiannBart/BanMod

## Related

[[wellsanticheat]] · [[bepinex-il2cppbase]] · [[il2cpp]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
