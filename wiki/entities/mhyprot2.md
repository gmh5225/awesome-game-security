---
title: mhyprot2
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__mhyprot2.md
updated: 2026-08-14
confidence: medium
---

# mhyprot2

Research tool documenting and exploiting miHoYo **`mhyprot2.sys`** — the signed Genshin Impact anti-cheat kernel driver — as a [[byovd]] primitive. The driver's IOCTL interface exposes kernel read/write and process-termination capabilities abusable from an unprivileged user process for kernel-level operations. Tracked as **CVE-2020-36603** in [[cve-2020-36603]] (HoYoVerse driver 1.0.0.0 fails to restrict unprivileged calls → SYSTEM LPE). Aimed at BYOVD and anti-cheat researchers studying vulnerable game AC driver surfaces. (source: wiki/sources/descriptions/gmh5225__mhyprot2.md)

Complements [[mhydeath]] (same author's BYOVD exploit lane), [[mhyprot2drvcontrol]] (C++ IOCTL control library for process R/W, module enum, and process kill), and [[evil-mhyprot-cli]] (CLI PoC for the same driver family); contrasts with [[mhynot2]], which studies circumvention of the driver's load requirement rather than IOCTL abuse. Anti-debug bypass samples such as [[genshin-debugger-bypass]] unload **`mhyprot2.sys`** and hook `IsDebuggerPresent` / `NtQueryInformationProcess` via Detours to hide debugger attach — same driver surface, different offensive lane. EasyPeasy AC bypass samples such as [[genshin-easy-peasy-bypass]] disable or circumvent the driver's integrity checks and detection to run modified Genshin clients — same driver surface, client-modification lane. Downstream title-internal samples such as [[paladins-internal-cheat]] wire the same **Mhyprot** backend into Paladins in-process cheat stacks as an alternative to a bespoke kernel driver.

## Links

- Repo: https://github.com/gmh5225/mhyprot2

## Related

[[byovd]] · [[cve-2020-36603]] · [[mhydeath]] · [[mhyprot2drvcontrol]] · [[evil-mhyprot-cli]] · [[mhynot2]] · [[genshin-debugger-bypass]] · [[genshin-easy-peasy-bypass]] · [[paladins-internal-cheat]] · [[loldrivers]] · [[physmem-drivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
