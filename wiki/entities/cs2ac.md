---
title: CS2AC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/karola3vax__CS2AC.md
updated: 2026-08-02
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

Targets community and dedicated CS2 server operators who want behavioral anti-cheat on servers they control—the same server-authoritative lane as [[open.mp-anticheat]] and [[gamesoftacs]], rather than kernel products such as [[easy-anti-cheat]] or [[vanguard]].

## Links

- Repo: https://github.com/karola3vax/CS2AC

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[cs2kac]] · [[cs2-hybrid-anticheat-proposal]] · [[gamesoftacs]] · [[open.mp-anticheat]]
