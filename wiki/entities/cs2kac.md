---
title: CS2KAC
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/speedskater1610__CS2KAC.md
updated: 2026-08-01
confidence: medium
---

# CS2KAC

Client-side, kernel-level anti-cheat component for Counter-Strike 2 that complements server-side plugins such as CS2AC and CS2FOW by exposing process, module, and handle integrity signals the game server cannot observe on the player's machine. Implemented as a Windows KMDF kernel driver (C) paired with a C++ user-mode service that loads the driver, attaches to `cs2.exe`, and polls detection reports over custom IOCTLs. (source: wiki/sources/descriptions/speedskater1610__CS2KAC.md)

## Architecture

- **Kernel driver:** WDK hooks including `ObRegisterCallbacks`, image and process notify routines, and thread creation monitoring.
- **Detection categories:** unsigned modules, suspicious cross-process handles, hidden thread entry points, manual-mapped drivers, debuggers, code integrity mismatches, heartbeat timeouts.
- **Reporting:** ring-buffer queue in the driver; usermode service forwards toward the server via a signed attestation channel (Discord webhook / bridge integration documented).

Targets game security researchers and anti-cheat developers building hybrid CS2 protection that combines server-side behavioral analysis with privileged client-side integrity checks.

## Links

- Repo: https://github.com/speedskater1610/CS2KAC

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[cs2ac]] · [[kernel-callbacks]] · [[cs2-hybrid-anticheat-proposal]] · [[sentinelac]] · [[darken-anticheat]]
