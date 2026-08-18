---
title: Vocem Overlay
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/ales-drnz__vocem-overlay.md
updated: 2026-08-18
confidence: medium
---

# Vocem Overlay

Linux **in-game overlay** that renders Discord voice-channel members (speaking/mute status) and direct messages inside a title's own framebuffer instead of as a separate compositor window. C++ with a Qt/QML settings GUI; injects through a **Vulkan implicit layer** and an **OpenGL `LD_PRELOAD` interposer** (32- and 64-bit). A standalone daemon holds the Discord connection via localhost RPC and publishes voice state through shared memory—network access and avatar decoding stay out of injected code. Supports HDR swapchains, Flatpak-sandboxed games, common-launcher auto-detection, and live configuration without restarting the game. Useful for studying in-process graphics hooking and overlay injection surfaces that anti-cheat systems target; not tested against commercial anti-cheat and does not attempt to hide itself. (source: wiki/sources/descriptions/ales-drnz__vocem-overlay.md)

Contrasts with Windows Present/vtable overlays such as [[vulkan-hook]] and third-party hijacks such as [[discord-overlay-hook]]; sits beside other Linux Vulkan implicit-layer samples such as [[ayypex]].

## Links

- Repo: https://github.com/ales-drnz/vocem-overlay

## Related

[[present-hook]] · [[ayypex]] · [[vulkan-hook]] · [[discord-overlay-hook]] · [[kiero2]] · [[asdf-overlay]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
