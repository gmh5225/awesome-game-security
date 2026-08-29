---
title: DragonHook
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mitros123__DragonHook.md
updated: 2026-08-13
confidence: medium
---

# DragonHook

Ghidra plugin that bridges static disassembly in [[ghidra]] with dynamic runtime instrumentation through [[frida]]. Exposes Ghidra database functions, comments, and cross-references to Frida agents via a localhost HTTP API, with a GUI to launch and configure Frida sessions from within Ghidra. Key capabilities include resolving dynamic indirect call targets at runtime, live-updating Ghidra with comments and xrefs, custom backtracing using Ghidra symbol names, function call tracing, string reference resolution, and experimental hardware watchpoint monitoring. Implementation is primarily Java for the Ghidra extension, with JavaScript Frida agents and a Python launcher script. Targets reverse engineers and binary analysts combining static analysis with live process introspection for malware analysis, vulnerability research, and game security work. (source: wiki/sources/descriptions/mitros123__DragonHook.md)

Ghidra-side counterpart to IDA Pro's [[frinet]] static+dynamic bridge — same Frida DBI lane, different disassembler host. Complements hook-script codegen extensions such as [[ghidra-frida-hook-gen]] (right-click Frida script emission from disassembly) when analysts need live GhidraDB sync rather than one-shot script templates.

## Links

- Repo: https://github.com/mitros123/DragonHook

## Related

[[ghidra]] · [[frida]] · [[frinet]] · [[ghidra-frida-hook-gen]] · [[ghidra-bridge]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dynamic-binary-instrumentation]]
