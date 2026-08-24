---
title: memmap
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/KGB-1337__memmap.md
updated: 2026-08-24
confidence: medium
---

# memmap

**memmap** (KGB-1337/memmap; Extend Manual Map) is a **C++ framework** for **driver-assisted process memory operations and module mapping**. It defines a **request-based communication layer** between user mode and a companion kernel driver for reading, writing, allocation, protection changes, and module queries. The sample workflow extends already-mapped modules and triggers execution through **hijacked API call paths**. Intended for advanced experimentation in memory manipulation, injection research, and game security analysis—not a turnkey stealth injector. (source: wiki/sources/descriptions/KGB-1337__memmap.md)

Contrasts with BTBD [[modmap]] (VAD/LDR host-module extension focus) and user-mode extend-map injectors such as [[modexmap]]; sits in the same driver-assisted manual-map research lane as [[kernelmode-dll-injector]] and [[rw-socket-driver]] for IOCTL-style cross-process control.

## Links

- Repo: https://github.com/KGB-1337/memmap

## Related

[[modmap]] · [[modexmap]] · [[kernelmode-dll-injector]] · [[rw-socket-driver]] · [[km-um-communication]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
