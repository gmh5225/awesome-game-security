---
title: frida-ceserver
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__frida-ceserver.md
updated: 2026-08-08
confidence: medium
---

# frida-ceserver

Cheat Engine server implemented through [[frida]] instrumentation: reads and writes process memory on mobile and desktop targets and exposes the **ceserver network protocol** so a desktop Cheat Engine client can connect, scan, and edit memory remotely. Works on **non-rooted Android** where Frida can attach, plus iOS and desktop platforms—aimed at mobile game-security researchers who want CE workflows without a jailbreak-only ceserver stack. (source: wiki/sources/descriptions/gmh5225__frida-ceserver.md)

Complements jailbroken iOS native ceserver [[ceserver-ios]], REST scanners such as [[memory-server]], and WASM-oriented [[wasm-ceserver]] when the workflow is desktop CE over Frida attach rather than a jailbreak-only ceserver stack, REST APIs, or browser WASM targets.

## Links

- Repo: https://github.com/gmh5225/frida-ceserver

## Related

[[frida]] · [[ceserver-ios]] · [[wasm-ceserver]] · [[memory-server]] · [[frida-il2cpp-datacollector]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
