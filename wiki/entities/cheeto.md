---
title: Cheeto
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/pealz1__cheeto.md
  - wiki/sources/README-categories.md
updated: 2026-10-01
confidence: medium
---

# Cheeto

**Cheeto** (pealz1/cheeto) is a **schema-driven Roblox networking compiler** that generates typed, buffer-packed Luau client/server modules from declarative event, function, and replicated-state descriptions. Listed under README **Anti Cheat**. Targets Roblox developers who want performant, type-safe networking with **server-authoritative security hardening** against remote exploit and cheat abuse. (source: wiki/sources/descriptions/pealz1__cheeto.md)

## Compiler output

The toolchain emits fully typed send/receive code with built-in **validation, rate limits, and policy hooks** that reject malformed or unauthorized packets before application handlers run. Production features include state channels with delta replication, client prediction, batching, packet capture/replay, and an optional maximum-security preset with client integrity checks, honeypots, and movement anti-cheat helpers. (source: wiki/sources/descriptions/pealz1__cheeto.md)

## Toolchain

Cross-platform CLI, Roblox Studio plugin, schema lockfile for versioning, and TypeScript definitions for roblox-ts projects. (source: wiki/sources/descriptions/pealz1__cheeto.md)

## Positioning

**Compile-time network security layer** — unlike runtime Luau movement AC such as [[volcano-ac]] or trust-scored moderation stacks such as [[anticheat-dashboard]], Cheeto hardens the remote boundary at code generation time with typed buffers and pre-handler policy rejection. Adjacent to [[bloxdesk]] passive telemetry and [[guard-game]] external validation for Roblox hosts on [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/pealz1/cheeto

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[volcano-ac]] · [[anticheat-dashboard]] · [[bloxdesk]] · [[guard-game]] · [[network-environment-evidence]]
