---
title: Nodejs Tracer
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/CheckPointSW__Nodejs-Tracer.md
updated: 2026-08-28
confidence: medium
---

# Nodejs Tracer

Lightweight **Node.js runtime tracing script** from CheckPoint Software that instruments core module calls at runtime. Logs API usage, can spoof selected behaviors to bypass anti-analysis checks, and preserves artifacts such as files written by the target process. Launched through Node's preload mechanism for easy attachment to heavily obfuscated scripts without major setup. Aimed at malware analysts and security researchers performing dynamic JavaScript behavior analysis. (source: wiki/sources/descriptions/CheckPointSW__Nodejs-Tracer.md)

Complements obfuscation tooling such as [[javascript-obfuscator]] on the analyst side — trace and deobfuscate what protected Node.js or browser-game scripts do at runtime rather than statically reversing source transforms. Pairs with CheckPoint's Windows anti-debug exploration harness [[showstopper]] in malware-analysis workflows.

## Links

- Repo: https://github.com/CheckPointSW/Nodejs-Tracer

## Related

[[overviews/reverse-engineering]] · [[javascript-obfuscator]] · [[js-debugger-bypass-script]] · [[showstopper]] · [[de4py]]
