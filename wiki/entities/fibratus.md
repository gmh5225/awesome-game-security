---
title: Fibratus
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/rabbitstack__fibratus.md
updated: 2026-07-25
confidence: medium
---

# Fibratus

Go-based Windows kernel exploration and observability tool that captures kernel event streams via ETW (Event Tracing for Windows). Monitors process creation, thread activity, file I/O, registry operations, network connections, and driver loading in real time, with filtering rules, alerting, and sinks including Elasticsearch. Includes a rule engine for suspicious-behavior patterns aimed at threat hunting and endpoint telemetry. (source: wiki/sources/descriptions/rabbitstack__fibratus.md)

Useful for defenders and AC researchers mapping kernel-level telemetry without treating it as a game AC product—complements provider/schema browsers such as [[etw-explorer]] and ThreatIntel consumers such as [[tietwagent]].

## Links

- Repo: https://github.com/rabbitstack/fibratus

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-explorer]] · [[tietwagent]] · [[systeminformer]] · [[wazuh]]
