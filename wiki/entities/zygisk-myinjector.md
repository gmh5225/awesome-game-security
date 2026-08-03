---
title: Zygisk-MyInjector
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/jiqiu2022__Zygisk-MyInjector.md
updated: 2026-08-03
confidence: medium
---

# Zygisk-MyInjector

Magisk **Zygisk** injector module (C/C++ and Java) for early native load into Android app processes via the zygote specialization path. Centers on kernel-level work, asset pipelines, and modding—useful for game-security researchers and reverse engineers studying offensive injection in the cheat / [[magisk]] lane. (source: wiki/sources/descriptions/jiqiu2022__Zygisk-MyInjector.md)

Contrasts with ptrace attach injectors ([[android-ptrace-injector]]) and no-root Virtual Space paths ([[android-virtual-inject]]); complements other Zygisk modules such as [[zygisk-frida]] (Frida gadget), [[zygisk-imgui-mod-menu]] (ImGui overlay), and [[zygisk-dump-dex]] (DEX extraction) on the same [[zygisk]] hook surface.

## Links

- Repo: https://github.com/jiqiu2022/Zygisk-MyInjector (Zygisk Injector)

## Related

[[zygisk]] · [[magisk]] · [[zygisk-frida]] · [[zygisk-imgui-mod-menu]] · [[android-ptrace-injector]] · [[android-virtual-inject]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
