+++
title = "DSA - 3 new - DP, Hashmap"
date = "2026-04-28"
slug = "2026-04-28-dp-houserobber-decode-ways-duplicate"
tags = ["dsa", "leetcode"]
+++

---
### 213. House Robber II
Insight: Same as House Robber (iterative DP). Since first & last are adjacent, split into 2 cases:
- Rob from index 0 → n-2
- Rob from index 1 → n-1  
Take max of both.

Comment: Brain fog. Couldn't even recall/formulate base House Robber logic.

---

### 217. Contains Duplicate
Insight:
1. Convert to Set → if size reduces → duplicate exists  
2. Use HashMap → check while inserting

Comment: Straightforward. Can do in O(n) using set/hash.

---

### 91. Decode Ways
Insight: DFS + memoization  
Recurrence: dfs(i) = dfs(i+1) + dfs(i+2)  
Base cases:
- Out of bounds → 1  
- Leading '0' → 0  
- Two-digit valid only if <= 26  

Comment: Weak formulation. Took help (NeetCode + Gemini) to complete.
