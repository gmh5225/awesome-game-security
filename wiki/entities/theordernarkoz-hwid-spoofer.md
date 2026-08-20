---
title: Hwid-Spoofer (Theordernarkoz)
kind: entity
topics: [game-hacking, anti-cheat, graphics-api, windows-kernel]
sources:
  - wiki/sources/descriptions/Theordernarkoz__Hwid-Spoofer.md
updated: 2026-08-20
confidence: medium
---

# Hwid-Spoofer (Theordernarkoz)

**Hwid-Spoofer** (Theordernarkoz) is a Windows desktop **HWID spoofer launcher** with a custom GUI. Written in C++, it uses **Dear ImGui** with **DirectX 9** for a simple interface that runs spoofing actions. The workflow downloads external **driver and helper binaries**, then executes a command-line step to apply spoofing changes. Intended for game **anti-cheat bypass** workflows, especially users who prefer a one-click front end. (source: wiki/sources/descriptions/Theordernarkoz__Hwid-Spoofer.md)

Distinct from the gmh5225 [[hwid-spoofer]] EAC/BattlEye kernel research sample and from the author's separate [[hwid--spoofer]] repo (`Hwid--Spoofer`), which embeds KMDF kernel spoof logic in-tree; this repo focuses on a usermode ImGui+DX9 launcher that orchestrates externally fetched driver/helper tooling.

Sits in the `Cheat > HWID` lane beside ImGui-loader HWID spoofer bases such as [[imgui-spoofer-leaked]] and [[hwid-spoofer-ud-fortnite-warzone-apex-rust-escape-from-tarkov-and-all-eac-be-games-imgui-loader-base]], kernel-mode samples such as [[easy-hwid-spoofer]] and [[hwid-spoofer-eac-be]], and Detection:HWID counterparts such as [[hwid-checker-mg]].

## Links

- Repo: https://github.com/Theordernarkoz/Hwid-Spoofer

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/graphics-api]] · [[imgui]] · [[imgui-spoofer-leaked]] · [[hwid--spoofer]] · [[hwid-spoofer]] · [[hwid-spoofer-eac-be]] · [[easy-hwid-spoofer]] · [[full-hwid-spoofer-v6]] · [[hwid-checker-mg]]
