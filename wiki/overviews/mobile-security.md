---
title: Mobile Security
kind: overview
topics: [mobile-security]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md
  - wiki/sources/descriptions/zhuowei__cheese.md
  - wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md
updated: 2026-07-17
confidence: high
---

# Mobile Security

Android and iOS game security: APK/IPA analysis, native/IL2CPP reversing, root/jailbreak ecosystems, dynamic instrumentation ([[frida]]), and mobile anti-cheat (root/Frida/emulator detection). (source: wiki/sources/skills/mobile-security.md)

## Key sub-areas

**Android:** apktool/jadx (agent-facing apktool via [[apktool-mcp-server]] MCP tools) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md), Magisk / KernelSU / APatch (e.g. [[cheese]] Magisk install on Quest 3/3S via Adreno CVE-2025-21479, no boot-partition rewrite) (source: wiki/sources/descriptions/zhuowei__cheese.md), Zygisk modules, ART/syscall hooks, eBPF tracers, kernel drivers, ACE/AppSealing-class protectors; agent-facing HTTP/HTTPS capture via [[android-proxy-mcp]] (mitmdump + SQLite + NL query) (source: wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md).

**iOS:** jailbreak tooling, class-dump, Logos hooks, sideloading / AltStore for non-jailbreak paths.

**Unity/Unreal mobile:** [[il2cpp]] (`libil2cpp.so` / UnityFramework + metadata), SDK dumps, memory editors (GameGuardian, H5GG).

## Related concepts

[[frida]] · [[il2cpp]] · [[apktool-mcp-server]] · [[android-proxy-mcp]] · [[cheese]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]

## README map

Cheat Magisk/Xposed/Frida/ART-syscall hooks/Android kernel*/Cellular-SIM/iOS jailbreak+network trees; Anti Cheat Detection:Android root; `WSA`, `Android Emulator`, `IOS Emulator` platform categories. (source: wiki/sources/README-categories.md)
