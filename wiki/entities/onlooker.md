---
title: Onlooker
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/DenuvoSoftwareSolutions__Onlooker.md
updated: 2026-08-26
confidence: medium
---

# Onlooker

**Onlooker** is a lightweight **Windows memory profiler** that records memory statistics for a **process tree**, similar to the Linux `time` command. A companion **Qt-based GUI** inspects traces and logs visually. Implemented mainly in **C++** with **CMake** and **Qt Widgets**, it also provides **JSON trace conversion** utilities. Primary use cases include diagnosing **memory growth**, **out-of-memory events**, and **performance regressions** in complex native toolchains. (source: wiki/sources/descriptions/DenuvoSoftwareSolutions__Onlooker.md)

Complements interactive debuggers such as [[windbg-tool]] and memory-layout RE tools such as [[reclass]] by focusing on lightweight, tree-wide memory telemetry rather than live breakpoint debugging or manual structure mapping.

## Links

- Repo: https://github.com/DenuvoSoftwareSolutions/Onlooker (README: Tool to collect and visualize memory usage of a process tree)

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[windbg-tool]] · [[reclass]] · [[x64dbg]] · [[drmemory]]
