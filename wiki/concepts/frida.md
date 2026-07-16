---
title: Frida
kind: concept
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/reverse-engineering.md
updated: 2026-07-16
confidence: high
---

# Frida

Cross-platform dynamic instrumentation toolkit widely used on Android/iOS (and desktop) to attach/spawn processes, intercept native/Java/ObjC APIs, and script runtime behavior without static patching. (source: wiki/sources/skills/mobile-security.md)

## Game-security uses

Hook game/[[il2cpp]] natives, bypass SSL pinning, probe root/jailbreak checks, trace anti-cheat detectors. Mobile ACs often ship Frida/ Magisk detection; hide stacks (DenyList/Shamiko, KernelSU isolation) appear in the same research space.

## Related

[[il2cpp]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
