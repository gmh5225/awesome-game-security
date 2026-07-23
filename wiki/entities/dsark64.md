---
title: DsArk64
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/sai2fast__DsArk64.md
updated: 2026-07-23
confidence: medium
---

# DsArk64

BYOVD research against Qihoo 360’s WHQL-signed `DsArk64.sys`: ring-0 process kill plus kernel read/write. The open path is process-image gated—spawn a 360 installer suspended (`CREATE_SUSPENDED`), inject shellcode that calls `CreateFileW("\\.\DsArk")` so `IoGetCurrentProcess()` sees a Qihoo-signed image, then `DuplicateHandle` the device handle back to the attacker and terminate the donor. Useful for game-security / RE study in the cheat vulnerable-driver lane. (source: wiki/sources/descriptions/sai2fast__DsArk64.md)

## Links

- Repo: https://github.com/sai2fast/DsArk64

## Related

[[byovd]] · [[av-edr-killer]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
