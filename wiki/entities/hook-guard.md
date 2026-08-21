---
title: HookGuard
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/SamuelTulach__HookGuard.md
updated: 2026-08-21
confidence: medium
---

# HookGuard

**HookGuard** (SamuelTulach) is a Windows kernel research driver that installs a **global exception-hook chain** to monitor and obfuscate **process address-space switching**. Implemented mainly in C, it works around low-level CR3 handling, exception dispatch flow, and debugger-related paths such as **`KdpDebugRoutineSelect`**, while aiming to remain **PatchGuard-aware** and **HVCI-compatible**. The technique logs attempted switches into a protected process context and demonstrates defensive concepts inspired by anti-cheat designs—useful for kernel anti-cheat research and advanced study of memory access control at context-switch time. README category: cheat / Global exception/KdpDebugRoutineSelect. (source: wiki/sources/descriptions/SamuelTulach__HookGuard.md)

Complements global exception-handler hook research such as [[hook-kdtrap]] and hypervisor-assisted address-space hooks such as [[hook-hvl-switch-virtual-address-space]], plus CR3 manipulation samples such as [[eac-cr3-shuffle]] from the same author.

## Links

- Repo: https://github.com/SamuelTulach/HookGuard

## Related

[[patchguard]] · [[hvci]] · [[hook-kdtrap]] · [[hook-hvl-switch-virtual-address-space]] · [[eac-cr3-shuffle]] · [[meme-rw]] · [[windows-kernel-pagehook]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
