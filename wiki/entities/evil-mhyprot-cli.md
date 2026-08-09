---
title: evil-mhyprot-cli
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/kkent030315__evil-mhyprot-cli.md
  - wiki/sources/descriptions/gmh5225__evil-mhyprot-cli.md
updated: 2026-08-09
confidence: medium
---

# evil-mhyprot-cli

CLI proof-of-concept for abusing **`mhyprot2.sys`** — the signed miHoYo / Genshin Impact anti-cheat kernel driver — to obtain arbitrary kernel and user-mode memory read/write from an unprivileged user process. Useful for Windows security researchers studying vulnerable anti-cheat drivers, ring3-to-ring0 memory primitives, and service-based [[byovd]] workflows. (source: wiki/sources/descriptions/kkent030315__evil-mhyprot-cli.md) (source: wiki/sources/descriptions/gmh5225__evil-mhyprot-cli.md)

Vulnerable IOCTL paths expose `MmCopyVirtualMemory` and memcpy-like behavior, allowing arbitrary kernel and user memory access once the service is running. The gmh5225 implementation finds a target process, initializes the vulnerable service and device in `mhyprot::init`, and dispatches tests or utility operations through a small driver abstraction — a usable front end for experimenting with the issue rather than only a writeup.

The driver is a canonical LOLdriver family entry (see [[loldrivers]]); these repos expose command-line interfaces rather than full mapper stacks. Complements [[mhyprot2]] and [[mhydeath]] from the same author lane.

## Links

- Repo (gmh5225): https://github.com/gmh5225/evil-mhyprot-cli
- Repo (kkent030315): https://github.com/kkent030315/evil-mhyprot-cli

## Related

[[byovd]] · [[mhyprot2]] · [[mhydeath]] · [[loldrivers]] · [[windows-kernel-exploits]] · [[physmem-drivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
