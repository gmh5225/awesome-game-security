---
title: ptrace_read_teb
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/pgarba__ptrace_read_teb.md
updated: 2026-07-26
confidence: medium
---

# ptrace_read_teb

C++ sample that uses **ptrace** to read the **TEB** (Thread Environment Block) of a process on Linux. Aimed at game-security researchers and reverse engineers studying offensive techniques in the Cheat / Wine lane — e.g. inspecting Windows thread state when a title runs under Wine on Linux. (source: wiki/sources/descriptions/pgarba__ptrace_read_teb.md)

Complements Linux process-watch tooling such as [[pwatch]] (HWBP without conventional attach) and Android ptrace injectors such as [[android-ptrace-injector]] (attach-and-inject rather than TEB inspect).

## Links

- Repo: https://github.com/pgarba/ptrace_read_teb (README: use ptrace to read the TEB of a process on Linux)

## Related

[[pwatch]] · [[android-ptrace-injector]] · [[libmem]] · [[holodori-kernel-bypass]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
