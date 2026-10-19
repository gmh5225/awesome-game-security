---
title: bootleg16
kind: entity
topics: [anti-cheat, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/anas1412__bootleg16.md
updated: 2026-10-19
confidence: medium
---

# bootleg16

**Bootleg16** (anas1412/bootleg16) is a from-scratch **Counter-Strike 1.6** reimplementation in **Rust** on **Bevy**: classic GoldSrc movement, weapons, and economy in a modern **5v5 competitive** flow. Dedicated GoldSrc asset readers load original-style data; work splits across **client**, **authoritative game server**, and **lobby** crates with shared networking, simulation, and **encrypted match traffic**. Online features include Steam authentication, voice chat, match recordings, parties and matchmaking, custom games (knife rounds, map vetoes), and deathmatch warmup. **Server-side anti-cheat** is built into the online stack; **Docker**-based hosting scales lobby and game servers. The project targets developers and operators studying multiplayer FPS architecture, legacy asset pipelines, and practical anti-cheat in a live competitive shooter. (source: wiki/sources/descriptions/anas1412__bootleg16.md)

## Links

- Repo: https://github.com/anas1412/bootleg16

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[bevy]] · [[bevy-personal-test]] · [[lightyear]] · [[halflife]] · [[regamedll-cs]] · [[cs16-client]] · [[detector-operations]]
