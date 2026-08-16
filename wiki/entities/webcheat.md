---
title: WebCheat
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/hasaneyldrm__webcheat.md
updated: 2026-08-16
confidence: medium
---

# WebCheat

**Chrome extension** that brings **Cheat Engine–style memory scanning and editing** to browser-based games built with **WebAssembly**. Hooks `WebAssembly` instantiation to capture the game's linear memory, then supports classic scan-and-narrow workflows across integer and floating-point types with read, write, and 60 Hz freeze on discovered addresses. Also provides **virtual clock** time control for speed adjustment, pause, and single-frame stepping, and can target games embedded in cross-origin iframes. Written in JavaScript as a **Manifest V3** extension with content scripts in both MAIN and ISOLATED worlds; runs entirely in the browser with no external server or debugger attachment. Aimed at game developers and security researchers analyzing client-side state in **Unity**, **Godot**, and **Emscripten WebGL** titles. (source: wiki/sources/descriptions/hasaneyldrm__webcheat.md)

Complements ceserver-style WASM tooling such as [[wasm-ceserver]] by offering an in-browser, no-attach workflow for WebGL/WASM game memory RE—useful when the target ships as a browser tab rather than a native process.

## Links

- Repo: https://github.com/hasaneyldrm/webcheat

## Related

[[wasm-ceserver]] · [[gddumper]] · [[memmcp]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
