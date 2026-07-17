---
title: EtwExplorer
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/zodiacon__EtwExplorer.md
updated: 2026-07-17
confidence: medium
---

# EtwExplorer

Windows GUI (C#/WPF) for browsing registered ETW providers and inspecting their event definitions, keywords, and metadata—manifest-based or TraceLogging schemas—with filter-by-name/GUID. Aimed at security researchers, admins, and EDR developers mapping Windows telemetry sources for detection and monitoring. (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md)

Useful when enumerating which providers/events exist before wiring consumers or studying AC/EDR ETW surfaces—not a bypass tool.

## Links

- Repo: https://github.com/zodiacon/EtwExplorer

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[kernel-callbacks]]
