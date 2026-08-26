---
title: ThreadJect
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/D4stiny__ThreadJect.md
updated: 2026-08-26
confidence: medium
---

# ThreadJect

Proof-of-concept **manual DLL injector** that **hijacks an existing thread** in a target Windows process (D4stiny). The implementation validates and maps the DLL payload, prepares loader metadata, patches shellcode with runtime addresses, and redirects thread execution to complete injection. Written in **C++** with **Visual Studio** project support, it emphasizes low-level control over the full injection chain. Primary use: process-injection research and building detection test cases for endpoint security studies. (source: wiki/sources/descriptions/D4stiny__ThreadJect.md)

README lane: **Injection Testing** — manual thread-hijack DLL load study sample.

Complements minimal thread-hijack PoCs such as [[thread-hijacking-injector]], educational multi-method samples such as [[inject-all-the-things]] and [[windows-dll-injector]], and broader corpora such as [[windows-process-injection]] and [[process-injection-techniques]].

## Links

- Repo: https://github.com/D4stiny/ThreadJect

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[thread-hijacking-injector]] · [[inject-all-the-things]] · [[windows-dll-injector]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[injectors]]
