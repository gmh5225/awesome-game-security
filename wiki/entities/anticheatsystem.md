---
title: AntiCheatSystem
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md
updated: 2026-09-09
confidence: medium
---

# AntiCheatSystem

Server-side **Counter-Strike 2** anti-cheat plugin (pavelinbs-afk) that runs as a **MetaMod:Source 2** native module on dedicated **Linux** game servers. Written in **C++17** with CMake, it performs in-process, server-authoritative cheat detection rather than relying solely on client-side or external services. (source: wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md)

## Detection stack

Modular analyzers cover aim snapping, wallhack visibility, movement speed, session statistics, and client integrity checks. Findings aggregate into a configurable **suspicion score**; when thresholds are reached the plugin logs warnings, files moderation reports, or applies bans.

## Operator integration

- JSON configuration for detection modules and scoring limits
- **AdminPlugin** and **PlaytimeReporter** integration over shared sanction and ticket APIs used by server administration tools
- Docker-based builds against **HL2SDK-CS2** for **linuxsteamrt64** deployment

## Links

- Repo: https://github.com/pavelinbs-afk/anticheatsystem

## Related

[[overviews/anti-cheat]] · [[cs2ac]] · [[little-anti-cheat]] · [[corner-culling-source-engine]] · [[cs2guard]] · [[nocheatz-3]] · [[detector-operations]]
