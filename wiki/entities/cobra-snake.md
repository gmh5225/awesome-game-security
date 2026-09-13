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

Modern web-based Snake arcade game (TypeScript, Next.js, React; HTML5 Canvas at 60 FPS) with a cloud-backed global Top 10 leaderboard. Server-side anti-cheat uses HMAC-signed game sessions, score plausibility validation, and rate-limited submissions to silently reject forged scores. LibSQL persistence with localStorage fallback when database credentials are unavailable. Practical reference for lightweight browser-game score validation—not kernel or client-integrity AC. (source: wiki/sources/descriptions/aryribeiro__cobra.md)

Distinct from Trail of Bits MBA simplifier [[cobra]] (CoBRA).

## Links

- Repo: https://github.com/aryribeiro/cobra

## Related

[[overviews/anti-cheat]] · [[input-provenance]] · [[detector-operations]] · [[network-environment-evidence]]
