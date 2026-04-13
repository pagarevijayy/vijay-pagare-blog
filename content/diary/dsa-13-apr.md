+++
date = '2026-04-13T22:30:00+05:30'
title = 'DSA - 1 New, 1 Revision (DP, Greedy, Heaps)'
description = 'Jump Game intuition (DP to Greedy), Median from Data Stream using 2 heaps, and growing problem-solving confidence.'
tags = ["leetcode", "dsa"]
+++

---
### New Problem 
**55. Jump Game**  
- DP (Bottom-up):  
  - Create `dp[]`, set `dp[last] = true`  
  - Fill from right to left using reachable indices  i.e. `dp[i+jumps]`
  - Optimization:  
    - Without pruning overflow jumps → exponential 
    - Even optimized DP → O(n²)  

- Greedy - O(n):  
  - Maintain `goal = last index`  
  - Traverse backwards  
  - If `i + nums[i] >= goal` → update `goal = i`  
  - Final check → `goal == 0`

Comment:  
Initially leaned towards backtracking (decision at each index), but constraints (`nums[i]` up to 10^5) made it infeasible. Key learning → recognize when brute force explodes due to branching factor. DP gave structure, but greedy revealed the optimal path.

---

### Revision

**295. Find Median from Data Stream**  
- Optimal: two heaps  
  - `maxHeap (left)` → smaller half  
  - `minHeap (right)` → larger half  
  - Insert → rebalance → compute median  
  - Median Logic:   
    - Equal size → average of tops  
    - Unequal → top of minHeap  

Comment:  
- First exposure → implemented a naive solution which exceeded time limit; Studied optimal solution using heaps/PQs.
- Second attempt → implemented smoothly (<15 mins)  
- Reinforced understanding of heap-based streaming problems

---

### Learning

Started watching Aditya Verma’s [DP playlist](https://www.youtube.com/playlist?list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn) on YouTube to build intuition.  
Early impression → structured and promising.

---

### Reflection

Solving more Blind 75 problems is leading to clear improvements in both coding ability and problem-solving.  Confidence is becoming practical rather than theoretical. Key shift: From “what approach to use?” → “which approach is optimal here and why?”

Growth is tangible.
