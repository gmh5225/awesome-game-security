---
title: Stoic
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/block__stoic.md
updated: 2026-08-17
confidence: medium
---

# Stoic

**Stoic** (Block) is a developer tool that injects code into any **debuggable Android process** (API 26+) via **JVMTI** without modifying the target APK. It supports live **Java/Kotlin method hooking**, **heap object inspection**, and **internal API calls** through a Kotlin/Java plugin system, with first-attach latency under three seconds and sub-second subsequent connections. Useful for Android reverse engineers and game-security researchers who need attach-time managed instrumentation on debuggable builds without repackaging. (source: wiki/sources/descriptions/block__stoic.md)

Requires a **debuggable** process (debug builds or `android:debuggable`); not a root/Zygote inject path. Complements ART inline hooking via [[canyie-pine]], attach-based [[frida]], and Xposed/LSPosed module tooling such as [[xposed-module-kit]]. Desktop JVM attach via JVMTI appears separately in clients such as [[phantom-client]].

## Links

- Repo: https://github.com/block/stoic

## Related

[[canyie-pine]] · [[frida]] · [[xposed-module-kit]] · [[lamda]] · [[mobile-re-skill]] · [[phantom-client]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
