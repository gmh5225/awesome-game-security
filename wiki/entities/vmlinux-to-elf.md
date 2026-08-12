---
title: vmlinux-to-elf
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/marin-m__vmlinux-to-elf.md
updated: 2026-07-30
confidence: medium
---

# vmlinux-to-elf

Python tool that converts raw **Linux kernel images** (`vmlinux`, `bzImage`, `zImage`) into proper **ELF** files with symbol tables. It extracts the kernel's **kallsyms** symbol table, reconstructs section headers, and produces an ELF binary loadable in IDA Pro, Ghidra, or other disassemblers with full function names. Aimed at Linux kernel researchers, exploit developers, and reverse engineers who need to analyze kernel binaries with proper symbol information. (source: wiki/sources/descriptions/marin-m__vmlinux-to-elf.md)

## Links

- Repo: https://github.com/marin-m/vmlinux-to-elf

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-kallsyms-symbol-renamer]] · [[vermagic]] · [[venom]] · [[wsl2-linux-kernel]]
