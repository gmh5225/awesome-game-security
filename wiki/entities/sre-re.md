---
title: sre-re
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/formix__sre-re.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: high
---

# sre-re

**sre-re** (formix/sre-re) reverse engineers **Solar Realms Elite 0.994b**, a classic DOS BBS door game whose original Borland C++ 3.0 source is lost, with the stated goal of documenting behavior and eventually shipping a Linux C++ remake. (source: wiki/sources/descriptions/formix__sre-re.md)

## Architecture

| Layer | Role |
|-------|------|
| **Ghidra (incl. headless export)** | Static analysis of the retail executable; VROOMM overlay flattening for study |
| **Python utilities** | Disassembly helpers, string/call annotation, encrypted `.II` save decoders |
| **Recovered specs** | File formats, turn-by-turn rules transcribed from decompiled logic |
| **DOSBox workflow** | Formula verification against the original binary |

## Capabilities

- Documents legacy x86 reverse engineering when no source tree exists: overlay handling, save-format cryptography, and rule recovery validated against live runs.
- Not live-game memory cheating or anti-cheat tooling—preservation and binary-recovery research aligned with [[static-runtime-evidence]] and [[binary-evidence]] discipline.

## Positioning

Listed under **Cheat → RE Tools** beside [[dreams-to-reality-re]] (1997 asset/toolkit RE) and DOS format docs such as [[pc-wackywheels-doc]]; pairs [[overviews/reverse-engineering]] classic-executable lanes.

## Links

- Upstream: https://github.com/formix/sre-re
