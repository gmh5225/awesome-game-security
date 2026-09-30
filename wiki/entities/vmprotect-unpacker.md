---
title: vmprotect-unpacker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/datcathuh__vmprotect-unpacker.md
  - wiki/sources/README-categories.md
updated: 2026-09-30
confidence: medium
---

# vmprotect-unpacker

Windows **C++ dynamic unpacker and dumper** for VMProtect-protected PE executables and DLLs (WIP; tested on VMProtect 3.8.4). Injects an unpacker DLL into the target process, waits for VMProtect to finish load-time unpacking, then snapshots decrypted memory and reconstructs the image including import-table repair. Also includes VMProtect bytecode detection and devirtualization support that can emit disassembly of recovered virtualized code, plus anti-debug hooks to reduce interference from VMProtect protection checks. Supports launching protected EXE/DLL targets or attaching to live processes by PID. Intended for security research, reverse-engineering education, and lawful analysis of authorized software. (source: wiki/sources/descriptions/datcathuh__vmprotect-unpacker.md)

Complements debugger-driven [[vmp-unpacker]], Python sogen emulation via [[vmpunpack]], and live-memory harvest via [[vmprotect-dumper]] by combining DLL-injected load-time wait, OEP discovery, memory dump, IAT rebuild, and optional bytecode devirt disasm emit in one Fix VMP workflow.

## Links

- Repo: https://github.com/datcathuh/vmprotect-unpacker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[vmp-unpacker]] · [[vmpunpack]] · [[vmpstatic]] · [[vmprotect-dumper]] · [[nuitka-themida-unpacker]]
