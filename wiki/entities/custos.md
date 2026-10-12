---
title: Custos
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/dybeky__custos.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: high
---

# Custos

**Custos** (dybeky/custos) is a **read-only** Windows desktop forensic anti-cheat scanner for game-server staff who need to screen players without relying on a live game client. Built as an **Electron** and TypeScript application with native Win32 memory access, it runs twenty-one offline artifact scanners covering Prefetch, Amcache, BAM, registry and browser traces, Defender history, DNS cache, file hashes, anti-forensics tampering, and related Windows evidence, then aggregates results through a risk engine into exportable reports with integrity hashing. Optional **Live Scan** mode, when run as administrator against a running title, streams detectors for injected modules, code hooks, suspicious threads, and pattern-based memory signatures. Keyword, hash, and signature resources drive detection; the app is designed to leave minimal persistent data on the player machine after a session. Suits competitive multiplayer moderation, appeal documentation, and hands-on cheat investigation on Windows. (source: wiki/sources/descriptions/dybeky__custos.md)

## Stack

- **Shell** — Electron + TypeScript GUI; native Win32 memory APIs for optional live lane.
- **Offline lane** — twenty-one artifact scanners matched against keyword/hash/signature resources.
- **Reporting** — risk-engine aggregation, exportable reports, integrity hashing for appeal documentation.

## Evidence model

- **Offline artifact lane** — Prefetch/BAM/registry/DNS/hash scanners with exportable, integrity-hashed reports.
- **Optional live lane** — admin-gated module/hook/thread/memory signature streaming against a running game.
- **Moderation framing** — vetting and documentation; pair verdicts with [[detector-operations]] corroboration discipline.

## Positioning

Complements read-only screenshare forensics such as [[dexcheck]] and kernel AC census tooling such as [[kac-inspector]] with a GUI-first desktop workflow for server staff PC checks (Anti Cheat / Guide).

## Peers

[[dexcheck]] · [[error-pc-check]] · [[aeterna-rongroi]] · [[kac-inspector]]

## Links

- Repo: https://github.com/dybeky/custos
