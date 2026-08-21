---
title: BingusLdr
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Sizeable-Bingus__BingusLdr.md
updated: 2026-08-21
confidence: medium
---

# BingusLdr

**BingusLdr** is a Windows **x64 DLL loader** built with **Crystal Palace** that loads payloads while using **CET-compatible stack spoofing**. Written in **C** with **mingw-w64**, it organizes loading, stitching, services, and memory-masking modules. Key capabilities include **CET-friendly stack spoofing**, **EAF-compatible API resolution**, and **heap/image masking** to reduce exposure of loaded code. Integrates with **Cobalt Strike** through a `.cna` script and LinkSpec-based build, and can wrap arbitrary DLLs into a **PIC-style binary**. Primary use case is offensive security research into **reflective loading**, **call-stack evasion**, and techniques relevant to anti-cheat and endpoint detection analysis. (source: wiki/sources/descriptions/Sizeable-Bingus__BingusLdr.md)

Sits in the `Cheat > Spoof Stack` / reflective-loader lane beside CET-backed loaders such as [[nocturneldr]] and simpler return-address spoof samples such as [[return-address-spoofer]].

## Links

- Repo: https://github.com/Sizeable-Bingus/BingusLdr

## Related

[[stack-spoofing]] · [[nocturneldr]] · [[return-address-spoofer]] · [[thread-stack-spoofer]] · [[silent-moonwalk]] · [[cet-research]] · [[windows-process-injection]] · [[scfw]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
