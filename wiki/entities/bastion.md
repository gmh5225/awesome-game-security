---
title: Bastion
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/dhehdjebejen-beep__Bastion.md
  - wiki/sources/README-categories.md
updated: 2026-09-28
confidence: medium
---

# Bastion

**Bastion** (dhehdjebejen-beep/Bastion) is a **server-side security suite** for **Minecraft Fabric 1.21.11** that protects **offline-mode (cracked) servers** through three cooperating mods requiring **no client installation**. Written in **Java** with **Gradle**, modules integrate via soft reflection bridges so each can run standalone or together. (source: wiki/sources/descriptions/dhehdjebejen-beep__Bastion.md)

README category: Anti Cheat / game:minecraft.

## Modules

### BastionAuth

Hardened login and registration for offline-mode servers:

- **Argon2id** password hashing
- Pre-login **packet firewall**
- **TOTP** two-factor authentication
- Multi-account detection

### BastionClaims

Server-side **mixin-enforced land protection** against griefing vectors such as explosions, fluids, pistons, and hoppers.

### BastionAC

Anti-cheat engine with **38 outcome- and signature-based checks**, **buffered violation levels with decay**, and targeted coverage of **Meteor** and **Wurst** cheat clients. Includes lag compensation.

## Operations

In-game **staff panels**, configurable thresholds, and extensive **unit tests** support operator tuning and regression coverage.

## Positioning

Layered **Fabric server-side** stack for operators who need **account security**, **territory protection**, and **fair-play enforcement** on cracked/offline-mode hosts—distinct from Paper Bukkit-event plugins such as [[nova-anticheat]] and [[h-ac]], consent-based client visibility such as [[mcace]], and Meteor-targeted Paper plugins such as [[ultimate-meteor-anticheat]].

## Peers

[[nova-anticheat]] · [[h-ac]] · [[ultimate-meteor-anticheat]] · [[silent-anticheat]] · [[minecraft-anticheat-list]]

## Links

- Repo: https://github.com/dhehdjebejen-beep/bastion

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]]
