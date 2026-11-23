---
title: BREACH
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ctrl-sagesh__breach.md
updated: 2026-11-23
confidence: medium
---

# BREACH

**Browser-based hacking terminal game** (ctrl-sagesh) where players take freelance missions to breach **simulated networks** and practice real offensive-security concepts in a safe, fictional environment. Built with **Next.js** and **TypeScript**; ships a **Kali-style shell** with completion, piping, and command history, plus a story campaign, daily challenges, achievements, and debriefs tied to mistakes such as weak credentials, bad hashing, and SQL injection. **Leaderboard integrity** uses **server-side replay**: the client submits only command logs and timing; **Supabase Edge Functions** re-run the same **deterministic game engine** to score runs and reject implausible or tampered submissions. Targeted at learners who want hands-on penetration-style problem solving without touching real systems; includes extensive **Vitest** coverage of missions, replay validation, and anti-cheat logic. (source: wiki/sources/descriptions/ctrl-sagesh__breach.md)

Sits beside browser hacking puzzle platforms such as [[htw]] and gamified RE academies such as [[re-dojo]], and beside server-replay leaderboard references such as [[dmn-minigame]], [[bitgeist]], and [[bevy-personal-test]].

## Links

- Repo: https://github.com/ctrl-sagesh/breach

## Related

[[htw]] · [[re-dojo]] · [[dmn-minigame]] · [[bitgeist]] · [[bevy-personal-test]] · [[intro-to-gamehacking]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]