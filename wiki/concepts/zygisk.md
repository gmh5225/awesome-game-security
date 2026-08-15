---
title: Zygisk
kind: concept
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/descriptions/ri-char__zygisk-dump-dex.md
  - wiki/sources/descriptions/reveny__Zygisk-ImGui-Mod-Menu.md
  - wiki/sources/descriptions/fedes1to__Zygisk-ImGui-Menu.md
updated: 2026-08-15
confidence: medium
---

# Zygisk

Magisk **Zygisk** API for native modules that hook the Android app specialization path—code runs inside `zygote`/`app_process` during fork before the target app's Java bootstrap completes. Primary injection surface for early native load, DEX extraction, and GLES overlay menus on rooted devices. (source: wiki/sources/skills/mobile-security.md)

## Module lifecycle

1. **`onLoad`** — receive `zygisk::Api` + `JNIEnv`; stash handles for later hooks.
2. **`preAppSpecialize`** — runs before the app process specializes (package name / UID known); filter target packages here.
3. **`postAppSpecialize`** — runs after specialization; inject native agents, hook `dlopen`, or attach render/input hooks before `Application.onCreate` / static class init.

Modules compile as `.so` loaded by Magisk's Zygisk loader ([[magisk]] DenyList / Shamiko may hide root from apps that also scan Zygisk artifacts).

## Game-security uses

- **DEX/metadata extraction** — [[zygisk-dump-dex]] hooks `libdexfile.so` on Android 14/15.
- **Overlay menus** — [[zygisk-imgui-menu]] (fedes1to; ImGui + cURL; `hook.cpp`; cheat / render-draw) (source: wiki/sources/descriptions/fedes1to__Zygisk-ImGui-Menu.md); in-dev [[zygisk-imgui-mod-menu]] and hobby [[zygisk-imgui-modmenu]]; complements non-Zygisk GLES templates ([[imgui-native-modmenu]], [[imgui-unity]]).
- **Conflict management** — managed-instrumentation workflows may disable conflicting Zygisk modules, reboot for analysis, then restore (source: wiki/sources/skills/mobile-security.md).

Pair with [[research-rigor]] when generalizing injection timing across OEM/Android versions.

## Related

[[magisk]] · [[kernelsu]] · [[frida]] · [[il2cpp]] · [[zygisk-dump-dex]] · [[zygisk-imgui-menu]] · [[zygisk-imgui-mod-menu]] · [[zygisk-imgui-modmenu]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
