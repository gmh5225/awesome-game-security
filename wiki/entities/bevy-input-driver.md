---
title: Bevy Input Driver
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/halfdeadgames__bevy_input_driver.md
  - wiki/sources/README-categories.md
updated: 2026-11-25
confidence: medium
---

# Bevy Input Driver

Rust **Bevy 0.20** plugin ([halfdeadgames/bevy_input_driver](https://github.com/halfdeadgames/bevy_input_driver)) that drives a live Bevy game for automated playtesting: scripted or live keyboard, mouse, scroll, touch, and gesture injection, screenshots, deterministic seeds, virtual time, frame stepping, and save-state hooks. README **Game Testing**. (source: wiki/sources/descriptions/halfdeadgames__bevy_input_driver.md)

## Control plane

- **Bevy Remote Protocol (BRP):** HTTP JSON-RPC on localhost for live command batches.
- **JSONL:** script file at launch for offline replay-style runs.
- **Python helper:** send command batches and wait on completion. (source: wiki/sources/descriptions/halfdeadgames__bevy_input_driver.md)

## Input fidelity

Injected events mirror real winit-style `WindowEvent` and `bevy_input` message pairs so picking and UI behave normally while the OS cursor stays put by default—**in-process** injection rather than OS-level automation (contrasts with stacks such as [[llm-game-automation-mcp]]). (source: wiki/sources/descriptions/halfdeadgames__bevy_input_driver.md)

## Repeatability

Deterministic seeds, virtual time control, frame stepping, save/load hooks, and status reporting support repeatable end-to-end gameplay and UI-flow tests. Targets game developers and security researchers who need faithful input-path exercise without external SendInput-style tooling. (source: wiki/sources/descriptions/halfdeadgames__bevy_input_driver.md)

## Links

- Repo: https://github.com/halfdeadgames/bevy_input_driver

## Related

[[bevy]] · [[bevy-personal-test]] · [[playgoblin]] · [[imgui-test-engine]] · [[airtest]] · [[pz-devharness]] · [[overviews/game-engine]]