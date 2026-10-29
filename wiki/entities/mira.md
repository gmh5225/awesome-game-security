---
title: Mira
kind: entity
topics: [anti-cheat, mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/vw2x__Mira.md
  - wiki/sources/README-categories.md
updated: 2026-10-29
confidence: medium
---

# Mira

**Mobile runtime detection workbench** for iOS and Android that turns live device cases into reusable workflows and detection notes. Host apps expose sandboxed shell, PTY, screen capture, and file tooling; **Frida** supports Java and native hooks with RPC for one-off runtime analysis. A Python relay server and web console connect devices over LAN or relay exposure, and an **MCP server** lets AI assistants operate in the same remote sessions. Stack spans Android Java, iOS Swift with an iSH compatibility layer, shared native PTY code, and a Next.js control UI. Targets mobile security researchers, reverse engineers, and integrity or anti-cheat teams exploring side channels such as root, emulator, projection, Magisk, LSPosed, and jailbreak indicators beside classic Frida-detection samples. (source: wiki/sources/descriptions/vw2x__Mira.md)

## Architecture

| Layer | Role |
|-------|------|
| Host apps | Android (Java) and iOS (Swift + iSH compatibility layer): sandboxed shell, PTY, screen capture, file tooling on live devices |
| Frida tasks | Java and native hooks with RPC for ad hoc runtime analysis |
| Relay + console | Python relay server and Next.js web UI; devices over LAN or relay exposure |
| MCP | AI assistants share the same remote device sessions as human operators |

Documented case library emphasizes environment and instrumentation side channels (root, emulator, screen projection, Magisk, LSPosed, jailbreak) for defender-side signal design and red-team validation—not a shipped game AC product.

## Links

- Repo: https://github.com/vw2x/Mira (README: Anti Cheat → Detection:Frida)

## Related

[[frida]] · [[detect-frida]] · [[mobile-anti-cheat]] · [[lamda]] · [[rootraven]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
