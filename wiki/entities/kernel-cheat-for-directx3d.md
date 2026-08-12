---
title: Kernel-Cheat-for-directx3D
kind: entity
topics: [windows-kernel, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__Kernel-Cheat-for-directx3D.md
updated: 2026-08-12
confidence: medium
---

# Kernel-Cheat-for-directx3D

Kernel and user-mode communication sample (gmh5225) that **hijacks `NtDxgkGetTrackedWorkloadStatistics` in dxgkrnl**: the driver overwrites the dxgkrnl export with a small absolute jump stub, then multiplexes the same syscall channel for **process memory read/write** (`MmCopyVirtualMemory`, `KeStackAttachProcess`) and **kernel-assisted drawing** via resolved win32k GDI routines (`NtUserGetDC`, `NtGdiPatBlt`, `NtGdiCreateSolidBrush`). The user-mode client invokes the hooked graphics syscall through **win32u.dll**, passing a `NULL_MEMORY` structure that can request module bases, draw rectangles, or dispatch other commands—treating the graphics syscall as a covert command interface. Mainly useful for Windows kernel researchers studying **graphics-adjacent communication hooks**, ad hoc read-write services, and **kernel overlay rendering** through win32k exports. (source: wiki/sources/descriptions/gmh5225__Kernel-Cheat-for-directx3D.md)

Adjacent to sibling dxgkrnl export-hook samples such as [[nulldriver-cheat]] (`NtOpenCompositionSurfaceSectionInfo` covert comms + GDI helpers), [[dxgkrnl-hook]] (screen-buffer overlay research), and kernel GDI frameworks such as [[krnl-gdi-render]].

## Links

- Repo: https://github.com/gmh5225/Kernel-Cheat-for-directx3D

## Related

[[dxgkrnl-hook]] · [[nulldriver-cheat]] · [[krnl-gdi-render]] · [[double-callback]] · [[present-hook]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
