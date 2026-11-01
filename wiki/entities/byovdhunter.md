---
title: BYOVD Hunter
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/chemsse576__BYOVDHunter.md
updated: 2026-11-01
confidence: medium
---

# BYOVD Hunter

Windows console tool (C#; .NET Framework 4.8) that statically scans installed and loaded kernel drivers for [[byovd]] abuse indicators. Cross-checks driver images against [[loldrivers]], Microsoft blocklist data, and custom heuristics while parsing PE exports to map IRP dispatch handlers, IOCTL surfaces, buffer validation, and reachability from user-mode device paths to dangerous kernel imports (physical memory mapping, callback unregistration, and similar primitives). Summarizes local hardening context—[[hvci]], driver signature enforcement, Secure Boot, VBS, and blocklist state—and ranks findings from informational through critical with optional JSON or CSV reporting. Targets kernel security research, endpoint hardening, and anti-cheat or game-security teams inventorying exploitable signed drivers on a host without loading or exploiting them. (source: wiki/sources/descriptions/chemsse576__BYOVDHunter.md)

## Links

- Repo: https://github.com/chemsse576/BYOVDHunter

## Related

[[byovd]] · [[loldrivers]] · [[ms-vulnerable-driver-list]] · [[hvci]] · [[driver-risk-scout]] · [[byovdfinder]] · [[vulnerable-driver-scanner]] · [[loldriverscan]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
