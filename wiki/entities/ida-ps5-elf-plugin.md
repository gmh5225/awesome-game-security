---
title: ida-ps5-elf-plugin
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ida_ps5_elf_plugin.md
updated: 2026-08-08
confidence: medium
---

# ida-ps5-elf-plugin

IDA Pro plugin for loading and analyzing **PlayStation 5 ELF binaries**. Handles PS5-specific ELF format extensions, segment types, and dynamic linking structures used by PS5 executables, enabling disassembly and analysis of PS5 game and system binaries in IDA Pro. Aimed at console security researchers and reverse engineers analyzing PlayStation 5 software. (source: wiki/sources/descriptions/gmh5225__ida_ps5_elf_plugin.md)

Loader plugin—not a full PS5 SDK generator or live-debug bridge. Complements HV/boot research tooling such as [[ps5-linux-loader]] and the PS4 module-loader helper [[ida-ps4-helper]] in the PlayStation static-RE lane.

## Links

- Repo: https://github.com/gmh5225/ida_ps5_elf_plugin

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-ps4-helper]] · [[ps5-linux-loader]] · [[cssfontface-exploit]] · [[vmlinux-to-elf]]
