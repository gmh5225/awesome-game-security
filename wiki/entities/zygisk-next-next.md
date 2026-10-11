---
title: Zygisk Next Next
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/VeryBaaad__ZygiskNextNext.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: high
---

# Zygisk Next Next

**Zygisk Next Next** (VeryBaaad) is an open-source **Magisk / KernelSU / APatch** module that reimplements the **ZygiskNext module API** from scratch so third-party modules load without relying on the closed-source ZygiskNext runtime. (source: wiki/sources/descriptions/VeryBaaad__ZygiskNextNext.md)

## Architecture

A native C++ loader injected into target processes loads matching modules and exposes **inline and PLT hooking** through backends such as Dobby, ShadowHook, rv64hook, LSPlt, ByteHook, xHook, and PLTI, plus **HyperOS Runtime** support for advanced injection scenarios. (source: wiki/sources/descriptions/VeryBaaad__ZygiskNextNext.md)

A Rust injector daemon handles process injection and control (ptrace-based operations, optional eBPF helpers). Gradle packages builds for Android 5 through current releases. (source: wiki/sources/descriptions/VeryBaaad__ZygiskNextNext.md)

## Module API

Targets the **ZygiskNext** module contract so existing ZygiskNext-style `.so` modules can load against this open runtime instead of the upstream closed-source ZygiskNext binary—useful when auditing hook timing, backend selection, or injection control paths. (source: wiki/sources/descriptions/VeryBaaad__ZygiskNextNext.md)

## Positioning

Targets rooted Android developers and researchers building or studying ZygiskNext-style hook modules—game modding, runtime instrumentation, and mobile RE—listed under README **Cheat / Magisk**. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/VeryBaaad/ZygiskNextNext

## Related

[[concepts/zygisk]] · [[rezygisk]] · [[jerrymanager]] · [[magisk-hub]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
