---
title: xnu_1day_practice
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/wh1te4ever__xnu_1day_practice.md
updated: 2026-08-04
confidence: medium
---

# xnu_1day_practice

Hands-on XNU (macOS/iOS) kernel one-day vulnerability practice: writeups and working exploit PoCs for historical CVEs (README notes CVE-2019 through CVE-2025 examples such as 30883, 24153, 24257, 43510, 43520, plus [[coruna]]/PEGruber research). Covers voucher/Mach IPC, IOSurface and IOAccelerator bugs, and KRW primitives in C/Objective-C, with root-cause notes, Mach/MIG/IPC voucher prerequisites, fakeport and OOL message techniques, and kernel-base discovery helpers. Lab/educational Apple kernel exploitation study—not for malicious use. (source: wiki/sources/descriptions/wh1te4ever__xnu_1day_practice.md)

Pairs with same-author DarkSword KRW playground [[darksword-kexploit-fun]], iOS 14 KRW app [[humptylock]], and adjacent iOS kernel/jailbreak trees [[coruna]], [[dirty-zero]], [[lara]], [[lightsaber]], [[dopamine2-roothide]], [[oob-entry]], [[cve-2026-xnu-aio-kevent-uaf]] (XNU `kern_aio.c` AIO+kevent UAF; iOS 26.2).

## Links

- Repo: https://github.com/wh1te4ever/xnu_1day_practice

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[coruna]] · [[dirty-zero]] · [[darksword-kexploit-fun]] · [[humptylock]] · [[lara]] · [[lightsaber]] · [[dopamine2-roothide]] · [[oob-entry]] · [[cve-2026-xnu-aio-kevent-uaf]]
