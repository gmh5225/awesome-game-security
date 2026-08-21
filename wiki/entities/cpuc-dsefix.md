---
title: CPUZ-DSEFix
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/SamLarenN__CPUZ-DSEFix.md
updated: 2026-08-21
confidence: medium
---

# CPUZ-DSEFix

Windows x64 utility that exploits a vulnerable CPU-Z driver to disable Driver Signature Enforcement (DSE) and load unsigned kernel drivers. Written in C++ with kernel memory patching, system-variable pattern scanning, and helper routines for driver-loading workflows. Targets `g_CiEnable` on older builds and `g_CiOptions` on newer systems, with explicit notes about [[patchguard]]-related crash risk. Primarily used in kernel security research and anti-cheat bypass experimentation involving unsigned drivers. (source: wiki/sources/descriptions/SamLarenN__CPUZ-DSEFix.md)

Adjacent to CI/`g_CiOptions` patch PoCs such as [[dse-patcher-2]] and CI.dll hook paths such as [[dse-hook]] — here the primitive chain starts from CPU-Z [[byovd]] abuse rather than direct in-process CI patching or certificate abuse such as [[pastdse]].

## Links

- Repo: https://github.com/SamLarenN/CPUZ-DSEFix

## Related

[[cpuz]] · [[byovd]] · [[dse-hook]] · [[dse-patcher-2]] · [[patchguard]] · [[kdmapper]] · [[vdm]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
