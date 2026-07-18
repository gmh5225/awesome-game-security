---
title: PresentHookDetection
kind: entity
topics: [graphics-api, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/weak1337__PresentHookDetection.md
updated: 2026-07-18
confidence: medium
---

# PresentHookDetection

PoC that replicates [[battleye]]-style detection of `IDXGISwapChain::Present` hooks: create a dummy D3D11 device/swap chain, read the Present function pointer from the vtable, and compare code bytes at that address against the original `dxgi.dll` image to spot inline JMP patches or vtable overwrites. Useful for AC implementers studying Present integrity checks and for cheat authors testing whether overlay hooks (ESP/aimbot draw paths) survive that class of prologue/module comparison. (source: wiki/sources/descriptions/weak1337__PresentHookDetection.md)

## Links

- Repo: https://github.com/weak1337/PresentHookDetection

## Related

[[present-hook]] · [[battleye]] · [[skiphook]] · [[eac-overlay]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
