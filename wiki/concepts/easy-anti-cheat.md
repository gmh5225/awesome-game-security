---
title: Easy Anti-Cheat
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md
updated: 2026-07-18
confidence: medium
---

# Easy Anti-Cheat

Epic’s Easy Anti-Cheat (EAC): multi-component architecture with service, kernel driver, and game-facing protections—process integrity, memory inspection, and runtime driver loading with strong client-side enforcement. Used by titles such as Fortnite, Apex Legends, and Rust. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Callback/handle surfaces ([[kernel-callbacks]]), memory/manual-map detection, driver trust and [[byovd]] blocklists, interaction with [[hvci]]/DSE, and DMA detection pipelines shared with other modern ACs.

Overlay / screenshot monitoring is another research surface: PoCs such as [[eac-overlay]] explore alternate rendering surfaces or window manipulation to draw ESP without tripping EAC overlay detection. (source: wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md)

## Related

[[battleye]] · [[vanguard]] · [[eac-overlay]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
