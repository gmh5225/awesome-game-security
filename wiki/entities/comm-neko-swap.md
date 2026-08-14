---
title: Comm-NekoSwap
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Comm-NekoSwap.md
updated: 2026-08-14
confidence: medium
---

# Comm-NekoSwap

Kernel-mode communication driver that establishes a **covert user↔kernel channel** through **swap-based memory page operations** instead of a conventional device IOCTL surface. Data exchange between user-mode and kernel-mode components leverages memory page swapping to reduce visibility to anti-cheat telemetry that monitors standard driver communication paths. The README tags the sample under **`[Win32kApiSetTable]`**, placing it in the win32k GUI-subsystem stealth-I/O lane. (source: wiki/sources/descriptions/gmh5225__Comm-NekoSwap.md)

Mainly useful for Windows kernel researchers studying non-IOCTL KM↔UM channels, win32k internal table abuse, and page-swap tradecraft for AC evasion — adjacent to [[comm-data-ptr-driver]], [[comm-data-pointer-swap]], [[data-ptr-swap]], [[dataptrswap-driver]], and [[custom-data-ptr-swap-sample]].

## Links

- Repo: https://github.com/gmh5225/Comm-NekoSwap

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[comm-data-ptr-driver]] · [[data-ptr-swap]] · [[dataptrswap-driver]] · [[custom-data-ptr-swap-sample]] · [[interep-driver-leak]] · [[window-hijack]]
