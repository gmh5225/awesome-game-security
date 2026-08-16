---
title: vac-hooks
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/danielkrupinski__vac-hooks.md
updated: 2026-08-16
confidence: medium
---

# vac-hooks

C DLL research project (danielkrupinski) that hooks WinAPI functions used by Valve Anti-Cheat, logging calls and intercepting arguments and return values. Listed under cheat / explore anticheat system:vac; useful for game-security researchers and reverse engineers studying offensive techniques against VAC. Build requires Visual Studio platform toolset v142 and Windows SDK 10.0. (source: wiki/sources/descriptions/danielkrupinski__vac-hooks.md)

Companion hooking surface to [[vook]] (VAC hook research), [[vac-bypass]] (Steam-client VAC scan inhibition), and [[vac3-inhibitor]] (VAC3 inhibition / memory analysis): this repo focuses on **WinAPI interception telemetry** for VAC-used APIs rather than decompiled module internals ([[vac]]) or module dumps ([[vac3-dumper]], [[vac-module-dumper]], [[vac-dumper]]) or ICE key recovery ([[vackeyretrieval]]).

## Links

- Repo: https://github.com/danielkrupinski/vac-hooks

## Related

[[vac]] · [[vac-bypass]] · [[vook]] · [[vac3-inhibitor]] · [[vac3-dumper]] · [[vac-module-dumper]] · [[vackeyretrieval]] · [[como-funciona-vac]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
