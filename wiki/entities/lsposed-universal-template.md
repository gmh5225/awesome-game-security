---
title: LSPosed Universal Template
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Jordan231111__lsposed-universal-template.md
updated: 2026-08-24
confidence: medium
---

# LSPosed Universal Template

Quick-start **Android module scaffold** for building **LSPosed** and **LSPatch** hook modules for authorized testing and rapid prototyping. Targets modern **libxposed API 102** with Java hooking, a runtime feature registry, a movable overlay mod menu, and optional native hooks via **ShadowHook** plus JNI memory utilities for pattern scanning and module lookup. (source: wiki/sources/descriptions/Jordan231111__lsposed-universal-template.md)

**Stack:** Java and C++ with Gradle and CMake. Includes **engine detection** for Unity, Unreal, Cocos2d-x, and Godot; **process filters** that skip common anti-cheat satellite processes; and Frida reconnaissance scripts plus documentation for IL2CPP and native game workflows.

**Use cases:** Android reverse engineers and game security researchers who need a structured starting point for hooking and analyzing mobile games and apps they are authorized to test.

## Links

- Repo: https://github.com/Jordan231111/lsposed-universal-template

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[xposed-module-kit]] · [[apppealing-new]] · [[canyie-pine]] · [[frida]] · [[il2cpp]] · [[game-engine-detector]] · [[mobile-anti-cheat]]
