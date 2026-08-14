---
title: AsusDrv
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__AsusDrv.md
updated: 2026-08-14
confidence: medium
---

# AsusDrv

User-mode wrapper that exploits ASUS motherboard utility driver **`AsusBiosIoDrv64.sys`**: hardware-monitoring IOCTLs intended for sensor access can be abused for arbitrary **physical memory read/write**, yielding a [[byovd]] kernel-access primitive. Targets BYOVD researchers studying ASUS driver vulnerabilities and OEM utility-driver IOCTL abuse. (source: wiki/sources/descriptions/gmh5225__AsusDrv.md)

Same ASUS signed-driver research lane as [[asus-bsitf-0-day-poc]] and [[windows-10-22h2-vulnerable-driver-communication]]; complements hardware-monitoring BYOVD samples such as [[openhardwaremonitor-poc]] and [[speedfan-exploit]].

## Links

- Repo: https://github.com/gmh5225/AsusDrv

## Related

[[byovd]] · [[asus-bsitf-0-day-poc]] · [[windows-10-22h2-vulnerable-driver-communication]] · [[imxyvimapper]] · [[openhardwaremonitor-poc]] · [[physmem-drivers]] · [[overviews/windows-kernel]]
