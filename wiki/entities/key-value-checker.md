---
title: KeyValueChecker
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/Kotsasmin__key-value-checker.md
  - wiki/sources/README-categories.md
updated: 2026-10-01
confidence: medium
---

# KeyValueChecker

**KeyValueChecker** (Kotsasmin/key-value-checker) is a lightweight **Java** **Paper/Spigot 1.21+** Minecraft server anti-cheat plugin that fingerprints **client-side cheat mods invisible to ordinary server telemetry**. It exploits Minecraft **translation components** by injecting fake signs bearing known mod language keys through **PacketEvents**, then comparing returned **UpdateSign** packet text to prove whether a client resolved those keys during **player join**. Configurable blacklist/whitelist groups target popular clients such as **Meteor Client**, **Freecam**, and **AutoTotem**; flagged players can be kicked with optional **Discord webhook** alerts. (source: wiki/sources/descriptions/Kotsasmin__key-value-checker.md)

## Detection mechanism

**Translation-key probe** — server sends sign payloads referencing mod-localization keys; honest vanilla clients leave probe text unchanged while cheat clients that ship those translation tables resolve recognizable strings, yielding packet-level evidence without client-side instrumentation.

## Configuration

- **Blacklist/whitelist groups** — per-mod translation-key sets for allowed or disallowed client modifications
- **Enforcement** — kick on positive match; optional Discord webhook alerts for staff review

## Positioning

**Join-time client-mod fingerprinting** — distinct from movement heuristics in [[h-ac]] or hash-whitelist admission in [[faircount]] and consent-gated telemetry in [[mcace]]. Adjacent to injectable passive observers such as [[rain-injectable]] and Fabric security suites such as [[bastion]] on [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/Kotsasmin/key-value-checker

## Related

[[overviews/anti-cheat]] · [[h-ac]] · [[faircount]] · [[mcace]] · [[rain-injectable]] · [[bastion]] · [[network-environment-evidence]] · [[detector-operations]]
