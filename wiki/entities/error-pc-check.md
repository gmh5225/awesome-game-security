---
title: error-pc-check
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/NotSkrib__error-pc-check.md
  - wiki/sources/README-categories.md
updated: 2026-09-14
confidence: medium
---

# error-pc-check

**Error SMP Screenshare** — consensual remote forensic screenshare for detecting cheating in **Minecraft Java Edition** on Windows. (source: wiki/sources/descriptions/NotSkrib__error-pc-check.md)

## Architecture

Pairs a signed **C#/.NET 8 client agent** with a **React/TypeScript** staff web panel backed by **Supabase**. Staff generate one-time keys; suspects run a consent-gated scan that streams live progress and uploads evidence over TLS.

## Forensic collectors

Modular Windows artifact collectors include Prefetch, BAM, UserAssist, ShimCache, NTFS USN journal analysis, registry and recycle-bin inspection, optional browser download history, and Minecraft-specific checks against a signature database for known cheat clients and mods.

## Correlation and reporting

A correlation engine ties findings across artifacts to surface anti-forensic tampering and repeated cheat indicators, producing **severity-ranked reports for human review** rather than automated punishment.

## Audience

Targets **Minecraft community moderators** and **game-security staff** who need ethical, transparent PC checks during screenshare investigations.

## Links

- Repo: https://github.com/NotSkrib/error-pc-check

## Related

[[jaranalyzer]] · [[aeterna-rongroi]] · [[alibi]] · [[local-anticheat-1-8-9]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
