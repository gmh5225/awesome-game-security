---
title: 7DTD
kind: entity
topics: [game-hacking, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/IntelSDM__7DTD.md
updated: 2026-08-24
confidence: medium
---

# 7DTD

**7DTD** (IntelSDM/7DTD) is a **full cheat ecosystem** for **7 Days to Die** spanning in-game modules and supporting backend infrastructure. It documents a **Unity/Mono-based loading approach**, **anti-cheat bypass** concepts, and feature modules including **ESP**, **aimbot**, **weapon modifiers**, and **player spoofing**. The project combines **C# cheat code** with **C++ client and server components** for authentication, data transport, and account controls. Aimed at advanced game security researchers studying end-to-end cheat delivery and operation. (source: wiki/sources/descriptions/IntelSDM__7DTD.md)

Sits in the Unity Mono internal/offensive lane beside managed hooking samples such as [[eft-monoeft]] and contrasts with server-side defensive mods such as [[7dtd-anticheatmod]] on non-[[easy-anti-cheat]] dedicated hosts. Same author as Facepunch Rust DMA framework [[rust-dma-cheat]].

## Architecture notes

- **Client layer:** Unity/Mono loader injects or hosts C# cheat modules against `Assembly-CSharp`-style managed game code.
- **Backend layer:** C++ client/server handles auth, encrypted or structured data transport, and account-control workflows—illustrating commercial-style cheat ops beyond a single injected DLL.
- **Feature surface:** ESP/wallhack, aim assistance, weapon stat modifiers, and identity/spoofing behaviors typical of multiplayer survival titles.

## Links

- Repo: https://github.com/IntelSDM/7DTD

## Related

[[7dtd-anticheatmod]] · [[easy-anti-cheat]] · [[mono]] · [[il2cpp]] · [[eft-monoeft]] · [[rust-dma-cheat]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/game-engine]]
