---
title: Phoenix AC
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/InsideExploit__phoenix-ac.md
  - wiki/sources/README-categories.md
updated: 2026-11-01
confidence: high
---

# Phoenix AC

**Self-leaked commercial-style FiveM anti-cheat stack** (InsideExploit; Windows; Anti Cheat / Open Source Anti Cheat System). Protects roleplay and multiplayer **FiveM** servers with a C++ usermode client agent, optional **kernel-mode driver**, TypeScript **WebSocket/MySQL** backend, **Next.js** operator dashboard, in-game **Lua** CitizenFX resource, and signed-artifact **updater**. Useful for studying full-stack client–server AC architecture without treating the leak as a supported product. (source: wiki/sources/descriptions/InsideExploit__phoenix-ac.md)

## Architecture

- **Client agent** — C++ usermode monitoring plus optional WDM-style kernel module for deeper integrity and driver/IRP signals.
- **Control plane** — TypeScript backend (WebSockets, MySQL persistence), Next.js staff dashboard, Lua server resource for in-game hooks, updater for signed delivery of client artifacts.

## Client detection and telemetry

Scans include overlays, suspicious hotkeys, cheat-related **DNS/hosts** entries, unsigned FiveM modules, **manual-mapped drivers** and **IRPs**, reverse-engineering and debugging tooling, **vulnerable drivers**, and **HVCI** or boot misconfiguration. Reports flow upstream as detections, **screenshots**, **minidumps**, hardware IDs, and **alt-account** correlation. (source: wiki/sources/descriptions/InsideExploit__phoenix-ac.md)

## Operator workflows

**Steam** and **Discord** authentication, pin-based enrollment, live session tracking, bans and suspensions, kill telemetry, and **Discord webhooks** for staff alerting—typical of hosted FiveM AC products. (source: wiki/sources/descriptions/InsideExploit__phoenix-ac.md)

## Links

- Repo: https://github.com/InsideExploit/phoenix-ac

## Related

[[atomicshieldclient]] · [[dead-anticheat]] · [[mf-antiesp]] · [[aeterna-rongroi]] · [[screenshare-signatures]] · [[hvci]] · [[byovd]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
