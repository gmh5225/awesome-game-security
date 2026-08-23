---
title: Bevy
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/bevyengine__bevy.md
  - wiki/sources/descriptions/cBournhonesque__lightyear.md
updated: 2026-08-23
confidence: medium
---

# Bevy

Refreshingly simple, data-driven game engine built in Rust — free and open-source. Aimed at game developers, engine programmers, and graphics researchers studying a modern ECS-centric engine codebase (rendering, scheduling, asset pipeline) in the README **Game Engine → Source** lane rather than a cheat or anti-cheat artifact. (source: wiki/sources/descriptions/bevyengine__bevy.md)

Anchors the Rust open-source engine lane cited elsewhere: multi-engine agent stacks such as [[godogen]] and skill routers such as [[awesome-gamedev-agent-skills]] fingerprint Bevy alongside Godot/Unity/Unreal for AI-assisted authoring. Security-oriented Bevy testbeds such as [[bevy-personal-test]] (rollback netcode, shadow-VM Wasm checks, Rhai sandbox VM, server replay validation) extend that lane for tamper-resistant multiplayer prototyping. Production netcode library [[lightyear]] (server-authoritative replication, prediction/rollback, lag compensation, WebTransport/wasm; Game Network / source) complements those testbeds for authoritative multiplayer and client-server trust-boundary study. (source: wiki/sources/descriptions/cBournhonesque__lightyear.md)

## Links

- Repo: https://github.com/bevyengine/bevy (README: [Rust])

## Related

[[bevy-personal-test]] · [[lightyear]] · [[godogen]] · [[awesome-gamedev-agent-skills]] · [[raylib]] · [[bgfx]] · [[godot]] · [[overviews/game-engine]] · [[overviews/graphics-api]]
