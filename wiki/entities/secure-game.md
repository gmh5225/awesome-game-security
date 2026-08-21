---
title: SecureGame
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/SamuelTulach__SecureGame.md
updated: 2026-08-21
confidence: medium
---

# SecureGame

**SecureGame** (SamuelTulach) is a Pong-like sample game that places **core game logic inside a Windows VBS enclave**. The solution splits a host application (rendering and input) from an enclave DLL that holds runtime state and gameplay rules. Built with C/C++, SDL2, Visual Studio, Windows SDK, and vcpkg-based dependencies on modern Windows with VBS features enabled. Intended for anti-cheat and trusted-execution research by showing how sensitive game logic can be isolated from normal user-mode tampering. README category: POC game using VBS enclaves to protect itself from cheating. (source: wiki/sources/descriptions/SamuelTulach__SecureGame.md)

Contrasts with offensive VBS enclave abuse PoCs such as [[fake-enclave]]—here the enclave is a **defensive isolation boundary** for gameplay state rather than a trust-boundary misuse study. Sits in the [[hvci]] / VBS research lane beside platform-trust features AC stacks may eventually leverage for client-side logic protection.

## Architecture

- **Host process** — SDL2 rendering, input handling, and UI outside the enclave.
- **Enclave DLL** — stores runtime state and enforces gameplay rules inside the VBS enclave boundary.

## Links

- Repo: https://github.com/SamuelTulach/SecureGame

## Related

[[hvci]] · [[fake-enclave]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
