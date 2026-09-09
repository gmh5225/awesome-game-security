---
title: Omikron TNS OMK Engine
kind: entity
topics: [reverse-engineering, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/sosso33__omikron-tns-omk-engine.md
  - wiki/sources/README-categories.md
updated: 2026-09-09
confidence: medium
---

# Omikron TNS OMK Engine

Open-source, from-scratch **C++20** reimplementation of the engine behind Quantic Dream and Eidos's 1999 title **Omikron: The Nomad Soul**, built from reverse-engineered documentation of the original `Runtime.exe` and shipped data formats. Python supports readers, web viewers, and a large automated verification suite; optional SDL and Vulkan backends enable interactive play. Documents and parses proprietary containers and subsystems—the 153-opcode script VM, 8192-byte game state, cutscenes, UI, audio, and 3D assets—and validates behavior by comparing announcement traces against captures from the original binary. Requires the user to supply their own legally owned game data. (source: wiki/sources/descriptions/sosso33__omikron-tns-omk-engine.md)

Sits in the Cheat **RE Tools** lane beside title-specific format studies such as [[pc-wackywheels-doc]] and curated indexes like [[awesome-game-file-format-reversing]]—evidence-backed late-1990s commercial engine preservation rather than a general tool.

## Scope

| Area | Focus |
|------|-------|
| **Engine core** | C++20 portable replica of original Runtime.exe behavior |
| **Formats** | Script VM (153 opcodes), game state, cutscenes, UI, audio, 3D assets |
| **Validation** | Automated trace comparison against original binary captures |
| **Tooling** | Python readers/viewers; optional SDL/Vulkan interactive backends |

## Links

- Repo: https://github.com/sosso33/omikron-tns-omk-engine

## Related

[[pc-wackywheels-doc]] · [[awesome-game-file-format-reversing]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[research-rigor]]
