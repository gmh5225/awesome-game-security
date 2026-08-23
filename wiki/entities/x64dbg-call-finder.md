---
title: x64dbg Call Finder
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Kwansy98__x64dbgCallFinder.md
updated: 2026-08-23
confidence: medium
---

# x64dbg Call Finder

[[x64dbg]] plugin (C++) that helps locate important runtime functions by **tracking call frequency**. It scans user functions, installs conditional breakpoints, and increments per-function counters so analysts can filter results by call count after triggering in-application actions (UI clicks, gameplay events, etc.). Useful for reverse engineers and game-security researchers who need to quickly identify handlers such as UI callbacks or gameplay logic without manual breakpoint triage. Bilingual usage documentation included. (source: wiki/sources/descriptions/Kwansy98__x64dbgCallFinder.md)

Not a standalone debugger—extends [[x64dbg]] for dynamic call-frequency profiling inside live debug sessions (Cheat x64dbg Plugins / Call Finder lane).

## Links

- Repo: https://github.com/Kwansy98/x64dbgCallFinder

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[xfindout]] · [[clawsearch]] · [[x64dbg-trace-reader]] · [[slothbp]]
