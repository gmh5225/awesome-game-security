---
title: BloxDesk
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/Buck3ttcode__bloxdesk.md
  - wiki/sources/README-categories.md
updated: 2026-09-23
confidence: medium
---

# BloxDesk

**BloxDesk** (Buck3ttcode/bloxdesk) is an enterprise-oriented **Roblox anti-cheat platform** that links in-game telemetry, Discord moderation workflows, and cross-server ban enforcement. (source: wiki/sources/descriptions/Buck3ttcode__bloxdesk.md)

## Detection surface

Luau **server-side SDK** passively monitors player physics at **4Hz** for speed hacks, flight anomalies, noclip wall passing, and remote event spam. Detected events feed webhook incident reporting; the SDK does **not** autonomously kick or ban players.

## Moderation pipeline

Incidents route to a backend where **Google Gemini** compares player appeal statements against recorded telemetry to assist staff triage. **Roblox Open Cloud** enables rapid cross-instance restrictions.

## Deployment

Ships as a ModuleScript and Studio model plus static HTML documentation and Discord bot setup guides. Targets Roblox developers and moderation teams building server-side exploit detection and appeal review pipelines — adjacent to lightweight Luau AC such as [[volcano-ac]], [[shprotect-ac]], and [[advanced-anticheat]].

## Links

- Repo: https://github.com/Buck3ttcode/bloxdesk

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[volcano-ac]] · [[shprotect-ac]] · [[advanced-anticheat]] · [[encryptic-roblox-anti-cheat]] · [[guard-game]] · [[detector-operations]]
