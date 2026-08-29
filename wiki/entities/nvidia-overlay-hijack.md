---
title: nvidia-overlay-hijack
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Calvin-LLC__nvidia-overlay-hijack.md
  - wiki/sources/descriptions/gmh5225__nvidia-overlay-hijack.md
updated: 2026-08-29
confidence: medium
---

# nvidia-overlay-hijack

**nvidia-overlay-hijack** (Calvin-LLC/nvidia-overlay-hijack) is a **DirectX 11 and Dear ImGui overlay sample** that renders a custom menu through the **NVIDIA GeForce Experience in-game overlay path**. Written in **C++** with helper drawing routines, menu animation logic, input handling, and **x86/x64** support, it focuses on practical overlay integration patterns rather than stealth and explicitly notes **anti-cheat detection risk**. Mainly used for graphics-hook experimentation, overlay prototyping, and cheat UI research. (source: wiki/sources/descriptions/Calvin-LLC__nvidia-overlay-hijack.md)

The technique hijacks NVIDIA's overlay render context to draw custom ESP or menu content **without creating new overlay windows**—reusing the vendor overlay surface to reduce anti-cheat monitoring for newly created overlay HWNDs. Useful for studying third-party NVIDIA overlay hijack techniques beside [[nvidia-overlay]], [[nvidia-overlay-renderer]], [[mwclap]], [[steam-overlay-x64]], and [[discord-overlay-hook]], not a maintained product. (source: wiki/sources/descriptions/gmh5225__nvidia-overlay-hijack.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| DirectX 11 | Target graphics API for overlay draw path |
| Dear ImGui | Custom in-game menu and debug UI |
| Helper draw routines | Reusable overlay rendering primitives |
| Menu animation + input | Interactive menu UX on the hijacked surface |
| x86/x64 | Dual-architecture build support |

See [[present-hook]] for swap-chain Present interception alternatives and [[imgui]] for the immediate-mode GUI substrate.

## Links

- Repo: https://github.com/Calvin-LLC/nvidia-overlay-hijack
- Mirror: https://github.com/gmh5225/nvidia-overlay-hijack

## Related

[[overviews/graphics-api]] · [[overviews/game-hacking]] · [[present-hook]] · [[imgui]] · [[nvidia-overlay]] · [[nvidia-overlay-renderer]] · [[mwclap]] · [[discord-overlay-hook]] · [[steam-overlay-x64]]
