---
title: PeregrineAntiCheat
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/PatchRequest__PeregrineAntiCheat.md
updated: 2026-08-22
confidence: medium
---

# PeregrineAntiCheat

Educational **Windows anti-cheat** reference implementation (PatchRequest) spanning kernel and usermode layers. A game-process **injected DLL** performs **YARA signature scanning**, **call stack validation**, **hardware breakpoint monitoring**, and **named pipe IPC** to report detections to a backend service. The broader stack adds a **kernel minifilter**, **ObRegisterCallbacks**, **APC injection**, **MinHook** API hooks, **ETW Threat Intelligence** telemetry, a **Tauri** operator GUI, and a bundled **cheat test suite** for validation. (source: wiki/sources/descriptions/PatchRequest__PeregrineAntiCheat.md)

## Detection stack

| Layer | Mechanism |
|-------|-----------|
| **Usermode agent** | In-process DLL: YARA scans, stack walks, HWBP watch, named-pipe detection reports |
| **Kernel driver** | Minifilter + ObCallbacks handle policy; APC-based injection path |
| **Telemetry** | ETW-TI cross-process memory events |
| **Integration** | MinHook API interception; Tauri GUI; cheat test harness |

## Positioning

Full-stack educational AC sample for studying how production Windows clients combine ring-3 scanners, kernel callbacks, signature rules, and backend reporting—more complete than ring-3-only teaching repos such as [[mandragora]] or [[basic-anti-cheat]], and closer to open defensive drivers like [[cs2kac]] and [[oac]].

## Links

- Repo: https://github.com/PatchRequest/PeregrineAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[concepts/kernel-callbacks]] · [[concepts/etw-threat-intelligence]] · [[anticheat-poc]] · [[kernel-anticheat]] · [[anti-cheat-testing-framework]] · [[mandragora]] · [[basic-anti-cheat]]
