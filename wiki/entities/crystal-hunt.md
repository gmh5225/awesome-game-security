---
title: Crystal-Hunt
kind: entity
topics: [anti-cheat, mobile-security, game-engine]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/worstpoetGIT__Crystal-Hunt.md
updated: 2026-10-18
confidence: medium
---

# crystal-hunt

**Unity** mobile **location-aware** multiplayer sample where players move on a real-world map, encounter others, and compete for crystal objectives. Primary stack is **C#** on **2D URP** with **Mapbox** for map rendering and geospatial overlays. **Firebase Authentication** and **Realtime Database** back accounts and shared game state; **Firebase App Check** hardens backend access against tampered clients. Custom networking combines **WebSocket** support with lobby, session, and debug HUD utilities, plus a **client simulator** and **unit tests** to exercise win conditions and game flow without live devices. Demonstrates **host-authoritative** **UDP** with **host-side movement speed clamping** as a lightweight cheat deterrent. Listed under Anti Cheat beside design-reference samples such as [[adaptive-boss-arena]], [[gatewarden-public]], and [[blastscale]]. (source: wiki/sources/descriptions/worstpoetGIT__Crystal-Hunt.md)

## Security / networking notes

Host-authoritative UDP with host-side speed clamping; Firebase App Check on cloud reads/writes; GPS permission and lobby/session flow suitable for studying location-spoof and movement-cheat surfaces on mobile.

## Links

- Repo: https://github.com/worstpoetGIT/Crystal-Hunt

## Related

[[adaptive-boss-arena]] · [[blastscale]] · [[gatewarden-public]] · [[guard-game]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[overviews/game-engine]]
