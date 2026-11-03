---
title: Jidr
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AbdurahmanAlmehdi__jidr.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# Jidr

**Jidr** (AbdurahmanAlmehdi/jidr) is an open-source **Apple Silicon macOS** desktop platform for running and controlling **fully rooted Android virtual devices**, positioned as a clean-room alternative to Genymotion. A Rust **daemon** drives the stock **AOSP emulator** over **gRPC**, the **telnet console**, and **ADB**; **Slint** GUI, **CLI**, and an **MCP server** are thin **JSON-RPC** clients on the same control plane. Built-in providers cover one-click root via **adb** or **Magisk ramdisk** patching, **build-property spoofing**, **snapshots**, and rich device widgets (GPS, sensors, network, media capture, developer tooling). Jidr manages its own **Android SDK cache** and **AVD lifecycle** while treating an existing **Android Studio** install as read-only. (source: wiki/sources/descriptions/AbdurahmanAlmehdi__jidr.md)

Listed under README **Android Emulator** (~13 links).

## Audience

Mobile developers and security researchers who need **reproducible, fully rooted emulators** for app testing, instrumentation, and Android-focused reverse engineering—not a hosted cloud device farm.

## Positioning

**macOS-native AOSP AVD control stack** with automation-first MCP/CLI: contrasts with Windows [[rooted-android-game-vm]] (WPF Magisk workbench), custom-QEMU macOS host [[kiln-android-emulator]] (LineageOS + `kilnctl` game profiles), and non-VM Linux APK host [[android-compatibility-layer]]; complements Genymotion-class workflows without requiring Genymotion licensing. (source: wiki/sources/descriptions/AbdurahmanAlmehdi__jidr.md)

## Surfaces

| Component | Role |
|-----------|------|
| **Daemon** | Rust; gRPC + telnet + ADB orchestration of AOSP emulator |
| **Clients** | Slint GUI, CLI, MCP server (JSON-RPC) |
| **Root / identity** | adb root, Magisk ramdisk patch, build.prop spoofing |
| **Lab widgets** | GPS, sensors, network, media capture, dev tooling |
| **Lifecycle** | Own SDK cache + AVD management; read-only Android Studio |

## Links

- Repo: https://github.com/AbdurahmanAlmehdi/jidr

## Related

[[kiln-android-emulator]] · [[rooted-android-game-vm]] · [[android-compatibility-layer]] · [[mobile-harness]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
