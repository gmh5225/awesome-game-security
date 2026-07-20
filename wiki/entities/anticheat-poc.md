---
title: anticheat-poc
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/thetuh__anticheat-poc.md
updated: 2026-07-20
confidence: medium
---

# anticheat-poc

Windows proof-of-concept anti-cheat (C/C++) that demonstrates common detection techniques: debugger presence, code-integrity checks, memory scanning for known cheat signatures, and process enumeration for suspicious tools. Serves as a reference for researchers studying anti-cheat architecture and detection methodology. (source: wiki/sources/descriptions/thetuh__anticheat-poc.md)

Listed under README **Instrumentation Callback**; complements Ring3 instrumentation samples such as [[instrumentation-callback-syscall-logger]].

## Links

- Repo: https://github.com/thetuh/anticheat-poc

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[instrumentation-callback-syscall-logger]] · [[cedetector]]
