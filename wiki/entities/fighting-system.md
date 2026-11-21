---
title: Fighting System
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/aloqqgem__fighting-system.md
updated: 2026-11-21
confidence: medium
---

# Fighting System

**Fighting System** (aloqqgem/fighting-system) is a **Roblox Luau melee combat framework** that pairs **server-authoritative hits** with **lag compensation** and **client-side prediction** so online fights stay responsive without trusting the client for damage. (source: wiki/sources/descriptions/aloqqgem__fighting-system.md)

## Combat features

Ships M1 combos, blocking and parrying with guard breaks, dodge dashes with invincibility frames, a four-ability kit, ragdolls, and training dummies. Shared hitbox logic keeps client previews aligned with server confirmation. (source: wiki/sources/descriptions/aloqqgem__fighting-system.md)

## Server authority

The server keeps **position history** to rewind targets for hit tests, validates combat requests with **schema checks** and **strike-based kicks**, and judges movement over a **sliding window** so legitimate latency is corrected with snap-backs instead of punishments. (source: wiki/sources/descriptions/aloqqgem__fighting-system.md)

## Implementation

Procedural R15 animation, a unified hit pipeline for players and dummies, and dozens of **automated Studio tests** round out the stack. (source: wiki/sources/descriptions/aloqqgem__fighting-system.md)

## Audience

Roblox developers and anyone studying **networked action-game design**, especially lag-tolerant anti-cheat patterns and **exploit-resistant combat validation**—alongside Luau AC frameworks such as [[acf]] and compile-time remote hardening via [[cheeto]].

## Links

- Repo: https://github.com/aloqqgem/fighting-system

## Related

[[overviews/game-engine]] · [[overviews/anti-cheat]] · [[acf]] · [[cheeto]] · [[encryptic-roblox-anti-cheat]] · [[roblox-exploit-auditor]] · [[input-provenance]]