---
title: Game Hacking
kind: overview
topics: [game-hacking]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zyhp__vac3_inhibitor.md
  - wiki/sources/descriptions/zodiacon__TotalPE2.md
  - wiki/sources/descriptions/zodiacon__QuickAsm.md
  - wiki/sources/descriptions/zoand__Injectors.md
  - wiki/sources/descriptions/zoand__BOOM.md
updated: 2026-07-17
confidence: high
---

# Game Hacking

Offensive technique taxonomy and threat model: how cheats escalate from user-mode memory/injection to kernel drivers, hypervisors, EFI, and [[dma]] as defenders raise the bar. (source: wiki/sources/skills/game-hacking.md)

## Escalation model

1. **User-mode** — RPM/WPM, DLL/shellcode injection, graphics/input hooks
2. **Kernel-mode** — signed/vulnerable drivers ([[byovd]]), callback/page-table work
3. **Below the OS** — hypervisor, PCIe DMA, external devices / second machines

## Key sub-areas

- Memory, injection, hooking (inline/IAT/VTable/HWBP); injection-testing samples such as [[injectors]] for AC stress evaluation. (source: wiki/sources/descriptions/zoand__Injectors.md)
- Visual ESP / aim / movement cheats; AI visual pipelines (OBS + YOLO + HID)
- Overlays via [[present-hook]] and external/DWM windows
- HWID spoofing, stack spoofing, driver communication channels (e.g. [[boom]] hijacks `Beep.sys` and alters hide/comm paths). (source: wiki/sources/descriptions/zoand__BOOM.md)
- EFI boot-time mappers; engine-specific paths (Unreal/Unity/Source)
- AC-system exploration repos (e.g. [[vac3-inhibitor]] for VAC3 hooking/memory work) sit in the user-mode lane of cheat research. (source: wiki/sources/descriptions/zyhp__vac3_inhibitor.md)
- PE triage of game/client modules (imports, TLS, .NET metadata) via viewers such as [[totalpe2]] before deeper RE. (source: wiki/sources/descriptions/zodiacon__TotalPE2.md)
- Rapid x86/x64 shellcode/asm prototyping with [[quickasm]] (assemble via Keystone, execute in-process). (source: wiki/sources/descriptions/zodiacon__QuickAsm.md)

## Related concepts

[[dma]] · [[byovd]] · [[present-hook]] · [[il2cpp]] · [[kernel-callbacks]] · [[vac3-inhibitor]] · [[totalpe2]] · [[quickasm]] · [[injectors]] · [[boom]] · [[overviews/anti-cheat]]

## README map

`Cheat` is the largest category (~2543 links): guides, debugging, packet sniff/capture, speedhack, RE tools, MBA/VMP/Themida/OLLVM fix lanes, DBI, PatchGuard/DSE, Windows/Linux/Android kernel explorers, Magisk/Xposed/Frida/ART-syscall hooks, iOS jailbreak/network, plus `Some Tricks` (Ring0/Ring3/Linux/Android). (source: wiki/sources/README-categories.md)
