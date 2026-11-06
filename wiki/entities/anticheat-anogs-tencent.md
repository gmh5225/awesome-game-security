---
title: AntiCheat Anogs Tencent
kind: entity
topics: [anti-cheat, mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/arx-oioi__-AntiCheat-Anogs-Tencent-.md
updated: 2026-11-06
confidence: medium
---

# AntiCheat Anogs Tencent

Documentation and analysis notes on Tencent’s client-side **ANOGS** (native `libanogs` / anti-abuse) protection: how the native library sits in the stack next to integrity checks and server-side adjudication. Described behaviors include memory-map scanning, hook and debugger detection, syscall monitoring, anti-debug and anti-dump paths, and reactions such as process termination, fake crashes, or delayed reporting. Materials mix Thai and English and reference Android JNI, background monitor threads, and state-machine style checks; some **C#** appears tied to specific game builds as supplemental inspection or decryption-oriented tooling. (source: wiki/sources/descriptions/arx-oioi__-AntiCheat-Anogs-Tencent-.md)

Listed in the README under **Reverse-engineering** as notes on Tencent mobile protection (`libanogs`): detection loops, anti-debug/inject/dump, and reaction paths.

Complements [[ff-ace-anticheat-analysis]] and [[ida-plugin-strings-decryptor-anogs]] on the [[mobile-anti-cheat]] concept page.

## Links

- Repo: https://github.com/arx-oioi/-AntiCheat-Anogs-Tencent-

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[ff-ace-anticheat-analysis]] · [[ida-plugin-strings-decryptor-anogs]] · [[research-rigor]]
