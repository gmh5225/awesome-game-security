---
title: spu2c
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Goatman13__spu2c.md
updated: 2026-08-25
confidence: medium
---

# spu2c

IDA Pro Python plugin that **annotates PlayStation 3 CELL Synergistic Processing Unit (SPU) machine code** with readable C-style comments per instruction. Decodes SPU opcodes and explains register operations with explicit vector lane sizes (128-bit, 8×16-bit, 16×8-bit, 4×32-bit). Resolves shuffle-byte masks when possible; reads opcode names from text while parsing fields from hex to avoid common IDA SPU plugin bugs. Supports scanning a single instruction, a selection, or an entire function via keyboard shortcuts. Aimed at reverse engineers and game-security researchers analyzing PS3 SPU firmware, libraries, or anti-cheat and protection code inside IDA. (source: wiki/sources/descriptions/Goatman13__spu2c.md)

Annotation plugin—not a PS3 emulator or live-debug bridge. Complements [[ps2-ida-vu-micro]] and other console static-RE IDA helpers such as [[ida-ps4-helper]] and [[ida-ps5-elf-plugin]] in the PlayStation RE lane.

## Links

- Repo: https://github.com/Goatman13/spu2c

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ps2-ida-vu-micro]] · [[ida-ps4-helper]] · [[ida-ps5-elf-plugin]] · [[idaplugins]] · [[ida-plugins]]
