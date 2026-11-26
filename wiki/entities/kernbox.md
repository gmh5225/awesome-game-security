---
title: KernBox
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Touka404x__KernBox.md
updated: 2026-11-26
confidence: medium
---

# KernBox

**KernBox** (Touka404x/KernBox) is an open-source **Android isolation framework** for rooted **ARM64** phones that provisions a stealthy, leak-resistant workspace inside an **Android Work Profile** enforced at the **kernel and system** layer. Delivered as compile-time-specialized **root-module** builds for multiple OEM, kernel, and root-manager combinations, plus a pure-SDK **controller app** and a **twelve-point verification probe**. (source: wiki/sources/descriptions/Touka404x__KernBox.md)

## Stack

Implemented primarily in **Go**, **C**, **C++**, and **Java**:

- **Fail-closed** **Netfilter** and **TProxy** routing for traffic isolation
- Least-privilege **broker** and **guard** daemon
- **Zygisk** native **PLT** hooks
- **Binder** proxies that sanitize connectivity and Work Profile APIs seen by sandboxed processes
- **Hot-freeze** and memory reclaim for idle drain control
- **Regional presets** for locale and carrier semantics (isolated apps and GMS)

## Use cases

Targets game security, anti-cheat, and mobile reverse-engineering workflows that need **strong sandbox boundaries**, **traffic isolation**, and resistance to **in-app environment fingerprinting** on a single physical device—without relying on host-no-root app cloners alone.

## Links

- Repo: https://github.com/Touka404x/KernBox (kernel-backed Android Work Profile sandbox for rooted devices: fail-closed network isolation, Zygisk hiding, lean OEM/root module variants, and control APK)

## Related

[[overviews/mobile-security]] · [[zygisk]] · [[magisk]] · [[kernelsu]] · [[apatch]] · [[shit-jumping-vm]] · [[zn-toolbox]] · [[virtual-app]] · [[rooted-android-game-vm]]