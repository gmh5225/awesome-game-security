---
title: MS KIT
kind: entity
topics: [game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/Kysnez4__MS_KIT.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: high
---

# MS KIT

Unofficial **mod loader and authoring framework** for the Android game *Magic Survival*, shipped as the side-by-side **Zombix** client that runs **without root**. (source: wiki/sources/descriptions/Kysnez4__MS_KIT.md)

The current stack centers on a **C# ModKit** built on **MelonLoader** with Harmony and Il2CppInterop: zip-based mods, in-game enablement UI, hooks, events, and shared libraries for combat, spells, artifacts, effects, and game data. An older **Frida** generation supports TypeScript/JavaScript mods for table and effect tweaks. Build/deploy tooling, example mods, table references, and docs target developers extending or reverse-engineering **Unity IL2CPP** gameplay on device.

## Modding surface

- **Current:** MelonLoader + Harmony patches, Il2CppInterop for managed hooks against AOT code, zip-packaged mods toggled from an in-game UI.
- **Legacy:** Frida-hosted TS/JS mods for data-table and visual-effect tweaks without the full C# ModKit pipeline.

Listed under README **Cheat** (Android injection / mod-loader lane beside [[android-virtual-inject]], [[inject-arm64]], and [[linjector-rs]]).

## Links

- Repo: https://github.com/Kysnez4/MS_KIT

## Related

[[il2cpp]] · [[frida]] · [[mobile-anti-cheat]] · [[terraria-android-modding]] · [[overviews/game-hacking]] · [[overviews/mobile-security]]
