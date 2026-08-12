---
title: Generic Game Detour API Hook
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/wesjian__GenericGameDetourAPIHook.md
updated: 2026-08-12
confidence: medium
---

# Generic Game Detour API Hook

Modular Windows API hooking framework (**DetourAPIHook**) built on [[detours]] that intercepts roughly **130 system calls** across **16 independent hook modules** to study and bypass commercial game anti-cheat protections. Deploys as a **`dinput8.dll` proxy** for transparent DLL-hijack injection into x86 and x64 game processes. Capabilities include process and module hiding, anti-debug neutralization, hardware and network identity spoofing, memory-integrity bypass, multi-instance support, and a **caller-check engine** that selectively blocks requests originating from known protection modules. Targets include NGS, BlackCipher, HackShield, XignCode, GameGuard, and TenProtect — intended for game-security research, reverse engineering, and studying client-side protection behavior. (source: wiki/sources/descriptions/wesjian__GenericGameDetourAPIHook.md)

## Links

- Repo: https://github.com/wesjian/GenericGameDetourAPIHook

## Related

[[detours]] · [[detoursnt]] · [[windows-dll-hijacking]] · [[hook-buster]] · [[hookhunter]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
