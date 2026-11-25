---
title: idagba
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Nico-Posada__IDAGBA.md
updated: 2026-11-25
confidence: medium
---

# idagba

**IDAGBA** (Nico-Posada/IDAGBA) is an **IDA Pro 9.1+** loader and plugin (Python) for **Game Boy Advance** cartridge, homebrew, and link-cable multiboot images. At load time it rebuilds the GBA memory map, labels I/O registers and hardware structures, traces **devkitARM**-style startup through `main`, and applies ROM-to-RAM copies so Hex-Rays decompilation matches runtime layout. Signature libraries cover common GBA toolchains; BIOS software-interrupt calls and Thumb call stubs lift into ordinary typed calls. Targets reverse engineers and security researchers who need readable decompilations without hand-tuning raw ARM/Thumb dumps in IDA. (source: wiki/sources/descriptions/Nico-Posada__IDAGBA.md)

## Positioning

README **Game Boy** lane — IDA-side peer to Ghidra GBA loading via [[gba-ghidra-loader]] and DMG-focused [[ghidradboy]]; complements runtime study via [[bizhawk]], [[kevboy]], and [[feather-gb]].

## Links

- Repo: https://github.com/nico-posada/idagba

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[gba-ghidra-loader]] · [[ghidradboy]] · [[pokedaisy]] · [[gbar5]]