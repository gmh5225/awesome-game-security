---
title: vac-dumper
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__VACDumper.md
updated: 2026-08-10
confidence: medium
---

# vac-dumper

**VAC3 live module dumper** (gmh5225): a DLL injected into `steam.exe` that hooks the `steamservice.dll` routine responsible for loading VAC modules (MinHook), capturing module bytes at load time and writing recovered modules to `C:\Modules` for offline analysis. Workflow: start Steam as administrator, inject before the game launches. Useful for reverse engineers studying Valve Anti-Cheat module loading, Steam-side interception points, and live-dump workflows for VAC analysis. (source: wiki/sources/descriptions/gmh5225__VACDumper.md)

Companion dump surface to [[vac3-dumper]] (timed multi-module loads) and [[vac-module-dumper]] (offline module dump): this repo focuses on **Steam-side load-time interception** rather than post-load reconstruction, ICE key recovery ([[vackeyretrieval]]), or runtime inhibition ([[vac3-inhibitor]]).

## Links

- Repo: https://github.com/gmh5225/VACDumper

## Related

[[vac3-dumper]] · [[vac-module-dumper]] · [[vac3-inhibitor]] · [[vackeyretrieval]] · [[vac-emulator]] · [[vacation3-emu]] · [[como-funciona-vac]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
