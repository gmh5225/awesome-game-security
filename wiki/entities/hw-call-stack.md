---
title: hw-call-stack
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/fortra__hw-call-stack.md
updated: 2026-08-15
confidence: medium
---

# hw-call-stack

Windows **hardware-breakpoint (HWBP) call-stack spoofer** from Fortra that uses **x86 debug registers (DR0–DR7)** to forge thread call stacks during **syscalls and API calls**. Written in C/C++; aimed at game-security researchers and reverse engineers studying offensive cheat / spoof-stack tradecraft in the `Cheat > Spoof Stack` / `[HWBP]` lane. (source: wiki/sources/descriptions/fortra__hw-call-stack.md)

Contrasts with return-address patching libraries such as [[spoof-stack-safecall]] and assembly-trampoline PoCs such as [[callstackspoofer-2]] by driving stack presentation through debug-register breakpoints rather than manual frame rewriting. Anti-cheat surfaces include DR7 inspection, VEH-based hardware-breakpoint checks (e.g. [[como-funciona-vac]]), and shadow-stack correlation via [[shadow-stack-walk]].

## Links

- Repo: https://github.com/fortra/hw-call-stack

## Related

[[stack-spoofing]] · [[spoof-stack-safecall]] · [[callstackspoofer-2]] · [[thread-stack-spoofer]] · [[silent-moonwalk]] · [[pwatch]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
