---
title: ringo-ac
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/000nico__ringo-ac.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: medium
---

# ringo-ac

**Ringo** (000nico) is a modular **Windows anti-cheat** stack for learning and research: a **WDM kernel driver**, **user-mode client**, and **C++ backend server** that does **not inject** into the game process. (source: wiki/sources/descriptions/000nico__ringo-ac.md)

## Driver telemetry

The driver registers **process**, **thread**, **image-load**, and **object** callbacks plus a **randomized scheduler** to collect telemetry. It detects **manual-mapped kernel drivers** and **BYOVD** abuse, verifies **module and section integrity**, and runs **red-pill** style checks for **hypervisors** and emulated environments. (source: wiki/sources/descriptions/000nico__ringo-ac.md)

## Platform posture

Records **hardware identity** and platform posture including **HVCI**, **VBS**, **Secure Boot**, **TPM**, test signing, and kernel debugging state. The device interface uses **caller signature checks** and **HMAC-protected IOCTLs**. (source: wiki/sources/descriptions/000nico__ringo-ac.md)

## Client and server

The client loads the driver and forwards reports to the server, which persists data in its own database and runs **rule-based analysis** to produce **player risk verdicts**. (source: wiki/sources/descriptions/000nico__ringo-ac.md)

## Audience

Targets game-security researchers and operators who want a readable, **non-injected** anti-cheat suitable for **community-managed servers** and similar environments where in-process modules are undesirable (e.g. CS2-style server protection research). Not positioned as a turnkey commercial product. (source: wiki/sources/descriptions/000nico__ringo-ac.md)

## Links

- Repo: https://github.com/000nico/ringo-ac

## Related

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[hawkeye]] · [[sentinelac]] · [[win-kernel-telemetry]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
