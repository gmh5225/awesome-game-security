---
title: evil-mhyprot-cli
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/kkent030315__evil-mhyprot-cli.md
updated: 2026-08-02
confidence: medium
---

# evil-mhyprot-cli

CLI proof-of-concept for abusing **`mhyprot2.sys`** — the signed miHoYo / Genshin Impact anti-cheat kernel driver — to obtain arbitrary kernel and user-mode memory read/write from an unprivileged user process. Useful for game-security researchers and reverse engineers studying offensive [[byovd]] / cheat vulnerable-driver primitives. (source: wiki/sources/descriptions/kkent030315__evil-mhyprot-cli.md)

The driver is a canonical LOLdriver family entry (see [[loldrivers]]); this repo exposes a command-line interface rather than a full mapper stack.

## Links

- Repo: https://github.com/kkent030315/evil-mhyprot-cli

## Related

[[byovd]] · [[loldrivers]] · [[windows-kernel-exploits]] · [[physmem-drivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
