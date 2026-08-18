---
title: pubg-internal
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__PUBG_Internal.md
  - wiki/sources/descriptions/iCollin__pubg-internal.md
  - wiki/sources/descriptions/ajkhoury__pubg_internal.md
updated: 2026-08-18
confidence: medium
---

# pubg-internal

PUBG internal cheat references in the cheat / game:pubg lane spanning a D3D11 Present-hook sample (gmh5225), a learning-oriented RE artifact (iCollin), and an archived user-mode + kernel-mode research stack (ajkhoury).

## gmh5225/PUBG_Internal

Internal PUBG cheat DLL (gmh5225). Injected into the PUBG process; hooks DirectX 11 **`IDXGISwapChain::Present`** via **MinHook** to insert custom draw calls in the game's rendering pipeline. ESP text uses **FW1FontWrapper** (DirectWrite-based D3D11 text library) for GPU-accelerated overlay rendering directly in the swap-chain Present path. Useful for game security researchers studying internal D3D11 Present-hook cheat architectures with MinHook-based function interception and DirectWrite overlay rendering—complementing external PUBG samples such as [[pubg-external-cheat]] and [[pubg-lite-esp]]. (source: wiki/sources/descriptions/gmh5225__PUBG_Internal.md)

- Repo: https://github.com/gmh5225/PUBG_Internal

## iCollin/pubg-internal

Learning-oriented PUBG internal cheat reference (iCollin). Code quality is explicitly not polished; the repo is meant as a study artifact for game security researchers and reverse engineers exploring offensive in-process techniques. (source: wiki/sources/descriptions/iCollin__pubg-internal.md)

- Repo: https://github.com/iCollin/pubg-internal

## ajkhoury/pubg_internal

Archived internal cheat research project (ajkhoury) combining **user-mode and kernel-mode** components in C/C++. Includes a **kernel driver for protected-process mapping**, a **game SDK generator**, and a **basic internal ESP** implementation. The code illustrates practical integration of memory access, game structure extraction, and in-process feature logic—primarily useful for studying historical cheat architecture and anti-cheat threat models on protected titles. (source: wiki/sources/descriptions/ajkhoury__pubg_internal.md)

- Repo: https://github.com/ajkhoury/pubg_internal

## Related

[[present-hook]] · [[ntminhook]] · [[pubg-dx]] · [[pubg-external-cheat]] · [[pubg-lite-esp]] · [[pubgstar]] · [[pubg-dump-offset]] · [[pubg-dumper]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[bypass-pubg-mobile-imgui]] · [[yolov5-pubg]]
