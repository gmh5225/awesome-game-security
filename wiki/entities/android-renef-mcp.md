---
title: android-renef-mcp
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/FlyPhantomFly__android-renef-mcp.md
updated: 2026-11-25
confidence: medium
---

# android-renef-mcp

Python **MCP (Model Context Protocol) server** that lets LLM agents drive **Renef** — a Frida-like dynamic instrumentation stack for **rooted Android ARM64** — over **ADB port forwarding** to `renef_server`. The server deploys and manages the on-device agent lifecycle, then exposes tools to attach or spawn processes, run **Lua** in the target, hook native and Java methods, scan and patch memory, and capture hook or strace output. Bundled Lua examples and a technique knowledge base focus on **SSL pinning** bypass patterns across native Android, Flutter, React Native, Unity, Xamarin, and similar stacks. Targets mobile security research, reverse engineering, and anti-tampering or anti-cheat analysis where **Lua-based in-process instrumentation** is preferred over Frida-style JavaScript on the device. (source: wiki/sources/descriptions/FlyPhantomFly__android-renef-mcp.md)

Complements sibling [[android-re-mcp]] (broader live-device APK RE orchestration with apktool/jadx/Frida/mitmproxy) by specializing in **agent-driven Renef dynamic hooking** rather than full static+dynamic RE pipelines.

## Links

- Repo: https://github.com/flyphantomfly/android-renef-mcp

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[android-re-mcp]] · [[frida]] · [[android-proxy-mcp]]