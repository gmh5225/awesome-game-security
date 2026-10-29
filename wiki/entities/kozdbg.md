---
title: KozDbg
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ivanpotatoes__KozDbg.md
  - wiki/sources/README-categories.md
updated: 2026-10-29
confidence: medium
---

# KozDbg

Open-source **x64dbg plugin** that bypasses **VMProtect anti-debug** checks so analysts can debug protected native **x64** programs without loading a kernel driver. Ships version-matched INI profiles for VMProtect **3.3.1–3.10.1**, using API interception on older builds and clustered or scattered direct syscalls on newer ones. Mitigates PEB and debugger API probes, remote/kernel debugger queries, debug objects, thread hiding, trap-flag delivery, hardware debug registers, instrumentation callbacks, and related checks resolved dynamically in the target process. Implemented in C++17 with CMake for Windows and the x64dbg plugin SDK; command-bar controls for RE workflows studying packer anti-debug behavior. (source: wiki/sources/descriptions/ivanpotatoes__KozDbg.md)

User-mode debugger lane beside ScyllaHide-class hides and kernel neutralizers such as [[anti-anti-debugger-driver]]; pairs VMProtect unpack/lift tooling such as [[vmprotect-unpacker]], [[vmplift]], and [[nuitka-themida-unpacker]] on the analysis vs protection axis.

## Links

- Repo: https://github.com/ivanpotatoes/KozDbg (README tag: Debugging / RE Tools)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[vmprotect-unpacker]] · [[vmplift]] · [[scyllahide-for-ida9.0rc]] · [[anti-anti-debugger-driver]] · [[mixed-boolean-arithmetic]]
