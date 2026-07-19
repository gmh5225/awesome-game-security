---
title: VMUnprotect
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/void-stack__VMUnprotect.md
updated: 2026-07-19
confidence: medium
---

# VMUnprotect

.NET (C#) tool that dynamically analyzes and instruments methods virtualized by VMProtect, focusing on method administration rather than full code recovery. Uses Harmony to hook and observe VMProtect runtime behavior: trace invokes inside virtualized methods and manipulate parameters / return values. Bypasses common VMProtect anti-debug checks (`NtQueryInformationProcess`, `Debugger.IsLogging`, `Debugger.IsAttached`); targets VMProtect 3.6.0 and several earlier versions under typical memory / import / resource protections. Aimed at REs studying VMProtect-protected .NET assemblies who need runtime visibility into virtualized calls. (source: wiki/sources/descriptions/void-stack__VMUnprotect.md)

Companion surface to other Cheat → Fix VMP research: runtime Harmony instrumentation of .NET VMP methods, vs symbolic-exec recovery ([[novmpy]]) or VTIL compile demos ([[vmdevirt-vtil]]). Dump/unpack sibling: [[vmunprotect-dumper]].

## Links

- Repo: https://github.com/void-stack/VMUnprotect

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmunprotect-dumper]] · [[novmpy]] · [[vmdevirt-vtil]] · [[deobf]]

