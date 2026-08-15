---
title: Deadlock Anti-Cheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/g8tsz__deadlock-anti-cheat.md
updated: 2026-08-15
confidence: medium
---

# Deadlock Anti-Cheat

**UrnIt Anticheat** — a Windows **user-mode** client-side anti-cheat for the game **Deadlock** (g8tsz). During play sessions it periodically collects process lists, PNG screenshots of the game window, focused-window key input, and CPU/GPU hardware details, then bundles evidence for staff review rather than kernel-level enforcement. A configurable cheat-process signature list (with optional forum scraping to refresh names) flags known tools; key-timing variance heuristics suggest possible macro or bot use. Reports upload automatically to Discord via webhook when the game exits or the player presses F12. C++ with Visual Studio build plus a Python helper script; aimed at tournament organizers and game-security staff who need lightweight session logging and remote review. (source: wiki/sources/descriptions/g8tsz__deadlock-anti-cheat.md)

Complements educational user-mode AC samples such as [[basic-anti-cheat]] and [[anticheat-poc]], and Windows screenshot capture research such as [[screenshot]] for validating what game-window PNG evidence reveals.

## Links

- Repo: https://github.com/g8tsz/deadlock-anti-cheat

## Related

[[basic-anti-cheat]] · [[anticheat-poc]] · [[screenshot]] · [[research-rigor]] · [[overviews/anti-cheat]] · [[concepts/anti-screenshot-capture]]
