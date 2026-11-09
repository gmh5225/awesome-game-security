---
title: Toxido AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ToxidoAAC__ToxidoAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-09
confidence: medium
---

# Toxido AntiCheat

**Toxido Anti Cheat** (ToxidoAAC/ToxidoAntiCheat) is a **client-side Minecraft Java** anti-cheat that monitors running game processes **without requiring a client mod**, by attaching a **Java agent** through the **JVM Attach API**. (source: wiki/sources/descriptions/ToxidoAAC__ToxidoAntiCheat.md)

Distinct from episodic PowerShell JVM audits such as [[jvm-inspector]] and consent-based screenshare stacks such as [[hapiscanner]]: Toxido runs as a **persistent Windows background service** that discovers JVMs, loads the agent, and maintains **signed backend sessions** with staff-facing **Discord** visibility.

## Architecture

| Component | Role |
|-----------|------|
| **Windows service** | Discovers vanilla, Fabric, Quilt, Forge, or NeoForge Minecraft JVMs; loads the injectable agent; loopback IPC handshake and heartbeats |
| **Java stack** | Maven modules for launcher app and injectable agent; phase-one ships as **jlink**-packaged standalone EXE |
| **Backend** | Python **FastAPI** with **HMAC-SHA256**-protected session API; **SQLite** persistence |
| **Staff bot** | **discord.py** bot opens and archives per-player **Now** and **Log** channels |

## Phases

- **Phase one (current):** session lifecycle, telemetry, and Discord staff visibility—attach and session infrastructure.
- **Phase two (planned):** JVM instrumentation for cheat and mod **signature scanning**.

## Audience

**Minecraft Java communities** that want **client-side detection and monitoring** alongside server enforcement—not purely server-plugin AC such as [[kozy-anticheat]], and not mod-based client integrity such as [[mcace]].

## Links

- Repo: https://github.com/ToxidoAAC/ToxidoAntiCheat

## Related

[[jvm-inspector]] · [[hapiscanner]] · [[nocturne-client]] · [[leaf-mod-analyzer]] · [[kozy-anticheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
