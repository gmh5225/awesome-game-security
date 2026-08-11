---
title: pubg-internal
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__PUBG_Internal.md
  - wiki/sources/descriptions/iCollin__pubg-internal.md
updated: 2026-08-11
confidence: medium
---

# pubg-internal

PUBG internal cheat references in the cheat / game:pubg lane spanning a D3D11 Present-hook sample (gmh5225) and a learning-oriented RE artifact (iCollin).

## gmh5225/PUBG_Internal

Internal PUBG cheat DLL (gmh5225). Injected into the PUBG process; hooks DirectX 11 **`IDXGISwapChain::Present`** via **MinHook** to insert custom draw calls in the game's rendering pipeline. ESP text uses **FW1FontWrapper** (DirectWrite-based D3D11 text library) for GPU-accelerated overlay rendering directly in the swap-chain Present path. Useful for game security researchers studying internal D3D11 Present-hook cheat architectures with MinHook-based function interception and DirectWrite overlay rendering—complementing external PUBG samples such as [[pubg-external-cheat]] and [[pubg-lite-esp]]. (source: wiki/sources/descriptions/gmh5225__PUBG_Internal.md)

- Repo: https://github.com/gmh5225/PUBG_Internal

## iCollin/pubg-internal

Learning-oriented PUBG internal cheat reference (iCollin). Code quality is explicitly not polished; the repo is meant as a study artifact for game security researchers and reverse engineers exploring offensive in-process techniques. (source: wiki/sources/descriptions/iCollin__pubg-internal.md)

- Repo: https://github.com/iCollin/pubg-internal

## Related

[[present-hook]] · [[ntminhook]] · [[pubg-dx]] · [[pubg-external-cheat]] · [[pubg-lite-esp]] · [[pubgstar]] · [[pubg-dump-offset]] · [[pubg-dumper]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[bypass-pubg-mobile-imgui]] · [[yolov5-pubg]]
