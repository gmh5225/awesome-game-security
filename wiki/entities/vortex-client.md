---
title: Vortex Client
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Marcinator31__Vortex-Client.md
  - wiki/sources/README-categories.md
updated: 2026-09-28
confidence: medium
---

# Vortex Client

**Vortex Client** (Marcinator31/Vortex-Client) is an open-source **Fabric** mod for **Minecraft Java Edition 1.21.11** that extends the game client with configurable HUD elements, ESP, waypoints, skins, and performance tools managed through an in-game menu. Built in **Java** with **Fabric Loader**, **Mixins**, and **Gradle**, it includes combat overlays, projectile path previews, base-hunting helpers, freecam, macros, and shareable preset profiles. Combat-automation modules such as aimbot, auto-totem, fly, and no-fall are exposed but explicitly marked by maintainers as easily detected by anti-cheat systems. Targets Minecraft modding audiences and game-security researchers studying client-side rendering hooks, information overlays, and how cheat-adjacent features are implemented and flagged. (source: wiki/sources/descriptions/Marcinator31__Vortex-Client.md)

README category: Cheat / game:minecraft.

## Architecture

| Component | Role |
|-----------|------|
| Fabric Loader + Mixins | In-process bytecode hooks for rendering, input, and game state |
| In-game menu | Configurable HUD, ESP, waypoints, skins, performance tools |
| Preset profiles | Shareable configuration bundles for module sets |
| Combat overlays | Projectile path previews, base-hunting helpers, automation modules |

## Anti-cheat interaction

Maintainers label combat-automation modules (aimbot, auto-totem, fly, no-fall) as **easily detected**—useful as a reference for how obvious client-side automation surfaces to server-side plugins such as [[grim]], [[windfall-anticheatf]], and [[uagc]], and for contrast with AC-aware timing in mods such as [[dino-printer]]. Information overlays (ESP, waypoints, freecam) sit in the same client-render hook lane as utility clients such as [[epsilon]] and [[lenrete-mod]]. (source: wiki/sources/descriptions/Marcinator31__Vortex-Client.md)

## Links

- Repo: https://github.com/Marcinator31/Vortex-Client

## Related

[[epsilon]] · [[lenrete-mod]] · [[dino-printer]] · [[anticheat-qa]] · [[grim]] · [[windfall-anticheatf]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
