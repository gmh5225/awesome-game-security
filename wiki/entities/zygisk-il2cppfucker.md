---
title: Zygisk-Il2CppFucker
kind: entity
topics: [game-engine, mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Darlenepurpleblack444__Zygisk-Il2CppFucker.md
updated: 2026-08-30
confidence: medium
---

# Zygisk-Il2CppFucker

**Zygisk Magisk module** that injects into Android Unity [[il2cpp]] game processes and turns the running title into a scriptable in-process reverse-engineering engine (Darlenepurpleblack444). Forked from [[zygisk-il2cppdumper]], it extends runtime metadata dumping with live memory manipulation, method invocation, Lua scripting, and overlay output — without external attach tools. README lane: live IL2CPP metadata dumping, in-process memory editing, method invocation, and Lua scripting on Android Unity games. (source: wiki/sources/descriptions/Darlenepurpleblack444__Zygisk-Il2CppFucker.md)

## Capabilities

- Dump IL2CPP metadata to `dump.cs`, including [[hybridclr]] hot-update classes
- Resolve classes, fields, and methods by name; scan instances in memory
- Read/write process memory and invoke game methods via `il2cpp_runtime_invoke`
- Embedded **Lua 5.4** with hot-reloadable `init.lua` and `run.lua` scripts
- File-based `.cmd` command channel and overlay drawing for live analysis

Built primarily in C++ with Gradle-based Android module packaging and optional Python helpers. Targets security researchers and reverse engineers who need to inspect and manipulate protected mobile game logic from inside the target process.

## Links

- Repo: https://github.com/Darlenepurpleblack444/Zygisk-Il2CppFucker

## Related

[[il2cpp]] · [[zygisk]] · [[zygisk-il2cppdumper]] · [[hybridclr]] · [[frida-il2cpp-bridge]] · [[bnm-android]] · [[il2cppdumpdroidgui]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
