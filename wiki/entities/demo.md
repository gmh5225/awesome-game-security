---
title: Demo
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/JingMatrix__Demo.md
updated: 2026-08-24
confidence: medium
---

# Demo

Android demo application from **JingMatrix** for detecting **user-space library injection** at runtime, with emphasis on **Zygisk-style** early native loads. Combines Kotlin Android UI with native C++ components built through CMake. Detection strategies include **soinfo linked-list integrity checks**, **virtual memory map inspection** (`/proc/self/maps`-style anomalies), and **module unload counter monitoring**. Primary use case is mobile anti-cheat and security research focused on identifying injection techniques rather than production deployment. (source: wiki/sources/descriptions/JingMatrix__Demo.md)

Complements ptrace-based Zygisk specialization probes such as [[detect-zygisk]] and broader instrumentation checks in [[mobile-anti-cheat]]—studying the defender side of early native injection documented under [[zygisk]] (DEX dump, ImGui menus, Frida gadget injectors).

## Links

- Repo: https://github.com/JingMatrix/Demo

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[zygisk]] · [[detect-zygisk]] · [[memdetection]] · [[magisk-detection]] · [[detection]]
