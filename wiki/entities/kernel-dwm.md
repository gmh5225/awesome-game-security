---
title: KernelDwm
kind: entity
topics: [windows-kernel, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/cs1ime__KernelDwm.md
updated: 2026-08-16
confidence: medium
---

# KernelDwm

Windows **kernel-mode DWM overlay** technique: a C driver hooks the Desktop Window Manager (DWM) composition pipeline from Ring0, intercepts DWM DirectX rendering calls at the kernel level, and injects custom draw commands into the desktop compositor. Overlays composed this way sit outside typical user-mode Present-hook and layered-window paths—aimed at stealthy overlay research and studying DWM composition internals. (source: wiki/sources/descriptions/cs1ime__KernelDwm.md)

README category tag: **`[DWM In Kernel]`** — same kernel DWM overlay lane as [[double-callback]], beside user-mode [[dwm-hook]] / [[dwmhook]] / [[dwm-dwmdraw]] and Ring0 GDI/dxgkrnl draw paths such as [[krnl-gdi-render]] and [[dxgkrnl-hook]].

## Links

- Repo: https://github.com/cs1ime/KernelDwm

## Related

[[double-callback]] · [[dwm-hook]] · [[dwmhook]] · [[dwm-dwmdraw]] · [[krnl-gdi-render]] · [[dxgkrnl-hook]] · [[present-hook]] · [[anti-screenshot-capture]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
