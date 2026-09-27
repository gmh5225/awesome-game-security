---
title: MCAce
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/TypeThe0ry__MCAce.md
  - wiki/sources/README-categories.md
updated: 2026-09-27
confidence: medium
---

# MCAce

**MCAce** (TypeThe0ry/MCAce) is a privacy-first **client visibility and admission stack** for modern **Minecraft** networks. It gives servers a narrow, consent-based view of a **Fabric** client and correlates that view with independently produced server-side evidence. (source: wiki/sources/descriptions/TypeThe0ry__MCAce.md)

README category: Anti Cheat / game:minecraft.

## Architecture

Ships as a **Fabric client mod** plus **Velocity** and **BungeeCord** proxy plugins and a **Paper/Folia** backend plugin. Written primarily in **Java** with a **Gradle/Kotlin** build targeting Minecraft **1.21.11**, **26.1.2**, and **26.2**.

## Consent and telemetry

After explicit **per-connection user consent**, MCAce collects **signed telemetry** such as:

- Loaded mod lists
- Active resource packs
- Shader selections

Client-reported facts are tied to server anti-cheat signals through integrations such as **Grim** and **Vulcan**.

## Evidence and policy

Evidence flows through **Ed25519-signed frames** with strict privacy boundaries, **fail-closed policy evaluation**, and bounded disposition actions:

- Observe
- Warn
- Challenge
- Quarantine

## Positioning

Targets **server administrators** who need **auditable, reversible admission and anti-cheat evidence workflows** rather than kernel-level or persistent client monitoring. Complements hash-whitelist Fabric integrity mods such as [[faircount]], encrypted client+server stacks such as [[the-dreamers-guards]], and consensual PC screenshare workflows such as [[error-pc-check]]; pairs with movement-simulation AC such as [[grim]] when server-side signals need client-inventory corroboration.

## Peers

[[faircount]] · [[katapult-anticheat]] · [[error-pc-check]] · [[grim]] · [[minecraft-anticheat-list]]

## Links

- Repo: https://github.com/TypeThe0ry/MCAce

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[input-provenance]]
