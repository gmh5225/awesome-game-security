---
title: Ironwall
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/wflores9__Ironwall.md
updated: 2026-07-31
confidence: medium
---

# Ironwall

Open-source anti-cheat **protocol stack** that chains client attestation, server-side simulation, and on-chain match recording into a layered trust model for competitive games. Targets game developers and security researchers building tamper-evident AC for competitive play, wagering, and dispute resolution. (source: wiki/sources/descriptions/wflores9__Ironwall.md)

## Architecture

- **Thin client:** Python, Rust, and C++ clients capture player inputs; signed and attested via a remote broker with periodic re-attestation.
- **TEE verification:** Intel SGX and AMD SEV trusted execution environment checks; ECDSA module signing; Rust game launcher scans signed game modules.
- **Human-input proofs:** Zero-knowledge PLONK proofs enforce constraints such as reaction time and mouse acceleration.
- **Immutable audit trail:** Hedera Consensus Service records with Merkle audit trails; dual-anchored match receipts on Hedera HCS + XRPL.
- **Engine integrations:** Unity and Unreal plugins; public tooling to verify match records.

## Links

- Repo: https://github.com/wflores9/Ironwall

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[certael]] · [[magnetite]] · [[keyattestation]] · [[ai-aimbot-detection]]
