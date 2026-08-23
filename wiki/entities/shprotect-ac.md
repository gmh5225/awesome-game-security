---
title: SHProtect AntiCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/sorrelhub__shprotect-ac.md
updated: 2026-08-03
confidence: medium
---

# SHProtect AntiCheat

**Server-first anti-cheat foundation** for **Roblox** experiences. Keeps enforcement decisions on the server while using lightweight client signals for monitoring only—not as a security boundary. Written in **Lua** for Roblox Studio or **Rojo** projects. (source: wiki/sources/descriptions/sorrelhub__shprotect-ac.md)

## Detection surface

**Movement:** speed, teleport, fly, noclip, fling, infinite jump.

**Network:** RemoteEvent spam and rate limiting.

**Integrity:** safe-position history, client heartbeat, and watchdog integrity checks.

## Enforcement

Configurable corrective actions through a central **Config** module: scoring, warnings, position rollbacks, and kicks.

Targets Roblox developers who need a modular, testable anti-cheat layer against common exploit scripts—the same server-authoritative model as [[encryptic-roblox-anti-cheat]], [[advanced-anticheat]], [[cs2ac]], and [[nocheatz-3]], applied to Roblox script games. Pair with [[lua-obfuscator-clyde-protection]] for Luau script hardening and [[roblox-cheats]] for the offensive Roblox client lane.

## Links

- Repo: https://github.com/sorrelhub/shprotect-ac

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[encryptic-roblox-anti-cheat]] · [[advanced-anticheat]] · [[roblox-cheats]] · [[lua-obfuscator-clyde-protection]]
