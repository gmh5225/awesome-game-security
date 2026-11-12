---
title: inject-hooks-android-rs
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/strazzere__inject-hooks-android-rs.md
  - wiki/sources/README-categories.md
updated: 2026-11-12
confidence: medium
---

# inject-hooks-android-rs

Rust stack for **remote shared-library injection** into live Android processes and **runtime API hooking** from native code. Bundles a TinyInjector-style injector (ptrace attach, remote memory map, `dlopen` in target PID) with an in-process hook library supporting **GOT rewrite** and **inline trampoline** patches on 32- and 64-bit ARM. Hook modules are discovered automatically at build time; a Makefile cross-compiles for Android ABIs and supports adb push of test binaries. Aimed at mobile reverse engineering and security research, including instrumentation of games and other native Android apps. (source: wiki/sources/descriptions/strazzere__inject-hooks-android-rs.md) (source: wiki/sources/README-categories.md)

Listed under Cheat / **injection:android**.

## Components

- **Injector** — ptrace-based attach; maps memory and calls `dlopen` in a target process without APK repack.
- **Hook library** — GOT interception or inline trampolines once the payload `.so` is loaded in-process.

## Links

- Repo: https://github.com/strazzere/inject-hooks-android-rs

## Related

[[android-ptrace-injector]] · [[linjector-rs]] · [[android-dll-injector]] · [[and64-inline-hook]] · [[adbi]] · [[frida]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
