---
title: GhostJoin
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/KuryCat__GhostJoin.md
updated: 2026-08-23
confidence: medium
---

# GhostJoin

Minimal **Minecraft Java Edition** protocol client in pure **Python** that connects to a server and stays online without rendering or in-game interaction. Implements the full modern connection flow—**Handshake**, **Login**, **Configuration**, and **Play**—using only the standard library (`socket`, `struct`, `hashlib`, `zlib`), including offline-mode UUID generation, packet compression, Client Information, brand plugin messages, and Keep Alive replies. Packet IDs target protocol versions around **773–776**, with optional debug logging to help adapt to other versions. Intended for **authorized** testing of Minecraft anti-bot and anti-cheat systems on offline-mode servers you own or have explicit permission to probe. (source: wiki/sources/descriptions/KuryCat__GhostJoin.md)

## Protocol stack

- **Connection phases** — Handshake → Login → Configuration → Play without a game client or renderer.
- **Stdlib-only I/O** — socket framing, zlib compression, offline UUID derivation, and Keep Alive handling.
- **Version band** — packet IDs aligned to protocol **773–776** with debug hooks for porting.

Complements headless automation bots such as [[eafe]] and server-side Java AC plugins such as [[windfall-anticheat]], [[ycbr-anticheat]], and [[minecraft-anti-cheat]]; contrasts with in-process JVM clients such as [[phantom-client]] and [[yuri]].

## Links

- Repo: https://github.com/KuryCat/GhostJoin

## Related

[[eafe]] · [[minecraft-anticheat-list]] · [[windfall-anticheat]] · [[ycbr-anticheat]] · [[minecraft-anti-cheat]] · [[phantom-client]] · [[yuri]] · [[minecpp]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
