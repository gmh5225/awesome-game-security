---
title: FROGMAN Disasm
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mattgodbolt__frogman.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: high
---

# FROGMAN Disasm

**frogman** (mattgodbolt/frogman) rebuilds an unreleased **1993 BBC Micro flip-screen platformer** as fully annotated **BeebASM 6502** that reassembles into a bootable disc image matching the original byte for byte. (source: wiki/sources/descriptions/mattgodbolt__frogman.md)

## Architecture

| Layer | Role |
|-------|------|
| **Annotated 6502 / BeebASM** | Engine and level logic with baron/BeebASM assembly workflow |
| **BBC BASIC boot loaders** | Disc boot path beside hand-written assembly |
| **Python utilities** | Runtime memory dumps, disassembly helpers, Tiled level editing |
| **jsbeeb** | Emulator capture when static images hide encrypted stages |

## Capabilities

- Documents a **multi-stage XOR loader** keyed off **VIA timer** timing—static analysis fails until decrypted code is captured from emulator memory.
- Combines **radare2** disassembly, **runtime dump RE**, and binary comparison to prove byte-exact engine rebuilds.
- Supports study of size-constrained 8-bit platform engines and timer-gated copy protection beside full-tree preservation projects.

## Use cases

Retro preservation and reverse engineering for analysts who need provably identical rebuilds and loader documentation—not live-game memory cheating. Pairs with [[static-runtime-evidence]] byte-match baselines and [[binary-diffing]] full-tree disassembly lanes.

## Positioning

Listed under **Cheat → RE Tools** next to mattgodbolt/[[pipeline-disasm]] (Superior Software PIPELINE rebuild). [[rom-weaver]] and [[ik-plus-reforged]] cover patch-first ROM workflows when a full annotated tree is not required.

## Links

- Repo: https://github.com/mattgodbolt/frogman

## Related

[[pipeline-disasm]] · [[rom-weaver]] · [[ik-plus-reforged]] · [[static-runtime-evidence]] · [[binary-diffing]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
