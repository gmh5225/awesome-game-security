---
title: ps2-ida-vu-micro
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Goatman13__ps2_ida_vu_micro.md
updated: 2026-08-25
confidence: medium
---

# ps2-ida-vu-micro

IDA Python plugin that **searches for and disassembles PlayStation 2 Vector Unit (VU) microcode** embedded in PS2 executables. Provides shortcut-driven workflows for both manual address ranges and automatic discovery from **VIF MPG command patterns**. Lightweight and practical for PS2 game reverse engineering and vector-unit program analysis; branch-target reconstruction has known limitations in some scenarios. (source: wiki/sources/descriptions/Goatman13__ps2_ida_vu_micro.md)

Disassembly plugin—not a PS2 emulator or live-debug bridge. Complements other console static-RE IDA helpers such as [[ida-ps4-helper]] and [[ida-ps5-elf-plugin]] in the PlayStation RE lane.

## Links

- Repo: https://github.com/Goatman13/ps2_ida_vu_micro

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-ps4-helper]] · [[ida-ps5-elf-plugin]] · [[idaplugins]] · [[ida-plugins]]
