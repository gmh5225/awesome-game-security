---
title: inline-syscall
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__inline-syscall.md
updated: 2026-08-08
confidence: medium
---

# inline-syscall

Simple C++ direct syscall wrapper with compatibility for x86 and x64 user-mode programs. Curated for anti-cheat engineers and defensive security researchers in the Anti Cheat → Compile Time lane — lightweight invocation stubs rather than full SSN table tooling. (source: wiki/sources/descriptions/gmh5225__inline-syscall.md)

Complements modular header-only libraries such as [[syscalls-cpp]], direct-call helpers such as [[higu-ntcall]], and SSN extraction via [[ntsleuth]]; defensive analysts pair invocation samples with syscall-origin checks such as [[syscall-detect]] and return-path telemetry such as [[instrumentation-callback-syscall-logger]].

## Links

- Repo: https://github.com/gmh5225/inline-syscall

## Related

[[syscalls-cpp]] · [[higu-ntcall]] · [[ntsleuth]] · [[syscall-detect]] · [[instrumentation-callback-syscall-logger]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
