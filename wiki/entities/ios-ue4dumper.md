---
title: iOS UE4Dumper
kind: entity
topics: [game-engine, mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/MJx0__iOS_UE4Dumper.md
updated: 2026-08-23
confidence: medium
---

# iOS UE4Dumper

**iOS Unreal Engine dumper** delivered as a **MobileSubstrate tweak** from MJx0. C++ and Objective-C++ codebase targeting **arm64** and **arm64e** devices; uses pattern-based discovery of core engine structures to dump offsets, classes, structs, enums, and functions, then emits analysis-ready symbol JSON for IDA and Ghidra. Primary use case is iOS game reverse engineering and Unreal Engine security research on mobile titles. (source: wiki/sources/descriptions/MJx0__iOS_UE4Dumper.md)

Sits in the Cheat / `[SDK Dump For IOS]` lane beside Android UE4 SDK dumpers such as [[ue4-apk-dumper]], [[ue4dumper]], and [[frida-ue4dump]], and desktop dumpers such as [[uedumper]] and [[shh0yauedumper]] on the [[unreal-object-model]] side.

## Links

- Repo: https://github.com/MJx0/iOS_UE4Dumper (README tag: [SDK Dump For IOS])

## Related

[[unreal-object-model]] · [[ue4-apk-dumper]] · [[ue4dumper]] · [[frida-ue4dump]] · [[uedumper]] · [[shh0yauedumper]] · [[game-engine-detector]] · [[ios-mod-menu-template-for-theos]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
