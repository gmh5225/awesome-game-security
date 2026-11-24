---
title: OdinGuard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/kxdrsrt__OdinGuard.md
updated: 2026-11-24
confidence: medium
---

# OdinGuard

**OdinGuard** (kxdrsrt) is a **modular open-source anti-cheat stack** for **Ragnarok Online** private servers on **rAthena** or compatible forks. Operators configure protection modules, challenges, cheat signatures, and rollout policy in **OdinGuard Studio** or the Rust **`og` CLI**, then ship **signed** client and server builds with per-server keys. The Windows client uses a **32-bit guard DLL** and **ijl15 proxy loader** (C); rAthena integration and the wire protocol live in C++ with shared protocol definitions. Defenses include **X25519** handshake and **XChaCha20-Poly1305** encrypted game traffic, integrity and anti-debug checks, updatable signature packs, and **server-authoritative** rules (rate limits, honeypots, ban waves) aimed at bots and public cheat tools—an auditable alternative to closed commercial AC for RO server owners and game-security practitioners. (source: wiki/sources/descriptions/kxdrsrt__OdinGuard.md)

Listed under **Anti Cheat → Open Source Anti Cheat System** beside other community defensive stacks.

## Links

- Repo: https://github.com/kxdrsrt/OdinGuard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[rathena]] · [[rathenacn]] · [[rebirth-guard]] · [[ultimate-anti-cheat]]