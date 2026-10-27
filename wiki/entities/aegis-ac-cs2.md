---
title: AegisAC (CS2)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ressiws__AegisAC.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: high
---

# AegisAC (CS2)

**AegisAC** (ressiws/AegisAC) is an open-source **Counter-Strike 2** server-side anti-cheat plugin that detects aimbots and unnatural aiming without requiring client-side software. Implemented in **C# on .NET**, it integrates with the **SwiftlyS2** dedicated-server framework. (source: wiki/sources/descriptions/ressiws__AegisAC.md)

Distinct from Paper Minecraft [[aegis-ac]] (projectsadameyd)—same project name, different game and host stack.

## Detection approach

- **Trajectory and angle math** — flags convergence snaps and automated targeting patterns.
- **Sub-tick user command correlation** — ties aim and view changes to tick-granular input.
- **Weapon-fire to damage event pairing** — correlates shots with hit outcomes for aim anomaly scoring.
- **Sliding-window evidence aggregation** — stacks high-confidence signals before sanctions to limit false positives; suited to CS2 gameplay telemetry research and community server administration. (source: wiki/sources/descriptions/ressiws__AegisAC.md)

## Operator controls

- Configurable detection strictness; live configuration reload.
- Modular punishments (kick, ban, and related enforcement actions).
- **Discord webhook** alerts when players are flagged.

Peers with [[cs2-anticheat-by-chmonya]], [[cs2-anticheat-pandathebeasty]], and [[sac-the-server-anticheat]] in the Open Source Anti Cheat System lane for CS2.

## Links

- Repo: https://github.com/ressiws/AegisAC

## Related

[[aegis-ac]] · [[cs2-anticheat-by-chmonya]] · [[cs2-anticheat-pandathebeasty]] · [[sac-the-server-anticheat]] · [[detector-operations]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
