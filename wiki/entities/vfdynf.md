---
title: vfdynf
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/jxy-s__vfdynf.md
updated: 2026-08-20
confidence: medium
---

# vfdynf

**vfdynf** (jxy-s) is a Windows **Application Verifier** provider implementing **Dynamic Fault Injection (DynFault)** — a stack-hash-based alternative to the built-in Low Resource Simulation (LowRes) tests. Written in C/C++, it hooks wait, heap, virtual memory, registry, file, event, section, and OLE APIs, and can optionally fuzz registry, file, section mapping, and network read buffers to expose logic errors and time-of-check-time-of-use (TOCTOU) vulnerabilities. Unlike randomized LowRes, DynFault tracks unique call stacks for improved coverage and supports PCRE2 regular-expression exclusions to omit specific code paths (e.g. MSVC debug iterator allocations). Integrates via `vfdynf.dll` for configurable Windows fault injection, robustness testing, and vulnerability discovery. (source: wiki/sources/descriptions/jxy-s__vfdynf.md)

Complements coverage-guided fuzzers such as [[winafl]] and IOCTL repeaters such as [[ioctlpus]] in the Windows fault-injection / API-fuzzing lane; same author as process-obfuscation PoC [[herpaderping]].

## Links

- Repo: https://github.com/jxy-s/vfdynf

## Related

[[winafl]] · [[fuzzable]] · [[ioctlpus]] · [[cfb]] · [[herpaderping]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
