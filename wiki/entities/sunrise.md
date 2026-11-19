---
title: Sunrise
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ui2506__Sunrise.md
updated: 2026-11-19
confidence: medium
---

# Sunrise

**Sunrise** (ui2506/Sunrise) is a dedicated-server anti-cheat **plugin** for **SCP: Secret Laboratory** that restores server authority over combat, visibility, and interaction checks the base game leaves client-trusted. Written in **C#**, it loads through **LabAPI** and applies **Harmony** patches to replace latency backtrack with server-side position and rotation history, implement room-based and raycast anti-wallhack, validate item pickups and door interactions, and enforce server-side Tesla gate damage. (source: wiki/sources/descriptions/ui2506__Sunrise.md)

## Detection and server authority

- **Combat backtrack** — server-side position/rotation history instead of client-trusted latency rewind
- **Anti-wallhack** — room-based visibility plus raycast checks
- **Interactions** — server validation for item pickups and door use
- **Tesla gates** — authoritative server-side damage (blocks Tesla immunity cheats)
- **Modular detections** — movement anti-cheat and patches for SCP-specific exploits: silent aim, spinbot, wallhack, pickup-through-walls, and related vectors

Targets SCP:SL server owners and game-security practitioners who need a practical, maintainable server-side AC rather than a generic cheat client or RE toolkit.

## Links

- Repo: https://github.com/ui2506/Sunrise

## Related

[[tshock-anticheat]] · [[fusion-anti-cheat]] · [[wellsanticheat]] · [[corner-culling]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]