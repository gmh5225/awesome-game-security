---
title: VapeRewrite
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/MinibloxCheaters2__VapeRewrite.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: medium
---

# VapeRewrite

**TypeScript Tampermonkey/Violentmonkey userscript** cheat stack aimed primarily at **Miniblox**, with additional packages for **Narrow.one**, **Kirka.io**, and related browser shooters/sandbox titles. Built as a **Bun + Rolldown** monorepo with **Solid or React** HUD layers, a shared module framework (keybinds, Brigadier-style in-game commands), and **runtime hooks** on ticks, packets, chat, movement, and rendering instead of brittle early-page patches. (source: wiki/sources/descriptions/MinibloxCheaters2__VapeRewrite.md)

Listed under README **Cheat** (browser userscript lane beside [[glotus-client]] and [[krunker-loader]]).

## Architecture

- **Delivery:** Violentmonkey-compatible userscript bundle from TypeScript sources.
- **Integration:** custom hook points for game loop, networking, and render paths; modular combat/movement/world/visual/inventory/network feature packages.
- **Research value:** documents how target browser games are bundled and obfuscated—useful for browser-game RE and client-side cheat/AC study.

## Links

- Repo: https://github.com/MinibloxCheaters2/VapeRewrite

See also: [[webcheat]], [[wasm-ceserver]], [[overviews/game-hacking]] browser userscript lane.
