---
title: OpenManager
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/uamo11__OpenManager.md
updated: 2026-11-08
confidence: medium
---

# OpenManager

**OpenManager** (uamo11/OpenManager) is an open-source GPLv3 **dual-panel Android file manager** and **on-device reverse-engineering workbench** for advanced package and filesystem workflows on rooted hardware. The stack is mainly **Kotlin and Java** (Android Gradle) with **native C/C++** for JNI and low-level syscall probing. (source: wiki/sources/descriptions/uamo11__OpenManager.md)

## Catalog lane

Cheat — Android File Explorer / RE workbench: Apktool, DEX/Smali editing, hex editor, ARSC/AXML tooling, with Magisk, KernelSU, and Shizuku support. (source: wiki/sources/descriptions/uamo11__OpenManager.md)

## Capabilities

Rooted file access, syntax-highlighted editors for **smali** and related formats, **DEX** and **ARSC** editors, APK tooling, script automation, **FTP server** mode, and **toast-dialog injection** helpers for APK modification. Intended for mobile reverse engineers, modders, and game-security researchers who patch, inspect, and analyze Android apps and game clients without leaving the device. (source: wiki/sources/descriptions/uamo11__OpenManager.md)

## Positioning

Sits beside [[file-explorer]], [[app-manager]], and [[butler]] as a rooted on-phone manager, but emphasizes integrated **smali/DEX/ARSC/AXML** editing and Apktool-style workflows rather than backup-only or host-side tooling. Complements desktop pipelines ([[jadx]], [[apktool]], [[apklab]]) when analysts need full package surgery on hardware with [[magisk]], [[kernelsu]], or Shizuku elevation.

## Links

- Repo: https://github.com/uamo11/OpenManager

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apktool]] · [[magisk]] · [[kernelsu]] · [[file-explorer]] · [[app-manager]]
