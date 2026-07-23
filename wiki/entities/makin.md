---
title: makin
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/secrary__makin.md
updated: 2026-07-23
confidence: medium
---

# makin

Windows anti-debugging / anti-VM detection probe written in C. Exercises **30+** debugger indicators and prints console pass/fail per check: Win32 APIs (`IsDebuggerPresent`, `CheckRemoteDebuggerPresent`), `NtQueryInformationProcess` flags, PEB fields, hardware breakpoints, timing attacks, TLS callbacks, and related anti-debug signals. Aimed at researchers studying technique coverage and effectiveness rather than shipping as a production AC component. (source: wiki/sources/descriptions/secrary__makin.md)

Complements Anti Debugging catalogs and anti-analysis hide/bypass tooling such as ScyllaHide-class plugins, [[steam-anti-anti-debug]], and VE-detection demos like [[anticuckoo]].

## Links

- Repo: https://github.com/secrary/makin

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[steam-anti-anti-debug]] · [[anticuckoo]] · [[cedetector]] · [[x64dbg]]
