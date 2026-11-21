---
title: dmn_minigame
kind: entity
topics: [anti-cheat, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/DMN-Software__dmn_minigame.md
updated: 2026-11-21
confidence: medium
---

# dmn_minigame

Collection of **twelve embeddable browser minigames** with a global leaderboard whose scores come only from **server-side input replay**, not client-submitted totals. The browser records **tick-aligned player input logs**; a **Fastify** API replays each run through the same seeded, bit-identical TypeScript simulation shared with the **React/Vite** web client so forged HTTP score posts cannot stand alone. (source: wiki/sources/descriptions/DMN-Software__dmn_minigame.md)

Game logic follows strict **determinism** rules—fixed tick rate, controlled randomness, no non-portable math. **SQLite** stores leaderboard state; the stack adds session tokens, log validation, rate limits, and one-time session consumption. Aimed at developers learning online score anti-cheat patterns; minigames can embed in pages or game clients (e.g. **FiveM NUI** iframes).

## Links

- Repo: https://github.com/DMN-Software/dmn_minigame

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[input-provenance]] · [[ghostline]] · [[bitgeist]] · [[pew-game]] · [[cobra-snake]] · [[game-quality-gates]]