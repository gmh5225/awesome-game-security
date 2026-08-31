---
title: CallStack-Spoofer
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Barracudach__CallStack-Spoofer.md
updated: 2026-08-31
confidence: medium
---

# CallStack-Spoofer

**CallStack-Spoofer** is a **C++ call-stack spoofing toolkit** (Barracudach) that aims to make **stack-based analysis harder** in both **user mode and kernel mode**. It provides **macros and templates** for spoofing function frames and **proxying calls through generated shellcode paths**. Targets **x64** environments and documents practical constraints such as **compiler settings** and **control-flow protections**. Primary use case: **anti-analysis and anti-cheat evasion research** where stack-walk visibility matters. (source: wiki/sources/descriptions/Barracudach__CallStack-Spoofer.md)

Sits in the `Cheat > Spoof Stack` lane beside x64 trampoline implementations such as [[callstackspoofer-2]], WithSecure Labs syscall PoCs such as [[callstackspoofer]], and Rust macro crates such as [[unwinder]].

## Links

- Repo: https://github.com/Barracudach/CallStack-Spoofer

## Related

[[stack-spoofing]] · [[callstackspoofer-2]] · [[callstackspoofer]] · [[ret-spoofing]] · [[unwinder]] · [[spoof-stack-safecall]] · [[thread-stack-spoofer]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
