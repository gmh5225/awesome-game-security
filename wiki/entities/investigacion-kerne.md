---
title: Investigacion-Kerne
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/N0tJ03__Investigacion-Kerne.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: medium
---

# Investigacion-Kerne

**Investigacion-Kerne** (N0tJ03) is a Spanish-language research notebook documenting how commercial **kernel-mode anti-cheat** and endpoint security software behaves at a systems level—not executable tooling. (source: wiki/sources/descriptions/N0tJ03__Investigacion-Kerne.md)

## Scope

Explains the typical three-layer model (ring-0 kernel drivers, ring-3 user-mode services, server-side monitoring with ML/telemetry) and compares **BattlEye**, **Easy Anti-Cheat**, and **Riot Vanguard**, including driver behavior, callbacks, whitelisting, and known failure modes such as BSODs. (source: wiki/sources/descriptions/N0tJ03__Investigacion-Kerne.md)

A second section analyzes the July 2024 **CrowdStrike Falcon** outage (File 291 configuration mismatch, buffer overflow, global impact, remediation). Material is Markdown with curated external references. (source: wiki/sources/descriptions/N0tJ03__Investigacion-Kerne.md)

## Positioning

Listed under README **Cheat / Guide** as architecture literacy for game-security and Windows kernel-protection researchers—not a bypass or exploit repository. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/N0tJ03/Investigacion-Kerne

## Related

[[concepts/easy-anti-cheat]] · [[concepts/battleye]] · [[concepts/vanguard]] · [[kernel-cve-analysis]] · [[anti-cheat-research-index]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
