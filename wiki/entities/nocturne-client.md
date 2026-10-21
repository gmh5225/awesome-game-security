---
title: Nocturne Client
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/liuyyx__nocturne-client.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: high
---

# Nocturne Client

**nocturne-client** ([liuyyx/nocturne-client](https://github.com/liuyyx/nocturne-client)) is a **JVM attach injector** and in-process **Java agent** packaged as one Gradle-built JAR for **Minecraft Java 1.8.9–26.3**. (source: wiki/sources/descriptions/liuyyx__nocturne-client.md)

## Version bridging

Per-release mapping tables cover vanilla, Fabric, Forge, and NeoForge runtime names while gameplay modules stay on **Mojmap-style** identifiers instead of a traditional mod entry point. Python utilities generate and verify mapping JSON.

## Hooks and modules

**ASM** bytecode transformers drive LWJGL frame hooks, draw callbacks, and input blocking. The client layer exposes cheat-style ESP, tracers, storage-search overlays, and a ClickGUI rendered through LWJGL2 fixed pipeline, modern GL core, or the game GUI extractor on newer stacks.

## Research use

Relevant to anti-cheat and RE work on **JVM attach**, dynamic instrumentation, obfuscation bridging, and how injected clients hook rendering and input—not a sanctioned multiplayer tool.

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[il2cpp]] · [[vortex-client]] · [[jsaclient]]

## Links

- Repo: https://github.com/liuyyx/nocturne-client
