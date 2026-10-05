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

**IK+ Reforged** (stephane-perez/ik-plus-reforged) is a patch and tooling project that enhances **International Karate+** on Atari ST by applying carefully verified binary fixes to a user-supplied copy of the game. (source: wiki/sources/descriptions/stephane-perez__ik-plus-reforged.md)

## Architecture

| Layer | Role |
|-------|------|
| **68000 assembly loaders/hooks** | Motorola assembly patches injected into the game image |
| **Python patch scripts** | Extract image, validate checksums and original bytes, apply hooks |
| **Validation toolchain** | vasm assembler, Hatari emulation, Capstone-based disassembly |

## Capabilities

- Checksum and original-byte validation before modification; no copyrighted game data distributed.
- STE-specific enhancements: DMA sound and blitter-based fighter rendering.
- Simultaneous three-player support via parallel-port or Jaguar joysticks.
- Platform compatibility fixes for STE and Mega STE hardware crashes.
- **JOYTEST** utility for diagnosing controller wiring.

## Use cases

Aimed at retro computing enthusiasts and reverse engineers who want to study or extend classic ST game binaries without distributing copyrighted game data. (source: wiki/sources/descriptions/stephane-perez__ik-plus-reforged.md)

## Positioning

Listed under **Cheat → RE Tools**. In-place 68000 binary patch workflow beside [[rom-weaver]] ROM delta formats and [[pc-wackywheels-doc]] DOS archive RE — preservation-oriented patching and hardware compatibility, not live-memory cheating. Pairs with [[binary-diffing]] retro patch lanes and [[overviews/reverse-engineering]] classic-platform tooling cluster.

## Links

- Repo: https://github.com/stephane-perez/ik-plus-reforged

## Related

[[rom-weaver]] · [[pc-wackywheels-doc]] · [[saturnkit]] · [[binary-diffing]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
