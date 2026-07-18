---
title: AV-EDR-Killer
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md
updated: 2026-07-18
confidence: medium
---

# AV-EDR-Killer

BYOVD research focused on `wsftprm.sys`. The vulnerable path is IOCTL `0x22201C` with a 1036-byte buffer whose first 4 bytes are the target Process ID as a DWORD—useful for game-security and RE study of cheat / vulnerable-driver AV/EDR-kill techniques. (source: wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md)

## Links

- Repo: https://github.com/xM0kht4r/AV-EDR-Killer

## Related

[[byovd]] · [[ven0m-ransomware]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
