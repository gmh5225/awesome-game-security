---
title: ROP-COMPILER
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Speedi13__ROP-COMPILER.md
updated: 2026-08-20
confidence: medium
---

# ROP-COMPILER

**ROP-COMPILER** (Speedi13) is a **return-oriented programming compiler** for building game cheat payloads targeting **CS:GO**, **Battlefield 3**, and **Battlefield 4**. It accepts custom x86 assembly-like scripts and translates them into ROP chains, with gadget scanning and offset handling implemented in C++. The repository ships practical examples including triggerbot, glow ESP, and minimap spotting logic. Primary use case is game security research into exploit-style cheat execution and anti-cheat evasion techniques. (source: wiki/sources/descriptions/Speedi13__ROP-COMPILER.md)

Sits in the script-to-chain ROP generation lane beside [[angrop]], [[exrop]], [[ropgadget-rs]], and [[agafi]]—game-targeted payload authoring rather than general binary gadget discovery.

## Examples

| Module | Role |
|--------|------|
| Triggerbot | Automated firing on crosshair target |
| Glow ESP | Player glow highlighting |
| Minimap spotting | Radar/minimap enemy visibility |

## Links

- Repo: https://github.com/Speedi13/ROP-COMPILER

## Related

[[angrop]] · [[exrop]] · [[ropgadget-rs]] · [[agafi]] · [[csgo-internal]] · [[osiris]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
