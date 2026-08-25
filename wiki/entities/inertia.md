---
title: Inertia
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/InertiaOrg__Inertia.md
  - wiki/sources/README-categories.md
updated: 2026-08-25
confidence: medium
---

# Inertia

Open-source **Minecraft anti-cheat foundation** (InertiaOrg) with a version-neutral engine that models **player behavior** rather than tying logic to specific server implementations (Bukkit/NMS). Written in **Java** with `inertia-api` (contracts for movement, packets, world snapshots, collision, debug tracing), `inertia-core` (evidence accumulator with confidence/decay and false-positive context: teleports, velocity grace, latency spikes, server health), and `inertia-testkit` (scenario-driven tests without a live server). Version profiles carry movement rules and limits; a **movement-prediction skeleton** tracks frame-by-frame state. Platform adapters are deferred; aimed at anti-cheat developers and server operators wanting a testable, platform-agnostic base for invalid-movement detection across many game versions. (source: wiki/sources/descriptions/InertiaOrg__Inertia.md)

## Design focus

Version-neutral `GameVersion` / `VersionProfile` rules; no `v1_8_R3`-style engine branching in core; evidence records with decay/reductions and movement debug traces; server-boot-free unit tests.

## Links

- Repo: https://github.com/InertiaOrg/Inertia
- Docs: https://inertiaorg.github.io/starlight-docs/

## Related

[[grim]] · [[minecraft-anticheat-list]] · [[nocheatplus]] · [[minecraft-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
