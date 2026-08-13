---
title: fortnite-external-cheat-source-code
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__Fortnite-External-Cheat-Source-Code.md
updated: 2026-08-13
confidence: medium
---

# fortnite-external-cheat-source-code

External Fortnite cheat source (gmh5225; cheat / game:fortnite). Out-of-process stack based on Vaselinikives' lineage: **DirectX 9 overlay rendering** with an **ImGui menu**, **world-to-screen** projection for ESP drawing, and a **basic aimbot** driven by standard **Win32 external memory reading** (no kernel driver in the described stack). Useful for studying user-mode external cheat architecture, legacy D3D9 overlay paths, and [[world-to-screen]]-based ESP on [[easy-anti-cheat]]-protected Fortnite clients. (source: wiki/sources/descriptions/gmh5225__Fortnite-External-Cheat-Source-Code.md)

Sits beside other user-mode external Fortnite samples such as [[fortnite-external-p2c]], driver-backed bases such as [[fortnite-external-base-source]] and [[fortnite-external-cheat-winsense-leak]], and [[fortnite-external]].

## Links

- Repo: https://github.com/gmh5225/Fortnite-External-Cheat-Source-Code

## Related

[[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[fortnite-external-p2c]] · [[fortnite-external-base-source]] · [[fortnite-external-cheat-winsense-leak]] · [[fortnite-external]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
