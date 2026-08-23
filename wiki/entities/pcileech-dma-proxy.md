---
title: PCILeech DMA Proxy
kind: entity
topics: [dma-attack, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md
updated: 2026-08-23
confidence: medium
---

# PCILeech DMA Proxy

**DLL proxy + loader** (MGreif) that **hooks standard Windows memory APIs** and **redirects them to a remote device over DMA** via the [[pcileech]]/MemProcFS stack. MinHook-based interception covers process, module, thread, and memory operations; bundled DMA memory library adds input and registry access. Useful for DMA security researchers studying **API-transparent remote memory access** and **DMA-proxied game interaction** where local tools call familiar Win32 APIs but backing reads/writes traverse external hardware. (source: wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md)

## Components

- **Proxy DLL** — MinHook layer on common process/module/thread/memory APIs
- **DMA memory library** — remote physical-memory path with input and registry helpers
- **Loader application** — injects proxy and wires the DMA backend

## Links

- Repo: https://github.com/MGreif/PCILeech_DMA_Proxy

## Related

[[dma]] · [[pcileech]] · [[dmalibrary]] · [[dma-invoker]] · [[cheat-engine-dma-plugin]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
