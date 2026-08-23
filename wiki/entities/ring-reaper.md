---
title: Ring Reaper
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/MatheuZSecurity__RingReaper.md
updated: 2026-08-23
confidence: medium
---

# Ring Reaper

**Linux post-exploitation agent** (MatheuZSecurity) designed to minimize detection by routing most I/O through **io_uring** instead of traditional read, write, send, and receive syscalls. The agent is primarily **C** with a **Python control server**, replacing many conventional syscall paths with asynchronous kernel I/O primitives. Command features include **file transfer**, **process and user enumeration**, **network inspection**, and **session control** while keeping data flow on io_uring backends. Intended for **offensive security research** and **EDR evasion testing** in controlled, authorized environments. (source: wiki/sources/descriptions/MatheuZSecurity__RingReaper.md)

Complements MatheuZSecurity Linux rootkit research such as [[rootkit]] and defensive hook-tampering monitors such as [[ksentinel]], plus broader Linux runtime-security platforms such as [[tracee]].

## Links

- Repo: https://github.com/MatheuZSecurity/RingReaper [Linux post-exploitation agent that uses io_uring to stealthily bypass EDR detection by avoiding traditional syscalls]

## Related

[[rootkit]] · [[ksentinel]] · [[tracee]] · [[forensia]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
