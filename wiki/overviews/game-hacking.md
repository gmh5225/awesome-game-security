---
title: Game Hacking
kind: overview
topics: [game-hacking]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/README-categories.md
updated: 2026-07-16
confidence: high
---

# Game Hacking

Offensive technique taxonomy and threat model: how cheats escalate from user-mode memory/injection to kernel drivers, hypervisors, EFI, and [[dma]] as defenders raise the bar. (source: wiki/sources/skills/game-hacking.md)

## Escalation model

1. **User-mode** — RPM/WPM, DLL/shellcode injection, graphics/input hooks
2. **Kernel-mode** — signed/vulnerable drivers ([[byovd]]), callback/page-table work
3. **Below the OS** — hypervisor, PCIe DMA, external devices / second machines

## Key sub-areas

- Memory, injection, hooking (inline/IAT/VTable/HWBP)
- Visual ESP / aim / movement cheats; AI visual pipelines (OBS + YOLO + HID)
- Overlays via [[present-hook]] and external/DWM windows
- HWID spoofing, stack spoofing, driver communication channels
- EFI boot-time mappers; engine-specific paths (Unreal/Unity/Source)

## Related concepts

[[dma]] · [[byovd]] · [[present-hook]] · [[il2cpp]] · [[kernel-callbacks]] · [[overviews/anti-cheat]]

## README map

`Cheat` is the largest category (~2500 links): debugging, injection, DMA, overlays, vulnerable drivers, EFI, HWID, game-specific trees, plus `Some Tricks` Ring0/Ring3. (source: wiki/sources/README-categories.md)
