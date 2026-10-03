---
title: Vigil (Fabric)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/vylorq__anti-cheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# Vigil (Fabric)

**Vigil** (vylorq/anti-cheat) is a **server-side Fabric mod** for **Minecraft 1.21.11** that combines anti-cheat detection with broad server protection. Written in **Java** with a testable core module, it runs movement upper-bound prediction, lag-compensated combat checks (reach, aim, autoclicking), and anti-x-ray ore hiding—scoring violations into **admin review cases with evidence clips** rather than automatic bans. (source: wiki/sources/descriptions/vylorq__anti-cheat.md)

README category: Anti Cheat / game:minecraft.

Distinct from [[vigil]] (TOSTcRa Rust eBPF Linux-native AC).

## Protection tooling

Beyond detection, Vigil bundles staff and moderation features: claims, barriers, jails, PvP arenas, secure player trading, watchlists, rollback, and a GUI-driven Vigil Panel. Optional **Geyser** and **Floodgate** support enables Java and Bedrock crossplay. CI gametest coverage supports regression validation.

## Positioning

Review-first **Fabric 1.21.11** server-side AC plus integrated world protection for operators wanting configurable cheat detection without auto-ban escalation—beside offline-mode suites such as [[bastion]] and alert-only mods such as [[silent-anticheat]].

## Links

- Repo: https://github.com/vylorq/anti-cheat

## Related

[[bastion]] · [[silent-anticheat]] · [[mcace]] · [[faircount]] · [[vigil]] · [[overviews/anti-cheat]]
