---
title: Inertia
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/README-categories.md
updated: 2026-08-25
confidence: low
---

# Inertia

Open-source **Minecraft anti-cheat foundation** (InertiaOrg) built around version-neutral engine design rather than Bukkit/NMS package branching. The project models behavior profiles, normalized movement and packet frames, world snapshots, collision models, and testable evidence accumulation with false-positive context (teleports, velocity grace, latency spikes, server-health drops). Current modules: `inertia-api` (neutral contracts), `inertia-core` (engine + evidence), `inertia-testkit` (scenario tests without a live server). Platform adapters and plugin bootstrap are intentionally deferred; movement prediction is a foundation pass, not full vanilla parity yet. (source: wiki/sources/README-categories.md)

## Design focus

Version-neutral `GameVersion` / `VersionProfile` rules; no `v1_8_R3`-style engine branching in core; evidence records with decay/reductions and movement debug traces; server-boot-free unit tests.

## Links

- Repo: https://github.com/InertiaOrg/Inertia
- Docs: https://inertiaorg.github.io/starlight-docs/

## Related

[[grim]] · [[minecraft-anticheat-list]] · [[nocheatplus]] · [[minecraft-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
