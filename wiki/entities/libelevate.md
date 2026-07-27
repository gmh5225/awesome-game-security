---
title: libelevate
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/notscimmy__libelevate.md
updated: 2026-07-27
confidence: medium
---

# libelevate

C++ library for **elevating handles** and bypassing Windows handle-access restrictions. Uses driver or kernel-level primitives to open processes with full access rights even when anti-cheat or security software strips or denies usermode `OpenProcess` rights, then exposes a clean API for elevated handles usable in memory read/write research. Aimed at game-security researchers studying handle-elevation techniques opposite AC handle-protection mechanisms. (source: wiki/sources/descriptions/notscimmy__libelevate.md)

README category: Elevating Handle.

## Links

- Repo: https://github.com/notscimmy/libelevate

## Related

[[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ntmemory]] · [[sentinelac]] · [[vaultguard]]
