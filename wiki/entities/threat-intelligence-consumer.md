---
title: ThreatIntelligenceConsumer
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/preludeorg__ThreatIntelligenceConsumer.md
updated: 2026-07-25
confidence: medium
---

# ThreatIntelligenceConsumer

PoC for consuming events from the Microsoft-Windows-Threat-Intelligence ETW provider without a kernel driver or PPL privilege. Formally tested on Windows 11 24H2 and 25H2 (plus Canary Insider Preview at upload time). Aimed at game-security researchers and reverse engineers studying offensive / telemetry surfaces in the Cheat → Windows kernel explorer lane. (source: wiki/sources/descriptions/preludeorg__ThreatIntelligenceConsumer.md)

Complements PPL/ELAM-oriented ThreatIntel agents such as [[tietwagent]], provider/schema browsers such as [[etw-explorer]], and broader ETW observability tools such as [[fibratus]] / [[openprocmon]].

## Links

- Repo: https://github.com/preludeorg/ThreatIntelligenceConsumer

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[tietwagent]] · [[etw-explorer]] · [[fibratus]] · [[openprocmon]]
