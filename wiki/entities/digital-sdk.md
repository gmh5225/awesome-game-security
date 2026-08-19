---
title: digital-sdk
kind: entity
topics: [game-hacking, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/W1lliam1337__digital-sdk.md
updated: 2026-08-19
confidence: medium
---

# digital-sdk

C++ **internal CS:GO cheat base** from W1lliam1337 structured around interfaces, netvars, rendering, and utility modules for extension. Ships common gameplay features—ESP, bunnyhop, engine prediction, autowall, and chams—and exposes hook points on **CreateMove** and **Direct3D reset**. Uses **ImGui** for the menu and **MinHook** for function interception. Intended primarily for cheat-development practice and reverse-engineering research on Source-engine titles. (source: wiki/sources/descriptions/W1lliam1337__digital-sdk.md)

Treat as a teaching-oriented internal scaffold—not a feature-complete production cheat.

## Architecture highlights

| Component | Role |
|-----------|------|
| MinHook | Inline/trampoline hooks on game and engine functions |
| CreateMove hook | Client-side input and movement manipulation |
| Direct3D reset hook | Overlay/render lifecycle on device reset |
| Interfaces module | Resolve and wrap Source 1 client/engine exports |
| Netvars module | Entity property offset maps for gameplay features |
| Rendering module | ESP, chams, and visual overlays |
| Utility modules | Shared helpers for feature extension |
| ImGui menu | In-game overlay for toggles and configuration |

See [[source-netvars]] for netvar layout work and [[csgo-cheat-base]] for a comparable MinHook-based internal base with glow ESP and engine prediction.

## Links

- Repo: https://github.com/W1lliam1337/digital-sdk

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-netvars]] · [[csgo-cheat-base]] · [[csgo-internal-base]] · [[present-hook]] · [[ntminhook]] · [[csgosimple]]
