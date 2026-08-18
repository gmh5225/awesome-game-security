---
title: idacpp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/allthingsida__idacpp.md
updated: 2026-08-18
confidence: medium
---

# idacpp

**C++ REPL scripting plugin for IDA Pro** that embeds a **Cling/Clang 20** interpreter directly into IDA's scripting engine. Provides native access to the full **IDA SDK** and **Hex-Rays** APIs in an interactive REPL using the same types as compiled plugins (`ea_t`, `func_t*`, `cfunc_t*`)—no FFI or bindings layer. Includes a snippet editor, an output-window REPL tab, and cross-platform support for **Windows** and **macOS**. Aimed at reverse engineers who want interactive C++ scripting with direct SDK-level access inside IDA. (source: wiki/sources/descriptions/allthingsida__idacpp.md)

Scripting/runtime lane—not compiled plugin scaffolding ([[ida-sdk]], [[idasdk-collection]]) or IDAPython IDE bridges ([[idacode]]). Complements IDAPython convenience layers such as [[sark]] and [[idawilli]], agent/SQL paths such as [[idasql]] (same maintainer) and [[ida-pro-mcp]], and C++ analysis helpers such as [[ida-medigate]] / [[ida-kcpp]] (the latter is iOS kernelcache vcall recovery, not a C++ REPL).

## Links

- Repo: https://github.com/allthingsida/idacpp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-sdk]] · [[idasdk-collection]] · [[idacode]] · [[idasql]] · [[sark]] · [[idawilli]]
