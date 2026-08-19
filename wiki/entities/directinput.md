---
title: DirectInput (adspro15)
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/adspro15__DirectInput.md
updated: 2026-08-19
confidence: medium
---

# DirectInput (adspro15)

Windows C++ research project that simulates **keyboard and mouse input** by calling **keyboard/mouse class service routines** instead of standard user-mode APIs such as `SendInput`. Includes a kernel-mode driver and user-mode companion module, built with Visual Studio and the Windows Driver Kit. Demonstrates discovering keyboard and mouse class stacks, capturing service callbacks, and injecting input through low-level driver paths—useful for input-pipeline research in game automation and anti-cheat behavior analysis. (source: wiki/sources/descriptions/adspro15__DirectInput.md)

Not to be confused with the legacy **Microsoft DirectInput** game-controller API covered by compatibility proxies such as [[xidi]] and [[dxwrapper]].

Complements MouClass ServiceCallback PoCs such as [[mouseclassservicecallbacktrick]], keyboard injection samples such as [[karlann]], and KM↔UM IPC learning material such as [[km-um-communication]] from the same author when threat-modeling ring-0 input injection and related AC telemetry.

## Links

- Repo: https://github.com/adspro15/DirectInput

## Related

[[mouseclassservicecallbacktrick]] · [[mouseclassservicecallbackmeme]] · [[kernel-mouse]] · [[karlann]] · [[ntuserinjectmouseinput-syscall]] · [[km-um-communication]] · [[hardware-input-injection]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
