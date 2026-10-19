---
title: 7DTD Anti-Cheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/CTRLKirk__7DTD-Anti-Cheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: high
---

# 7DTD Anti-Cheat

Server-side **anti-cheat mod for 7 Days to Die** dedicated servers that validates player network traffic and movement on the host without a client install. C# for .NET Framework 4.8; Harmony patches on networking and inventory handlers; movement monitor and detection service for god mode, teleport, speed/fly/noclip, illegal or oversized items, excessive damage and melee reach, and suspicious level jumps. XML-tuned detections with actions from logging through kick or ban, admin alerts, optional Discord webhooks, and console commands to reload settings and review recent flags. **EAC-compatible** for operators who run [[easy-anti-cheat]] alongside host-side checks; tunable **multipliers and exemption lists** help modded servers scale thresholds without disabling checks. (source: wiki/sources/descriptions/CTRLKirk__7DTD-Anti-Cheat.md)

Contrasts with [[7dtd-anticheatmod]], which targets non-EAC dedicated hosts with a lighter command/movement rule set (majimaakane).

## Links

- Repo: https://github.com/CTRLKirk/7DTD-Anti-Cheat

## Related

[[7dtd-anticheatmod]] · [[7dtd]] · [[easy-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
