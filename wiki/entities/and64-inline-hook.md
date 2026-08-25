---
title: And64InlineHook
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Rprop__And64InlineHook.md
updated: 2026-08-21
confidence: medium
---

# And64InlineHook

Lightweight **Android ARM64 inline hooking library** (ARMv8 / AArch64). C++ implementation patches target instructions, relocates affected AArch64 branches, and builds trampolines so original code can continue safely after hooks are installed. Handles low-level runtime details such as executable memory changes and instruction cache flushing. Useful for mobile reverse engineering, instrumentation, and game security experimentation on ARMv8 platforms. (source: wiki/sources/descriptions/Rprop__And64InlineHook.md)

Sits in the native Android hook lane beside [[android-inline-hook-arm64]], [[dobby]], [[adbi]], [[pyasm-patch]], and Substrate/xHook-style ARM64 `.so` instrumentation.

## Links

- Repo: https://github.com/Rprop/And64InlineHook

## Related

[[android-inline-hook-arm64]] · [[adbi]] · [[dobby]] · [[pyasm-patch]] · [[farm64]] · [[qbdi-tracer-android]] · [[china-pubg]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
