---
title: pplorer
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/cellebrite-labs__PPLorer.md
updated: 2026-08-17
confidence: medium
---

# pplorer

IDA Pro Python plugin (Cellebrite Labs) that resolves **PPL** (Page Protection Layer) gate calls in iOS and macOS kernelcaches to their actual underlying PPL functions. Automatic IDB analysis identifies and annotates PPL cross-references; **Ctrl-Shift-X** jumps between PPL call sites and target functions; context-menu actions support bidirectional PPL function ↔ call-site resolution. Uses `ida-netnode` for persistent storage. Mainly useful for iOS kernel researchers and reverse engineers tracing PPL-protected code paths in Apple kernelcaches. (source: wiki/sources/descriptions/cellebrite-labs__PPLorer.md)

Complements [[ida-kernelcache-ng]] (kernelcache load/analysis) and [[ida-kcpp]] (C++ virtual-call resolution on the same class hierarchy)—this project focuses on Apple PPL dispatch indirection, not vtable recovery or pip/cli loading alone.

## Links

- Repo: https://github.com/cellebrite-labs/PPLorer

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[ida-kernelcache-ng]] · [[ida-kcpp]] · [[ida-bridge]] · [[aimachdec]] · [[binja-kc]] · [[ida-ios-helper]]
