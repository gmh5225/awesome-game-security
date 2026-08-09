---
title: FF3 MMO
kind: entity
topics: [anti-cheat, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/joeltco__ff3mmo.md
updated: 2026-08-09
confidence: medium
---

# FF3 MMO

Browser-based multiplayer online RPG that recreates Final Fantasy III (NES) with co-op exploration, party play, trading, and PvP. Written in JavaScript: a Node.js WebSocket backend pairs with a canvas front end that loads a user-supplied NES ROM to drive sprites, encounters, items, and music. (source: wiki/sources/descriptions/joeltco__ff3mmo.md)

Server-side **arbiters** and **inventory mirrors** validate combat outcomes, economy events, trades, and equipment changes so crafted client packets cannot duplicate items, inflate stats, or spoof rewards. ROM reverse-engineering tooling built on jsnes extracts monster graphics, palettes, and game data from the emulator PPU for faithful recreation. Useful for studying server-authoritative multiplayer design and anti-cheat patterns in untrusted browser game clients.

## Links

- Repo: https://github.com/joeltco/ff3mmo

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[certael]] · [[socket-io]] · [[javascript-obfuscator]]
