---
title: PUBG-DX
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__PUBG-DX.md
updated: 2026-08-11
confidence: medium
---

# PUBG-DX

Internal **PUBG** cheat DLL (gmh5225; cheat / game:pubg). Hooks **DirectX 11** to render an **ImGui** overlay menu with ESP (player boxes, per-weapon icons as embedded PNG textures), aimbot, and item ESP. Protected by **VMProtect SDK** integration. (source: wiki/sources/descriptions/gmh5225__PUBG-DX.md)

Memory access uses **kernel driver** communication (`drive.h`). Offensive RE resolves UE4 **`GObjects`/`GWorld`/`FNameEntry`** arrays and decrypts PUBG **Xenuine-protected** pointers (`decrypt.h`). **Return-address spoofing** via `SpoofCall.asm` hides call origins from anti-cheat stack-walking. (source: wiki/sources/descriptions/gmh5225__PUBG-DX.md)

Useful for game security researchers studying internal DX11 hook-based cheat rendering, Xenuine pointer decryption, VMProtect integration, and stack-spoofing in UE4 title cheats—complementing [[pubg-internal]] (FW1FontWrapper Present-hook variant), external samples such as [[pubg-external-cheat]], and offset/SDK tooling such as [[pubg-dump-offset]] / [[pubg-dumper]].

## Links

- Repo: https://github.com/gmh5225/PUBG-DX

## Related

[[present-hook]] · [[stack-spoofing]] · [[vmprotect]] · [[unreal-object-model]] · [[pubg-internal]] · [[pubg-external-cheat]] · [[pubg-dump-offset]] · [[pubg-dumper]] · [[pubgstar]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
