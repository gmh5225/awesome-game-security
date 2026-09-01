---
title: Stresser
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/AvivShabtay__Stresser.md
updated: 2026-09-01
confidence: medium
---

# Stresser

**Endpoint security platform** (AvivShabtay) combining **host agents** with **centralized management** for telemetry collection, artifact processing, policy handling, and detection logic. The repository is primarily **C++** and spans **user-mode and kernel-mode** modules. Architecture emphasizes **ETW-driven monitoring**, **dynamic and static analysis** paths, and coordinated **response workflows**. Intended for **malware defense research** and enterprise-style endpoint protection experiments; README tags it as anti-virus that also covers anti-cheat. (source: wiki/sources/descriptions/AvivShabtay__Stresser.md)

## Architecture

| Component | Role |
|-----------|------|
| **Host agents** | UM + KM telemetry, artifact processing, local detection |
| **Central management** | Policy distribution, coordinated response |
| **Analysis** | ETW monitoring; dynamic and static detection paths |

## Positioning

Full-stack **agent–manager endpoint protection** sample in the same research lane as EDR references such as [[openedr]] and [[bluespawn]], and ETW-heavy educational AC stacks such as [[peregrine-anticheat]]—oriented toward defensive telemetry and detection experimentation rather than game-specific client integration.

## Links

- Repo: https://github.com/AvivShabtay/Stresser

## Related

[[peregrine-anticheat]] · [[kernelmon]] · [[openprocmon]] · [[tietwagent]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
