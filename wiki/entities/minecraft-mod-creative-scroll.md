---
title: Scroll of Creative Mode (minecraft-mod-creative-scroll)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Ender3D__minecraft-mod-creative-scroll.md
updated: 2026-11-21
confidence: medium
---

# Scroll of Creative Mode (minecraft-mod-creative-scroll)

**Scroll of Creative Mode** (Ender3D/minecraft-mod-creative-scroll) is a **Minecraft Fabric** server mod that lets operators grant **temporary Creative Mode** through a consumable **admin-only scroll** instead of leaving `/gamemode` wide open. Written in **Java** with **Fabric Loader**, **Fabric API**, and **server-side Mixins**, enforcement runs at **tick** and **network packet** layers. Sessions use a **configurable timer** with **persistent countdowns** across disconnects and restarts; **inventory sandboxing** restores the player’s pre-session gear; **packet-level blocking** rejects disallowed creative spawns; and **container, drop, and smuggling restrictions** apply for the active session. Operators tune duration, blocked item lists, and expiry safety effects (e.g. **Slow Falling**), and can reload settings or end sessions via in-game commands. Targets multiplayer server moderation and game-security teams that need **controlled creative building** without economy abuse, duplication, or client-bypass exploits. (source: wiki/sources/descriptions/Ender3D__minecraft-mod-creative-scroll.md)

README category: Anti Cheat / game:minecraft.

## Enforcement model

- **Admin-issued scroll** — consumable grant path replaces open gamemode commands for creative privilege.
- **Timed sessions** — configurable duration; countdown survives disconnects and server restarts.
- **Inventory sandbox** — snapshots and restores pre-session gear when creative ends.
- **Packet spawn blocklist** — mixins block disallowed creative-item spawns at the network layer.
- **Container and drop isolation** — limits containers, drops, and item smuggling during an active session.
- **Operator commands** — reload config, end sessions, and tune blocklists without restarts.

Sandboxed creative sessions complement heuristic moderation mods such as [[cheatcheck]] and offline-mode security suites such as [[bastion]], and contrast with always-on Paper creative exemptions tuned in fly-focused plugins such as [[nofly]].

## Links

- Repo: https://github.com/Ender3D/minecraft-mod-creative-scroll

## Related

[[cheatcheck]] · [[bastion]] · [[vylorq-vigil]] · [[minecraft-anticheat-list]] · [[minecraft-anticheat-docs]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]