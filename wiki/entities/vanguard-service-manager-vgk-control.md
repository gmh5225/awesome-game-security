---
title: vanguard-service-manager-vgk-control
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Karwmam__Vanguard-Service-Manager-vGK-Control.md
updated: 2026-08-24
confidence: medium
---

# vanguard-service-manager-vgk-control

Windows utility package (C++; Visual Studio) with two command-line tools for managing Riot [[vanguard]]'s kernel anti-cheat service (`vgk`) through the Service Control Manager. **vgkChecker** reports whether Vanguard is running and configured for automatic startup; **noVanguard** toggles the service's auto-start setting. Both tools use SCM APIs, colored console logging, and administrator privilege checks, with optional restart prompts so configuration changes take effect. Aimed at players and system administrators who want control over when Vanguard loads—reducing unnecessary kernel-level overhead when Riot titles are not in use—rather than runtime AC bypass or cheat development. (source: wiki/sources/descriptions/Karwmam__Vanguard-Service-Manager-vGK-Control.md)

Complements update-monitoring tooling such as [[vanguard-update-notifier]] and legitimate cleanup utilities such as [[wardsweep]] on the Vanguard service-management lane.

## Links

- Repo: https://github.com/Karwmam/Vanguard-Service-Manager-vGK-Control

## Related

[[vanguard]] · [[vanguard-update-notifier]] · [[wardsweep]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
