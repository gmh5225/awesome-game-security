---
title: Dse-Patcher-2
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Dse-Patcher-2.md
updated: 2026-08-13
confidence: medium
---

# Dse-Patcher-2

Windows Driver Signature Enforcement (DSE) bypass research tool that locates **`ci.dll!g_CiOptions`** and patches it to disable kernel-mode code-integrity validation, allowing unsigned driver images to load. (source: wiki/sources/descriptions/gmh5225__Dse-Patcher-2.md)

Adjacent to CI/`g_CiOptions` controllers such as [[kvc]] and [[kexecdd]], CI.dll hook / `g_CiEnabled` patch PoCs such as [[dse-hook]], and multi-method runtime disable tooling such as [[upgdsed]] — here the focus is a direct `g_CiOptions` write rather than signed-helper IOCTL paths, verification hooks, or certificate abuse such as [[pastdse]].

## Links

- Repo: https://github.com/gmh5225/Dse-Patcher-2

## Related

[[dse-hook]] · [[kvc]] · [[kexecdd]] · [[kernel-research-kit]] · [[upgdsed]] · [[pastdse]] · [[byovd]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
