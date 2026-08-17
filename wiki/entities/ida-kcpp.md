---
title: ida-kcpp
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/cellebrite-labs__ida_kcpp.md
updated: 2026-08-17
confidence: medium
---

# ida-kcpp

IDAPython plugin for reverse engineering iOS kernelcaches that maps C++ virtual method calls to their actual implementations. Leverages [[ida-kernelcache-ng]]'s class hierarchy reconstruction to synchronize binary functions with original virtual methods—enabling double-click navigation on C++ virtual calls and cross-reference tracking. Inspired by [[ida-medigate]]; exploits the unique structure of iOS kernelcaches for vtable-heavy C++ analysis. Mainly useful for iOS kernel security researchers studying virtual dispatch patterns and vtable-based code flow in Apple kernelcaches. (source: wiki/sources/descriptions/cellebrite-labs__ida_kcpp.md)

Scoped as iOS kernelcache C++ vcall recovery—not general GCC RTTI hierarchy tooling ([[ida-medigate]]) or pip/cli kernelcache loading alone ([[ida-kernelcache-ng]]). Complements [[pplorer]] (PPL gate-call resolution in the same kernelcache IDBs), [[binja-kc]] (Binary Ninja MachO kernelcache / KDK dSYM loader), and [[aimachdec]] (LLM ARM64 Mach-O decompilation).

## Links

- Repo: https://github.com/cellebrite-labs/ida_kcpp

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[ida-kernelcache-ng]] · [[ida-medigate]] · [[aimachdec]] · [[binja-kc]] · [[ida-ios-helper]]
