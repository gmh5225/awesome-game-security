---
title: Genshin Debugger Bypass
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__GenshinDebuggerBypass.md
updated: 2026-08-12
confidence: medium
---

# Genshin Debugger Bypass

DLL-based bypass for **Genshin Impact** anti-debugging that hooks critical Windows APIs with **Microsoft Detours** (`detours-x64.lib`) to neutralize **`mhyprot2.sys`** kernel-driver checks and allow attaching a debugger to the game process. A **CloseMhyprot2** module terminates or unloads the miHoYo anti-cheat kernel driver; **DebuggerBypass.cpp** intercepts `NtQueryInformationProcess`, `IsDebuggerPresent`, and related anti-debug calls to hide debugger presence from integrity checks. (source: wiki/sources/descriptions/gmh5225__GenshinDebuggerBypass.md)

Framed for game-security researchers studying anti-debug bypass against miHoYo/HoYoverse **`mhyprot2`** protection — complementary to [[mhynot2]] (driver-load circumvention research) and [[mhyprot2]] BYOVD IOCTL abuse, not a gameplay cheat.

## Links

- Repo: https://github.com/gmh5225/GenshinDebuggerBypass

## Related

[[mhyprot2]] · [[mhynot2]] · [[evil-mhyprot-cli]] · [[letme-gg]] · [[generic-game-detour-api-hook]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
