---
title: AntiKernelDebug-POC
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__AntiKernelDebug-POC.md
updated: 2026-08-15
confidence: medium
---

# AntiKernelDebug-POC

Windows **C kernel driver** proof-of-concept for **detecting and preventing kernel-mode debugging** — checks for attached kernel debuggers such as WinDbg and KD via debug-port status, the `KdDebuggerEnabled` flag, `KUSER_SHARED_DATA` fields, and interrupt-based detection. Demonstrates anti-kernel-debug techniques used by anti-cheat systems and protected software; aimed at kernel security researchers studying debugger detection and anti-debug bypass. (source: wiki/sources/descriptions/gmh5225__AntiKernelDebug-POC.md)

Complements offensive break-prevention PoCs such as [[letme-gg]] and stealth KD protocol tooling such as [[nokd]]; pairs with defensive anti-debug catalogs such as [[makin]] and kernel debugging setup guides such as [[windows-kernel-debugging-guide]].

## Links

- Repo: https://github.com/gmh5225/AntiKernelDebug-POC

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[letme-gg]] · [[nokd]] · [[titanhide]] · [[windows-kernel-debugging-guide]] · [[makin]] · [[wubbaboomark]]
