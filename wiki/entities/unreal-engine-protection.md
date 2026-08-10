---
title: UnrealEngine-Protection
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__UnrealEngine-Protection.md
updated: 2026-08-10
confidence: medium
---

# UnrealEngine-Protection

**SCUE4** (*Secure-Client* anti-cheat plugin for **Unreal Engine 4**, Windows 32/64-bit). Drop-in `Plugins/` integration that generates substantial C++ project code; activate by setting **`SafeGameInstance`** as the default Game Instance (or re-parenting a custom instance from it). Disabling is a matter of swapping the default Game Instance back. (source: wiki/sources/descriptions/gmh5225__UnrealEngine-Protection.md)

Defensive surfaces for anti-cheat engineers and UE protection researchers under README **Game Engine Protection:Unreal**:

- **SC Safe Types** — Blueprint Get/Set nodes encrypt common property types (bool, int, float, string, vectors, rotator, transform, etc.); Details-panel values are decoy copies; only graph nodes can read/write real encrypted state. Documented Get/Set footprint ~0.00–0.01 ms vs multi-ms Tick events.
- **Game-Guard** — external scanner (VS2015 + .NET 4) plus in-game fallback via `SafeGameInstance` that can force a crash if the external app is bypassed.
- **Anti-debugger** — optional in-editor observation via a Blueprint child of `SafeGameInstance` (`Hide Game-Guard` / `Allow Debugging` toggles; typically off until Shipping packaging).

Packaging for non-Windows targets is not broken, but AC features target Windows builds only. ASCII-only text/string encryption is a documented limitation.

## Links

- Repo: https://github.com/gmh5225/UnrealEngine-Protection
- Forum reference: https://forums.unrealengine.com/t/plugin-anti-cheat-system/213948

## Related

[[static-variables-obfuscator-ue4]] · [[usecurity]] · [[unreal-object-model]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
