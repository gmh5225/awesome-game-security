---
title: ReadWriteDriver
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ryan-weil__ReadWriteDriver.md
updated: 2026-07-23
confidence: medium
---

# ReadWriteDriver

Kernel research sample centered on **`ntUserSetSysColors`** as a cheat / driver-communication path—studying Ring0↔usermode I/O via a system-colors API rather than obvious IOCTL or named-device surfaces. (source: wiki/sources/descriptions/ryan-weil__ReadWriteDriver.md)

Function addresses are hardcoded for Windows 11 kernel `10.0.22000.376`, so the sample is version-sensitive and mainly useful for game-security and reverse-engineering researchers mapping offensive KM↔UM channels (adjacent to [[data-ptr-swap]], [[evcommunication]], [[boom]]).

## Links

- Repo: https://github.com/ryan-weil/ReadWriteDriver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[evcommunication]] · [[boom]] · [[window-hijack]] · [[ntmemory]]
