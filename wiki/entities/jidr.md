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

**Jidr** — open-source Apple Silicon macOS platform for running and controlling rooted Android virtual devices (Genymotion-style clean-room alternative). (source: wiki/sources/descriptions/AbdurahmanAlmehdi__jidr.md)

## Architecture

Rust daemon drives the AOSP emulator over gRPC, telnet console, and ADB; **Slint** GUI, CLI, and **MCP** server expose JSON-RPC control. Built-in providers cover one-click root (adb or Magisk ramdisk patch), build-property spoofing, snapshots, and widgets for GPS, sensors, network, media capture, and developer tooling. Manages its own Android SDK cache and AVD lifecycle while treating an existing Android Studio install as read-only.

## Audience

Mobile developers and security researchers who need reproducible, fully rooted emulators for app testing, instrumentation, and Android-focused RE.

## Links

- Repo: https://github.com/AbdurahmanAlmehdi/jidr

## Related

[[kiln-android-emulator]] · [[android-compatibility-layer]] · [[mobile-harness]] · [[overviews/mobile-security]]
