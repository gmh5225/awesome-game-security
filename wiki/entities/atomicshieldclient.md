---
title: AtomicShield Client
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/adem-hosni__AtomicShieldClient.md
updated: 2026-08-19
confidence: medium
---

# AtomicShield Client

Windows anti-cheat client that connects player machines to an AtomicShield server, focused on **FiveM** game protection. Combines a C#/.NET tray agent (WinForms + WebView2 dashboard) that downloads updates and talks to the backend over encrypted HTTP APIs with a native C++ anti-cheat engine. (source: wiki/sources/descriptions/adem-hosni__AtomicShieldClient.md)

## Architecture

- **Agent** — C#/.NET WinForms tray UI and WebView2 operator dashboard; encrypted HTTP for updates and backend comms.
- **Engine** — native C++ runtime with process, module, heuristic, and manual-mapping guards; anti-debugging; hardware ID collection; screenshots; WebSocket networking; AES and related crypto in shared libraries.
- **Loaders** — **EngineLoader** and **RuntimeLoader** use in-process manual mapping and named pipes to load and run the engine without standard module load paths.

Primary use case: client-side game anti-cheat for operators who need monitoring, integrity checks, and server-backed enforcement on Windows players.

## Links

- Repo: https://github.com/adem-hosni/AtomicShieldClient

## Related

[[certael]] · [[sentinelac]] · [[windfall-anticheat]] · [[faultline]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
