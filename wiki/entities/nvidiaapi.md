---
title: NvidiaApi
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/weak1337__NvidiaApi.md
updated: 2026-07-18
confidence: medium
---

# NvidiaApi

C++ library that talks to NVIDIA’s undocumented NvAPI: loads `nvapi64.dll`, resolves internals via `NvAPI_QueryInterface`, and queries GPU hardware details (serial numbers, physical GPU handles, board names, driver versions). Wraps both public calls (`EnumPhysicalGPUs`, `GetFullName`) and private interfaces that the stock NvAPI SDK does not expose. (source: wiki/sources/descriptions/weak1337__NvidiaApi.md)

Useful for HWID-spoofer research and for studying how anti-cheat systems fingerprint NVIDIA GPUs via serial / board identity.

## Links

- Repo: https://github.com/weak1337/NvidiaApi

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]]
