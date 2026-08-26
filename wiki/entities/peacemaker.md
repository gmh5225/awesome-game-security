---
title: PeaceMaker
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/D4stiny__PeaceMaker.md
updated: 2026-08-26
confidence: medium
---

# PeaceMaker

Windows **kernel-mode threat detection platform** focused on **behavior-based malware and cheat telemetry**. The driver monitors process creation, image loading, remote-thread activity, hidden code execution, and suspicious filesystem or registry operations, attaching **stack-trace context** to events for analyst review. The codebase ships a kernel driver, command-line tooling, and a **Qt-based GUI** for telemetry collection and response workflows. Aimed at defensive security experiments, anti-malware research, and high-visibility test environments where kernel behavioral visibility matters for AC engineering. (source: wiki/sources/descriptions/D4stiny__PeaceMaker.md)

Complements multi-vector open-source kernel AC references such as [[ac]] and [[kernel-anti-cheat]], load-image stack-trace validators such as [[driver-watchowl]], and anti-analysis test suites such as [[al-khaser]] used to validate defensive visibility.

## Monitored signals

| Signal | Role |
|--------|------|
| **Process creation** | Early lifecycle visibility for suspicious parent/child chains |
| **Image loading** | Module map and injection forensics |
| **Remote threads** | Cross-process execution and injection indicators |
| **Hidden code execution** | Non-standard execution-path detection |
| **Filesystem / registry ops** | Persistence and tamper telemetry with stack context |

## Links

- Repo: https://github.com/D4stiny/PeaceMaker

## Related

[[ac]] · [[kernel-anti-cheat]] · [[driver-watchowl]] · [[kernel-callbacks]] · [[al-khaser]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
