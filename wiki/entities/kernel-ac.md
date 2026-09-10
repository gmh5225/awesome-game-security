---
title: Kernel-AC
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/LucasAlgera__Kernel-AC.md
updated: 2026-09-10
confidence: medium
---

# Kernel-AC

**Educational Windows kernel anti-cheat graduation project** (LucasAlgera) pairing a KMDF kernel driver with a C++ console launcher to protect a running game process—not a production anti-cheat product. The driver registers **ObRegisterCallbacks** on process and thread handle create/duplicate operations, strips dangerous access rights from untrusted callers, and enforces a whitelist of trusted process names (e.g. `explorer.exe`, `discord.exe`). The user-mode client loads the driver through the Service Control Manager, communicates via IOCTLs to register the protected game PID, and serves as a learner-oriented reference for Windows kernel anti-cheat and game-security techniques. (source: wiki/sources/descriptions/LucasAlgera__Kernel-AC.md)

## Architecture

| Layer | Role |
|-------|------|
| **Kernel driver (KMDF)** | ObCallbacks on process/thread handles; access-right stripping; trusted-process whitelist |
| **User-mode launcher** | SCM driver load; IOCTL registration of protected game PID |
| **IOCTL surface** | Protected-process registration and driver control |

## Links

- Repo: https://github.com/LucasAlgera/Kernel-AC

## Related

[[kernel-callbacks]] · [[mini-anti-cheat-v2]] · [[bloom-anticheat]] · [[peregrine-anticheat]] · [[sentinelac]] · [[oac]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
