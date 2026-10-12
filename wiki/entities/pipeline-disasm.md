---
title: pipeline-disasm
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# pipeline-disasm

Byte-identical rebuild-from-source disassembly of **PIPELINE** (1988 BBC Micro puzzle game) by mattgodbolt. (source: wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md)

## Capabilities

- Annotated 6502 assembly (baron) and reconstructed BBC BASIC replace each binary; Python and Node.js tools disassemble, lay out discs, compare images, and run headless jsbeeb emulation.
- Flux and disc outputs match the retail release byte for byte; symbol dumps and execution traces support debugger labels and step-by-step verification.
- Documents Superior Software copy protection: uncatalogued sectors, deleted data address marks, hidden stub loaders, and a self-decrypting hidden utility.

## Use cases

Preservation and reverse-engineering of classic game engines, mission data formats, and retro anti-piracy on the BBC Micro — adjacent to [[rom-weaver]] patch workflows and [[static-runtime-evidence]] byte-match validation, not live-game memory cheating.

## Links

- Repo: https://github.com/mattgodbolt/pipeline-disasm (README: Cheat / RE Tools)

## Related

[[rom-weaver]] · [[ik-plus-reforged]] · [[pc-wackywheels-doc]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
