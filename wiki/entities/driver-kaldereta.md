---
title: Driver-kaldereta
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-kaldereta.md
updated: 2026-08-13
confidence: medium
---

# Driver-kaldereta

Unsigned kernel driver with a user-mode sample that exposes a broad memory-manipulation and input-simulation feature set through a custom communication hook instead of a conventional public device interface. (source: wiki/sources/descriptions/gmh5225__Driver-kaldereta.md)

The archived README lists process lookup, module-base discovery, virtual memory allocation and protection changes, read/write primitives, input simulation, pattern scanning, and manual DLL mapping. The sample wrapper sends `KALDERETA_MEMORY` requests through a hooked Win32 call path (`NtTokenManagerGetAnalogExclusiveTokenEvent`) rather than IOCTL-based device I/O. Useful as both a feature-rich cheat-driver skeleton and a reference for pairing kernel memory operations with a higher-level user-mode helper library—mainly for Windows kernel and reverse-engineering researchers studying driver communication hooks, memory tooling primitives, and integrated user/kernel manual-mapping workflows.

## Links

- Repo: https://github.com/gmh5225/Driver-kaldereta

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[evcommunication]] · [[data-ptr-swap]] · [[custom-data-ptr-swap-sample]] · [[ultra-driver-game-cheat]] · [[driver-read-write]] · [[interep-driver-leak]]
