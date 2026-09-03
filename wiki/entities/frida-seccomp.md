---
title: Frida-Seccomp
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Abbbbbi__Frida-Seccomp.md
updated: 2026-09-03
confidence: medium
---

# Frida-Seccomp

Android **syscall tracing and hooking** stack combining [[frida]] with **seccomp** trap handling. JavaScript instrumentation plus Python process orchestration captures **SVC** calls, stack traces, register arguments, and return values, with multi-process logging. Linker symbol inspection and a Frida **CModule** redirect and replay syscall behavior from a controlled thread context—aimed at mobile reverse engineering and game security analysis where low-level syscall visibility is needed. (source: wiki/sources/descriptions/Abbbbbi__Frida-Seccomp.md)

## Links

- Repo: https://github.com/Abbbbbi/Frida-Seccomp

## Related

[[frida]] · [[frida-smali-trace]] · [[frida-find-jni-native-methods]] · [[stackplz]] · [[mobile-re-skill]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
