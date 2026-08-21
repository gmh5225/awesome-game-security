---
title: KernelDrawing
kind: entity
topics: [graphics-api, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Sentient111__KernelDrawing.md
updated: 2026-08-21
confidence: medium
---

# KernelDrawing

Proof-of-concept Windows kernel driver that draws graphics from Ring0 **without installing traditional hooks**. Implemented in C++; invokes GDI-related kernel paths by spoofing required thread-context values to satisfy internal checks. The sample includes supporting primitives and documents version-dependent NT offsets and loading methods—aimed at low-level graphics and anti-cheat evasion research in controlled environments. (source: wiki/sources/descriptions/Sentient111__KernelDrawing.md)

Contrasts with hook-based Ring0 overlay frameworks such as [[krnl-gdi-render]] and dxgkrnl export hijacks such as [[kernel-cheat-for-directx3d]] that patch or trampoline graphics-kernel paths.

## Links

- Repo: https://github.com/Sentient111/KernelDrawing

## Related

[[krnl-gdi-render]] · [[kernel-cheat-for-directx3d]] · [[kernel-dwm]] · [[dxgkrnl-hook]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
