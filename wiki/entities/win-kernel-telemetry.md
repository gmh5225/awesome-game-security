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

Hands-on **Windows kernel driver lab** (dancing4am/win-kernel-telemetry) teaching EDR and anti-cheat primitives through small, commented **KMDF** and **WDM** examples — not a production anti-cheat product. (source: wiki/sources/descriptions/dancing4am__win-kernel-telemetry.md)

## Capabilities (four incremental drivers)

| Example | APIs / focus |
|---------|----------------|
| Minimal KMDF skeleton | WDK driver bring-up baseline |
| Process create/exit monitor | `PsSetCreateProcessNotifyRoutineEx` |
| Image-load telemetry | `PsSetLoadImageNotifyRoutine` (filtered DLL and driver loads) |
| Process memory protection | **ObRegisterCallbacks** with fake game and reader test harness |

## Architecture

| Layer | Role |
|-------|------|
| **Kernel drivers (KMDF/WDM)** | Incremental C examples for process/image notify and object callbacks |
| **User-mode harness** | C++ console utilities demonstrating protection behavior |
| **Build targets** | x64 and ARM64 via the Windows Driver Kit |

## Positioning

**Anti Cheat / Windows Ring0 Callback** educational lane beside [[kernel-ac]] and [[mini-anti-cheat-v2]] — aimed at security researchers, game-security engineers, and reverse engineers learning how endpoint and AC components observe and protect processes in an isolated VM with test signing enabled.

## Links

- Repo: https://github.com/dancing4am/win-kernel-telemetry

## Related

[[kernel-callbacks]] · [[kernel-ac]] · [[mini-anti-cheat-v2]] · [[peregrine-anticheat]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
