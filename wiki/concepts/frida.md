---
title: Frida
kind: concept
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/yring-me__ts-ue4dumper.md
updated: 2026-07-17
confidence: high
---

# Frida

Cross-platform dynamic instrumentation toolkit widely used on Android/iOS (and desktop) to attach/spawn processes, intercept native/Java/ObjC APIs, and script runtime behavior without static patching. (source: wiki/sources/skills/mobile-security.md)

## Game-security uses

Hook game/[[il2cpp]] natives, bypass SSL pinning, probe root/jailbreak checks, trace anti-cheat detectors. Mobile ACs often ship Frida/ Magisk detection; hide stacks (DenyList/Shamiko, KernelSU isolation) appear in the same research space. Unreal explorers also script Frida dumpers in TypeScript (e.g. [[ts-ue4dumper]], with C++ offset helpers). (source: wiki/sources/descriptions/yring-me__ts-ue4dumper.md)

## Related

[[il2cpp]] · [[ts-ue4dumper]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
