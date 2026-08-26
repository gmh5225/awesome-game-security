---
title: PC Wacky Wheels Doc
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/vs-sr-dev__pc-wackywheels-doc.md
  - wiki/sources/README-categories.md
updated: 2026-08-26
confidence: medium
---

# PC Wacky Wheels Doc

Reverse-engineering documentation for **Wacky Wheels** (1994 DOS kart racer, Beavis Soft / Apogee). Analyzes retail 1994 build data: **WACKY.DAT** archive layout, track and sprite formats, fixed-point lookup tables behind the pseudo-3D floor renderer, audio assets, and save/config files. Pure **Python 3** tools (numpy, Pillow) parse and extract formats, rebuild world textures, and cross-reference related titles such as Skunny Kart. Archaeological work from shipped files rather than fan reconstructions—aimed at retro game RE and classic DOS engine/data-structure research. (source: wiki/sources/descriptions/vs-sr-dev__pc-wackywheels-doc.md)

Sits beside curated game file-format indexes such as [[awesome-game-file-format-reversing]] in the Cheat **RE Tools** lane — a title-specific DOS asset-format case study rather than a general index.

## Scope

| Area | Focus |
|------|-------|
| **WACKY.DAT** | Archive layout and embedded asset extraction |
| **Tracks / sprites** | On-disk format documentation |
| **Renderer LUTs** | Fixed-point lookup tables for pseudo-3D floor rendering |
| **Audio / saves** | Sound assets and configuration/save-file layouts |
| **Tooling** | Python 3 parsers/extractors (numpy, Pillow) |
| **Cross-refs** | Related Apogee-era titles such as Skunny Kart |

Methodology derives from the **1994 retail build** shipped data, not fan reconstructions — useful for studying classic DOS pseudo-3D render pipelines and proprietary archive layouts.

## Links

- Repo: https://github.com/vs-sr-dev/pc-wackywheels-doc (README tag: [RE documentation for Wacky Wheels])

## Related

[[awesome-game-file-format-reversing]] · [[batteryshark-github-io]] · [[devilution]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
