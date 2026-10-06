---
title: LSPFRIDA
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/wzxwhxcz__LSPFRIDA.md
  - wiki/sources/README-categories.md
updated: 2026-10-06
confidence: medium
---

# LSPFRIDA

**LSPosed Android module** that embeds a **Frida GumJS** script engine (QuickJS) directly into target application processes, enabling on-device writing, execution, and debugging of Frida scripts **without `frida-server`, ADB, or a connected PC**. (source: wiki/sources/descriptions/wzxwhxcz__LSPFRIDA.md)

Pairs a statically linked GumJS runtime with **LSPlant**-powered hooking through libxposed, exposing `frida-java-bridge`-compatible APIs (`Java.perform`, `Java.use`) for method interception, parameter rewriting, and return-value override. Supports early injection before `Application.onCreate`, class-loader-aware hook registration with timeout fallbacks, hot script reload over IPC, and persistent logging from a Kotlin host app with Miuix Compose UI and a built-in syntax-highlighted script editor.

Built in Kotlin and C++ for **arm64 Android 8.0+** with Magisk-class root and LSPosed 2.1.1+. Listed in the README under **Cheat → Frida** beside server-based Frida workflows and KernelSU module injectors.

Complements [[frida-mobile-kit]], [[moabille]], [[frida-ide]], and [[ksu-rust-frida]] for mobile game-security dynamic analysis when PC-attached instrumentation is unavailable or undesirable.

## Links

- Repo: https://github.com/wzxwhxcz/LSPFRIDA

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[frida]] · [[lsposed-universal-template]] · [[mobile-anti-cheat]]
