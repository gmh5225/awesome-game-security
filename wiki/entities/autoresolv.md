---
title: AutoResolv
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/airbus-seclab__AutoResolv.md
updated: 2026-08-18
confidence: medium
---

# AutoResolv

IDA plugin that resolves external library calls in ELF binaries and maps wrapper functions back to their real implementations. Built with IDAPython using PyQt5 and pyelftools for an interactive workflow and cached analysis data. Can annotate call sites, list resolved library paths, and import function signatures from related binaries to improve decompilation accuracy. Targets reverse engineers who need faster understanding of dynamically linked ELF code across multiple architectures. (source: wiki/sources/descriptions/airbus-seclab__AutoResolv.md)

Sits in the Cheat IDA Plugins / ELF symbol-recovery lane beside [[vmlinux-to-elf]] and [[ida-ps5-elf-plugin]].

## Links

- Repo: https://github.com/airbus-seclab/AutoResolv

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idaplugins]] · [[vmlinux-to-elf]] · [[ida-ps5-elf-plugin]] · [[ida-kallsyms-symbol-renamer]]
