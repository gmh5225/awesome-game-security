---
title: OAC (Open Anti-Cheat)
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/lauralex__OAC.md
updated: 2026-08-15
confidence: medium
---

# OAC (Open Anti-Cheat)

**OAC** (Open Anti-Cheat) is a demand-start defensive anti-cheat framework for Windows that pairs a kernel-mode driver with a user-mode client. The stack protects game processes through pre-launch integrity gates and continuous runtime monitoring, aimed at game security engineers and researchers building kernel-assisted anti-cheat. (source: wiki/sources/descriptions/lauralex__OAC.md)

## Architecture

| Layer | Role |
|-------|------|
| **Kernel driver** | CPU state snapshots, hardware breakpoint detection, hypervisor and integrity checks, post-start driver-load gating, optional `MmUnloadedDrivers` and PiDDB trace analysis |
| **User-mode client** | Preflight orchestration, suspended launch, process protection, handle policy enforcement, HVCI and code-integrity telemetry |

The driver uses **ObRegisterCallbacks** for handle filtering and cross-view integrity checks. The client builds a privacy-preserving composite hardware identity from corroborated system signals and supports audit, test, and production deployment modes with configurable severity thresholds, optional anti-debug hardening, and server-issued challenge binding. (source: wiki/sources/descriptions/lauralex__OAC.md)

PowerShell and Python tooling covers test-signing, driver policy management, and Hyper-V–based validation. (source: wiki/sources/descriptions/lauralex__OAC.md)

## Links

- Repo: https://github.com/lauralex/OAC

## Related

[[kernel-anti-cheat]] · [[darken-anticheat]] · [[cs2kac]] · [[sentinelac]] · [[kernel-callbacks]] · [[hvci]] · [[kernel-pool-scanning]] · [[fn-dma-cheat]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
