---
title: AntiCheat Scanner
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/PickAngE__AntiCheat-Scanner.md
updated: 2026-08-22
confidence: medium
---

# AntiCheat Scanner

**AntiCheat Scanner** is a read-only **Windows forensic utility** (Python 3.10+) that detects the presence, configuration, and execution traces of third-party anti-cheat products through multi-layer local system analysis. It scans drivers, processes, services, registry keys, scheduled tasks, filesystem artifacts, and execution traces such as BAM, Prefetch, and MUICache against an external signature database. Matching uses an O(1) signature index, fuzzy name matching via rapidfuzz, PE metadata, and batched Authenticode verification, with parallel checkers under a shared `BaseChecker` interface. Targets include ACE, EA Anti-Cheat/Javelin, [[easy-anti-cheat]], BattlEye, and HoYoProtect. Intended for forensic auditing, privacy review, and educational game-security research on the user's own machine. (source: wiki/sources/descriptions/PickAngE__AntiCheat-Scanner.md)

## Detection surfaces

| Layer | Examples |
|-------|----------|
| **Kernel / services** | Loaded drivers, running services, process inventory |
| **Persistence** | Registry keys, scheduled tasks, filesystem artifacts |
| **Execution traces** | BAM, Prefetch, MUICache |

Complements attestation kits such as [[alibi]] and driver-inventory scanners such as [[driver-risk-scout]] by focusing specifically on **commercial game anti-cheat footprint enumeration** rather than cheat-tool or DMA detection.

## Links

- Repo: https://github.com/PickAngE/AntiCheat-Scanner

## Related

[[alibi]] · [[windows-forensic-artifacts]] · [[driver-risk-scout]] · [[dfirtriage]] · [[easy-anti-cheat]] · [[battleye-region-walking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
