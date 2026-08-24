---
title: kernel-eac-be-comm
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/JGonz1337__kernel-eac-be-comm.md
updated: 2026-08-24
confidence: medium
---

# kernel-eac-be-comm

**Windows kernel-to-user communication framework** (JGonz1337) that routes commands through a **hooked win32k function pointer**. A C++ kernel driver pairs with a user-mode client and exposes process-base lookup, module lookup, memory read/write, allocation, freeing, and protection changes via custom request structures, XOR-obfuscated strings, and a compact ring-3↔ring-0 control protocol. Geared toward **anti-cheat bypass** and game memory tooling research under [[easy-anti-cheat]] and [[battleye]]—not a maintained bypass product. README lane: `NtGdiPolyPolyDraw`. (source: wiki/sources/descriptions/JGonz1337__kernel-eac-be-comm.md)

## Links

- Repo: https://github.com/JGonz1337/kernel-eac-be-comm

## Related

[[kernel-eac-be-injector]] · [[comm-data-ptr-driver]] · [[interep-driver-leak]] · [[data-communication]] · [[km-um-communication]] · [[easy-anti-cheat]] · [[battleye]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
