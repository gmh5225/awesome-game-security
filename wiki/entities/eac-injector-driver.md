---
title: Eac-Injector-Driver
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Eac-Injector-Driver.md
updated: 2026-08-13
confidence: medium
---

# Eac-Injector-Driver

User client plus **manually mapped** kernel driver that repurposes **`NtQueryIntervalProfile`** as a covert KM↔UM control channel for toggling [[easy-anti-cheat]] runtime state (gmh5225). The driver patches **HalDispatchTable** so syscall traffic through `NtQueryIntervalProfile` reaches a custom handler, then locates `EasyAntiCheat.sys` threads to suspend or resume them and temporarily disables **object callbacks** at a tracked altitude before restoring them. Usermode builds a small shellcode stub, resolves `NtQueryIntervalProfile` from `ntdll`, and sends `CODE_DISABLE` or `CODE_RESTORE` while handling DLL-loading workflow around the target process. Primarily a research sample for syscall-backed driver communication, HalDispatchTable abuse, and EAC thread/callback manipulation—not a maintained bypass product. (source: wiki/sources/descriptions/gmh5225__Eac-Injector-Driver.md)

## Links

- Repo: https://github.com/gmh5225/Eac-Injector-Driver

## Related

[[easy-anti-cheat]] · [[eac-bypass-1]] · [[kernel-callbacks]] · [[poseidon]] · [[r69-driver]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
