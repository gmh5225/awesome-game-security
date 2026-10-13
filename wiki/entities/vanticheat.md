---
title: VAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/GQS5__VAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: high
---

# VAntiCheat

**VAntiCheat** (GQS5/VAntiCheat) is a **Paper** and **Folia** **1.21.x** Minecraft server plugin (**Java 21**) that identifies specific client mods and cheat-related clients through **configuration-driven probes** rather than movement or combat heuristics. It targets server administrators and game-security practitioners who want explicit, evidence-based mod and client identification on modded **1.21.x** networks without bundling a proxy or client component. (source: wiki/sources/descriptions/GQS5__VAntiCheat.md)

## Detection model

A modular **detection registry** combines:

- **Passive plugin-message observation** — watches inbound custom payload channels configured in YAML.
- **Optional interactive sign-editor protocol** — translation-key fingerprinting when operators need stronger client-mod proof.
- **Corroboration rules** — multiple signals must align before a identity is treated as confirmed.
- **Centralized enforcement** — kick or ban actions for confirmed client/mod identities.

Automatic join checks default to **non-interactive passive probes** so players are not prompted on every login; staff can run **manual scans** and tune policy through YAML. (source: wiki/sources/descriptions/GQS5__VAntiCheat.md)

## Integrations

- **Lunar Client** via Apollo.
- **Java vs Bedrock** classification through **Geyser** and **Floodgate**.
- **Trusted-player exemptions**, **Forge mod-list denylisting**, and terrain-mask related packet handling documented in the project. (source: wiki/sources/descriptions/GQS5__VAntiCheat.md)

## Positioning

**Evidence-first client/mod fingerprinting** on the authoritative server—distinct from physics-prediction AC such as [[grim]], heuristic movement/combat plugins such as [[bs-anticheat]], and single-mechanism translation-key probes such as [[key-value-checker]]. Complements hacked-client signature plugins such as [[chanhne-dev-anticheat]] and catalog comparison via [[minecraft-anticheat-list]]. (source: wiki/sources/descriptions/GQS5__VAntiCheat.md)

## Links

- Repo: https://github.com/GQS5/VAntiCheat

## Related

[[key-value-checker]] · [[chanhne-dev-anticheat]] · [[virgola-anticheat]] · [[bs-anticheat]] · [[grim]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
