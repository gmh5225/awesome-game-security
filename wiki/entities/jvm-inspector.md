---
title: jvm-inspector
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/ItzMeow80__jvm-inspector.md
updated: 2026-10-28
confidence: medium
---

# jvm-inspector

Read-only **PowerShell forensics suite** for **Minecraft Java screenshare** and cheat detection on Windows. Single-file, dependency-free scanners aimed at moderators, anti-cheat staff, and reverse engineers doing JVM-focused game security reviews. (source: wiki/sources/descriptions/ItzMeow80__jvm-inspector.md)

## Main scanner (two-phase)

- **Phase 1 — live JVM audit:** inspect running `javaw.exe` / `java.exe` for `javaagent` JARs, native agents, bootclasspath tweaks, and other JVM injection flags; whitelist trusted launchers (Modrinth, Lunar, Badlion, Fabric).
- **Phase 2 — disk sweep:** scan common launcher directory layouts for ghost versions, suspicious mods, and renamed or repacked JARs (real identity from `fabric.mod.json` or manifests); match **70+ hard cheat signatures** inside class bytes with a **zero-noise** reporting policy.

## Suspicious DLL Finder

Companion script adds injected-DLL, manual-map, reflective-loader, and persistence checks when cheats bypass command-line inspection alone. (source: wiki/sources/descriptions/ItzMeow80__jvm-inspector.md)

## Links

- Repo: https://github.com/ItzMeow80/jvm-inspector

## Related

[[jaranalyzer]] · [[leaf-mod-analyzer]] · [[error-pc-check]] · [[screenshare-signatures]] · [[local-anticheat-1-8-9]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
