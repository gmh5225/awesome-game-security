---
title: Goodmans Kernel
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/zer0condition__GoodmansKernel.md
updated: 2026-08-19
confidence: medium
---

# Goodmans Kernel

Signed Windows **WDM driver** that embeds the **wasm3** WebAssembly interpreter to load unsigned **wasm32** modules and expose direct FFI to NT/HAL kernel exports. Developers write kernel logic in C or Rust, compile to WebAssembly, and hot-load modules through IOCTLs without rebuilding or re-signing the driver on each iteration. (source: wiki/sources/descriptions/zer0condition__GoodmansKernel.md)

Key capabilities include per-module permission manifests, SEH-guarded kernel memory access, **InfinityHook** trampolines, process and image notify callbacks, watchdog and trace rings, plus CLI, Qt6 GUI, and WinDbg tooling. Built in C/C++ with Visual Studio and the WDK; targets **HVCI-compliant** kernel research, reverse engineering, and game-security scenarios such as hooking, process tracing, and introspection.

Complements register-machine bytecode VMs such as [[gexec]] and scripting hosts such as [[ntlua]] with a WebAssembly hot-load lane; uses [[infinityhook]] for ETW-backed syscall trampolines.

## Links

- Repo: https://github.com/zer0condition/GoodmansKernel

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[hvci]] · [[infinityhook]] · [[gexec]] · [[kernel-callbacks]] · [[ntmemory]]
