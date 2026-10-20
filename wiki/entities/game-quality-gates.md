---
title: Game Quality Gates
kind: entity
topics: [anti-cheat, game-engine, game-server-security]
sources:
  - wiki/sources/descriptions/abczsl520__game-quality-gates.md
  - wiki/sources/README-categories.md
updated: 2026-10-20
confidence: medium
---

# Game Quality Gates

Documented quality standard and **OpenClaw agent skill** for HTML5, Canvas, and WebGL games. Encodes prevention patterns from dozens of production bugs into **twelve universal rules** aimed at combination failures, memory leaks, double-spend exploits, and trivial score or payment bypass—not only isolated defects. (source: wiki/sources/descriptions/abczsl520__game-quality-gates.md)

## Twelve-rule quality gate (summary)

| Area | Intent |
|------|--------|
| Lifecycle & state | Tear down listeners, timers, and scene objects; avoid stale closures across route or level changes |
| Simulation | Frame-rate–independent movement and timers (`deltaTime`), not raw frame counts |
| Audio & input | Safe mute/unmute, gesture-gated audio, debounced controls, focus/blur handling |
| Persistence | Versioned saves and migration paths |
| Network | Timeouts, retries, idempotent retries, graceful offline/degraded modes |
| Assets | Loading progress, failure surfaces, and cache invalidation |
| Trust model | Client treated as untrusted; sensitive outcomes validated server-side |

Treats the browser client as untrusted and documents a baseline server-side anti-cheat posture alongside general ship-readiness checks. (source: wiki/sources/descriptions/abczsl520__game-quality-gates.md)

## Server-side anti-cheat patterns

Wiki-documented H5 guidance (not a runtime AC product):

- **One-time raid tokens** bind sensitive actions to server-issued credentials.
- **Duration and score sanity checks** reject implausible session timelines or leaderboard values.
- **Atomic purchase flows** reduce double-spend and replay abuse on in-game economies.

Engine-specific reference guides extend the rules for Phaser 3 arcade physics and [[three-js]] WebGL stacks (disposal, compression, animation). Aimed at developers and reviewers who want a pre-deploy checklist for browser titles. Compare live implementations such as [[cobra-snake]] (HMAC sessions + score plausibility) and [[shinobix]] (server-authoritative reward integrity). (source: wiki/sources/descriptions/abczsl520__game-quality-gates.md)

## Links

- Repo: https://github.com/abczsl520/game-quality-gates

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[engine-trust-boundaries]] · [[input-provenance]] · [[detector-operations]] · [[network-environment-evidence]] · [[cobra-snake]] · [[shinobix]] · [[three-js]]
