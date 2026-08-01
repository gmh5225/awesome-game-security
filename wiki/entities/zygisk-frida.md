---
title: zygisk-frida
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/lico-n__ZygiskFrida.md
updated: 2026-08-01
confidence: medium
---

# zygisk-frida

Magisk **Zygisk** module that injects the **Frida gadget** into Android application processes. Zygisk runs module code during app specialization so the gadget loads early in every target process—useful for game-security researchers and reverse engineers working in the cheat / Magisk lane who need in-process dynamic instrumentation without external `frida-server` attach. (source: wiki/sources/descriptions/lico-n__ZygiskFrida.md)

Contrasts with boot-persistent server modules such as [[florida-zygisk]] (Florida anti-detection `frida-server`). Framework home: [[magisk]] · [[zygisk]] · [[frida]].

## Links

- Repo: https://github.com/lico-n/ZygiskFrida (Injects Frida gadget using Zygisk)

## Related

[[frida]] · [[zygisk]] · [[magisk]] · [[florida-zygisk]] · [[fridare]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[antifrida]] · [[frida-detection]]
