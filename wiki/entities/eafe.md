---
title: EAFE
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/eksses__EAFE.md
updated: 2026-08-15
confidence: medium
---

# EAFE

**EAFE** (Autonomous Elytra Flight Engine) is a protocol-level navigation system for long-range autonomous elytra flight in Minecraft. It pairs detailed architecture specifications with a **Node.js mineflayer** bot implementation aimed at researchers studying Minecraft movement validation, bot navigation, and how automated clients mimic human-like flight under server-side anti-cheat scrutiny. (source: wiki/sources/descriptions/eksses__EAFE.md)

## Navigation model

Models vanilla per-tick elytra physics—including axis-decoupled drag, pitch energy exchange, and firework boost cycles—through a finite-state machine managing takeoff, cruise, descent, and precision landing. Covers adaptive obstacle avoidance, Nether hazard scoring, player threat evasion, and fail-safe recovery for rubberbanding, chunk unload, and depleted resources.

## Anti-cheat evasion

Movement integrates anti-cheat evasion via cubic Bézier look-vector smoothing, Gaussian perturbation, slew-rate limits, and asymmetric packet jitter so automated flight paths resemble human input under server-side movement validation.

## Links

- Repo: https://github.com/eksses/EAFE

## Related

[[phantom-client]] · [[lenrete-mod]] · [[local-anticheat-1-8-9]] · [[windfall-anticheat]] · [[windfall-anticheatf]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[minecpp]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
