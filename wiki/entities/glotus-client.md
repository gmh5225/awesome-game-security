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

Listed under README **Cheat / Debugging**.

## Architecture

- **Injection:** Tampermonkey userscript at document-start; minified bundle built with **Bun**.
- **Hook surface:** WebSocket packet/socket managers, in-game object state, and input events.
- **Automation:** modular feature system spanning combat, control, grinding, and bot modules; movement simulation and spatial indexing for targeting/pathing.
- **Rendering:** custom overlay rendering on top of the game canvas.
- **Anti-bot bypass:** **Altcha proof-of-work solver** using Web Workers to satisfy server verification before the WebSocket session connects.

Useful for studying browser-game client manipulation, anti-bot challenge bypass, and real-time multiplayer web-game attack surfaces.

## Links

- Repo: https://github.com/murka007/glotus-client

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[krunker-loader]] · [[webcheat]] · [[ff3mmo]] · [[js-debugger-bypass-script]]
