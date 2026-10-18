---
title: Samurais Scripts
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/YimMenu-Lua__Samurais-Scripts.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: high
---

# Samurais Scripts

**Samurai's Scripts (SSV2)** ([YimMenu-Lua/Samurais-Scripts](https://github.com/YimMenu-Lua/Samurais-Scripts)) is a **modular Lua 5.4 framework and script suite** for **Grand Theft Auto V** that loads into the **YimMenu** mod menu. It extends gameplay through an **ImGui** interface, **command console**, and organized feature modules rather than shipping a standalone injectable menu binary. (source: wiki/sources/descriptions/YimMenu-Lua__Samurais-Scripts.md)

Built on the **SmallBase** template, the codebase combines **reverse-engineered GTA V class bindings**, **native and pointer abstractions**, **script globals**, and large static datasets with online-oriented tools (business managers, heist editing, stat control, casino helpers) plus vehicle, self, and world enhancements. (source: wiki/sources/descriptions/YimMenu-Lua__Samurais-Scripts.md)

## Architecture

Backend **lifecycle**, **services**, reusable **libraries**, and **frontend tabs** are split so contributors can add behavior without mixing UI and game logic. The project targets **mod authors** and **reverse-engineering researchers** who want a reference for how menu Lua interacts with **in-memory structures**, **multiplayer script state**, and the **YimMenu scripting API** on supported **Legacy** and **Online** builds. (source: wiki/sources/descriptions/YimMenu-Lua__Samurais-Scripts.md)

## Catalog

Listed under README **Cheat** as a **GPL-3.0** Lua script collection and base for **YimMenu-focused GTA Online** roleplay and menu automation; complements the documentation-only [[yimmenu]] repo and full mod-menu implementations such as [[phake]] and [[bigbasev2]]. (source: wiki/sources/README-categories.md)

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[yimmenu]] · [[gta-reversed-modern]] · [[gta-5-sigs-1.59]] · [[phake]] · [[bigbasev2]]

## Links

- Repo: https://github.com/YimMenu-Lua/Samurais-Scripts
