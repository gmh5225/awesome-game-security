---
title: Zygisk-Il2CppDumper
kind: entity
topics: [game-engine, mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Perfare__Zygisk-Il2CppDumper.md
updated: 2026-08-22
confidence: medium
---

# Zygisk-Il2CppDumper

**Android runtime IL2CPP dumping module** via Magisk [[zygisk]] (Perfare). Native C/C++ with Android build tooling injects into target apps and collects runtime metadata that may be encrypted, obfuscated, or packed in static `libil2cpp.so` / metadata files. Post-load dumping can bypass certain mobile Unity protection layers that block static IL2CPPDumper workflows. README lane `[Il2Cpp Dump for Android Platform]`. (source: wiki/sources/descriptions/Perfare__Zygisk-Il2CppDumper.md)

Complements static Android dumpers such as [[il2cppdumper]], on-device GUI tooling such as [[il2cppdumpdroidgui]], and live Frida harvesters such as [[frida-il2cpp-bridge]] on the mobile Unity explorer lane.

## Links

- Repo: https://github.com/Perfare/Zygisk-Il2CppDumper

## Related

[[il2cpp]] · [[zygisk]] · [[il2cppdumper]] · [[il2cppdumpdroidgui]] · [[frida-il2cpp-bridge]] · [[rezygisk]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
