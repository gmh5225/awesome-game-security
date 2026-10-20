---
title: Game Quality Gates
kind: entity
topics: [anti-cheat, game-server-security]
sources:
  - wiki/sources/descriptions/abczsl520__game-quality-gates.md
  - wiki/sources/README-categories.md
updated: 2026-10-20
confidence: medium
---

# Game Quality Gates

Documented quality standard and **OpenClaw agent skill** for HTML5, Canvas, and WebGL games. Encodes prevention patterns from production bugs into twelve universal rules covering lifecycle cleanup, frame-rate–independent logic, audio/input safety, save versioning, network fault tolerance, and asset loading. Treats the browser client as untrusted and documents a baseline server-side anti-cheat posture. (source: wiki/sources/descriptions/abczsl520__game-quality-gates.md)

## Server-side anti-cheat patterns

Wiki-documented H5 guidance (not a runtime AC product):

- **One-time raid tokens** bind sensitive actions to server-issued credentials.
- **Duration and score sanity checks** reject implausible session timelines or leaderboard values.
- **Atomic purchase flows** reduce double-spend and replay abuse on in-game economies.

Engine-specific reference guides extend the rules for Phaser 3 arcade physics and Three.js WebGL (disposal, compression, animation). Aimed at developers and reviewers who want a pre-deploy checklist for browser titles. Compare live implementations such as [[cobra-snake]] (HMAC sessions + score plausibility) and [[shinobix]] (server-authoritative reward integrity). (source: wiki/sources/descriptions/abczsl520__game-quality-gates.md)

## Links

- Repo: https://github.com/abczsl520/game-quality-gates

## Related

[[overviews/anti-cheat]] · [[input-provenance]] · [[detector-operations]] · [[network-environment-evidence]] · [[cobra-snake]] · [[shinobix]]
