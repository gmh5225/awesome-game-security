---
title: phantom-frida
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/TheQmaks__phantom-frida.md
updated: 2026-08-20
confidence: medium
---

# phantom-frida

Build system that patches upstream Frida and produces stealth `frida-server` binaries that evade common anti-instrumentation detection. Python patch scripts and name generators randomize recognizable Frida strings, symbols, and build artifacts during compilation; WSL build support and JavaScript-based tests help reproduce hardened builds. Targets mobile reverse engineers and security researchers who need anti-Frida-resistant Frida deployments against protected apps and mobile anti-cheat checks. (source: wiki/sources/descriptions/TheQmaks__phantom-frida.md)

Related patch/repack lanes include source-level automation via [[florida]] and hex-replace repacks such as [[fridare]].

## Links

- Repo: https://github.com/TheQmaks/phantom-frida (Build anti-detection Frida server from source)

## Related

[[frida]] · [[florida]] · [[fridare]] · [[florida-zygisk]] · [[antifrida]] · [[frida-detection]] · [[detect-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
