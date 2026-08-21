---
title: Bloom Anti-Cheat
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Rycooop__Bloom-Anticheat.md
updated: 2026-08-21
confidence: medium
---

# Bloom Anti-Cheat

Multi-component **Windows x64 anti-cheat prototype** from Rycooop that combines kernel and user-mode protections for experimentation—not a production anti-cheat product. The driver layer registers **ObRegisterCallbacks** to shield both the anti-cheat process and the protected target process from hostile handle create/duplicate operations. Supporting DLL and application code plus Visual Studio project setup complete the stack for studying practical tradeoffs between kernel callbacks and user-mode monitoring. (source: wiki/sources/descriptions/Rycooop__Bloom-Anticheat.md)

## Architecture

| Layer | Role |
|-------|------|
| **Kernel driver** | Object callbacks (`ObRegisterCallbacks`) for handle-operation filtering on AC and target processes |
| **User-mode DLL / app** | Companion monitoring and orchestration alongside the driver |
| **Build** | Visual Studio projects for Windows x64 driver and usermode components |

## Links

- Repo: https://github.com/Rycooop/Bloom-Anticheat

## Related

[[kernel-callbacks]] · [[kernel-anticheat]] · [[oac]] · [[sentinelac]] · [[ac]] · [[darken-anticheat]] · [[anticheat-poc]] · [[van1338]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
