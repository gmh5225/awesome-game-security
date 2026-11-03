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

**HapiScanner** (abdulhamitakdag/hapiscanner) is an open-source, **consent-based** Windows client that scans a player's PC for known cheat artifacts and delivers **structured evidence to server staff**—it does not issue bans on its own. (source: wiki/sources/descriptions/abdulhamitakdag__hapiscanner.md)

Distinct from standalone JAR triage such as [[jaranalyzer]] or PowerShell live-JVM audits such as [[jvm-inspector]]: HapiScanner is a **full verification stack** (signed client sessions, backend validation, proxy-side staff workflow) aimed at Minecraft Java Edition network operators.

## Architecture

| Component | Role |
|-----------|------|
| **Client** | C# on **.NET 8**; candidate-first pipeline over Minecraft folders, launchers, file metadata, **MFT/USN Journal** forensics, and runtime inspection of the active Java Edition process linked to the server |
| **HapiVerify** | Python **FastAPI** backend; validates signed challenge-response sessions, heartbeats, and rule-engine outputs |
| **Velocity plugin** | Staff start and review verifications on the proxy |

## Trust model

Signed JSON rule packs, cross-language cryptographic checks, and strict **data minimization** (no full-disk hashing, no personal file uploads). Enforcement remains a human decision. (source: wiki/sources/descriptions/abdulhamitakdag__hapiscanner.md)

## Audience

**Minecraft Java Edition server staff** and **game-security researchers** who want transparent, consent-gated PC checks during screenshares—comparable workflow lane to [[error-pc-check]] (React/Supabase panel) but centered on **Velocity** + **HapiVerify** session cryptography and NTFS/process-module evidence.

## Links

- Repo: https://github.com/abdulhamitakdag/hapiscanner

## Related

[[error-pc-check]] · [[screenshare-signatures]] · [[jvm-inspector]] · [[jaranalyzer]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
