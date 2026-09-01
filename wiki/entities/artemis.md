---
title: artemis
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/ArtemisDevGroup__Artemis.md
updated: 2026-09-01
confidence: medium
---

# artemis

**artemis** (ArtemisDevGroup/Artemis) is a **C++ game modification framework** targeting **Rainbow Six: Siege Shadow Legacy**. It ships injection and hooking infrastructure built around **ImGui** and **MinHook**, plus managers for events, keybinds, drawing, and game interactions. The architecture is modular so user-made extensions can plug into a shared framework rather than forking monolithic cheat code. Intended for cheat development and reverse-engineering experimentation under [[battleye]] on the Siege client. (source: wiki/sources/descriptions/ArtemisDevGroup__Artemis.md)

Sits in the R6 in-process internal lane beside [[r6-internal]], [[internal-rainbow-six-cheat-v3]], [[epic-r6-v9]], and [[r6table-internal]] as a modular cheat-base framework emphasizing extension hooks, ImGui UI, and MinHook-based interception rather than a single fixed feature set.

## Architecture

| Component | Role |
|-----------|------|
| Injection / hooking | In-process bring-up and API interception via MinHook |
| ImGui | In-game menu and draw pipeline |
| Event manager | Framework lifecycle and callback dispatch |
| Keybind manager | User-configurable input bindings |
| Draw manager | Overlay and visual feature scaffolding |
| Game interaction manager | Title-specific gameplay hooks and accessors |
| Extension model | Modular plug-in surface for user-made modules |

See [[present-hook]] for DXGI/D3D Present interception patterns and [[world-to-screen]] for ESP projection.

## Links

- Repo: https://github.com/ArtemisDevGroup/Artemis

## Related

[[r6-internal]] · [[internal-rainbow-six-cheat-v3]] · [[epic-r6-v9]] · [[r6table-internal]] · [[rainbow-six-cheat]] · [[present-hook]] · [[world-to-screen]] · [[battleye]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
