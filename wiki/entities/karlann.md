---
title: Karlann
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/hkx3upper__Karlann.md
updated: 2026-08-05
confidence: medium
---

# Karlann

Windows kernel driver proof-of-concept combining **keyboard input injection** (`Kbd.c`) and **Winsock Kernel (WSK)** network I/O (`Wsk.c` with [[libwsk]]). README category: `[Keyboard]`. (source: wiki/sources/descriptions/hkx3upper__Karlann.md)

Useful for studying kernel-mode keyboard simulation paths beside MouClass mouse research such as [[kernel-mouse]], and for covert ring-0 TCP/UDP channels alongside BSD-style WSK wrappers such as [[ksocket]] and [[libwsk]].

## Links

- Repo: https://github.com/hkx3upper/Karlann

## Related

[[kernel-mouse]] · [[ksocket]] · [[libwsk]] · [[keyboardkit]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
