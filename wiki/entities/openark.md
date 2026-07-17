---
title: OpenArk
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/yyl-20020115__OpenArk.md
updated: 2026-07-17
confidence: medium
---

# OpenArk

Open-source Windows kernel analysis and anti-rootkit toolkit with a Qt GUI and a kernel driver for deep system inspection. Enumerates processes, threads, modules, drivers, and [[kernel-callbacks]]; inspects kernel objects; views SSDT/shadow SSDT; monitors registry; lists network connections; and unlocks files—aimed at analysts and rootkit hunting rather than AC bypass. (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md)

Useful as a defensive/forensic lens on the same surfaces (callbacks, drivers, SSDT) that game-security research often studies from the attack side.

## Links

- Repo: https://github.com/yyl-20020115/OpenArk

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[bustercall]] · [[etw-explorer]]
