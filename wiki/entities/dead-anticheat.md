---
title: Dead-Anticheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Dead-Scripts__Dead_antiCheat.md
updated: 2026-09-01
confidence: medium
---

# Dead-Anticheat

**FiveM server resource** (Dead-Scripts) that detects and blocks common mod-menu and cheat behavior on **GTA V** multiplayer roleplay servers. Written in **Lua** as a client–server **CitizenFX** script. (source: wiki/sources/descriptions/Dead-Scripts__Dead_antiCheat.md)

## Detection surface

Client-side monitors include noclip, spectating, fake chat messages, blacklisted props and peds, godmode, infinite ammo, unauthorized weapons, and injected Lua commands or mod-menu globals. Server-side logic enforces bans through a JSON ban list, logs detections to **Discord webhooks** with optional screenshots, and supports configurable blacklists for events, keys, commands, and entity models. Staff bypass permissions are included; entity enumeration and client integrity checks draw on community anticheat techniques.

## Audience

Targets **FiveM server operators** who need lightweight, configurable protection against modders and exploit abuse—server-authoritative checks rather than a native Windows client AC stack.

## Links

- Repo: https://github.com/Dead-Scripts/Dead_antiCheat

## Related

[[atomicshieldclient]] · [[gvmp-anticheat]] · [[phake]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
