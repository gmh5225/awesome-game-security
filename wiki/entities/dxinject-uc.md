---
title: DXInject-UC
kind: entity
topics: [game-hacking, graphics-api, windows-kernel]
sources:
  - wiki/sources/descriptions/a0yark__DXInject-UC.md
updated: 2026-08-19
confidence: medium
---

# DXInject-UC

Proof-of-concept for **GPU-assisted process hollowing** using **DirectX 11 shared buffers** and **HLSL compute shaders** (a0yark). The C++ codebase splits into an **Injector** that encodes shellcode and uploads it to a GPU shared buffer, and a **Target** that uses a compute shader to decode the payload on the GPU before executing it on the CPU. Cross-process synchronization uses **named events**, **shared memory**, and **DXGI shared handles**. Intended for security researchers studying GPU-based payload transport, compute-shader abuse, and novel code-injection techniques—not production cheat tooling. (source: wiki/sources/descriptions/a0yark__DXInject-UC.md)

## Links

- Repo: https://github.com/a0yark/DXInject-UC

## Related

[[windows-process-injection]] · [[dirty-vanity]] · [[game-lag-reducer]] · [[intro-to-dx11-revisited]] · [[pubg-demo]] · [[duckov-marketmod]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
