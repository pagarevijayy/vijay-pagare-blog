+++
title = "DSA - 2 New, 2 revision (DFS, HashMap, Greedy)"
date = "2026-04-20"
slug = "2026-04-20-number-of-islands-set-matrix-zeroes-jump-game-anagrams"
tags = ["dsa", "leetcode"]
+++
---
## 2 New Problems

### 200. Number of Islands
**Insight:** Traverse the grid; whenever a cell is land, increment the island count and sink all connected land using DFS (or BFS).

**Comment:** Knew the core idea, but fumbled deciding where exactly to increment the island count (before vs after traversal).


### 73. Set Matrix Zeroes
**Insight:** Identify rows and columns that need to be zeroed, then update them. Basic solution uses O(m × n) space. Optimized solution uses the first row and column as markers to achieve O(1) space.

**Comment:** Took 5–10 minutes to arrive at the solution. The in-place optimization required deeper thinking.

---

## 2 Revision

### 55. Jump Game
**Insight:** Greedy approach — track `lastReachable` initialized to the last index. Traverse from right to left; if current index can reach `lastReachable`, update it. If it reaches index 0, return true.

**Comment:** Smooth solve using greedy approach. Time complexity O(n).


### 49. Group Anagrams
**Insight:** Group strings by sorting characters — identical sorted strings indicate anagrams.

**Comment:** Solved in under 5 minutes. Straightforward mapping problem.

---

## 🧠 Key Takeaways

- Grid problems → Think **DFS/BFS + marking visited (sink pattern)**
- Matrix problems → Look for **in-place optimizations using first row/column**
- Greedy problems → Often involve **working backwards or tracking reachability**
- Hashing problems → Reduce to **canonical representation (e.g., sorted string)**

---

## ⚡ Pattern Recognition Notes

- **"Connected components in grid" ⇒ DFS/BFS**
- **"Modify matrix in-place" ⇒ Use matrix itself as storage**
- **"Can reach end?" ⇒ Greedy > DP (usually)**
- **"Grouping problems" ⇒ HashMap + normalization**

---
