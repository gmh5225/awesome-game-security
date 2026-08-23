---
title: WebUI X Portable
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/MMRLApp__WebUI-X-Portable.md
updated: 2026-08-23
confidence: medium
---

# WebUI X Portable

**Standalone Android application** that hosts HTML and JavaScript **WebUI X** interfaces for **MMRL root modules**, letting users browse, install, configure, and interact with **Magisk**, **KernelSU**, **APatch**, and related modules without installing the full MMRL manager. Written in **Kotlin** with **Jetpack Compose**, it embeds a **HybridWebUI** engine and exposes a **JavaScript bridge** for root shell execution, filesystem access, and module metadata, plus built-in developer tools, module importers, and configuration editors. (source: wiki/sources/descriptions/MMRLApp__WebUI-X-Portable.md)

Supports **Magisk**, **KernelSU**, **KernelSU Next**, **APatch**, and **SukiSU**, with a **non-root portable mode** and optional **spoofed builds** that randomize package and app names—useful when disguising the host app helps evade detection by other software. Targets Android modders and root-module developers who need a lightweight WebUI runtime for module tooling. (source: wiki/sources/descriptions/MMRLApp__WebUI-X-Portable.md)

Sits in the Cheat / Android root module WebUI lane beside [[frida-rs]] (KernelSU module WebUI), [[rescuex]] (boot-recovery WebUI), and [[file-explorer]] (root module browser); requires or complements a supported root stack ([[magisk]], [[kernelsu]], [[apatch]]) or runs in limited non-root portable mode.

## Links

- Repo: https://github.com/MMRLApp/WebUI-X-Portable

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk]] · [[kernelsu]] · [[apatch]] · [[frida-rs]] · [[rescuex]] · [[rezygisk]] · [[file-explorer]] · [[nohello]]
