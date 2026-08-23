---
title: Shirakumo
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/M3351AN__Shirakumo.md
updated: 2026-08-23
confidence: medium
---

# Shirakumo

**Proof-of-concept RPM/WPM proxy** from **M3351AN** that forwards cross-process memory operations over **named pipes**. Written in **C++**, it separates read/write execution into another process and supports optional **DLL loading** for proxy deployment. The project is explicitly **experimental**: x64-only, not thread-safe, and intended for studying **process-separated memory access** patterns in game tooling and evasion research—not production use. README tag: **RPM for Windows**. (source: wiki/sources/descriptions/M3351AN__Shirakumo.md)

Sits in the usermode named-pipe external memory lane beside [[nobastian-v2]] and [[creadmemory]], and complements same-author kernel PoCs such as [[usugumo]] and [[ukia-rpm]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Named-pipe transport | IPC between client and memory-execution worker |
| Process separation | RPM/WPM runs in a distinct process from the caller |
| Optional DLL proxy | Loadable proxy module for deployment flexibility |
| Limitations | x64-only; not thread-safe; experimental PoC |

## Links

- Repo: https://github.com/M3351AN/Shirakumo (README: RPM for Windows)

## Related

[[nobastian-v2]] · [[creadmemory]] · [[usugumo]] · [[ukia-rpm]] · [[km-um-communication]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
