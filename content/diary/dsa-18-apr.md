+++
date = '2026-04-18T09:46:24+05:30'
slug = "2026-04-18-climbing-stairs-fibonacci-dp-pattern"
tags = ["leetcode", "dsa"]
title = "DSA - 1 new - climbing stairs (DP)"
+++

---

## 70. Climbing Stairs — DP (Fibonacci pattern)
**Insight** — Problem follows Fibonacci recurrence; solve via recursion + memoization (store intermediate states in hashmap)

**Comment** — Recognized pattern only after manually enumerating paths; without that, the recurrence wasn’t obvious

### Note

Whenever you see a problem where:

- You are moving toward a target
- Your move choices are fixed constants (e.g., 1, 2, 5)
- The order of moves matters

→ It almost always reduces to a linear recurrence relation (Fibonacci-like DP)
