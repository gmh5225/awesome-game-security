---
title: Krunker Loader
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/levifrsn63__krunker-loader.md
updated: 2026-08-17
confidence: medium
---

# Krunker Loader

**Keyless cheat stack** for the browser FPS **Krunker.io**, delivered as **Tampermonkey** and **Violentmonkey** userscripts with an optional client loader. The main script injects at **document-start**, sets a local **anti-tamper token** to bypass client integrity checks, and exposes aimbot, ESP and wallhack, player and weapon chams, FOV and skin changers, bunny hop, and a keybindable ImGui-style mod menu. An optional loader emulates **Quirify-style license and heartbeat validation** without a key and can boot a bundled clean game client instead of the stock one. Written in JavaScript; useful for studying browser game client manipulation, userscript-based injection, and anti-cheat evasion techniques. (source: wiki/sources/descriptions/levifrsn63__krunker-loader.md)

Sits in the browser userscript cheat lane beside WASM memory tooling such as [[webcheat]] and anti-debug UserScripts such as [[js-debugger-bypass-script]] — the offensive counterpart to client-side script protection such as [[javascript-obfuscator]].

## Links

- Repo: https://github.com/levifrsn63/krunker-loader

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[webcheat]] · [[js-debugger-bypass-script]] · [[javascript-obfuscator]] · [[ff3mmo]]
