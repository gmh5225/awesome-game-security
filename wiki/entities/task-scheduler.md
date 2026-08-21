---
title: TaskScheduler
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/SergeyMakeev__TaskScheduler.md
updated: 2026-08-21
confidence: medium
---

# TaskScheduler

Cross-platform, **fiber-based C++ task scheduler** aimed at high-performance game workloads. Provides multi-threaded job execution, task grouping, work-stealing-style scheduling, and platform abstractions for Windows and POSIX. Bundles extensive tests, examples, and third-party low-level context-switching components for fiber systems. Primary audience: engine programmers building scalable job systems for parallel game logic and rendering pipelines—not a cheat or anti-cheat artifact. (source: wiki/sources/descriptions/SergeyMakeev__TaskScheduler.md)

Listed under README **Task Scheduler** (~1 link). Sits beside other engine infrastructure references such as [[cpp-game-engine-book]] (multithreaded rendering chapters) and open engine source trees like [[serious-engine-base]].

## Links

- Repo: https://github.com/SergeyMakeev/TaskScheduler

## Related

[[overviews/game-engine]] · [[cpp-game-engine-book]] · [[serious-engine-base]] · [[tracy]] · [[optick]]
