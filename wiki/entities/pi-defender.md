---
title: PI-Defender
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/PI-Defender__pi-defender.md
updated: 2026-08-22
confidence: medium
---

# PI-Defender

Windows **kernel security driver** (PI-Defender) designed to block process injection techniques by protecting target processes at the handle layer. The driver filters dangerous handle rights—remote memory write and related operation permissions—that injection chains rely on, aiming to stop past, current, and future injection vectors without patching every usermode API individually. (source: wiki/sources/descriptions/PI-Defender__pi-defender.md)

## Coverage

The C++ driver codebase ships with tests and documentation covering injection families including **process hollowing**, **process doppelgänging**, **process ghosting**, and **DLL injection**. Primarily useful for defensive security research and anti-cheat-style hardening on Windows rather than offensive cheat development.

## Mechanism

| Layer | Approach |
|-------|----------|
| **Kernel driver** | Handle-right filtering on protected processes |
| **Documentation** | Injection technique coverage + test harness |
| **Audience** | Defensive researchers, AC hardening experiments |

## Positioning

Defensive counterpart to injection corpora such as [[windows-process-injection]], [[injectors]], and [[poolparty]]—studies how kernel handle policy can break injection prerequisites before usermode shellcode runs. Complements ObCallback-focused AC samples such as [[oac]], [[cs2kac]], and [[peregrine-anticheat]] with a narrower injection-blocking mandate.

## Links

- Repo: https://github.com/PI-Defender/pi-defender

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[concepts/kernel-callbacks]] · [[windows-process-injection]] · [[injectors]] · [[oac]] · [[peregrine-anticheat]]
