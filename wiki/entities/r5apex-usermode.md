---
title: R5Apex-UserMode
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/3nolan5__R5Apex-UserMode.md
updated: 2026-09-04
confidence: medium
---

# R5Apex-UserMode

**R5Apex-UserMode** (3nolan5/R5Apex-UserMode) is a **user-mode external framework** for **Apex Legends** cheating research, implemented in **C++**. It demonstrates **shared-memory communication** with a **mapped kernel driver** for cross-process **read and write** operations. The sample feature set includes **glow** and **highlight** manipulation plus a minimal baseline architecture intended for extension. Primary use case is educational experimentation with external cheat design and driver-assisted memory access patterns under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/3nolan5__R5Apex-UserMode.md)

Sits in the Apex Legends driver-assisted external lane beside [[uc-apex-remastered]], [[project-branthium]], and [[nullptr-apex-external]]—user-mode control with kernel-backed memory I/O rather than a full hybrid overlay stack.

## Architecture

| Component | Role |
|-----------|------|
| User-mode client | External cheat framework and feature modules |
| Mapped kernel driver | Privileged cross-process memory R/W |
| Shared memory | KM↔UM communication channel |
| Glow / highlight | Sample visual manipulation features |

See [[driver-read-write]] for hijack-style driver I/O patterns and [[overviews/windows-kernel]] for KM↔UM IPC fundamentals.

## Links

- Repo: https://github.com/3nolan5/R5Apex-UserMode (External)

## Related

[[uc-apex-remastered]] · [[project-branthium]] · [[nullptr-apex-external]] · [[apex-external]] · [[apex-legends-cheat]] · [[driver-read-write]] · [[easy-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
