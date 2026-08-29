---
title: ghidra-frida-hook-gen
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/CENSUS__ghidra-frida-hook-gen.md
updated: 2026-08-29
confidence: medium
---

# ghidra-frida-hook-gen

**ghidra-frida-hook-gen** (CENSUS) is a **Java Ghidra extension** that **generates Frida hook scripts directly from disassembly context**. Right-click actions in Ghidra emit **full hook scripts**, **reusable snippets**, and **advanced hook configuration** without hand-writing boilerplate from raw addresses. The plugin supports **function-level hooks** and **arbitrary address hooks** to accelerate dynamic analysis setup. It targets reverse engineers and security researchers who bridge **static analysis in [[ghidra]]** with **runtime instrumentation in [[frida]]**. (source: wiki/sources/descriptions/CENSUS__ghidra-frida-hook-gen.md)

Complements live static+dynamic bridge plugins such as [[dragonhook]] and IDA-side counterparts such as [[frinet]] — this tool focuses on **script codegen from disassembly** rather than bidirectional GhidraDB sync during an active Frida session.

## Links

- Repo: https://github.com/CENSUS/ghidra-frida-hook-gen

## Related

[[ghidra]] · [[frida]] · [[dragonhook]] · [[frinet]] · [[frinja]] · [[overviews/reverse-engineering]] · [[dynamic-binary-instrumentation]]
