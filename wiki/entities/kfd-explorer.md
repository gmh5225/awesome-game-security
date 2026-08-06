---
title: kfd-explorer
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/hackcatml__kfd-explorer.md
updated: 2026-08-06
confidence: medium
---

# kfd-explorer

iOS kernel memory explorer (Python/Swift) for browsing and analyzing XNU kernel memory after obtaining kernel read/write. Targets game-security researchers and reverse engineers in the Cheat / iOS memory explorer lane—kernel-level memory inspection complementary to userland editors (H5GG, Flex) and hook frameworks such as [[xnuspy]]. (source: wiki/sources/descriptions/hackcatml__kfd-explorer.md)

Same maintainer as Android Zygisk dump tooling [[zygisk-memdump]]; pairs with XNU exploit study [[xnu-1day-practice]] and modern jailbreak/kernel-R/W trees [[dopamine]] / [[dirty-zero]] when the research question is live kernel layout rather than userland IPA or dylib hooks.

## Links

- Repo: https://github.com/hackcatml/kfd-explorer

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[xnuspy]] · [[xnu-1day-practice]] · [[zygisk-memdump]] · [[dopamine]] · [[dirty-zero]]
