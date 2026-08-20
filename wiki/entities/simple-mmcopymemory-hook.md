---
title: Simple-MmcopyMemory-Hook
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Spuckwaffel__Simple-MmcopyMemory-Hook.md
updated: 2026-08-20
confidence: medium
---

# Simple-MmcopyMemory-Hook

**Educational Windows kernel driver** (Spuckwaffel) that hooks **`MmCopyMemory`** to demonstrate basic kernel hook mechanics and observe memory-copy behavior used by anti-cheat scanners. The code is intentionally simple and documented for learning; the project explicitly describes itself as **unstable and detectable** in real environments. Main use case: understanding kernel hook installation and inspecting anti-cheat telemetry on cross-process memory-copy paths—not production evasion. Listed under cheat / Hook MmcopyMemory. (source: wiki/sources/descriptions/Spuckwaffel__Simple-MmcopyMemory-Hook.md)

Sits in the **`MmCopyMemory` hook study** lane beside compact detour libraries such as [[driver-kdtour]] and PatchGuard-safe EFI runtime hooks such as [[efi-monitor]], and defensive research on AC reliance on copy helpers such as [[callmewin32kdriver]] and [[badeye]].

## Links

- Repo: https://github.com/Spuckwaffel/Simple-MmcopyMemory-Hook

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[driver-kdtour]] · [[efi-monitor]] · [[callmewin32kdriver]] · [[badeye]] · [[uedumper]]
