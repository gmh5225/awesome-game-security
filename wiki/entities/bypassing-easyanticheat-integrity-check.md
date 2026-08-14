---
title: Bypassing EasyAntiCheat Integrity check
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Bypassing-EasyAntiCheat-Integrity-check.md
updated: 2026-08-14
confidence: medium
---

# Bypassing EasyAntiCheat Integrity check

Technical analysis and bypass research for **EasyAntiCheat kernel-mode driver self-integrity checks**. Documents how EAC validates its own driver sections through **CreateProcess** and **LoadImage** kernel notification routines, ships a **Capstone**-based deobfuscation utility that strips garbage instructions to expose the underlying integrity-check logic, and includes reconstructed **C++** for the integrity function showing section-by-section comparison against a stored driver copy. Listed under cheat / explore anticheat:eac `[Bypassing integrity check]`; aimed at researchers studying EAC driver tamper detection and callback-driven image-load validation. (source: wiki/sources/descriptions/gmh5225__Bypassing-EasyAntiCheat-Integrity-check.md)

## Links

- Repo: https://github.com/gmh5225/Bypassing-EasyAntiCheat-Integrity-check

## Related

[[easy-anti-cheat]] · [[kernel-callbacks]] · [[easyanticheat-reversing]] · [[eac-easyanticheat-src-1]] · [[eac]] · [[deobfuscator]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
