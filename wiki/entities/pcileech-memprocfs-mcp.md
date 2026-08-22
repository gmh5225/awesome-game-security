---
title: pcileech-memprocfs-mcp
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Neverdecel__pcileech-memprocfs-mcp.md
updated: 2026-08-22
confidence: medium
---

# pcileech-memprocfs-mcp

Linux-native **Model Context Protocol (MCP)** server that exposes **PCILeech** / **MemProcFS** DMA memory operations to AI assistants. Written in Python on **memprocfs** and **leechcorepyc**, it offers dozens of tools for live memory read/write, process and module analysis, pattern scanning, pointer-chain discovery, and cross-reference finding. Engine-specific helpers dump **Unreal Engine 4/5** C++ SDKs and **Unity IL2CPP** class definitions; FPGA control covers benchmarks and PCIe TLP operations. Primary use case: **DMA-assisted reverse engineering and game security research**—driving memory inspection and SDK extraction through natural language instead of manual CLI work. (source: wiki/sources/descriptions/Neverdecel__pcileech-memprocfs-mcp.md)

Contrasts with usermode CE-style MCP servers such as [[memmcp]] and [[cheatengine-mcp-bridge]] by operating on the **external DMA / physical-memory** path via the canonical [[pcileech]] stack rather than in-process or CE-attached targets.

## Links

- Repo: https://github.com/Neverdecel/pcileech-memprocfs-mcp

## Related

[[pcileech]] · [[memprocfs-analyzer]] · [[cheat-engine-ceserver-pcileech]] · [[memmcp]] · [[cheatengine-mcp-bridge]] · [[volk-dma]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
