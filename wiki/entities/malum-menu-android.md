---
title: malum-menu-android
kind: entity
topics: [mobile-security, game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/astra1dev__MalumMenu-Android.md
updated: 2026-08-18
confidence: medium
---

# malum-menu-android

**malum-menu-android** is an **Among Us Android** cheat and mod menu that overlays a floating UI on the game. Written mainly in **TypeScript**, it uses **Frida** with **[[frida-il2cpp-bridge]]** to hook Unity **[[il2cpp]]** at runtime and **frida-java-menu** for the on-screen interface. Features include movement cheats (NoClip, speedhack), ESP options (no shadows), ship controls (meetings, sabotages, vents), cosmetics unlocks, and other utilities. The menu is packaged by embedding **Frida gadget** into the APK with **objection** so it can run **without root** on real Android devices. (source: wiki/sources/descriptions/astra1dev__MalumMenu-Android.md)

Aimed at game modding, mobile reverse engineering, and experimenting with Among Us client-side behavior on Android. Same architectural pattern as [[fallguys-frida-modmenu]] (TypeScript + frida-il2cpp-bridge + frida-java-menu + Objection gadget injection).

## Links

- Repo: https://github.com/astra1dev/MalumMenu-Android

## Related

[[frida]] · [[frida-il2cpp-bridge]] · [[il2cpp]] · [[fallguys-frida-modmenu]] · [[apk-sh]] · [[wellsanticheat]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
