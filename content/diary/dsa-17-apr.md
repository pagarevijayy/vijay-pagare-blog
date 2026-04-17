+++
date = '2026-04-17T20:55:26+05:30'
title = 'DSA - 2 new (DP Formulation, Union-Find Revisit)'
description = 'Coin Change using bottom-up DP formulation and revisiting Union-Find for connected components; uncovered JS push() return gotcha.'
tags = ["leetcode", "dsa"]
featured_image = "images/dsa.png"
+++
---

## 322. Coin Change  
**Insight**: 
- dp[amount] = minimum coins needed; 
- base case dp[0] = 0; 
- transition: dp[a] = min(dp[a], 1 + dp[a - coin]) for all coins; 
- solved via bottom-up DP (iterative state build, not actual BFS).  

**Comment**: Could brute force some cases using backtracking + greedy, but optimal DP formulation wasn’t immediate. Need stronger instinct for defining dp state and transitions.

## 323. Number of Connected Components in Undirected Graph  
**Insight**: Union-Find: union edges, then count unique roots using find (with path compression); ensure isolated nodes are counted as separate components.  

**Comment**: Took longer than expected even after recalling the logic. Implementation details + edge cases (like isolated nodes) slowed me down. Needs more repetition to make Union-Find second nature.

---

## Learning  
- DP clarity comes from **state definition first**, not approach (BFS/DFS confusion).  
- Union-Find is simple conceptually but **error-prone in implementation** — needs muscle memory.  
- JS gotcha: `arr.push(x)` returns new length, not the array — easy to misuse in chaining or assignments.
