---
title: ac
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/donnaskiez__ac.md
updated: 2026-08-16
confidence: medium
---

# ac

Open-source **Windows kernel anti-cheat driver** from donnaskiez that combines multiple defensive telemetry paths in one research codebase. Detection modules include **NMI-based stack walking**, **APC/DPC stack analysis**, **`.text` integrity checks**, **handle stripping** via `ObRegisterCallbacks`, and **chained data-pointer detection**. Additional checks cover **attached-thread detection**, **return-address exception-hook detection**, **system-module device-object verification**, and **process handle-table enumeration** to flag suspicious cross-process access. Aimed at anti-cheat engineers and game-security researchers studying kernel-level cheat detection and building defensive AC prototypes — not a production anti-cheat product. (source: wiki/sources/descriptions/donnaskiez__ac.md)

Complements focused NMI stack-walk teaching drivers such as [[nmi-callback-handler]] from the same author, multi-telemetry AC sandboxes such as [[kernel-anti-cheat]], and the broader [[kernel-callbacks]] / object-callback handle-policy lane.

## Detection modules

| Module | Technique |
|--------|-----------|
| **NMI stack walk** | Cross-CPU stack forensics via NMI callbacks |
| **APC/DPC stacks** | APC and DPC stack analysis for anomalous execution |
| **`.text` integrity** | Code-section tamper / hook detection |
| **Handle stripping** | `ObRegisterCallbacks` to revoke suspicious handle rights |
| **Chained data pointers** | Follow chained kernel data structures for cheat artifacts |
| **Attached threads** | Detect threads attached to protected processes |
| **Return-address hooks** | Exception-path return-address hook detection |
| **Module device objects** | Verify system-module device objects |
| **Handle-table enum** | Enumerate process handle tables for suspicious access |

## Links

- Repo: https://github.com/donnaskiez/ac

## Related

[[nmi-callback-handler]] · [[kernel-anti-cheat]] · [[kernel-callbacks]] · [[nmi-callback]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
