---
title: AegisAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/projectsadameyd__AegisAC.md
  - wiki/sources/README-categories.md
updated: 2026-10-10
confidence: medium
---

# AegisAC

**AegisAC** (projectsadameyd/AegisAC) is a conservative, **alert-first** anti-cheat plugin for **Paper Minecraft 1.21.11** servers. Implemented in **Java 21**, it detects common client cheats through **server-side Bukkit event analysis** rather than packet-level simulation—emphasizing sustained evidence and staged sanctions before hard bans. (source: wiki/sources/descriptions/projectsadameyd__AegisAC.md)

README category: Anti Cheat / Open Source Anti Cheat System / game:minecraft.

## Architecture

Standard **Paper plugin** (no client mod): cheat signals come from **server-side Bukkit events**, not packet-level movement simulation—conservative **alert-first** defaults with combat and movement analyzers that accumulate heuristic scores until sustained evidence warrants escalation. (source: wiki/sources/descriptions/projectsadameyd__AegisAC.md)

## Detection surface

Movement and combat checks include **Speed**, **Fly**, **Timer**, **Reach**, **AutoClicker**, **FastPlace**, and **Velocity**. **Remote block break, placement, and interaction** beyond server-side reach are canceled to limit freecam-style abuse.

## Enforcement and ops

Staff receive alerts and console audit logs. Configurable **staged enforcement** runs from kicks through temporary login blocks; optional **permanent IP bans** are reserved for remote-interaction evidence. An optional **VPN pre-login gate** can reject joins using proxycheck.io.

## Positioning

Lightweight **Paper 1.21.11** operator tooling with explicit enforcement controls and appeal-friendly sanction ladders—beside modular stacks such as [[novaguard]] and [[h-ac]], Fabric offline-mode suites such as [[bastion]], and Meteor-targeted Paper plugins such as [[ultimate-meteor-anticheat]].

## Peers

[[bastion]] · [[novaguard]] · [[h-ac]] · [[ultimate-meteor-anticheat]] · [[minecraft-anticheat-list]]

## Links

- GitHub: https://github.com/projectsadameyd/AegisAC
