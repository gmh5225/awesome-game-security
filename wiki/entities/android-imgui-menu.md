---
title: android_imgui_menu
kind: entity
topics: [mobile-security, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/horoni__android_imgui_menu.md
updated: 2026-08-05
confidence: medium
---

# android_imgui_menu

Rust ARM64 `cdylib` that injects Dear ImGui overlay menus into running Android applications: hooks `libEGL.so` (OpenGL ES) and `libvulkan.so` (Vulkan) render chains, uses ARM64 inline hooking with `xdl` symbol resolution, and auto-loads via a constructor hook. Custom Rust bindings cover ImGui, Vulkan, and Android input—aimed at in-process debug panels, mod menus, and reverse-engineering tooling on Android. (source: wiki/sources/descriptions/horoni__android_imgui_menu.md)

Complements Java/C++ native-app ImGui samples ([[android-native-app-imgui]]), GLES/JNI templates ([[imgui-native-modmenu]]), Zygisk-injected menus ([[zygisk-imgui-mod-menu]], [[imgui-zygisk-unity]]), and Unity-on-Android ImGui scaffolds ([[imgui-unity]]) with a Rust cdylib + dual-backend (EGL/Vulkan) interception lane.

## Links

- Repo: https://github.com/horoni/android_imgui_menu

## Related

[[android-native-app-imgui]] · [[imgui-native-modmenu]] · [[zygisk-imgui-mod-menu]] · [[imgui-zygisk-unity]] · [[imgui-unity]] · [[present-hook]] · [[overviews/mobile-security]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
