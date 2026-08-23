---
title: APICallProxy
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/MahmoudZohdy__APICallProxy.md
updated: 2026-08-23
confidence: medium
---

# APICallProxy

Windows **API call obfuscation** framework (MahmoudZohdy; C/C++). Routes user-mode operations through a kernel driver: file, process, memory, registry, and network actions are exposed via **DeviceIoControl** IOCTL handlers instead of direct Win32/NT API calls. Sample clients demonstrate APC-based injection, driver loading, and socket communication workflows. Intended for low-level security research and controlled experiments on **API monitoring evasion** and behavioral-analysis hardening. (source: wiki/sources/descriptions/MahmoudZohdy__APICallProxy.md)

README lane: **Windows API Call Obfuscation** — kernel-proxied API dispatch for usermode behavioral-telemetry evasion study.

Complements static import obfuscation such as [[iat-obfuscation]] and [[call-obfuscator]], KM↔UM IPC learning samples such as [[km-um-communication]], and IOCTL interface RE tooling such as [[ioctlpus]]. Same author as [[process-injection-techniques]].

## Links

- Repo: https://github.com/MahmoudZohdy/APICallProxy

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[iat-obfuscation]] · [[call-obfuscator]] · [[km-um-communication]] · [[ioctlpus]] · [[process-injection-techniques]]
