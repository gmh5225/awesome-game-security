---
title: AntiCheatPlugin EasyAntiCheat
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/GeneralsOnlineDevelopmentTeam__AntiCheatPlugin_EasyAntiCheat.md
updated: 2026-09-27
confidence: medium
---

# AntiCheatPlugin EasyAntiCheat

**AntiCheatPlugin EasyAntiCheat** (GeneralsOnlineDevelopmentTeam/anticheatplugin_easyanticheat) is a **Windows 32-bit anti-cheat middleware plugin DLL** that integrates **Easy Anti-Cheat** through the **Epic Online Services (EOS) SDK** for online multiplayer games. Written in **C++20** and built with **CMake**, it implements the host game's plugin interface for initialization, player registration, session management, and callback-driven handling of integrity violations and required player actions. (source: wiki/sources/descriptions/GeneralsOnlineDevelopmentTeam__AntiCheatPlugin_EasyAntiCheat.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Architecture

The plugin wraps EOS EAC integration behind a host-game plugin contract:

- **Initialization** — EOS product/deployment credentials configured at compile time; x86 EOS SDK supplied separately by the developer
- **Player lifecycle** — registration, session join/leave, and callback dispatch for integrity violations and mandated player actions
- **Secure transport** — routes gameplay and anti-cheat traffic over **EOS P2P networking** with connection-state tracking, latency measurement, and peer authentication

## Positioning

Production-grade **EAC + EOS middleware** for game developers and mod teams adding commercial anti-cheat and authenticated P2P transport to **legacy or custom online titles**—contrasts with client-interface stubs such as [[easyanticheat-emulator]] and server-protocol RE such as [[eac-leak]]. Complements the broader [[easy-anti-cheat]] integration surface for titles that cannot rely on first-party Epic launcher plumbing.

## Peers

[[easyanticheat-emulator]] · [[eac-emu]] · [[eac-leak]] · [[eac]]

## Links

- Repo: https://github.com/generalsonlinedevelopmentteam/anticheatplugin_easyanticheat

## Related

[[concepts/easy-anti-cheat]] · [[overviews/anti-cheat]]
