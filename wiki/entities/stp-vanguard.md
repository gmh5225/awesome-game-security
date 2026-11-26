---
title: STP-Vanguard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/FOCUSGAMERCH__STP-Vanguard.md
updated: 2026-11-26
confidence: medium
---

# STP-Vanguard

**STP-Vanguard** (FOCUSGAMERCH) is a **client–server anti-cheat stack** for **Grand Theft Auto: San Andreas Multiplayer (SA-MP)**—not to be confused with Riot [[vanguard]]. The client ships as a Windows **ASI** C++ module; the server side is a native SA-MP plugin with Pawn gamemode includes and optional SQL-backed signatures. (source: wiki/sources/descriptions/FOCUSGAMERCH__STP-Vanguard.md)

## Client

- Hooks the game **RakNet** path for custom handshake and detection traffic.
- **Hardware identity** collection, **memory integrity** checks, **filesystem** scanning, and detection of **injected modules** and known cheat artifacts.
- **CLEO-allowed** and **no-CLEO** build variants; **compile-time string obfuscation**.

## Server

- Native **SA-MP plugin** plus **Pawn** includes exchanging custom packets with connected clients.
- Optional **MySQL** signature data; callbacks for **bans**, **timeouts**, and **dynamic file hashing**.

## Audience

SA-MP **server operators** and researchers who want practical enforcement and instrumentation in that multiplayer ecosystem.

## Links

- Repo: https://github.com/FOCUSGAMERCH/STP-Vanguard

## Related

[[vortexac]] · [[alt-v-anticheat-guide]] · [[basic-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]