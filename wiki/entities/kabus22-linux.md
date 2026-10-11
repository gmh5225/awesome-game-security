---
title: Kabus 22 Linux
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/sergen213__kabus22-linux.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: medium
---

# Kabus 22 Linux

**kabus22-linux** (sergen213/kabus22-linux) is a **reverse-engineered native Linux** implementation of the *Kabus 22* game engine: a standalone runtime that loads the player’s **legally owned** original scripts and assets without Wine or the Windows binary. Listed under README **Cheat / RE Tools** as engine-port research—not a redistributable game build. (source: wiki/sources/descriptions/sergen213__kabus22-linux.md)

## Runtime stack

Core is **C++20** with **CMake**, centered on a **WDL script runtime**, **ODE** physics, **SDL2** windowing, and **FFmpeg** media. Rendering supports **OpenGL** or **Vulkan** with optional hardware ray tracing, PBR, and **FSR** upscaling. (source: wiki/sources/descriptions/sergen213__kabus22-linux.md)

## Distribution and tooling

Ships a **GTK** installer, launcher, and **Ed25519-signed** updater for native Linux deployment. Documentation covers executable layout, data structures, and resource formats discovered during RE. (source: wiki/sources/descriptions/sergen213__kabus22-linux.md)

## Audience

Targets reverse engineers, engine porters, and researchers studying legacy Windows titles on Linux from user-supplied retail media—similar preservation lanes to [[omikron-tns-omk-engine]] and console static-recomp projects such as [[saturnkit]] and [[motorstorm-mv-recomp]]. (source: wiki/sources/descriptions/sergen213__kabus22-linux.md)

## Links

- Repo: https://github.com/sergen213/kabus22-linux

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[concepts/static-runtime-evidence]] · [[motorstorm-mv-recomp]]
