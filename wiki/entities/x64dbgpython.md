---
title: x64dbgpython
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ElvisBlue__x64dbgpython.md
updated: 2026-08-25
confidence: medium
---

# x64dbgpython

[[x64dbg]] plugin that adds **Python 3** scripting support inside the debugger. Built in C++ and exposes debugger functionality through Python-friendly wrappers that mirror common plugin SDK APIs. Ships example scripts for memory access, assembly tasks, module inspection, and GUI interactions to automate repetitive reversing workflows. Primary use case is reverse engineering and debugger automation for analysts who want to script x86 and x64 debugging tasks. (source: wiki/sources/descriptions/ElvisBlue__x64dbgpython.md)

In-process Python 3 scripting complements external Automate RPC via [[x64dbg-automate-pyclient]] and other in-debugger script runtimes such as [[x64dbg-playtime]] (Lua) and [[chaiscript-plugin]] (ChaiScript). README category: Running python3 script.

## Links

- Repo: https://github.com/ElvisBlue/x64dbgpython

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[x64dbg-automate-pyclient]] · [[x64dbg-playtime]] · [[chaiscript-plugin]] · [[dotx64dbg]]
