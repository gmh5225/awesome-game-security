---
title: WHIDS
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/0xrawsec__whids.md
updated: 2026-09-05
confidence: medium
---

# WHIDS

Open-source **Windows EDR** platform focused on **detection-driven response**. Built largely in Go, it ingests **ETW** and **Sysmon** telemetry and evaluates rules with the **Gene** engine. Alerts can trigger near real-time artifact collection—files, registry data, and process memory—and a manager service exposes an administrative API. Primary use case is incident response and enterprise endpoint monitoring with transparent, customizable detection logic. (source: wiki/sources/descriptions/0xrawsec__whids.md)

README category: `[EDR]`.

## Capabilities

| Area | Role |
|------|------|
| **Telemetry** | ETW and Sysmon event ingestion |
| **Detection** | Gene-powered rule evaluation on collected events |
| **Response** | Alert-triggered artifact collection (files, registry, process memory) |
| **Management** | Manager service with administrative API |

## Positioning

ETW/Sysmon-driven open-source EDR on the defensive side—complements full-stack references such as [[openedr]] and [[bluespawn]], ETW observability stacks such as [[fibratus]] and [[openprocmon]], and synthetic telemetry generators such as [[bamboozledr]] when studying how endpoint agents combine transparent rules, telemetry, and incident-response workflows.

## Links

- Repo: https://github.com/0xrawsec/whids

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[openedr]] · [[bluespawn]] · [[bamboozledr]] · [[fibratus]] · [[openprocmon]] · [[concepts/etw-threat-intelligence]] · [[stresser]]
