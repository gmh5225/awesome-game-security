---
title: AsthenGuard (AntiCheat-Asthen)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ElbsxS1__AntiCheat-Asthen.md
  - wiki/sources/README-categories.md
updated: 2026-11-22
confidence: medium
---

# AsthenGuard (AntiCheat-Asthen)

**AsthenGuard** (ElbsxS1/AntiCheat-Asthen) is a **Maven-built Java plugin** that adds **server-side anti-cheat** for **Minecraft Paper/Folia 26.3** without requiring client modifications. It targets Paper server owners who want **lightweight, low false-positive** cheat detection alongside native Paper x-ray hardening. (source: wiki/sources/descriptions/ElbsxS1__AntiCheat-Asthen.md)

README category: Open Paper/Folia **26.3** server anti-cheat with movement, combat, mining checks, Bedrock-aware tuning, and bundled Paper anti-xray assets.

## Detection modules

| Lane | Checks |
|------|--------|
| **Movement** | Speed, flight, no-fall, phase |
| **Combat** | Reach, kill-aura variants, autoclick |
| **World** | Nuker, fast place |
| **Mining** | Statistical x-ray monitor (suspicious ore-to-stone ratios) |

Violation levels **decay over time** and can escalate to staff alerts, kicks, or optional bans.

## X-ray hardening

Bundled **Paper world YAML** assets enable **engine-mode anti-xray** ore obfuscation across Overworld, Nether, and End—complementing the statistical ore-ratio monitor with native Paper obfuscation.

## Bedrock and operations

Integrates with **Floodgate** and **Geyser** for Bedrock players. **Grace periods** after teleports and world changes reduce false positives. Admin commands cover alerts, violation inspection, and configuration reload.

## Positioning

Sits beside heuristic Paper plugins such as [[umbraac]], [[bs-anticheat]], and [[xray-anticheat]] (statistical ore-vision) for operators who want **self-hosted heuristics plus bundled anti-xray assets** on modern Paper/Folia without a remote inference engine.

## Links

- Repo: https://github.com/ElbsxS1/AntiCheat-Asthen

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[umbraac]] · [[bs-anticheat]] · [[xray-anticheat]] · [[fox-addition]] · [[vyx-anticheat]]