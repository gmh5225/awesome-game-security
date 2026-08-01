---
title: AntiHook
kind: entity
topics: [windows-kernel, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/kouzhudong__AntiHook.md
updated: 2026-08-01
confidence: medium
---

# AntiHook

Windows research project for **enumerating and removing hooks** at kernel level, spanning driver development and graphics-hook surfaces. Aimed at game-security researchers and reverse engineers studying offensive cheat / RE tooling—finding installed hooks and restoring original bytes or dispatch paths rather than installing new trampolines. (source: wiki/sources/descriptions/kouzhudong__AntiHook.md)

Complements hook-install libraries ([[polyhook]], [[polyhook-2-0]], [[detoursnt]], [[skiphook]]) and defensive hook-discovery tools ([[hook-buster]], [[hookhunter]]); sits beside kernel hook samples such as [[windows-kernel-pagehook]] and [[kptnhook]].

## Links

- Repo: https://github.com/kouzhudong/AntiHook (README tag: Enum and Remove Hook in Windows)

## Related

[[present-hook]] · [[hook-buster]] · [[hookhunter]] · [[windows-kernel-pagehook]] · [[kptnhook]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
