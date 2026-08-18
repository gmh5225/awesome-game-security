---
title: comida
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/airbus-cert__comida.md
updated: 2026-08-18
confidence: medium
---

# comida

**IDA Pro plugin for Windows COM-centric static analysis.** Scans binaries for known COM GUID references and correlates them with registry metadata to identify related classes and interfaces. With Hex-Rays, performs type inference around `CoCreateInstance`, `CoGetCallContext`, and `QueryInterface` to clean up decompiled output. Targets malware analysts and reverse engineers who need faster COM triage and deeper Windows internals visibility in protected game clients and AC components. (source: wiki/sources/descriptions/airbus-cert__comida.md)

Complements live COM tracing via WinDbg extension [[comon]] (factory / `QueryInterface` paths during attach) and static C++ class tooling such as [[classy]] — focused on GUID/registry correlation and Hex-Rays COM API typing rather than runtime breakpoints or vtable layout management. Pairs with fellow Airbus tooling [[autoresolv]] for ELF import resolution on Linux targets.

## Links

- Repo: https://github.com/airbus-cert/comida (README tag: An IDA Plugin that help analyzing module that use COM)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[comon]] · [[classy]] · [[autoresolv]] · [[cognitor]]
