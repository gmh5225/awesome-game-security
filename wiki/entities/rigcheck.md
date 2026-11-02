---
title: RigCheck
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Glory42__RigCheck.md
updated: 2026-11-02
confidence: medium
---

# RigCheck

**RigCheck** is a **local-first Linux desktop** application that answers whether a PC can run **Steam** games by comparing detected hardware against each title’s minimum and recommended requirements. Implemented as a **Rust** Cargo workspace with an **iced** GUI, **SQLite** game databases, and crates for Linux hardware probing, Steam library discovery, requirement parsing, and allowlisted HTTP fetches, it extends raw spec matching with Linux-specific blockers: **ProtonDB** compatibility tiers, **anti-cheat status** from [[are-we-anti-cheat-yet]], Vulkan and driver needs, and **Steam Deck** verification—including explicit **BLOCKED** stamps when Linux cannot run a game regardless of hardware. Users get a searchable Steam store catalog, an installed-library view with cover art, per-component bottleneck breakdowns, and “what if” CPU or GPU overrides on **My Rig**. It targets Linux gamers, compatibility researchers, and purchase or library planning without accounts or telemetry. (source: wiki/sources/descriptions/Glory42__RigCheck.md)

The tool consumes public compatibility signals rather than bypassing anti-cheat; it complements web trackers such as [[are-we-anti-cheat-yet]] and [[aclist-github-io]] with an offline, hardware-aware verdict layer on the desktop.

## Links

- Repo: https://github.com/Glory42/RigCheck

## Related

[[are-we-anti-cheat-yet]] · [[proton]] · [[linux-anticheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
