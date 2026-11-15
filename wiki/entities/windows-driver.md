---
title: windows-driver
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/optic-fyi__windows-driver.md
  - wiki/sources/README-categories.md
updated: 2026-11-15
confidence: medium
---

# windows-driver

**Rust KMDF kernel driver** (optic-fyi/windows-driver) for **Optic** on-device anti-cheat: supervises a paired user-mode Optic service via a named device, **IOCTL heartbeat** and status queries, and **WDF timers** that flag missed pings. Tamper events land in the **registry** and **Windows event log**. Core driver–service protocol logic lives in a separate **no_std** crate with golden tests that pin the wire contract; the KMDF layer owns device creation, ACLs, and **caller image-path verification**. Built on Microsoft **windows-drivers-rs**. Threat model treats even local **administrators** as hostile—emphasis on **detection and durable evidence**, not perfect prevention. (source: wiki/sources/descriptions/optic-fyi__windows-driver.md)

README lane: Open Source Anti Cheat System — kernel-assisted service supervision and anti-tamper telemetry.

## Links

- Repo: https://github.com/optic-fyi/windows-driver

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[windows-kernel-rs]] · [[win-kernel-telemetry]] · [[core-ac]] · [[driver-trust-boundaries]]