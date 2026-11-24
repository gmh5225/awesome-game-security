---
title: FIREAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/AmirrezaJaberi__FIREAC.md
updated: 2026-11-24
confidence: medium
---

# FIREAC

Free, lightweight **FiveM** anti-cheat **resource** (AmirrezaJaberi) pairing client- and server-side checks with a web admin panel and MySQL persistence. Primary implementation is **Lua** on CitizenFX; administration uses HTML/CSS/JavaScript with **oxmysql** for ban and configuration storage. (source: wiki/sources/descriptions/AmirrezaJaberi__FIREAC.md)

## Detection surface

**Client** monitors typical GTA V mod-menu abuse: god mode, teleporting, weapon and health tampering, spectating, noclip, and related trainer behaviors.

**Server** blocks spam, blacklisted events and explosions, injection, unauthorized admin actions, and similar exploit patterns.

## Operations

Integrates with **ESX**, **QBCore**, and standalone frameworks. Supports whitelisting, bans, **Discord webhook** notifications, and optional screenshot evidence via **discord-screenshot**.

## Audience

Targets **FiveM server owners and administrators** who want practical cheat deterrence and admin tooling without a heavy commercial anti-cheat stack—comparable niche to community Lua resources such as [[dead-anticheat]], with richer panel and framework integration.

## Links

- Repo: https://github.com/AmirrezaJaberi/FIREAC

## Related

[[dead-anticheat]] · [[phoenix-ac]] · [[mf-antiesp]] · [[fivem-backdoor-scanner]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]