---
title: Overwatch 1 Cheat Source
kind: entity
topics: [game-hacking, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Overwatch-1-cheat-source.md
updated: 2026-08-11
confidence: medium
---

# Overwatch 1 Cheat Source

Internal **Overwatch 1** cheat DLL (gmh5225) that hooks **DirectX 11** `Present` via **Microsoft Detours** to render an **ImGui** overlay with **ESP**, **aimbot**, **skin changer** (per-hero cosmetic selection), and a full menu system. Protected by **VMProtect SDK**. (source: wiki/sources/descriptions/gmh5225__Overwatch-1-cheat-source.md)

Offensive evasion includes **return-address spoofing** (`Spoofcall.masm`) to bypass **Warden** stack checks, **hardware breakpoint**-based hooking (`BreakPoint.h`), SDK offset entity reads (`SKD.hpp`), and **SendInput** mouse simulation. Loader/license validation uses curl-based authentication. README tag: `[NtUserInjectMouseInput]`. Useful for game security researchers studying internal DX11 hook-based cheats with VMProtect integration, stack spoofing, and Warden anti-cheat evasion in Overwatch. (source: wiki/sources/descriptions/gmh5225__Overwatch-1-cheat-source.md)

Contrasts with engine-native glow ESP such as [[ow-outlines]] (outline memory writes; no Present menu) and zero-memory Overwatch 2 pipelines such as [[overwatch2-colorbot-cheats]]. Complements Overwatch 2 internal samples such as [[overwatch-2-cheat-aimbot-esp]], protected-binary tooling such as [[overwatch-iat-fixer]], and broader multi-title research such as [[meowsense]].

## Links

- Repo: https://github.com/gmh5225/Overwatch-1-cheat-source

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]] · [[present-hook]] · [[stack-spoofing]] · [[vmprotect]] · [[ow-outlines]] · [[overwatch-2-cheat-aimbot-esp]] · [[overwatch2-colorbot-cheats]] · [[overwatch-iat-fixer]] · [[meowsense]] · [[x14-08-coverstory-blizzard]]
