---
title: android-re-mcp
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/FlyPhantomFly__android-re-mcp.md
updated: 2026-11-23
confidence: medium
---

# android-re-mcp

PyPI-distributed **MCP (Model Context Protocol) server** (Python 3.11+) that wires AI assistants to a **live Android device** and target APK for end-to-end reverse engineering. It exposes dozens of structured tools covering static analysis (apktool, jadx, androguard, apkid, apkleaks, quark-engine), dynamic hooking with [[frida]] and bundled bypass scripts, DEX/smali and native ELF patching, mitmproxy traffic capture, and APK signing plus reinstall workflows. Built-in RASP/packer identification, guided assessment prompts, and knowledge resources cover protections such as SSL pinning, root and Frida detection, and obfuscation. Aimed at mobile security researchers, malware analysts, and game-security practitioners who want an LLM-driven workflow over real hardware instead of ad hoc CLI scripting. (source: wiki/sources/descriptions/FlyPhantomFly__android-re-mcp.md)

Broader than single-purpose MCP bridges such as [[apktool-mcp-server]] (apktool decode/rebuild) or [[delamain]] (jadx decompile/xrefs/Frida hooks) and wider than traffic-only [[android-proxy-mcp]] — one server orchestrates static, dynamic, patch, capture, and protection-assessment lanes on a connected device.

## Links

- Repo: https://github.com/FlyPhantomFly/android-re-mcp

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apktool-mcp-server]] · [[delamain]] · [[android-proxy-mcp]] · [[jadx]] · [[frida]] · [[apkid]]