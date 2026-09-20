---
title: terraria-android-modding
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/abcd123rft__terraria-android-modding.md
  - wiki/sources/README-categories.md
updated: 2026-09-20
confidence: medium
---

# terraria-android-modding

**terraria-android-modding** (abcd123rft) — reusable **skill package** and ready-to-run in-game mod menu for the Android build of **Terraria**, a Unity IL2CPP title on arm64. Documents and implements IL2CPP hooking **by member name** rather than fixed addresses, using Frida and JsHook-based JavaScript injection with per-frame hooks on `Player` methods such as `UpdateEquips` and `PlayerFrame`. README **Cheat / Frida** lane. (source: wiki/sources/descriptions/abcd123rft__terraria-android-modding.md)

## Architecture

- **Frida / JsHook** — JavaScript injection with il2cpp-by-name hooks (no hard-coded RVAs); per-frame `Player` method interception
- **Native Android system UI** — overlay menus built with system views so touches do not pass through to the game
- **Python utilities** — offline APK unpacking, item icon atlas extraction, and name-table generation for asset RE

## Use cases

Reverse engineering, mobile game modding, and single-player memory editing research on arm64 Android devices. (source: wiki/sources/descriptions/abcd123rft__terraria-android-modding.md)

## Links

- Repo: https://github.com/abcd123rft/terraria-android-modding [Documented Android Terraria IL2CPP modding skill plus Frida/JsHook injectable mod menu: il2cpp-by-name hooks, system-UI overlay menus, and offline icon extraction tooling]

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[il2cpp]] · [[frida]] · [[malum-menu-android]] · [[fallguys-frida-modmenu]] · [[android-modding]] · [[research-rigor]]
