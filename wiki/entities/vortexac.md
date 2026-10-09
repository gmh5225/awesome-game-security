---
title: Vortex Anti-Cheat
kind: entity
topics: [anti-cheat, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/AliShe3a__VortexAC.md
updated: 2026-10-09
confidence: medium
---

# Vortex Anti-Cheat

**User-mode client–server anti-cheat** and **engine patcher** for **CrossFire private servers** (AliShe3a/VortexAC). Targets operators who need session security, cheat deterrence, and legacy client fixes on self-hosted CF deployments—not commercial live-service CrossFire. (source: wiki/sources/descriptions/AliShe3a__VortexAC.md)

## Capabilities

| Area | Coverage |
|------|----------|
| Client detections | Direct3D9 hook inspection, CRC32 memory integrity, process and debugger scanning |
| Asset protection | Microsoft [[detours]]-based Win32 API hooks decrypt protected game assets at runtime |
| Session control | MS SQL Server stored procedures for validation, heartbeats, tiered bans, hardware ID enforcement |
| Server services | TCP authentication/heartbeats; UDP live screen streaming and VOIP; embedded HTTP admin panel; Discord WebSocket alerts |
| Engine maintenance | Client limit patches and long-standing engine bug fixes alongside AC |

## Architecture

| Layer | Role |
|-------|------|
| **C++ game client module** | Heuristic checks and on-the-fly asset decrypt hooks in user mode |
| **Validation server** | Auth, heartbeat, streaming, and admin-facing HTTP/Discord integrations |
| **SQL backend** | Authoritative session and ban state via stored procedures |

## Positioning

Listed as an **open-source CrossFire private-server AC** with integrated server tooling. Defensive counterpart to cheat samples such as [[cfclap]] and [[titancf]] in the **game:crossfire** lane; client graphics checks overlap the [[present-hook]] detection surface (D3D9 hook inspection).

## Links

- Repo: https://github.com/AliShe3a/VortexAC

## Related

[[cfclap]] · [[titancf]] · [[detours]] · [[present-hook]] · [[overviews/anti-cheat]]
