---
title: defender-control
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/qtkite__defender-control.md
updated: 2026-07-25
confidence: medium
---

# defender-control

C# GUI utility to toggle Windows Defender real-time protection, Tamper Protection, and automatic sample submission via registry keys and service configuration—without walking through Windows Security UI. Aimed at developers and security researchers who need temporary Defender disable during testing, malware analysis, or software development. (source: wiki/sources/descriptions/qtkite__defender-control.md)

User-mode / config-path counterpart to kernel privilege-escalation Defender control such as [[windefctl]] (Win11 26H1; Tamper Protection via driver) and COM UAC-bypass + token-escalation tooling such as [[disable-windows-defender-]] (gmh5225). Useful when mapping AV/EDR-control surfaces that game-security and AC research hosts may disable or monitor during lab work.

## Links

- Repo: https://github.com/qtkite/defender-control

## Related

[[windefctl]] · [[disable-windows-defender-]] · [[cmdt]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
