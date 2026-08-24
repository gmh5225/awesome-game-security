---
title: BLUESPAWN
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/ION28__BLUESPAWN.md
updated: 2026-08-24
confidence: medium
---

# BLUESPAWN

Open-source **Windows active defense** and **endpoint detection and response (EDR)** platform (ION28). Organizes operator workflows into **Hunt**, **Mitigate**, **Monitor**, and **Scan** modes with ATT&CK-oriented detections, **YARA** scanning, **ETW-based** monitoring, and automated response actions such as quarantine or process suspension. Implementation is largely C++ with deep Windows API integration and rule-driven detection content for blue-team operators and security researchers defending enterprise endpoints. (source: wiki/sources/descriptions/ION28__BLUESPAWN.md)

README category: `[EDR]`.

## Capabilities

| Workflow | Role |
|----------|------|
| **Hunt** | ATT&CK-aligned threat hunting across endpoint telemetry |
| **Mitigate** | Automated response (quarantine, process suspension) |
| **Monitor** | ETW-backed continuous endpoint monitoring |
| **Scan** | YARA and rule-driven content scanning |

## Positioning

Full-stack open EDR on the defensive side of game-security research—complements lightweight incident-prevention tools such as [[raccine]], ETW event generators such as [[bamboozledr]], and educational AC stacks such as [[peregrine-anticheat]] when studying how endpoint agents combine telemetry, signatures, and response.

## Links

- Repo: https://github.com/ION28/BLUESPAWN

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[concepts/etw-threat-intelligence]] · [[bamboozledr]] · [[raccine]] · [[peregrine-anticheat]] · [[wazuh]] · [[the-hive]]
