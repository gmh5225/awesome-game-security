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

**Actively maintained TypeScript Tampermonkey/Violentmonkey userscript** cheat client aimed primarily at **Miniblox**, with additional packages for **Narrow.one**, **Kirka.io**, and other browser shooters and sandbox titles. The repo is a **Bun + Rolldown** monorepo that emits a Violentmonkey-compatible bundle, with **Solid or React** HUD layers and a shared module framework (configurable HUDs, keybinds, **Brigadier-style in-game commands**). (source: wiki/sources/descriptions/MinibloxCheaters2__VapeRewrite.md)

Game integration uses **custom runtime hooks** on ticks, packets, chat, movement, and rendering rather than brittle early-page code patching. Feature modules span combat, movement, world interaction, visuals, **inventory automation**, and **network-oriented tricks**.

Listed under README **Cheat** (browser userscript lane beside [[glotus-client]] and [[krunker-loader]]).

## Architecture

- **Delivery:** Violentmonkey-compatible userscript bundle from TypeScript sources.
- **Integration:** hook points for game loop, networking, chat, and render paths; per-game packages share the module framework.
- **Operator surface:** modular HUDs, keybinds, and in-game command dispatch aligned with Brigadier-style UX.

## Security research

The repository documents how target browser games are **bundled and obfuscated**, making it a practical reference for **reverse engineering browser games** and for studying **client-side cheating techniques** relevant to anti-cheat and game-security research. (source: wiki/sources/descriptions/MinibloxCheaters2__VapeRewrite.md)

## Links

- Repo: https://github.com/MinibloxCheaters2/VapeRewrite

## Related

[[webcheat]] · [[wasm-ceserver]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
