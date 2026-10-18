---
title: Saturn Anti Cheat
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Optccopa__SaturnAntiCheat.md
updated: 2026-10-18
confidence: medium
---

# Saturn Anti Cheat

**Educational Windows kernel-mode anti-cheat stack** (Optccopa/SaturnAntiCheat) aimed at protecting **Counter-Strike 2** when launched with the `-insecure` option—not a production anti-cheat product. A WDK-built **WDM driver** (C) pairs with a native **launcher/GUI** that loads the driver as a service, verifies liveness via **IOCTL heartbeat**, and manages load/unload for research sessions. (source: wiki/sources/descriptions/Optccopa__SaturnAntiCheat.md)

## Detection surface

The driver registers **process**, **thread**, and **image-load** callbacks to track CS2, maintains allowlists of legitimate game, Steam, and System32 modules, and logs:

- Suspicious **remote threads** whose entry points lie outside mapped PE images
- **Unsigned** or non-allowlisted **DLL** loads

(source: wiki/sources/descriptions/Optccopa__SaturnAntiCheat.md)

## Architecture

| Layer | Role |
|-------|------|
| **Kernel driver (WDM, C)** | Process/thread/image-load callbacks; module allowlists; remote-thread and DLL-load telemetry |
| **Native launcher (GUI)** | SCM driver service management; IOCTL heartbeat; session-oriented load/unload |
| **Build** | CMake + Windows Driver Kit |

## Positioning

**Anti Cheat** educational lane beside [[kernel-ac]], [[mini-anti-cheat-v2]], and [[win-kernel-telemetry]] — for developers and researchers studying custom anti-cheat design and kernel-level cheat detection on Windows (injection/thread-origin and module-trust signals).

## Links

- Repo: https://github.com/Optccopa/SaturnAntiCheat [Educational Windows kernel anti-cheat with a WDM driver (thread origin checks) and a launcher that manages driver load/unload for `-insecure` game sessions]

## Related

[[kernel-callbacks]] · [[kernel-ac]] · [[win-kernel-telemetry]] · [[process-injection-detection-lab]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
