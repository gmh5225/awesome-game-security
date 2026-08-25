---
title: MmCopyMemory
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/EBalloon__MmCopyMemory.md
updated: 2026-08-25
confidence: medium
---

# MmCopyMemory

**MmCopyMemory** (EBalloon) is a short Windows **kernel anti-cheat proof of concept** in C++ focused on **`MmCopyMemory`** behavior during **memory scans**. It explains how kernel-mode scanners can copy process memory and ships a minimal example that **patches a specific check path** to alter scan handling. The repository is small and targets one mechanism rather than a full bypass framework. Primary use cases are **anti-cheat bypass research** and **defensive study** of kernel memory-inspection techniques. README category: cheat / Bypass MmCopyMemory. (source: wiki/sources/descriptions/EBalloon__MmCopyMemory.md)

Sits in the **`MmCopyMemory` bypass study** lane beside educational hook telemetry samples such as [[simple-mmcopymemory-hook]], PatchGuard-safe EFI runtime hooks such as [[efi-monitor]], and AC copy-path research such as [[callmewin32kdriver]] and [[badeye]]. Complements page-remapping protected-process access PoCs such as [[remap]] from the same author by focusing on **scan-path tampering** rather than surrogate-process VA remapping.

## Links

- Repo: https://github.com/EBalloon/MmCopyMemory

## Related

[[simple-mmcopymemory-hook]] · [[efi-monitor]] · [[callmewin32kdriver]] · [[badeye]] · [[remap]] · [[map-page]] · [[driver-kdtour]] · [[readphys]] · [[ksldump]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
