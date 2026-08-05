---
title: Etw-Syscall
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/huoji120__Etw-Syscall.md
updated: 2026-08-05
confidence: medium
---

# Etw-Syscall

C/C++ research project focused on **ETW syscall** instrumentation — modding and hooking in the Some Tricks / Windows Ring3 lane. Aimed at low-level Windows researchers studying syscall telemetry, ETW provider interaction, and user-mode hook surfaces adjacent to anti-cheat detection. (source: wiki/sources/descriptions/huoji120__Etw-Syscall.md)

Complements passive EtwTi syscall loggers such as [[etw-syscall-monitor]] and Instrumentation Callback hook samples such as [[etwti-syscall-hook]] by emphasizing ETW-backed syscall hook/modding rather than pure consumer telemetry or ntdll patching alone.

## Links

- Repo: https://github.com/huoji120/Etw-Syscall

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[etw-threat-intelligence]] · [[etw-syscall-monitor]] · [[etwti-syscall-hook]] · [[instrumentation-callback-syscall-logger]] · [[hooking-via-instrumentation-callback]] · [[hidden-syscall-monitoring]] · [[syscall-detect]]
