---
title: fallguys-frida-modmenu
kind: entity
topics: [mobile-security, game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/repinek__fallguys-frida-modmenu.md
updated: 2026-08-15
confidence: medium
---

# fallguys-frida-modmenu

**fallguys-frida-modmenu** is an **Android mod menu** for the **Fall Guys mobile** title. It injects a configurable overlay at runtime via **Frida** dynamic instrumentation, written primarily in **TypeScript**. Gameplay hooks go through Unity **[[il2cpp]]** via **[[frida-il2cpp-bridge]]**; the overlay UI is built with **frida-java-menu** (Java-based). APK patching uses **Objection** and **APKEditor**. (source: wiki/sources/descriptions/repinek__fallguys-frida-modmenu.md)

Modular toggles include movement manipulation, round-specific helpers, teleports, ban bypass, platform spoofing, and network/analytics debugging. Targets reverse engineers and mobile game-security researchers studying IL2CPP hooking, anti-cheat bypass, and Android game modification.

Contrasts with desktop Fall Guys stacks such as [[fall-guys-sharp]] (C# IL2CPP managed injection) and [[fall-guys]] (kernel external memory manipulation on PC).

## Links

- Repo: https://github.com/repinek/fallguys-frida-modmenu

## Related

[[frida]] · [[frida-il2cpp-bridge]] · [[il2cpp]] · [[android-il2cpp-modspeed]] · [[fall-guys-sharp]] · [[fall-guys]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
