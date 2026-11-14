---
title: GTA 5 Trainer Menu Base (MenuForge)
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/misnopini1987__GTA-5-Trainer-Menu-Base.md
updated: 2026-11-14
confidence: medium
---

# GTA 5 Trainer Menu Base (MenuForge)

**MenuForge** is an MIT **C++17** scaffold for building modular in-game **trainer-style overlay menus** for **Grand Theft Auto V** on Windows—not a finished cheat menu, but reusable plumbing for custom trainer UIs and injection experiments. Layers separate **state**, **render**, **input**, and **content**, wired through **DirectX 11** and **Dear ImGui**. A registry-driven content API and deterministic navigation state machine drive menu structure; developers get semantic theme tokens, JSON localization with fallbacks, crash-safe atomic config persistence, runtime key rebinding with conflict detection, and stacked notification toasts. (source: wiki/sources/descriptions/misnopini1987__GTA-5-Trainer-Menu-Base.md)

## Audience

Targets modders, tool authors, and researchers who need a reusable **overlay framework** for GTA V tooling rather than shipping gameplay features out of the box. (source: wiki/sources/descriptions/misnopini1987__GTA-5-Trainer-Menu-Base.md)

## Posture

Sits in the **menu scaffold / ImGui** lane beside full GTA mod menus such as [[bigbasev2]], [[phake]], and [[grandtheftautov-cheat]], and beside scripting docs such as [[yimmenu]]—this repo supplies **UI architecture and D3D11 presentation plumbing**, not game logic or bypasses.

## Links

- Repo: https://github.com/misnopini1987/GTA-5-Trainer-Menu-Base

## Related

[[yimmenu]] · [[bigbasev2]] · [[phake]] · [[grandtheftautov-cheat]] · [[gtaiii-de-goldhook]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]