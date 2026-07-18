---
title: BootBypass
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__BootBypass.md
updated: 2026-07-18
confidence: medium
---

# BootBypass

Windows Secure Boot / early-boot research utility that patches boot-manager security checks, disables Driver Signature Enforcement (DSE), and loads unsigned kernel drivers by manipulating boot configuration and CI.dll validation routines. Framed as a native-mode (`subsystem:native`) tool for DSE and [[hvci]] (Memory Integrity) bypass via smart `SeCiCallbacks` patching and independent Memory Integrity management. (source: wiki/sources/descriptions/wesmar__BootBypass.md)

Same-author lane as [[kvc]] and [[kernel-research-kit]]: here the focus is boot-manager / CI early-phase control rather than a signed-driver `g_CiOptions` controller or a multi-method map toolkit.

## Links

- Repo: https://github.com/wesmar/BootBypass

## Related

[[kvc]] · [[kernel-research-kit]] · [[hvci]] · [[byovd]] · [[efitool]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
