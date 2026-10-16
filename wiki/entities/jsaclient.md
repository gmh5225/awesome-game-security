---
title: JSA Client
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/bliper2__jsaclient.md
updated: 2026-10-16
confidence: medium
---

# JSA Client

Multi-version **Minecraft Java** utility toolkit aimed at **single-player** and **open LAN** play, covering client releases from **1.6.4** through **26.3**. Built as a **Gradle** multi-module Java project: a version-agnostic **core** exposes movement, combat, render, player, and prank modules through a **platform abstraction**, **event bus**, and **ClickGUI**. A **reflective loader** adapts to arbitrary Minecraft client JARs on the classpath using era maps and capability gates; an optional **Fabric** layer applies **mixins** for a pinned release (default **1.20.1**) and can integrate with **Meteor Client** to surface external addon modules. Useful for studying client-side mod architecture, cross-era version compatibility, and how features degrade when APIs differ; the project explicitly does **not** target anti-cheat bypass on public servers. (source: wiki/sources/descriptions/bliper2__jsaclient.md)

## Architecture

| Component | Role |
|-----------|------|
| Gradle core / fabric / loader | Multi-module layout separating portable logic from platform hooks |
| Platform abstraction + event bus | Module hooks without hard-coding one Minecraft version |
| Reflective loader | Classpath JAR adaptation via era maps and capability gates |
| Fabric + mixins | Pinned-release integration (default 1.20.1) |
| Meteor integration | Lists external addon modules when Meteor is present |

## Links

- Repo: https://github.com/bliper2/jsaclient

## Related

[[epsilon]] · [[lenrete-mod]] · [[vortex-client]] · [[dino-printer]] · [[chanhne-dev-anticheat]] · [[overviews/game-hacking]]
