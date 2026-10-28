---
title: qortime-ai
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/ConWan30__qortime-ai.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# qortime-ai

**QorTime AI** is an advisory layer (ConWan30) that uses Meta models to explain and stress-test **deterministic verdicts** on signed video-game **match receipts** for competitive integrity and anti-cheat workflows. Implemented mainly in **Python** with browser verification panels in **JavaScript**; generative outputs sit beside a fixed referee—they **cannot override or upgrade** the final match status. (source: wiki/sources/descriptions/ConWan30__qortime-ai.md)

## Model modules

| Component | Role |
|-----------|------|
| **Muse Spark** | Guarded plain-English rulings and independent score cross-checks |
| **Muse Wonder** | Red-team receipt tampering against the unmodified verifier |
| **SAM 3.1** | Evidence Lens scorebug tracking; Challenge Echo pause-menu input checks |
| **Show Your Hands** | Input-to-pixel alignment checks |
| **Advisory sidecars** | Ed25519-signed advisories bound to receipt hashes |

**Lower-only rules:** AI signals may reduce `VERIFIED` to `PARTIAL` but never elevate or replace the deterministic referee outcome—useful for studying LLM narration boundaries beside [[detector-operations]] shadow-mode and human-review-first pipelines. (source: wiki/sources/descriptions/ConWan30__qortime-ai.md)

## Audience

Developers and researchers working on **verifiable esports outcomes**, receipt-based anti-cheat, and adversarial testing of game-security verifiers without letting generative AI set the final match status. Pairs with hardware-rooted controller attestation in [[qortroller]] and explainable observable-data scoring such as [[cs2-tracker]].

## Links

- Repo: https://github.com/ConWan30/qortime-ai

## Related

[[qortroller]] · [[cs2-tracker]] · [[detector-operations]] · [[research-rigor]] · [[overviews/anti-cheat]]
