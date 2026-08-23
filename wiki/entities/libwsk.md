---
title: libwsk
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/MiroKaku__libwsk.md
updated: 2026-08-23
confidence: medium
---

# libwsk

Windows kernel networking library (C/C++) that wraps **Winsock Kernel (WSK)** behind a familiar user-mode **socket-style API**. Ships with NuGet and MSBuild integration for WDK and Visual Studio driver workflows; maps `connect`, `send`, `recv`, and address-conversion helpers to kernel-mode WSK calls. Targets kernel driver developers and security researchers who need ring-0 network I/O with lower integration friction than raw WSK. (source: wiki/sources/descriptions/MiroKaku__libwsk.md)

Complements BSD-style WSK wrappers such as [[ksocket]] and is used as a helper in combined input + covert-network PoCs such as [[karlann]] (`Wsk.c`).

## Links

- Repo: https://github.com/MiroKaku/libwsk

## Related

[[ksocket]] · [[karlann]] · [[rw-socket-driver]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
