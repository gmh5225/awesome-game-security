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

**Vigil** (vylorq/anti-cheat) is a **server-side Fabric mod** for **Minecraft 1.21.11** that combines anti-cheat detection with broad server protection. Written in **Java** with a testable core module, it targets Minecraft server administrators who want configurable, **review-first** cheat detection and integrated world protection on Fabric servers—without automatic ban escalation. (source: wiki/sources/descriptions/vylorq__anti-cheat.md)

README category: Anti Cheat / game:minecraft.

Distinct from [[vigil]] (TOSTcRa Rust eBPF Linux-native AC).

## Detection

- **Movement** — upper-bound prediction on server-authoritative physics.
- **Combat** — lag-compensated reach, aim, and autoclicking checks.
- **World** — anti-x-ray ore hiding.
- **Watcher telemetry** — server-side observation pipeline feeding violation scoring and staff review (source: wiki/sources/descriptions/vylorq__anti-cheat.md).

Violations accumulate into **admin review cases with evidence clips** rather than autonomous bans.

## Architecture

Testable Java core module on Fabric **1.21.11**; optional **Geyser** and **Floodgate** integration for Java and Bedrock crossplay. CI gametest coverage supports regression validation.

## Staff tooling

Claims, barriers, jails, PvP arenas, secure player trading, watchlists, rollback, and a GUI-driven **Vigil Panel** for moderation workflows.

## Positioning

Review-first **Fabric 1.21.11** server-side AC plus integrated world protection for operators wanting configurable cheat detection without auto-ban escalation—beside offline-mode suites such as [[bastion]], modular Paper plugins such as [[novaguard]], and alert-only mods such as [[silent-anticheat]].

## Peers

[[bastion]] · [[novaguard]] · [[chanhne-dev-anticheat]] · [[windfall-anticheatf]] · [[silent-anticheat]] · [[mcace]]

## Links

- Repo: https://github.com/vylorq/anti-cheat

## Related

[[vigil]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]]
