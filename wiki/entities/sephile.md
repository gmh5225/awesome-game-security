---
title: sephile
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/vastobb__sephile.md
updated: 2026-10-18
confidence: medium
---

# sephile

Rooted **Android** application for **runtime memory analysis** and live editing of other processes, aimed at beginners and researchers who want a modern alternative to classic game-memory tools. **Kotlin** + **Jetpack Compose** UI; **C++ NDK** layer uses **ptrace** and **`/proc` maps** to attach, scan typed values, refine searches, edit and freeze addresses, and inspect memory with a live hex-style viewer. Includes a process browser, optional **Lua** scripting hooks for automation, and root integration via **`su`** for ptrace access. Positioned as an **educational and research** tool for reverse engineering and studying how mobile games and apps hold state in memory—not for bypassing online anti-cheat on live services. CI publishes built APKs. Listed under Cheat **Android Memory Explorer** beside CE-style tools such as [[charlyengine]], [[memdbg]], and [[cheap-engine]]. (source: wiki/sources/descriptions/vastobb__sephile.md)

## Technical notes

Ptrace attach path with proc-maps–aware scanning; typed value search with refinement; address freeze; live hex inspector; optional Lua automation layer.

## Links

- Repo: https://github.com/vastobb/sephile

## Related

[[charlyengine]] · [[memdbg]] · [[cheap-engine]] · [[ace-the-game]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
