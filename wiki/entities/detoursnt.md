---
title: DetoursNT
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/wbenny__DetoursNT.md
updated: 2026-07-18
confidence: medium
---

# DetoursNT

Port of Microsoft Detours that depends **only on `NTDLL.DLL`**, without modifying the upstream Detours sources. Useful when studying offensive hooking / trampoline techniques in environments where higher-level Win32 imports are undesirable or unavailable; the author points to [[injdrv]] for the NTDLL-only adaptation pattern. Aimed at game-security and reverse-engineering research in the cheat / hook lane. (source: wiki/sources/descriptions/wbenny__DetoursNT.md)

## Links

- Repo: https://github.com/wbenny/DetoursNT

## Related

[[injdrv]] · [[skiphook]] · [[scfw]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
