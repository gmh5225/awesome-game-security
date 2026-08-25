---
title: magisk-hluda
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Exo1i__MagiskHluda.md
updated: 2026-08-25
confidence: medium
---

# magisk-hluda

Magisk module that auto-starts a **stealth-modified `frida-server`** at Android boot. Ships Magisk module scripts for install and service lifecycle management, a small C++ helper for update metadata and server downloads, and an HTML/JavaScript WebUI for start/stop control, status display, and custom launch parameters. Targets mobile reverse engineering and security testing workflows that need persistent instrumentation with reduced Frida detection surface. (source: wiki/sources/descriptions/Exo1i__MagiskHluda.md)

Contrasts with Florida-patched boot modules such as [[florida-zygisk]] and stock-server supervisors such as [[frida-rs]]. Framework home: [[magisk]] · [[frida]].

## Links

- Repo: https://github.com/Exo1i/MagiskHluda (Run a more undetectable frida server on boot using magisk)

## Related

[[frida]] · [[magisk]] · [[florida-zygisk]] · [[frida-rs]] · [[fridare]] · [[phantom-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[antifrida]] · [[frida-detection]]
