---
title: HP Hardware Diagnostics PoC
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__HPHardwareDiagnostics-PoC.md
updated: 2026-08-12
confidence: medium
---

# HP Hardware Diagnostics PoC

Proof-of-concept exploit targeting vulnerabilities in the **HP Hardware Diagnostics** kernel driver (**`etdsupp.sys`**). The sample demonstrates abusing the diagnostics driver's **IOCTL interface** to obtain elevated privileges on HP systems — a typical OEM preinstalled-driver [[byovd]] / local privilege escalation research path rather than a full mapper framework. (source: wiki/sources/descriptions/gmh5225__HPHardwareDiagnostics-PoC.md)

Sits in the same OEM diagnostics-driver lane as [[lenovo-mapper]] / [[lenovo-exec]] (**`LenovoDiagnosticsDriver.sys`**) and other signed utility-driver IOCTL abuse PoCs catalogued under [[byovd]].

## Links

- Repo: https://github.com/gmh5225/HPHardwareDiagnostics-PoC

## Related

[[byovd]] · [[lenovo-mapper]] · [[lenovo-exec]] · [[openhardwaremonitor-poc]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
