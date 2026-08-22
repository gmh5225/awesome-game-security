---
title: AMSI-ETW-Patch
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Mr-Un1k0d3r__AMSI-ETW-Patch.md
updated: 2026-08-22
confidence: medium
---

# AMSI-ETW-Patch

**Security research proof of concept** (Mr-Un1k0d3r) for bypassing **AMSI** and **ETW** with **minimal byte patches**. Includes C, PowerShell, and C# examples showing where to patch branch logic in AMSI paths and how to short-circuit telemetry-related tracing calls. Diagrams and notes explain control flow and why single-byte changes can reduce the modification footprint. Primary use case: red-team simulation and defensive validation of detection coverage around in-memory tampering. README **[ETW Testing]**. (source: wiki/sources/descriptions/Mr-Un1k0d3r__AMSI-ETW-Patch.md)

Complements ETW blind/stress samples such as [[disable-threat-tracing]] and [[kernel-callback-removal]], and sits in the same user-mode ETW silencing lane documented in [[concepts/etw-threat-intelligence]].

## Links

- Repo: https://github.com/Mr-Un1k0d3r/AMSI-ETW-Patch

## Related

[[disable-threat-tracing]] · [[kernel-callback-removal]] · [[concepts/etw-threat-intelligence]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
