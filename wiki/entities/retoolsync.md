---
title: REToolSync
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__REToolSync.md
updated: 2026-08-22
confidence: medium
---

# REToolSync

Synchronization framework for collaborative reverse engineering that keeps multiple analysis and debugging tools aligned on the same memory address and selection. A central Python Tornado WebSocket server coordinates plugins for IDA Pro, Binary Ninja, x64dbg, WinDbg, and a VS Code extension; Ctrl+click hex addresses in the terminal to jump every connected tool at once. Clients broadcast cursor and selection updates and respond to shared navigation commands such as goto, so analysts can move seamlessly between static disassembly, live debugging, and scripting environments. (source: wiki/sources/descriptions/mrexodia__REToolSync.md)

Complements Git-backed annotation sync via [[binsync]] and real-time IDA IDB co-editing via [[idarling]]—REToolSync targets live cursor/goto navigation across disassemblers and debuggers rather than shared names, comments, or types. Peers with IDA-only partial IDB sync via [[labsync]] and debugger-side automation such as [[x64dbg-mcp]] / [[ida-pro-mcp]].

## Links

- Repo: https://github.com/mrexodia/retoolsync

## Related

[[overviews/reverse-engineering]] · [[binsync]] · [[idarling]] · [[labsync]] · [[x64dbg]] · [[ida-pro-mcp]] · [[binary-ninja-mcp]]
