---
title: MouseClassServiceCallbackMeme (ekknod)
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/ekknod__MouseClassServiceCallbackMeme.md
updated: 2026-08-16
confidence: medium
---

# MouseClassServiceCallbackMeme (ekknod)

C Windows kernel research centered on the **MouseClassServiceCallback** meme — a sibling PoC lane to [[mouseclassservicecallbacktrick]] for invoking or abusing the MouClass service callback to inject mouse input from ring 0 without user-mode APIs such as `SendInput` or win32k injection syscalls. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / **triggerbot & aimbot** area. (source: wiki/sources/descriptions/ekknod__MouseClassServiceCallbackMeme.md)

Complements MouClass filter-driver samples such as [[kernel-mouse]], vendor-driver HID paths such as [[logitech-cve]], and user-mode win32k reference material such as [[ntuserinjectmouseinput-syscall]] when threat-modeling kernel mouse input injection and related AC telemetry.

## Links

- Repo: https://github.com/ekknod/MouseClassServiceCallbackMeme

## Related

[[mouseclassservicecallbacktrick]] · [[kernel-mouse]] · [[logitech-cve]] · [[ntuserinjectmouseinput-syscall]] · [[hardware-input-injection]] · [[human-mouse-movement]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
