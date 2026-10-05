---
title: win-kernel-telemetry
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/dancing4am__win-kernel-telemetry.md
updated: 2026-10-05
confidence: medium
---

# win-kernel-telemetry

Hands-on **Windows kernel driver lab** teaching EDR and anti-cheat primitives through small, commented **KMDF** and **WDM** examples. Four incremental drivers cover a minimal KMDF skeleton, process create/exit monitoring via `PsSetCreateProcessNotifyRoutineEx`, filtered DLL and driver image-load telemetry with `PsSetLoadImageNotifyRoutine`, and anti-cheat-style process memory protection using **ObRegisterCallbacks** with a fake game and reader test harness. C drivers target x64 and ARM64 via the Windows Driver Kit; companion C++ console utilities demonstrate protection behavior. Aimed at security researchers, game-security engineers, and reverse engineers learning how endpoint and AC components observe and protect processes in an isolated VM with test signing enabled. (source: wiki/sources/descriptions/dancing4am__win-kernel-telemetry.md)

## Links

- Repo: https://github.com/dancing4am/win-kernel-telemetry

## Related

[[kernel-callbacks]] · [[kernel-ac]] · [[mini-anti-cheat-v2]] · [[peregrine-anticheat]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
