---
title: frida-il2cpp-datacollector
kind: entity
topics: [game-engine, mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__frida-il2cpp-datacollector.md
updated: 2026-08-08
confidence: medium
---

# frida-il2cpp-datacollector

Frida script for collecting Unity [[il2cpp]] runtime data on **Android and iOS**: hooks the IL2CPP runtime to enumerate classes, dump method signatures, extract field offsets, and gather type metadata at attach time. Ports Cheat Engine's MonoDataCollector workflow to mobile Frida instrumentation; output supports IL2CPP SDK generation for game hacking research. (source: wiki/sources/descriptions/gmh5225__frida-il2cpp-datacollector.md)

Complements static APK dumpers such as [[il2cppdumper]] and live bridges like [[frida-il2cpp-bridge]] when the goal is CE-style runtime metadata harvesting without a desktop Cheat Engine client.

## Links

- Repo: https://github.com/gmh5225/frida-il2cpp-datacollector

## Related

[[frida]] · [[il2cpp]] · [[frida-il2cpp-bridge]] · [[il2cpp-runtime-dumper]] · [[il2cppdumper]] · [[overviews/mobile-security]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
