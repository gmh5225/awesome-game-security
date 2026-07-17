---
title: TiEtwAgent
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md
updated: 2026-07-17
confidence: medium
---

# TiEtwAgent

ETW-based process-injection detection agent that consumes `Microsoft-Windows-Threat-Intelligence` events for kernel-visible injection telemetry. Uses krabsetw for session setup, includes Yara-assisted detection logic, and is designed to run as a protected service with ELAM/PPL considerations. (source: wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md)

Useful for anti-cheat and defensive researchers studying injection detection without fragile userland hooks—complements provider/schema browsers such as [[etw-explorer]] and injection-test harnesses such as [[injectors]].

## Links

- Repo: https://github.com/xuanxuan0/TiEtwAgent

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[etw-explorer]] · [[injectors]]
