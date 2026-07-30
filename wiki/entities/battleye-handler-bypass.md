---
title: BattlEye Handler BYPASS
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/masterpastaa__BattlEye-Handler-BYPASS.md
updated: 2026-07-30
confidence: medium
---

# BattlEye Handler BYPASS

Windows **KMDF kernel driver** that bypasses [[battleye]] **handle-stripping** by continuously re-creating process handles before BattlEye’s approximately **5-second cleanup cycle** removes them. Built with the WindowsKernelModeDriver10.0 toolset; exposes IOCTL dispatch routines for usermode communication. Useful for researchers studying BE object-callback handle protection and kernel-assisted handle maintenance opposite AC strip logic. (source: wiki/sources/descriptions/masterpastaa__BattlEye-Handler-BYPASS.md)

Complements usermode handle-elevation research such as [[libelevate]]; differs by running in kernel and racing BE’s periodic handle cleanup rather than elevating rights on a single open.

## Links

- Repo: https://github.com/masterpastaa/BattlEye-Handler-BYPASS

## Related

[[battleye]] · [[kernel-callbacks]] · [[libelevate]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
