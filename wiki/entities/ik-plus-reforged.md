---
title: IK+ Reforged
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/stephane-perez__ik-plus-reforged.md
  - wiki/sources/README-categories.md
updated: 2026-10-05
confidence: medium
---

# IK+ Reforged

Assembly patch and Python tooling project enhancing **International Karate+** on Atari ST from stephane-perez. (source: wiki/sources/descriptions/stephane-perez__ik-plus-reforged.md)

## Capabilities

- Motorola 68000 assembly loaders and hooks applied to a user-supplied game image via Python patch scripts.
- Checksum and original-byte validation before modification; no copyrighted game data distributed.
- STE-specific enhancements: DMA sound and blitter-based fighter rendering.
- Simultaneous three-player support via parallel-port or Jaguar joysticks.
- Platform compatibility fixes for STE and Mega STE hardware crashes.
- JOYTEST utility for controller wiring diagnostics.

## Architecture

Patch pipeline extracts the game image, verifies bytes, applies assembly hooks, and optionally enables STE hardware paths. Development and validation use vasm assembler, Hatari emulation, and Capstone-based disassembly utilities.

## Use cases

Aimed at retro computing enthusiasts and reverse engineers studying or extending classic Atari ST game binaries. Retro-console binary patch lane beside [[rom-weaver]] ROM delta workflows and [[pc-wackywheels-doc]] DOS format RE — preservation-oriented patching, not live-memory cheating.

## Links

- Repo: https://github.com/stephane-perez/ik-plus-reforged

## Related

[[rom-weaver]] · [[pc-wackywheels-doc]] · [[saturnkit]] · [[binary-diffing]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
