---
title: Killing Floor Bot Client
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/geekrainian__killingfloor-bot-client.md
updated: 2026-08-15
confidence: medium
---

# Killing Floor Bot Client

**L2Walker-style headless client** for **Killing Floor** that speaks the native **Unreal Engine 2.5** network protocol over **UDP** without launching the game or injecting code. Implemented primarily in **JavaScript on Node.js** with an **Electron** desktop GUI, optional **Python** for GameSpy server queries, **UnrealScript** server mutators, and **Ghidra scripts** used to reverse engineer the UE2 bitstream, packet handshake, and Killing Floor-specific **Steam authentication** flow. (source: wiki/sources/descriptions/geekrainian__killingfloor-bot-client.md)

The bot can join servers using either **Goldberg Steam emulation** with a synthetic ticket on owned test hosts or genuine Steam tickets via a 32-bit FFI helper. It includes a **UDP MITM relay**, packet disassembly, and extensive protocol documentation for capture and debugging. Aimed at game security researchers and reverse engineers studying legacy UE2 multiplayer networking, Steam ticket validation, and client-server interoperability on **authorized or self-hosted** Killing Floor servers.

Sits in the Cheat → **Packet Sniffer&Filter** / headless-client lane beside wire-capture tooling such as [[packet-sniffer]] and [[akebi-packet-sniffer]], and complements [[goldberg-emulator]] when the research target is Killing Floor's Steam ticket path rather than generic Steamworks API emulation.

## Links

- Repo: https://github.com/geekrainian/killingfloor-bot-client

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[goldberg-emulator]] · [[ghidra-scripts]] · [[ghidra]] · [[packet-sniffer]] · [[akebi-packet-sniffer]] · [[unreal-network-profiler]]
