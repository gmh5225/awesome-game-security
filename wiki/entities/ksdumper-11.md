---
title: KsDumper-11
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mastercodeon314__KsDumper-11.md
updated: 2026-07-30
confidence: medium
---

# KsDumper-11

Classic Windows kernel-mode process dumper: a C# GUI talks to a custom driver (`KsDumperDriver.sys`) over IOCTL to read and dump target process memory. Loads the driver via KDU (Kernel Driver Utility) vulnerable-driver mapping to bypass Driver Signature Enforcement. Enumerates processes through undocumented NT APIs, parses PE32/PE64 headers in dumps, and ships registry patches to disable the Microsoft Vulnerable Driver Blocklist. README tags it as a legendary KsDumper lineage tool in the Cheat / Windows kernel explorer lane. (source: wiki/sources/descriptions/mastercodeon314__KsDumper-11.md)

## Links

- Repo: https://github.com/mastercodeon314/KsDumper-11

## Related

[[ks-dumper]] · [[byovd]] · [[known-driver-mappers]] · [[nemesis]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
