---
title: Codm-Cheat
kind: entity
topics: [game-hacking, reverse-engineering, mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/hi-bi-hs-13__Codm-Cheat.md
updated: 2026-09-29
confidence: medium
---

# Codm-Cheat

Multi-session reverse-engineering archive of the **BestCheatIR** commercial **Call of Duty Mobile** PC cheat (hi-bi-hs-13). Documents a **VMProtect**-protected loader, injected DLL, and online license infrastructure. Maps **ESP**, **aimbot**, bullet track, and magic bullet logic through x64 disassembly, memory dumps, and IPC protocol analysis between the loader overlay and game memory layer. Python tooling built on Unicorn, Capstone, and pefile unpacks protected binaries, emulates license authentication, and serves fake offset responses via a replicated **HMAC-SHA256** login protocol. Detailed reports capture **libunity** TypeInfo offset chains, resolver behavior, and session-by-session crash and offset verification notes. Intended for game security researchers, anti-cheat engineers, and malware analysts studying commercial cheat ecosystems—not for deploying cheats. (source: wiki/sources/descriptions/hi-bi-hs-13__Codm-Cheat.md)

Sits beside other commercial P2C loader RE reports such as [[pubg-p2c-re]] and [[cs2-p2c-templates]], runnable CODM offensive samples such as [[codm-esp-aimbot-mod-menu]], IL2CPP dump tooling such as [[codm-dumper]], and VMProtect study surfaces such as [[vmprotect]].

## Links

- Repo: https://github.com/hi-bi-hs-13/Codm-Cheat

## Related

[[vmprotect]] · [[pubg-p2c-re]] · [[cs2-p2c-templates]] · [[codm-esp-aimbot-mod-menu]] · [[codm-dumper]] · [[il2cpp]] · [[world-to-screen]] · [[mixed-boolean-arithmetic]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
