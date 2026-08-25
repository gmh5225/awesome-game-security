---
title: KsDumper
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/EquiFox__KsDumper.md
updated: 2026-08-25
confidence: medium
---

# KsDumper

Windows **kernel-assisted process dumper** (EquiFox; C++): a custom driver plus user-mode client copies a target process **main module** from memory and rebuilds **PE32/PE64** headers and sections. Targets **protected applications** where user-mode handles are restricted—documented workflow covers driver loading, dump generation, and handling **anti-cheat-protected** targets. Primary use case is low-level reverse-engineering research on protected game binaries and kernel–user interaction patterns. README tag: *Dumping processes using the power of kernel space*. Lineage predecessor to GUI forks such as [[ksdumper-11]]. (source: wiki/sources/descriptions/EquiFox__KsDumper.md)

## Links

- Repo: https://github.com/EquiFox/KsDumper

## Related

[[ksdumper-11]] · [[byovd]] · [[dumpepe]] · [[league-dumper]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
