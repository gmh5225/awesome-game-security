---
title: Pine (canyie)
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/canyie__pine.md
updated: 2026-08-17
confidence: medium
---

# Pine (canyie)

**Pine** is a dynamic **Java method hooking** framework for **Android** targeting the **ART** runtime. It intercepts Java methods at runtime by modifying ART internal method entry points, supporting **inline hooks** and **method replacement** without requiring root. Works on **Android 7.0+** and exposes an **Xposed-compatible API** for before/after method hooks. Aimed at Android reverse engineers and app modifiers who need runtime Java interception without the full Xposed framework. (source: wiki/sources/descriptions/canyie__pine.md)

Complements Xposed/LSPosed module tooling such as [[xposed-module-kit]] and attach-based Java intercept via [[frida]]; distinct from the unrelated neural-network aim/trigger project [[pine]] (petercunha).

## Links

- Repo: https://github.com/canyie/pine

## Related

[[xposed-module-kit]] · [[locusmimic]] · [[frida]] · [[adbi]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
