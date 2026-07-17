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
  - wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md
  - wiki/sources/descriptions/zhuzhu-Top__deobf.md
  - wiki/sources/descriptions/zhuowei__cheese.md
  - wiki/sources/descriptions/zhitkur__DayZzz.md
  - wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md
  - wiki/sources/descriptions/zhaodice__qemu-anti-detection.md
  - wiki/sources/descriptions/zer0condition__NTMemory.md
updated: 2026-07-17
confidence: high
---



# Game Hacking

Offensive technique taxonomy and threat model: how cheats escalate from user-mode memory/injection to kernel drivers, hypervisors, EFI, and [[dma]] as defenders raise the bar. (source: wiki/sources/skills/game-hacking.md)

## Escalation model

1. **User-mode** — RPM/WPM, DLL/shellcode injection, graphics/input hooks
2. **Kernel-mode** — signed/vulnerable drivers ([[byovd]]), callback/page-table work; cross-process R/W via MDL/CR3 helpers such as [[ntmemory]] (source: wiki/sources/descriptions/zer0condition__NTMemory.md)
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
- Title-specific offset/token dumps (e.g. Fortnite FLTokens via [[fortnite-fltokens-and-offsets]]) illustrate ephemeral cheat-research artifacts that rot quickly. (source: wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md)
- Fix OLLVM / deobfuscation plugins targeting `libtprt.so` (e.g. [[deobf]]) sit in the Cheat Fix OLLVM lane. (source: wiki/sources/descriptions/zhuzhu-Top__deobf.md)
- Magisk-style root on Android VR (Quest 3/3S) via [[cheese]] (Adreno CVE-2025-21479; temporary root, no boot rewrite) sits in the Cheat Magisk lane. (source: wiki/sources/descriptions/zhuowei__cheese.md)
- Title-specific DayZ cheat/modding samples such as [[dayzzz]] (SDK generation + overlays) illustrate game:dayz offensive research surface. (source: wiki/sources/descriptions/zhitkur__DayZzz.md)
- Hidden-PVE / QEMU-KVM anti-detection (e.g. [[proxmox-ve-anti-detection]], [[qemu-anti-detection]] device-string spoof such as QEMU→ASUS keyboard) sits in the `Cheat > QEMU/KVM/PVE/VBOX` lane. (source: wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md) (source: wiki/sources/descriptions/zhaodice__qemu-anti-detection.md)

## Related concepts

[[dma]] · [[byovd]] · [[present-hook]] · [[il2cpp]] · [[kernel-callbacks]] · [[ntmemory]] · [[vac3-inhibitor]] · [[totalpe2]] · [[quickasm]] · [[injectors]] · [[boom]] · [[fortnite-fltokens-and-offsets]] · [[deobf]] · [[cheese]] · [[dayzzz]] · [[proxmox-ve-anti-detection]] · [[qemu-anti-detection]] · [[overviews/anti-cheat]]



## README map

`Cheat` is the largest category (~2543 links): guides, debugging, packet sniff/capture, speedhack, RE tools, MBA/VMP/Themida/OLLVM fix lanes, DBI, PatchGuard/DSE, Windows/Linux/Android kernel explorers, Magisk/Xposed/Frida/ART-syscall hooks, iOS jailbreak/network, plus `Some Tricks` (Ring0/Ring3/Linux/Android). (source: wiki/sources/README-categories.md)
