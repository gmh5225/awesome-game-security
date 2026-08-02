---
title: TelemetrySourcerer
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jthuraisamy__TelemetrySourcerer.md
updated: 2026-08-02
confidence: medium
---

# TelemetrySourcerer

Windows kernel driver for **enumerating and disabling kernel callbacks and ETW** telemetry—aimed at game-security researchers and reverse engineers studying offensive Windows kernel / cheat-development techniques. The driver ships **unsigned**; loading requires test-signing mode, temporary DSE disable, or signing with a valid certificate. (source: wiki/sources/descriptions/jthuraisamy__TelemetrySourcerer.md)

Complements defensive callback browsers such as [[openark]], ETW provider mappers such as [[etw-explorer]], ThreatIntel consumers such as [[tietwagent]], and broader ETW/callback blinders such as [[edrsandblast]] and [[disable-threat-tracing]].

## Links

- Repo: https://github.com/jthuraisamy/TelemetrySourcerer

## Related

[[kernel-callbacks]] · [[etw-threat-intelligence]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[etw-explorer]] · [[disable-threat-tracing]] · [[edrsandblast]]
