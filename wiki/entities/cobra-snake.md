---
title: Cobra (web Snake)
kind: entity
topics: [anti-cheat, game-server-security]
sources:
  - wiki/sources/descriptions/aryribeiro__cobra.md
  - wiki/sources/README-categories.md
updated: 2026-09-13
confidence: medium
---

# Cobra (web Snake)

Production web Snake arcade game built with **TypeScript**, **Next.js**, and **React**, rendering on HTML5 Canvas at 60 FPS with visual and audio juice effects. Includes 40+ emoji power-ups, responsive desktop and mobile controls, and a cloud-backed global **Top 10** leaderboard persisted via **LibSQL** with **localStorage** fallback when database credentials are unavailable. (source: wiki/sources/descriptions/aryribeiro__cobra.md)

## Server-side anti-cheat

Lightweight browser-game score validation—not kernel or client-integrity AC:

- **HMAC-signed game sessions** bind score submissions to server-issued session state.
- **Score plausibility validation** rejects impossible or inconsistent results.
- **Rate-limited submissions** throttle leaderboard POST traffic.
- **Silent rejection** of forged scores (no client-visible cheat feedback).

Practical reference for implementing server-side anti-cheat in browser-based arcade games. Compare defensive patterns with [[pew-game]] (twin-stick shooter; HMAC tokens + replay checks). (source: wiki/sources/descriptions/aryribeiro__cobra.md)

Distinct from Trail of Bits MBA simplifier [[cobra]] (CoBRA).

## Links

- Repo: https://github.com/aryribeiro/cobra

## Related

[[overviews/anti-cheat]] · [[input-provenance]] · [[detector-operations]] · [[network-environment-evidence]] · [[pew-game]]
