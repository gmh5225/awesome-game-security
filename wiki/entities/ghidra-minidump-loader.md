---
title: ghidra-minidump-loader
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Rantanen__ghidra-minidump-loader.md
updated: 2026-08-21
confidence: medium
---

# ghidra-minidump-loader

Ghidra extension that loads Windows minidump (`.dmp`) files as analyzable programs inside Ghidra. Maps dump modules to their runtime addresses, imports private memory regions and thread stacks, and stores thread metadata for analysis. Built primarily in Java with Gradle; extends PE loading internals and adds a thread-view workflow with stack-walking support. Aimed at reverse engineers and incident responders inspecting crash dumps or post-mortem malware samples without leaving Ghidra. (source: wiki/sources/descriptions/Rantanen__ghidra-minidump-loader.md)

Bridges programmatic minidump parsers such as [[minidump]] / [[minidumpreader]] / [[libmdmp]] and Unicorn replay harnesses such as [[dumpulator]] with Ghidra's decompiler, xref, and scripting ecosystem. Complements other Ghidra loaders/plugins such as [[gba-ghidra-loader]] and [[ghidra-nativeaot]].

## Links

- Repo: https://github.com/Rantanen/ghidra-minidump-loader [Windows Minidump loader for Ghidra]

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ghidra]] · [[minidump]] · [[minidumpreader]] · [[libmdmp]] · [[dumpulator]] · [[ephemera]] · [[mcp-windbg]]
