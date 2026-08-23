---
title: KSOCKET
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/wbenny__KSOCKET.md
updated: 2026-07-18
confidence: medium
---

# KSOCKET

Windows kernel-mode socket library (C) that wraps the Windows Sockets Kernel (WSK) API behind a simplified BSD-style socket interface. Drivers can open TCP/UDP connections from ring 0 with no user-mode helper—useful for studying covert kernel network channels and for network-capable research drivers. (source: wiki/sources/descriptions/wbenny__KSOCKET.md)

Contrasts with user-mode NDIS packet-filter APIs such as [[ndisapi]] (inspect/modify at the packet layer rather than BSD sockets in-kernel). Complements socket-style WSK wrappers such as [[libwsk]] (NuGet/MSBuild; familiar connect/send/recv API; WDK/VS driver workflows).

## Links

- Repo: https://github.com/wbenny/KSOCKET

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[libwsk]] · [[ndisapi]] · [[keyboardkit]] · [[injdrv]]
