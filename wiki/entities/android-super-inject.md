---
title: AndroidSuperInject
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/cs1ime__AndroidSuperInject.md
updated: 2026-08-16
confidence: medium
---

# AndroidSuperInject

Android native code injection framework in the Cheat / injection:android lane. Injects shared libraries into running application processes via **ptrace-based attach** or **Zygote hooking**, loading custom `.so` payloads for runtime instrumentation and modding. README targets injection into **SELinux-protected system service processes**; some configurations work without root. (source: wiki/sources/descriptions/cs1ime__AndroidSuperInject.md)

Contrasts with no-root Virtual Space inject via [[android-virtual-inject]] and ptrace-only attach via [[android-ptrace-injector]]; complements Zygote-injection game-mod samples such as [[android-mod-games-by-inject-zygote]] and ptrace-free Rust inject research such as [[linjector-rs]].

## Links

- Repo: https://github.com/cs1ime/AndroidSuperInject

## Related

[[android-ptrace-injector]] · [[android-mod-games-by-inject-zygote]] · [[android-dll-injector]] · [[linjector-rs]] · [[android-virtual-inject]] · [[zygisk-myinjector]] · [[frida]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
