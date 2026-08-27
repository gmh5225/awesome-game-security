---
title: OpenEDR
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/ComodoSecurity__openedr.md
updated: 2026-08-27
confidence: medium
---

# OpenEDR

Open-source **Endpoint Detection and Response (EDR)** platform by Comodo Security. The large C++ codebase implements system monitoring, event collection, threat detection, and cloud-based analysis integration through AWS SDK connectivity. It provides real-time endpoint telemetry and response capabilities for identifying malicious activity on Windows systems. Mainly useful for security researchers and anti-cheat engineers studying EDR architecture, endpoint monitoring techniques, and defensive security system design. (source: wiki/sources/descriptions/ComodoSecurity__openedr.md)

README category: `[EDR]`.

## Capabilities

| Area | Role |
|------|------|
| **Monitoring** | System-wide endpoint telemetry and event collection |
| **Detection** | Threat detection on collected endpoint events |
| **Response** | Real-time endpoint response for malicious activity |
| **Cloud** | AWS SDK integration for cloud-based analysis |

## Positioning

Full-stack open-source EDR reference on the defensive side—complements active-defense platforms such as [[bluespawn]], lightweight incident-prevention tools such as [[raccine]], and offensive EDR blind/bypass research such as [[edrsandblast]] when studying how endpoint agents combine telemetry, detection rules, and response.

## Links

- Repo: https://github.com/ComodoSecurity/openedr

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[bluespawn]] · [[raccine]] · [[bamboozledr]] · [[edrsandblast]] · [[concepts/etw-threat-intelligence]] · [[kernel-callbacks]]
