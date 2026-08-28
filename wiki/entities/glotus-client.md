---
title: Glotus Client
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Murka007__Glotus-Client.md
updated: 2026-08-28
confidence: medium
---

# Glotus Client

**TypeScript Tampermonkey userscript** cheat client for the browser multiplayer game **Moomoo.io**. Injects at **document-start**, hooks **WebSocket** traffic, game objects, and input handling to automate combat, defense, grinding, and bot-assisted play through dozens of modular combat, control, and utility features. (source: wiki/sources/descriptions/Murka007__Glotus-Client.md)

Includes client-side packet and socket managers, movement simulation, spatial indexing, custom rendering overlays, and an **Altcha proof-of-work solver** using Web Workers to bypass server verification before connecting. Built with **Bun** and distributed as a minified userscript bundle — useful for studying browser-game client manipulation, anti-bot challenge bypass, and real-time multiplayer web-game attack surfaces.

## Links

- Repo: https://github.com/murka007/glotus-client

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[krunker-loader]] · [[webcheat]] · [[ff3mmo]]
