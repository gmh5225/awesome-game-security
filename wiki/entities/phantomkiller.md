---
title: PhantomKiller
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/redteamfortress__PhantomKiller.md
updated: 2026-07-24
confidence: medium
---

# PhantomKiller

Windows BYOVD process-killer that abuses a signed Lenovo `BootRepair.sys` via IOCTL `0x222014` to call `ZwTerminateProcess`, terminating PPL-protected AV/EDR (and similar) processes through direct kernel process-object manipulation. Useful reference for signed OEM-driver terminate primitives in the same vulnerable-driver lane as other AV/EDR killers. (source: wiki/sources/descriptions/redteamfortress__PhantomKiller.md)

## Links

- Repo: https://github.com/redteamfortress/PhantomKiller

## Related

[[byovd]] · [[av-edr-killer]] · [[lenovo-cve-2025-8061]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
