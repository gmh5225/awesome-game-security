---
title: Point Blank Linux
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/ertunc-ozbay__pointblank-linux.md
updated: 2026-10-17
confidence: medium
---

# Point Blank Linux

**pointblank-linux** (ertunc-ozbay) — standalone community **Rust** launcher with a **Slint** GUI and shell helpers that runs the Zepetto and TAM **Point Blank** Windows client on **GNU/Linux** using unmodified official game files and the native **CheatBlocker** anti-cheat, without bypassing or disabling protection. Manages an isolated Wine prefix, a TLS-aligned **Wine 11** or **Wine-GE** runner, and Winetricks provisioning for Visual C++ runtimes, DirectX 9 and 11 components, and Edge **WebView2** for login. Addresses game-specific compatibility (16-byte TLS alignment for DirectX 11, legacy D3DX9 shader DLLs, Linux asset-path symlinks) and verifies that official CheatBlocker binaries remain intact. Targets players and researchers who want legitimate Linux play and a reproducible Wine environment while preserving official anti-cheat behavior—not cheat development or AC evasion. (source: wiki/sources/descriptions/ertunc-ozbay__pointblank-linux.md)

Sits in the Wine/Proton **compatibility-with-AC-intact** lane beside [[proton]], GNU/Linux AC compatibility trackers such as [[are-we-anti-cheat-yet]] and [[aclist-github-io]], and Linux host tooling such as [[archmod]] and [[elden-ring-ct-tga]] that also depend on correct prefix/runner setup.

## Stack

- **Launcher:** Rust + Slint GUI; shell helpers for prefix/runner lifecycle.
- **Runtime:** Isolated Wine prefix; Wine 11 or Wine-GE with TLS alignment for D3D11.
- **Provisioning:** Winetricks — VC++ runtimes, DX9/DX11, WebView2.
- **Protection:** Unmodified CheatBlocker; integrity checks on official AC binaries.

## Links

- Repo: https://github.com/ertunc-ozbay/pointblank-linux [Rust standalone launcher to run Point Blank (Zepetto/TAM) on Linux with unmodified CheatBlocker anti-cheat via Wine-GE/Proton, TLS-aligned runner, and prefix setup]

## Related

[[proton]] · [[are-we-anti-cheat-yet]] · [[aclist-github-io]] · [[ac-compat-research]] · [[archmod]] · [[elden-ring-ct-tga]] · [[winehooks]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
