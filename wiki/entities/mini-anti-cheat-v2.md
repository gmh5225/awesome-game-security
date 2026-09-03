---
title: Mini Anti-Cheat V2
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Abdelnour2__MiniAntiCheatV2.md
updated: 2026-09-03
confidence: medium
---

# Mini Anti-Cheat V2

Small **educational Windows anti-cheat sample** (Abdelnour2) pairing a user-mode “game” application with a kernel driver to demonstrate basic process protection—not a production anti-cheat product. The driver exposes IOCTL interfaces for blacklist checks, game PID registration, and shield disable; the game communicates via `DeviceIoControl`. A blacklisted process (`Notepad.exe`) is blocked at game start and while running through **process-creation notify** routines. V2 adds a **memory shield** using **ObRegisterCallbacks** to strip sensitive handle rights (VM read/write, terminate) from other user-mode processes. (source: wiki/sources/descriptions/Abdelnour2__MiniAntiCheatV2.md)

## Architecture

| Layer | Role |
|-------|------|
| **User-mode game** | Registers with driver via IOCTL; triggers blacklist and shield controls |
| **Kernel driver** | Process-creation notify blacklist enforcement; ObCallbacks handle stripping (“memory shield”) |
| **IOCTL surface** | Blacklist checks, game PID registration, shield disable |

## Links

- Repo: https://github.com/Abdelnour2/MiniAntiCheatV2

## Related

[[kernel-callbacks]] · [[bloom-anticheat]] · [[peregrine-anticheat]] · [[anticheat-poc]] · [[ci-dll-demo]] · [[sentinelac]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
