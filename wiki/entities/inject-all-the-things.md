---
title: injectAllTheThings
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/DanielRTeixeira__injectAllTheThings.md
updated: 2026-08-26
confidence: medium
---

# injectAllTheThings

Educational **Visual Studio** project demonstrating multiple **Windows DLL injection** techniques (DanielRTeixeira). Implements seven methods—**CreateRemoteThread**, **NtCreateThreadEx**, **QueueUserAPC**, **SetWindowsHookEx**, **RtlCreateUserThread**, **SetThreadContext**, and **reflective DLL loading**—with support for **x86 and x64** targets. Each technique lives in its own source file so learners can compare implementation differences and execution trade-offs. Primary audience: security learners, reverse engineers, and researchers studying process-injection mechanics. (source: wiki/sources/descriptions/DanielRTeixeira__injectAllTheThings.md)

README lane: **Injection Testing** — per-technique educational DLL load study sample.

Complements multi-method injectors such as [[windows-dll-injector]] and [[guided-hacking-injector]], broader corpora such as [[windows-process-injection]] and [[process-injection-techniques]], and host-based catalogs such as [[code-injection]].

## Links

- Repo: https://github.com/DanielRTeixeira/injectAllTheThings

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[windows-dll-injector]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[code-injection]] · [[injectors]]
