---
title: VirtualApp
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ServenScorpion__VirtualApp.md
updated: 2026-08-21
confidence: medium
---

# VirtualApp

**Android application virtualization framework** for running and managing **cloned apps** in an **isolated container**. Primarily **Java** with Android XML resources, plus native **C/C++** for low-level hooks and runtime interception. Integrates **Xposed** compatibility and **SandHook**-based instrumentation, with virtual package, process, and component management. Aimed at mobile reverse engineering, app behavior analysis, and multi-instance sandbox use cases. (source: wiki/sources/descriptions/ServenScorpion__VirtualApp.md)

Sits in the app-cloning / sandbox lane beside no-root Virtual Space inject via [[android-virtual-inject]]; complements Xposed module scaffolding ([[xposed-module-kit]]) and ART Java hooks ([[canyie-pine]]) when analysts need isolated duplicate-app environments rather than attach-time DBI alone.

## Links

- Repo: https://github.com/ServenScorpion/VirtualApp

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[android-virtual-inject]] · [[xposed-module-kit]] · [[canyie-pine]] · [[frida]] · [[mobile-anti-cheat]]
