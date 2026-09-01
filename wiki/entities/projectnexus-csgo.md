---
title: Project Nexus CSGO
kind: entity
topics: [game-hacking, graphics-api, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Atonl200__ProjectNexus-CSGO.md
updated: 2026-09-01
confidence: medium
---

# Project Nexus CSGO

**Project Nexus** (Atonl200/ProjectNexus-CSGO) is a C++20 Counter-Strike 2 internal cheat suite built with CMake. It injects a feature DLL into the game process and pairs it with a separate external DirectX 11 ImGui overlay for rendering and configuration. Features include aimbot, triggerbot, recoil control, ESP, movement assists, and skin changing, implemented via MinHook hooks with CS2 schema and offset resolution. Shared-memory IPC connects the in-process module to the overlay. A usermode loader performs manual-map injection through direct syscalls; optional kernel driver, [[byovd]], and PE mapper components support advanced injection workflows. Intended for game security researchers and reverse engineers studying cheat architecture, memory manipulation, and anti-cheat evasion in modern FPS titles. (source: wiki/sources/descriptions/Atonl200__ProjectNexus-CSGO.md)

Sits in the hybrid internal/external CS2 lane beside research frameworks such as [[rabsztyncc-cs2-internal]] and feature samples such as [[asphyxia-cs2]] and [[cs2-cheat-source]].

## Links

- Repo: https://github.com/Atonl200/ProjectNexus-CSGO

## Related

[[present-hook]] · [[byovd]] · [[cs2-offsets]] · [[cs2-dumper]] · [[cs2-internal-sdk]] · [[asphyxia-cs2]] · [[rabsztyncc-cs2-internal]] · [[cs2-cheat-source]] · [[cs2-cheat-base]] · [[syscall-detect]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
