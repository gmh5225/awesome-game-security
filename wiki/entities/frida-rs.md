---
title: Frida-RS
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MiChongs__Frida-RS.md
updated: 2026-08-23
confidence: medium
---

# Frida-RS

**KernelSU** module that packages the official **Frida server** as an installable root module for Android. A Rust supervisor daemon (`frida-ksud`) manages server lifecycle — start, stop, restart, PID tracking, crash recovery, and logging — while a Material 3 WebUI exposes configuration and status control. (source: wiki/sources/descriptions/MiChongs__Frida-RS.md)

Builds ship multi-ABI packages (arm64-v8a, armeabi-v7a, x86_64, x86), pull and verify official Frida binaries, and default to loopback listening with token requirements for non-local exposure. Targets security researchers, reverse engineers, and authorized app debugging on rooted Android devices via [[kernelsu]], USB/ADB, or controlled TCP access. (source: wiki/sources/descriptions/MiChongs__Frida-RS.md)

Contrasts with gadget-inject modules such as [[ksu-rust-frida]] (Zygote-fork in-process agent) and stealth server repacks such as [[florida-zygisk]] — Frida-RS runs stock `frida-server` under supervised module lifecycle management.

## Links

- Repo: https://github.com/MiChongs/Frida-RS (KernelSU module wrapping official frida-server with a Rust supervisor and Material 3 WebUI)

## Related

[[frida]] · [[kernelsu]] · [[ksu-rust-frida]] · [[florida-zygisk]] · [[fridare]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
