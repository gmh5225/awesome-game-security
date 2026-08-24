---
title: MouseClassServiceCallbackTrick (ekknod)
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/ekknod__MouseClassServiceCallbackTrick.md
updated: 2026-08-16
confidence: medium
---

# MouseClassServiceCallbackTrick (ekknod)

C Windows kernel research centered on the **MouseClassServiceCallback** trick — invoking or abusing the MouClass service callback to inject mouse input from ring 0 without user-mode APIs such as `SendInput` or win32k injection syscalls. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / **triggerbot & aimbot** lane. (source: wiki/sources/descriptions/ekknod__MouseClassServiceCallbackTrick.md)

Complements MouClass filter-driver samples such as [[kernel-mouse]], vendor-driver HID paths such as [[logitech-cve]], user-mode win32k reference material such as [[ntuserinjectmouseinput-syscall]], and defensive callback hook-detection PoCs such as [[detect-mouseclassservicecallback]] when threat-modeling kernel mouse input injection and related AC telemetry.

## Links

- Repo: https://github.com/ekknod/MouseClassServiceCallbackTrick

## Related

[[mouseclassservicecallbackmeme]] · [[detect-mouseclassservicecallback]] · [[kernel-mouse]] · [[logitech-cve]] · [[ntuserinjectmouseinput-syscall]] · [[hardware-input-injection]] · [[human-mouse-movement]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
