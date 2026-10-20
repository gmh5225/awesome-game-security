---
title: CS2AC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/karola3vax__CS2AC.md
updated: 2026-10-20
confidence: medium
---

# CS2AC

Open-source **server-side anti-cheat plugin** for Counter-Strike 2 dedicated servers. Built in C++ as a **Metamod:Source** plugin for Windows and Linux x64, it analyzes player aim, movement, inputs, and client settings without requiring anything on the client. (source: wiki/sources/descriptions/karola3vax__CS2AC.md)

## Detection surface

Ships about seventeen detection modules covering cheats such as aimbot, aimlock, silent aim, anti-aim, bunny hop, autostrafe, DLL injection, doubletap, invalid cvars, and related timing or input abuse.

## Operator features

- Chat and on-screen detection announcements
- Configurable kick or ban commands
- Player whitelists
- Optional Discord webhook evidence reporting

Targets community and dedicated CS2 server operators who want behavioral anti-cheat on servers they control—the same server-authoritative lane as [[plugify-cs2ac]] (ViTaminza; Plugify/s2sdk rewrite with Polyhook `libserver.so` usercmd/movement detours and s2sdk event/net/cvar/schema hooks while preserving [[cs2ac]] behavior), [[sac-the-server-anticheat]], [[anticheatsystem]], [[open.mp-anticheat]], and [[gamesoftacs]], rather than kernel products such as [[easy-anti-cheat]] or [[vanguard]]. (source: wiki/sources/descriptions/ViTaminza__plugify-cs2ac.md)

## Links

- Repo: https://github.com/karola3vax/CS2AC

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[plugify-cs2ac]] · [[cs2-calladmin]] · [[cs2kac]] · [[cs2-hybrid-anticheat-proposal]] · [[sac-the-server-anticheat]] · [[anticheatsystem]] · [[gamesoftacs]] · [[open.mp-anticheat]]
