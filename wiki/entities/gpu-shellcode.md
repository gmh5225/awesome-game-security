---
title: GPU_ShellCode
kind: entity
topics: [anti-cheat, game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/H1d3r__GPU_ShellCode.md
updated: 2026-08-25
confidence: medium
---

# GPU_ShellCode

Proof-of-concept that **stores active payload data in NVIDIA GPU memory** instead of keeping it in normal process memory. Windows C/C++ sample using **CUDA APIs** and **MinHook** to intercept functions such as `Sleep` and `VirtualAlloc`, then restores execution through a **vectored exception handler (VEH)** when needed. During idle periods the workflow copies a staged payload to GPU VRAM; on wake-up it repopulates executable pages, demonstrating **memory hiding** against conventional process-memory inspection. Useful for low-level offensive security research and for studying anti-cheat or anti-malware memory-scan evasion. (source: wiki/sources/descriptions/H1d3r__GPU_ShellCode.md)

## Technique

1. Hook sleep/allocation APIs (MinHook) to detect idle vs active execution windows.
2. Stage shellcode/payload bytes into **CUDA-managed GPU memory** while the process appears quiescent.
3. On resume, use a **VEH** to fault into controlled restore paths that remap or repopulate **RX** executable pages from GPU-resident copies.
4. Keeps sensitive bytes outside typical usermode VirtualQuery / working-set scans that only walk host RAM.

## Links

- Repo: https://github.com/H1d3r/GPU_ShellCode

## Related

[[shellcode-fluctuation]] · [[shellcode-plain-sight]] · [[no-access-protection]] · [[deepsleep]] · [[veh]] · [[dxinject-uc]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
