---
title: windows_kernel_shadow_stack
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/synacktiv__windows_kernel_shadow_stack.md
updated: 2026-07-21
confidence: medium
---

# windows_kernel_shadow_stack

Synacktiv research on Windows kernel-mode shadow stacks under Intel CET (Control-flow Enforcement Technology). Documents how Windows implements KM shadow stacks, interaction with [[patchguard]], and potential bypass or weakening scenarios—covering KVAS shadow-stack initialization, exception handling, and compatibility with existing kernel exploitation techniques. Aimed at researchers studying CET’s impact on kernel exploitation and Windows hardening under the README `Windows Security Features` / Shadow Stack lane. (source: wiki/sources/descriptions/synacktiv__windows_kernel_shadow_stack.md)

Pairs with broader CET material such as [[cet-research]] when modeling how hardware-enforced stacks raise the cost of ROP-style control-flow abuse alongside VBS/[[hvci]].

## Links

- Repo: https://github.com/synacktiv/windows_kernel_shadow_stack (README tag: Shadow Stack)

## Related

[[cet-research]] · [[patchguard]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
