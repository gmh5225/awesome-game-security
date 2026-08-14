---
title: Comm-ImMiraclela
kind: entity
topics: [windows-kernel, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__Comm-ImMiraclela.md
updated: 2026-08-14
confidence: medium
---

# Comm-ImMiraclela

Paired user-mode and kernel-mode **Escape From Tarkov overlay framework** (gmh5225) that communicates through a hook on **`NtDxgkGetTrackedWorkloadStatistics`** in **dxgkrnl**: the kernel component patches the export with a small jump stub, handles **module-base lookup** and **process memory read/write**, and resolves **win32k drawing exports** to render boxes and text from kernel space. The user-mode side wraps the same syscall from **win32u.dll**, sends request structures into the hooked path, and layers an **ImGui-based overlay** with game-specific visuals on top of that channel. Mainly useful for reverse engineers studying **dxgkrnl-based driver communication**, **kernel-assisted drawing paths**, and mixed user/kernel overlay designs for Tarkov-style tooling. (source: wiki/sources/descriptions/gmh5225__Comm-ImMiraclela.md)

Adjacent to sibling `NtDxgkGetTrackedWorkloadStatistics` samples such as [[kernel-cheat-for-directx3d]] (covert KM↔UM comms + win32k GDI draw), [[nulldriver-cheat]] (`NtOpenCompositionSurfaceSectionInfo`), and [[dxgkrnl-hook]] (screen-buffer overlay research). EFT cheat scaffolds such as [[eft-internal]], [[eft-veil-eft]], and [[eft-newtarkov-cheatproject]] sit in the same **game:eft** lane with different memory/render paths.

## Links

- Repo: https://github.com/gmh5225/Comm-ImMiraclela

## Related

[[kernel-cheat-for-directx3d]] · [[nulldriver-cheat]] · [[dxgkrnl-hook]] · [[krnl-gdi-render]] · [[eft-internal]] · [[eft-veil-eft]] · [[present-hook]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
