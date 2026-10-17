---
title: deadlocked
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/avitran0__deadlocked.md
updated: 2026-10-17
confidence: medium
---

# deadlocked

**Linux-only external Counter-Strike 2** assistant in Rust that reads live game state from the running client process and drives an on-screen overlay. The workspace maps CS2 shared libraries, resolves **schema-based offsets**, and implements combat and visual aids (aimbot, recoil control, triggerbot, ESP-style player/world rendering, flash/smoke tweaks, grenade lineup helpers). Map geometry is built from the game physics **BVH** for visibility checks and hitbox ray tests; the HUD uses **egui** and OpenGL. Match data can stream to a companion **web radar** (Rust TCP/WebSocket server + TypeScript front end). Releases, **uinput** setup, and an update checker are documented upstream. Aimed at game security researchers and reverse engineers studying external Linux cheat architecture, memory layout, and feature design—not a minimal PoC. (source: wiki/sources/descriptions/avitran0__deadlocked.md)

Complements other Linux CS2 externals such as [[counterstrike2-linux-cheat]] and Rust overlay stacks such as [[proext]]; shares offset/schema concerns with [[cs2-dumper]] and [[cs2-offsets]]; web-radar lane overlaps [[cs2-webradar]].

## Links

- Repo: https://github.com/avitran0/deadlocked

## Related

[[counterstrike2-linux-cheat]] · [[proext]] · [[cs2-webradar]] · [[cs2-dumper]] · [[cs2-offsets]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
