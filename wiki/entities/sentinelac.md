---
title: SentinelAC
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/vovasicidk__sentinelac.md
updated: 2026-07-24
confidence: medium
---

# SentinelAC

Open-source Windows-first anti-cheat skeleton (**Project Sentinel**) for studios building client integrity and signature distribution—not a finished commercial product. Stacks a thin in-process SDK, a separate signed usermode service, and a kernel-mode driver: the SDK exposes Init/Heartbeat/Shutdown, auto-maps PE `.text` and imports for integrity hashing without manual offsets, and reaches the service over named pipes or ALPC so enforcement stays outside the game binary. (source: wiki/sources/descriptions/vovasicidk__sentinelac.md)

The kernel agent uses documented [[kernel-callbacks]] such as `ObRegisterCallbacks` and load-image notify for process protection and unauthorized-driver detection; usermode adds call-stack validation and overlay / window-station guards. A Node.js backend ingests telemetry over mTLS, stores signatures (e.g. Postgres), and fans out blacklist updates via SSE for analyst-driven detection and response. README lane: open-source AC skeleton with usermode SDK, ObRegisterCallbacks kernel stub, overlay isolation, and stack-walk injection detection. Complements educational PoCs such as [[anticheat-poc]] and server-authoritative OSS stacks such as [[certael]].

## Links

- Repo: https://github.com/vovasicidk/sentinelac

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[kernel-callbacks]] · [[anticheat-poc]] · [[certael]] · [[easy-anti-cheat]] · [[vanguard]]
