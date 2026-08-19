---
title: florida-zygisk
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/thelok1s__florida-zygisk.md
  - wiki/sources/descriptions/Ylarod__Florida.md
updated: 2026-08-19
confidence: medium
---

# florida-zygisk

Magisk, KernelSU, and APatch root module that auto-starts **Florida** — a patched anti-detection build of `frida-server` — at boot. Ships architecture-specific Florida binaries built with Ylarod's source-level Frida patches plus Python carry-fix scripts to keep RPC obfuscation and anti-anti-Frida agent renaming working across new Frida releases. Derived from the magisk-frida template; shell service scripts start the server on a random port, expose runtime status in module metadata, and support toggling via a KernelSU Action button. Targets Android reverse engineers and game-security researchers who need persistent, harder-to-detect Frida instrumentation for dynamic analysis and bypassing common anti-Frida / anti-cheat heuristics. (source: wiki/sources/descriptions/thelok1s__florida-zygisk.md)

Upstream patch/build automation: [[florida]] (Ylarod; source-level Frida patches for anti-detection `frida-server`). (source: wiki/sources/descriptions/Ylarod__Florida.md) Adjacent stealth Frida tooling includes [[fridare]] (string/symbol hex-replace repacks). Framework home: [[magisk]] · [[kernelsu]] · [[zygisk]].

## Links

- Repo: https://github.com/thelok1s/florida-zygisk (Magisk/Zygisk module that auto-starts Florida anti-detection frida-server on boot)

## Related

[[frida]] · [[florida]] · [[fridare]] · [[magisk]] · [[kernelsu]] · [[zygisk]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[antifrida]] · [[frida-detection]]
