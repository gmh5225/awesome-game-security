---
title: PIPELINE Disasm
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: high
---

# PIPELINE Disasm

**pipeline-disasm** (mattgodbolt/pipeline-disasm) is a full rebuild-from-source disassembly of **PIPELINE** (1988 BBC Micro puzzle game), producing disc and flux images that match the original Superior Software release byte for byte. (source: wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md)

## Architecture

| Layer | Role |
|-------|------|
| **Annotated 6502 assembly** | Per-binary sources assembled with baron; replaces retail machine code |
| **Reconstructed BBC BASIC** | High-level sources for BASIC-hosted components |
| **Python / Node.js tooling** | Disassembly, disc layout, image comparison, automation |
| **jsbeeb** | Headless BBC Micro emulation for verification runs |

## Capabilities

- Flux and disc outputs match the retail release byte for byte; symbol dumps and execution traces support debugger labels and step-by-step reassembly verification.
- Documents Superior Software copy protection: programs in uncatalogued sectors with deleted data address marks, hidden stub loaders, and a self-decrypting hidden utility.
- Supports study of classic game engine logic, mission data formats, and retro anti-piracy mechanics on the BBC Micro.

## Use cases

Preservation and reverse engineering for enthusiasts who need annotated sources and provably identical rebuilds—not live-game memory cheating. Pairs with [[static-runtime-evidence]] byte-match baselines and [[binary-diffing]] retro preservation lanes.

## Positioning

Listed under **Cheat → RE Tools**. Full-source disassembly rebuild beside [[ik-plus-reforged]] in-place ST patches and [[pc-wackywheels-doc]] DOS archive RE; [[rom-weaver]] delta formats apply when the goal is patch distribution rather than annotated full-tree rebuild.

## Links

- Repo: https://github.com/mattgodbolt/pipeline-disasm

## Related

[[rom-weaver]] · [[ik-plus-reforged]] · [[pc-wackywheels-doc]] · [[static-runtime-evidence]] · [[binary-diffing]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
