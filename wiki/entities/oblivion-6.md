---
title: Oblivion 6 (Oblivion Hack Shield)
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Hansel38__Oblivion-6.md
  - wiki/sources/README-categories.md
updated: 2026-11-12
confidence: medium
---

# Oblivion 6 (Oblivion Hack Shield)

**Client–server anti-cheat stack** (Hansel38) aimed at **online MMO-style games on Windows**: a Visual Studio–built **C++ client DLL** loaded into the game process, plus a **companion authorization server** with Windows and Linux builds. Violations detected on the client are reported over the network; the server uses **heartbeat**, **hardware ID**, and **ban lists** to authorize sessions and remotely kick or block cheaters. Useful as an **open-source reference** for studying MMO-oriented usermode AC design and lightweight server-side enforcement. (source: wiki/sources/descriptions/Hansel38__Oblivion-6.md)

## Client protection

Continuous in-process checks include **debuggers**, **injection**, **IAT hooks**, **suspicious memory**, **overlays**, **file tampering**, **digital signatures**, and **self-integrity**, with **cross-process heuristics** and **anti-suspend** logic on watched processes.

## Server

Heartbeat protocol, HWID generation, ban-list driven session authorization, remote kick/block, **secret obfuscation**, logging, and deployment helpers for operating the shield in production or lab environments.

## Architecture

| Layer | Role |
|-------|------|
| **Client DLL** | In-process integrity, anti-debug, injection/overlay detection, telemetry to server |
| **Authorization server** | Heartbeat, HWID, bans, remote enforcement (Win/Linux) |

Sits in the README **Open Source Anti Cheat System** lane beside full-stack samples such as [[ultimate-anti-cheat]] and educational usermode frameworks.

## Links

- Repo: https://github.com/Hansel38/Oblivion-6

## Related

[[overviews/anti-cheat]] · [[ultimate-anti-cheat]] · [[rebirth-guard]] · [[betashield]] · [[odzhan-hwid]]
