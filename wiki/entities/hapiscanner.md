---
title: HapiScanner
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/abdulhamitakdag__hapiscanner.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# HapiScanner

**HapiScanner** — open-source, consent-based Windows client that scans a player's PC for known cheat artifacts and reports structured evidence to server staff (no autonomous bans). (source: wiki/sources/descriptions/abdulhamitakdag__hapiscanner.md)

## Pipeline

C#/.NET 8 candidate-first workflow over Minecraft folders, launchers, file metadata, **MFT/USN Journal** forensics, and runtime inspection of the active Java Edition process tied to the server. Python **FastAPI** backend (HapiVerify) validates signed challenge-response sessions, heartbeats, and rule-engine output; a **Velocity** plugin lets staff start and review verifications.

## Trust model

Signed JSON rule packs, cross-language cryptographic checks, and data minimization (no full-disk hashing, no personal file uploads)—human staff make enforcement decisions.

## Links

- Repo: https://github.com/abdulhamitakdag/hapiscanner

## Related

[[error-pc-check]] · [[screenshare-signatures]] · [[jvm-inspector]] · [[jaranalyzer]] · [[overviews/anti-cheat]]
