---
title: nullptr-apex-external
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/M1fisto__nullptr-apex-external.md
updated: 2026-08-23
confidence: medium
---

# nullptr-apex-external

**nullptr-apex-external** (M1fisto/nullptr-apex-external) is a **tutorial-style external cheat codebase** for **Apex Legends** that documents how kernel-assisted memory access supports out-of-process game manipulation. Implemented in **C++**, it covers **kernel hijacking**, **cross-process game memory read/write**, and **SDK-based entity handling**, with separate **user-mode** components for external visualization and control logic. Intended for educational exploration of external cheat architecture and related **anti-cheat detection** challenges under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/M1fisto__nullptr-apex-external.md)

Sits in the Apex Legends external learning lane beside [[apex-legends-esp]], [[apex-external]], and [[apex-legends-cheat]], and beside kernel-hijack research samples such as [[driver-read-write]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Kernel hijacking | Kernel-assisted cross-process memory access path |
| Memory R/W | Game memory read/write from an external process |
| SDK entity handling | Entity iteration and field access via generated/layout structures |
| User-mode control | External visualization and control logic |

## Links

- Repo: https://github.com/M1fisto/nullptr-apex-external (External)

## Related

[[apex-legends-esp]] · [[apex-external]] · [[apex-legends-cheat]] · [[apex-legends-sdk]] · [[driver-read-write]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
