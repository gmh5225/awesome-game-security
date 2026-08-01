---
title: osx-cpu-temp
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/lavoiesl__osx-cpu-temp.md
updated: 2026-08-01
confidence: medium
---

# osx-cpu-temp

Command-line **macOS CPU temperature** reader that queries the Apple **SMC** (System Management Controller) for thermal sensor data and prints current CPU temperature in Celsius or Fahrenheit. The C implementation talks to IOKit's `AppleSMC` service directly—aimed at macOS developers and system-monitoring tool builders who need programmatic hardware temperature access. Listed under Anti Cheat → Detection:HWID beside cross-platform inventory libs and Windows sensor tools. (source: wiki/sources/descriptions/lavoiesl__osx-cpu-temp.md)

Complements cross-platform inventory via [[hwinfo]], Windows sensor monitors such as [[openhardwaremonitor]], and WMI inventory CLIs such as [[windows-hardware-info]].

## Links

- Repo: https://github.com/lavoiesl/osx-cpu-temp (README tag: CPU temperature for OSX)

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[hwinfo]] · [[openhardwaremonitor]] · [[windows-hardware-info]]
