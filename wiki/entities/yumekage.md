---
title: Yumekage
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Xyrem__Yumekage.md
updated: 2026-08-19
confidence: medium
---

# Yumekage

**Yumekage** (Xyrem/Yumekage) is a C++ proof-of-concept for creating **hidden or shadowed memory regions** in Windows processes. It demonstrates **guarded-region** techniques tied to **context-switch behavior** and low-level memory semantics, with demo-oriented code and media showing how concealed regions can behave under runtime inspection. Intended for reverse engineering and anti-cheat bypass research rather than production deployment. (source: wiki/sources/descriptions/Xyrem__Yumekage.md)

Complements per-process **PTE hooks** such as [[windows-kernel-pagehook]], **#PF page-fault hooks** in [[fast-pf-hook]], cross-platform page-table editors such as [[pteditor]], and context-switch–scoped concealment such as [[hook-hvl-switch-virtual-address-space]].

## Links

- Repo: https://github.com/Xyrem/Yumekage (README tag: PTE Hook)

## Related

[[windows-kernel-pagehook]] · [[fast-pf-hook]] · [[pteditor]] · [[page-table-injector]] · [[readphys]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
