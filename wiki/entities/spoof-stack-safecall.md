---
title: spoof-stack-SafeCall
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__spoof-stack-SafeCall.md
updated: 2026-08-07
confidence: medium
---

# spoof-stack-SafeCall (SafeCall)

**SafeCall** is a Windows **return-address spoofing library** that rewrites the call stack before sensitive API calls: real return addresses are replaced with fake but legitimate-looking module return addresses so stack walks and call-origin analysis cannot reveal the true caller. Targets EDR stack-based detection and anti-cheat thread stack inspection; aimed at red-team operators and game-security researchers studying stack spoofing and its detection. (source: wiki/sources/descriptions/gmh5225__spoof-stack-SafeCall.md)

Sits in the `Cheat > Spoof Stack` lane beside illustrative samples such as [[return-address-spoofer]], thread call-stack PoCs such as [[thread-stack-spoofer]], and research PoCs such as [[silent-moonwalk]].

## Links

- Repo: https://github.com/gmh5225/spoof-stack-SafeCall

## Related

[[stack-spoofing]] · [[return-address-spoofer]] · [[thread-stack-spoofer]] · [[silent-moonwalk]] · [[byoud]] · [[windows-process-injection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
