---
title: ClrGuard
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/endgameinc__ClrGuard.md
updated: 2026-08-15
confidence: medium
---

# ClrGuard

Windows **defensive** tool that monitors and blocks .NET **CLR** (Common Language Runtime) assembly loading in processes. Uses **DLL hooking** through ClrHook to intercept CLR initialization, log PE metadata and hashes of loaded assemblies, and optionally run as a Windows service for persistent monitoring. (source: wiki/sources/descriptions/endgameinc__ClrGuard.md)

Mainly useful for defensive security researchers and blue-team operators studying .NET-based attack detection and CLR loading control — the inverse lane of managed packers/protectors such as [[confuserex]] and [[netcrypt]] in the Anti Cheat → CLR Protection category.

## Links

- Repo: https://github.com/endgameinc/ClrGuard

## Related

[[confuserex]] · [[netcrypt]] · [[obfuscar]] · [[mono]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
