---
title: Interep Driver Leak
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Interep-Driver-Leak.md
updated: 2026-08-12
confidence: medium
---

# Interep Driver Leak

Leaked Windows **kernel driver** used for game cheating: provides a ring-0 component for **stealthy cross-process memory read/write** with user-mode communication designed to evade anti-cheat **driver detection** by avoiding conventional monitored device IOCTL surfaces. The archived README tags the sample under **`[NtGdiPolyPolyDraw]`**, placing it in the win32k **GDI syscall covert-comms** lane rather than a standard `\Device\` IOCTL channel. (source: wiki/sources/descriptions/gmh5225__Interep-Driver-Leak.md)

Useful for researchers studying leaked cheat-driver architectures, kernel-mediated RPM/WPM paths, and anti-cheat telemetry evasion via undocumented win32k messaging. Adjacent to other stealth I/O samples such as [[read-write-driver]], [[nulldriver-cheat]], [[kernel-cheat-for-directx3d]], and [[r69-driver]].

## Links

- Repo: https://github.com/gmh5225/Interep-Driver-Leak

## Related

[[read-write-driver]] · [[nulldriver-cheat]] · [[kernel-cheat-for-directx3d]] · [[r69-driver]] · [[cheat-driver]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
