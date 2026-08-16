---
title: vac-bypass-kernel
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/crvvdev__vac-bypass-kernel.md
updated: 2026-08-16
confidence: medium
---

# vac-bypass-kernel

**Kernel-mode VAC bypass** (crvvdev) aimed at the **external VAC scanner** path: VAC runs largely out-of-process and uses syscalls such as `NtReadVirtualMemory` to read game memory and perform integrity checks. This repo implements a fully working kernel-side countermeasure for researchers studying how external VAC memory reads can be interfered with. Listed under cheat / explore anticheat system:vac for game-security researchers and reverse engineers studying offensive VAC bypass techniques. (source: wiki/sources/descriptions/crvvdev__vac-bypass-kernel.md)

Contrasts with usermode Steam-client bypasses such as [[vac-bypass]] / [[vac-bypass-loader]] (inject into `Steam.exe`, patch `steamservice.dll`) and telemetry hooks such as [[vac-hooks]] / [[prevent-vac]]. Aligns architecturally with [[como-funciona-vac]]'s description of `steam.exe` as an external scanner using cross-process memory reads. Broader multi-AC kernel hide/R/W samples such as [[battleye-vac-eac-kernel-bypass]] target BattlEye/EAC alongside VAC rather than VAC-specific external-read bypass alone.

## Links

- Repo: https://github.com/crvvdev/vac-bypass-kernel

## Related

[[vac-bypass]] · [[vac-bypass-loader]] · [[como-funciona-vac]] · [[vac]] · [[battleye-vac-eac-kernel-bypass]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
