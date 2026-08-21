---
title: subzero-fortnite-cheat
kind: entity
topics: [game-hacking, graphics-api, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Saxmason__Subzero-Fortnite-Cheat.md
updated: 2026-08-21
confidence: medium
---

# subzero-fortnite-cheat

**SubZero** is a Windows C++ Visual Studio **Fortnite external cheat** (Saxmason/Subzero-Fortnite-Cheat; cheat / game:fortnite [External]). Out-of-process design: a **kernel-style driver interface** supplies remote memory reads; **game offsets** and **mesh-based visibility checks** drive smooth mouse aim toward on-screen targets. Renders via a **DirectX 9 ImGui overlay** and menu. Input path uses **`NtUserSendInput`-based mouse injection** with library spoofing; codebase also includes **call-stack spoofing**, **XOR string obfuscation**, and optional authentication helpers. Useful for game-security research into external overlay cheats, kernel memory access patterns, and Windows evasion techniques on EAC-protected UE clients. (source: wiki/sources/descriptions/Saxmason__Subzero-Fortnite-Cheat.md)

Sits beside other driver-backed Fortnite externals such as [[fortnite-external-cheat-leak]], [[fortnite-external-cheat-base]], [[fortnite-external-5]], and [[nigusfn]].

## Links

- Repo: https://github.com/Saxmason/Subzero-Fortnite-Cheat

## Related

[[easy-anti-cheat]] · [[world-to-screen]] · [[stack-spoofing]] · [[hardware-input-injection]] · [[fortnite-external-cheat-leak]] · [[fortnite-external-cheat-base]] · [[fortnite-external-cheat-source-code]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/graphics-api]]
