---
title: Carbon Android
kind: entity
topics: [reverse-engineering, mobile-security, graphics-api]
sources:
  - wiki/sources/descriptions/Chizuui__Carbon-Android.md
  - wiki/sources/README-categories.md
updated: 2026-11-27
confidence: medium
---

# Carbon Android

Unofficial **Android arm64** port of the original Xbox edition of *Need for Speed: Carbon* (Chizuui/Carbon-Android). Retail XBE machine code is **statically recompiled** into C++ rather than executed under a full Xbox emulator. Users bring their own game assets; the repository ships no copyrighted content. (source: wiki/sources/descriptions/Chizuui__Carbon-Android.md)

## Stack

- **Lift:** **XboxXBE-Recomp** SDK portable runtime—OG Xbox kernel and XDK high-level emulation with **Direct3D 8** guest graphics.
- **Host:** custom **arm64** renderer via **Vulkan 1.1**; windowing, audio, and input through **SDL3**.
- **Android:** **Gradle** + Java shell; **CMake** native C++ with hook and symbol tables driven by **TOML** for the recompiler.
- **UX / tooling:** touch layouts, controller and keyboard remapping, **ImGui** settings overlay, log export, optional performance tracing. (source: wiki/sources/descriptions/Chizuui__Carbon-Android.md)

## Audience

Reverse engineers and game-security researchers studying **OG Xbox binary recompilation**, **D3D8→Vulkan** API translation, and native mobile ports of legacy retail titles without a full-system emulator—beside other Xbox lift references such as [[ngbrecomp]] and Android lift kits such as [[sc2-android-recomp]]. Pair lift/HLE boundaries with [[static-runtime-evidence]] when comparing runtime behavior to emulator traces. (source: wiki/sources/descriptions/Chizuui__Carbon-Android.md)

## Links

- Repo: https://github.com/Chizuui/Carbon-Android

## Related

[[ngbrecomp]] · [[sf33rdsxbrecompo]] · [[sc2-android-recomp]] · [[xemu]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/graphics-api]]