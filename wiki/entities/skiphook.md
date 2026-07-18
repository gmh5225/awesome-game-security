---
title: SkipHook
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/weak1337__SkipHook.md
updated: 2026-07-18
confidence: medium
---

# SkipHook

Header-only C++ library that builds **function-call trampolines which skip the first instruction** of a target, so inline hooks (`0xE9` JMP) and breakpoint traps (`0xCC` INT3) on WinAPI / game prologues are never executed. Uses HDE (Hacker Disassembly Engine) for x86/x64 length decoding, then runs the original first instruction locally and jumps to `instruction+1`; return-address checks still see a legitimate call origin. Cited against [[battleye]]-style API hooks; useful for studying trampoline-based hook evasion. (source: wiki/sources/descriptions/weak1337__SkipHook.md)

## Links

- Repo: https://github.com/weak1337/SkipHook

## Related

[[battleye]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[system-thread-finder]]
