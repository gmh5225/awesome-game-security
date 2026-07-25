---
title: OpenProcmon
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/progmboy__openprocmon.md
updated: 2026-07-25
confidence: medium
---

# OpenProcmon

Open-source Windows process monitor inspired by Sysinternals Process Monitor. Captures real-time process create/exit, file-system, registry, network, and DLL-load activity via ETW plus minifilter drivers. C++ GUI with filtering, highlighting, and export—aimed at admins, malware analysts, and security researchers studying host telemetry rather than as a game AC product. (source: wiki/sources/descriptions/progmboy__openprocmon.md)

Complements ETW schema browsers such as [[etw-explorer]], kernel event-stream tools such as [[fibratus]], and process explorers such as [[systeminformer]] / [[openark]].

## Links

- Repo: https://github.com/progmboy/openprocmon

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-explorer]] · [[fibratus]] · [[systeminformer]] · [[openark]] · [[tietwagent]]
