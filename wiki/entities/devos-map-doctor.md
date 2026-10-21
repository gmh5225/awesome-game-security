---
title: Devo's Map Doctor
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/devoltzz__devos-map-doctor.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: high
---

# Devo's Map Doctor

**devos-map-doctor** ([devoltzz/devos-map-doctor](https://github.com/devoltzz/devos-map-doctor)) is a **Warcraft III** map toolkit for diagnosing, repairing, unprotecting, and porting custom maps (**1.24–Reforged**) without modifying originals in place. (source: wiki/sources/descriptions/devoltzz__devos-map-doctor.md)

## Implementation

Python core with Rust script checkers, native C helpers for **MPQ** cryptography, and browser or desktop UI on Windows, Linux, and the web. It rebuilds and validates MPQ archives, reverses protectors such as **SProtect** and **KK** encryption, restores scripts and object data, and can port Chinese KK and Korean M16 maps by emulating platform natives and save behavior.

## Security research

Supports translation workflows, crash/replay diagnostics, Reforged compatibility checks, and optional cheat-pack injection or analysis for studying in-map cheat menus and platform anti-cheat bait logic—used by map authors and analysts inspecting integrity and script tampering.

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[hivewe]] · [[binary-evidence]]

## Links

- Repo: https://github.com/devoltzz/devos-map-doctor
