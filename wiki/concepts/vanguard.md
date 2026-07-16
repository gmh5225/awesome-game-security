---
title: Vanguard
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
updated: 2026-07-16
confidence: medium
---

# Vanguard

Riot Games anti-cheat featuring a **boot-start** kernel driver for early visibility into later-loaded drivers, boot-time initialization, driver allowlisting, and aggressive system trust checks. Used by Valorant and League of Legends. (source: wiki/sources/skills/anti-cheat.md)

## Distinguishing trait

Early load timing changes the BYOVD/test-sign window relative to runtime-loaded ACs ([[easy-anti-cheat]], [[battleye]]). Research often pairs Vanguard with FACEIT AC discussions on kernel integrity.

## Related

[[easy-anti-cheat]] · [[battleye]] · [[hvci]] · [[byovd]] · [[overviews/anti-cheat]]
