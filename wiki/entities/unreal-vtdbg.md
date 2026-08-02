---
title: UnrealVTDbg
kind: entity
topics: [windows-kernel, reverse-engineering, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/xhscfq__UnrealVTDbg.md
updated: 2026-08-02
confidence: medium
---

# UnrealVTDbg

Windows **hypervisor-assisted debugging framework** aimed at Unreal Engine games: Delphi front-end plus C/C++ kernel drivers, injection DLLs, and hook components. The VT-x driver and DbgkSys modules implement Intel VMX, EPT, and vmcall-based virtualization with EPT hooks, hardware debug-register handling, APC injection, and Microsoft Detours for stealthy breakpoints and debug events. Supporting tooling covers symbol resolution, Blowfish encryption, shared-memory IPC, and VMProtect integration, with separate Windows 10 and Windows 11 builds. Intended for game security research, reverse engineering, and authorized anti-cheat or kernel debugging where low-level visibility into protected Unreal processes is required. (source: wiki/sources/descriptions/xhscfq__UnrealVTDbg.md)

Sits in the VT-x/EPT kernel-debugging lane beside [[erisdbg]] and [[vt-debuuger]], with Unreal-specific focus; cataloged in [[anti-cheat-research-index]] as featured VT-x/EPT-assisted kernel debugging work.

## Links

- Repo: https://github.com/xhscfq/UnrealVTDbg

## Related

[[anti-cheat-research-index]] · [[erisdbg]] · [[vt-debuuger]] · [[hypervisor]] · [[ept-hook-detection]] · [[unreal-object-model]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
