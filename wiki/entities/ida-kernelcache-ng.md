---
title: ida-kernelcache-ng
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/gilboz__ida_kernelcache_ng.md
updated: 2026-08-15
confidence: medium
---

# ida-kernelcache-ng

IDA plugin for analyzing iOS kernelcaches. Prefer installing as a pip package and running `cli.py`. Targets game-security researchers and reverse engineers studying offensive techniques in the cheat / IDA Plugins lane. (source: wiki/sources/descriptions/gilboz__ida_kernelcache_ng.md)

Complements other iOS kernelcache tooling such as [[binja-kc]] (Binary Ninja MachO kernelcache / KDK dSYM loader), LLM-assisted Mach-O decompilation via [[aimachdec]], C++ virtual-call resolution via [[ida-kcpp]] (leverages this plugin's class hierarchy), and PPL gate-call resolution via [[pplorer]]—this project focuses on IDA-centric kernelcache analysis workflows.

## Links

- Repo: https://github.com/gilboz/ida_kernelcache_ng

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[ida-ios-helper]] · [[ida-kcpp]] · [[aimachdec]] · [[binja-kc]]
