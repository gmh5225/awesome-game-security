---
title: Root bypass Frida detection
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MarcosFx1323__Root-bypass-frida-detection.md
updated: 2026-11-28
confidence: medium
---

# Root bypass Frida detection

**Root-bypass-frida-detection** (MarcosFx1323/root-bypass-frida-detection) is a single Apache 2.0 **Frida JavaScript** module that evades common Android **root**, **RASP**, and **dynamic instrumentation** checks by hooking both **native libc** and the **Java/ART** runtime. (source: wiki/sources/descriptions/MarcosFx1323__Root-bypass-frida-detection.md)

## Mechanism

| Layer | Behavior |
|-------|----------|
| Native (libc) | Filter Frida-related lines from `/proc/maps` reads; spoof `getprop` / system properties; block access to typical `su` and Magisk paths; sanitize mount tables |
| Java/ART | Spoof `Build` fields; deny or redirect `su`-related shell commands from `Runtime.exec`; hide root-manager packages from `PackageManager` and Binder APIs |

Targets probes for **Magisk**, **KernelSU**, **APatch**, **SuperSU**, **LSPosed**, and **Frida** itself during integrity or anti-tamper checks common in mobile games and hardened apps.

## Workflow

Load with **Frida spawn** mode on a rooted test device or **gadget-injected** builds. Intended for mobile reverse engineers, security researchers, and practitioners studying game or app anti-cheat and root-detection logic—not a substitute for server-side attestation or Play Integrity validation.

Complements bundled pentest suites such as [[android-frida-bypass-suite]] and tracing-oriented [[root-detection-low-level]] (analysis, not bypass). Pairs with Frida-detection counter-collections such as [[frida-detection-bypass]] and [[anti-frida-bypass]] on the offensive instrumentation side of [[mobile-anti-cheat]] checks.

## Links

- Repo: https://github.com/marcosfx1323/root-bypass-frida-detection (Cheat / Frida)

## Related

[[frida]] · [[android-frida-bypass-suite]] · [[frida-mobile-kit]] · [[root-detection-low-level]] · [[frida-detection-bypass]] · [[anti-frida-bypass]] · [[ultimate-frida-bypass]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]