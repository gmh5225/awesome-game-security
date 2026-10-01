---
title: Rearguard
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/GloriousBrendon__rearguard.md
  - wiki/sources/README-categories.md
updated: 2026-10-01
confidence: medium
---

# Rearguard

**Rearguard** (GloriousBrendon/rearguard) is an open-source **zero-access anti-cheat SDK** pairing a **Rust server module** with a **Godot 4 GDExtension** engine plugin. It runs without kernel drivers on **Linux and Windows**, planting per-match **server-seeded probes** in gameplay signals such as mouse sensitivity and recoil, then detecting input cheats—including **aimbots and recoil macros**—by observing which clients react to hidden cues. Built primarily in Rust with a Godot demo client, telemetry pipeline, simulation harness, and evaluation tooling that reports detection and false-positive rates together. Early prototype focused on the input-cheat detection layer, aimed at game developers and anti-cheat researchers seeking a user-mode alternative to invasive kernel protections. (source: wiki/sources/descriptions/GloriousBrendon__rearguard.md)

## Detection mechanism

**Server-seeded input probe** — per-match secret parameters embedded in gameplay signals (mouse sensitivity, recoil curves); honest clients follow server-authoritative settings while automation that reads or overrides local input state reacts to hidden cue changes, yielding distinguishable telemetry without kernel instrumentation.

## Architecture

- **Engine plugin:** Godot 4 GDExtension binding + demo client integration
- **Server module:** Rust detector with per-match probe seeding and telemetry export
- **Evaluation:** simulation harness for detection-rate vs false-positive tradeoffs

## Positioning

**User-mode input-provenance AC** — unlike kernel AC such as [[easy-anti-cheat]] or [[battleye]], Rearguard avoids driver install and cross-platform kernel variance. Complements behavioral server-side plugins such as [[yaacs-anticheat]] and compile-time network hardening such as [[cheeto]] on [[overviews/anti-cheat]]. Pairs with [[input-provenance]] and [[ai-aimbot-detection]] research framing for probe-based macro/aim detection; sits beside other Godot AC tooling such as [[void-engine]] and [[dot-server-security]] on [[overviews/game-engine]].

## Links

- Repo: https://github.com/GloriousBrendon/rearguard

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[void-engine]] · [[dot-server-security]] · [[input-provenance]] · [[ai-aimbot-detection]] · [[hardware-input-injection]] · [[detector-operations]]
