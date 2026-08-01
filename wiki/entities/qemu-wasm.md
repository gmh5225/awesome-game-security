---
title: qemu-wasm
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ktock__qemu-wasm.md
updated: 2026-08-01
confidence: medium
---

# qemu-wasm

WebAssembly port of **QEMU** that runs virtual machines directly in web browsers: x86 and other architecture emulators compiled to WASM via Emscripten, enabling Linux, Windows, and other guest OSes to boot in a browser tab without server-side processing. VirtIO device emulation, networking, and storage are bridged through browser APIs. (source: wiki/sources/descriptions/ktock__qemu-wasm.md)

Useful for emulation researchers, educators, and developers who need browser-based VM access—adjacent to desktop QEMU lab hosts such as [[quickemu]] and [[proxmox]], but with client-only execution in the `Cheat > QEMU/KVM/PVE/VBOX` research lane.

## Links

- Repo: https://github.com/ktock/qemu-wasm (README tag: QEMU on browser)

## Related

[[quickemu]] · [[proxmox]] · [[xqemu]] · [[panda]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
