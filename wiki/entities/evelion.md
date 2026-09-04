---
title: Evelion
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/3a1__Evelion.md
updated: 2026-09-04
confidence: medium
---

# Evelion

**Evelion** (3a1/Evelion) is an **external ESP cheat** for **Counter-Strike 1.6** written in **C++**. It uses an **ImGui-based overlay** with configurable visuals and a **stream-proof presentation model** designed to stay outside normal game capture paths. The project is structured for **Visual Studio** builds and targets a legacy CS 1.6 environment in **windowed mode**. Primary audience is learners exploring **external cheat architecture**, **rendering overlays**, and **basic anti-cheat evasion** ideas. README tag: `[External]`. (source: wiki/sources/descriptions/3a1__Evelion.md)

Contrasts with ring-0 CS 1.6 samples from the same author such as [[zodiak]] (kernel GDI ESP + MouHID aimbot) by staying fully out-of-process while still drawing ESP visuals. Pairs with overlay scaffolds such as [[imgui-external-overlay]] and CS 1.6 study repos such as [[ezfrags]], [[oxware]], and [[hpp-hack]].

## Techniques

| Area | Approach |
|------|----------|
| Architecture | External (no in-process injection) |
| Visuals | ImGui overlay; configurable ESP-style visuals |
| Capture evasion | Stream-proof presentation outside normal game capture paths |
| Build | Visual Studio; windowed-mode CS 1.6 target |
| Audience | Educational external cheat + overlay + AC evasion study |

## Links

- Repo: https://github.com/3a1/Evelion (CS 1.6 External)

## Related

[[zodiak]] · [[imgui-external-overlay]] · [[ezfrags]] · [[oxware]] · [[hpp-hack]] · [[anti-screenshot-capture]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
