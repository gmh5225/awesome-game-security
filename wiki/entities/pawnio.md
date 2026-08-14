---
title: PawnIO
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/namazso__PawnIO.md
updated: 2026-08-14
confidence: medium
---

# PawnIO

Windows kernel driver (WDK, C++20 + platform assembly) that embeds a **Pawn scripting VM in kernel mode**. User-mode clients load **signed AMX bytecode modules** and invoke their functions through device **IOCTLs**. Natives expose low-level hardware and kernel interaction: physical and virtual memory R/W, MSR and PCI config access, CPUID, control/debug registers, I/O ports, and SMM invocation on x64. Module authenticity is verified with SHA-256 hashing and trusted public keys before execution. Companion user-mode libraries and Pawn include files support developing and signing scripts that run inside the driver. Aimed at kernel and game security researchers who need a scriptable interface for low-level Windows hardware, memory, and driver research. (source: wiki/sources/descriptions/namazso__PawnIO.md)

## Links

- Repo: https://github.com/namazso/PawnIO

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[physmem-drivers]] · [[readphys]] · [[ntmemory]] · [[driver-buddy-reloaded]]
