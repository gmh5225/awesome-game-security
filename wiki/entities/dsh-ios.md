---
title: dsh-ios
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/mzydgnh2__dsh-ios.md
updated: 2026-11-08
confidence: medium
---

# dsh-ios

**dsh-ios** (mzydgnh2/dsh-ios) is an unsigned jailbreak-targeted iOS app that packages the official **DeepSeek Harness (dsh)** agent stack for one-click on-device deployment on iPhones and iPads. A **SwiftUI** shell handles deployment, workspaces, logging, health checks, and background keep-alive while spawning a cross-compiled **Node.js 26** runtime to run the unmodified dsh web stack locally. The repository ships a substantial iOS port of Node with **JIT-disabled** execution, WASM and libffi compatibility patches, POSIX workarounds (in-process shell where `fork` is blocked), and an optional **LAN TCP relay** so other devices on the same network can reach the UI. Distribution is via unsigned or ad-hoc signed IPAs for **TrollStore**, sideloading, or rootless/rootful jailbreak installs. Targets developers and researchers who want a self-hosted DeepSeek coding agent on mobile hardware and practical patterns for running server-style tooling inside iOS sandbox and jailbreak constraints. (source: wiki/sources/descriptions/mzydgnh2__dsh-ios.md)

README category: Cheat / iOS jailbreak (on-device RE agents).

## Stack

SwiftUI deploy UI; embedded cross-compiled Node.js 26; official dsh web stack unmodified; workspace and health monitoring; background keep-alive; optional LAN bridge for remote UI access. (source: wiki/sources/descriptions/mzydgnh2__dsh-ios.md)

## Positioning

Complements desktop DSH tooling ([[dsh-rea-plugin]], [[dsh-rea-powerpack]], [[dsh-plugins]], [[dsh-ghidra]]) by bringing the same harness family to jailbroken iOS. Pair with [[trollstore]] sideload workflows and [[overviews/mobile-security]] iOS jailbreak lanes; agent-RE context in [[overviews/reverse-engineering]] DSH MCP cluster.

## Links

- Repo: https://github.com/mzydgnh2/dsh-ios

## Related

[[dsh-rea-plugin]] · [[dsh-rea-powerpack]] · [[dsh-plugins]] · [[trollstore]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
