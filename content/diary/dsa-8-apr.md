+++
date = '2026-04-08T21:02:17+05:30'
title = "DSA: 1 new, 2 revision  (DP, Backtracking, Graph)"
slug = "dsa-daily-log-2026-04-08"
featured_image = "images/ccc-banner.png"
tags = ["dsa", "leetcode", "study"]
math = true
description = "Reflections on Longest Increasing Subsequence, Combination Sum, and the tricky edge cases of Alien Dictionary."
+++


Today’s session was a mix of one new challenge and two deep-dive revisions. The focus remains on identifying the "core pattern" rather than just memorizing the syntax.

---

## New Challenge: 300. Longest Increasing Subsequence

**The Insight:** The key here is building a `dp` array where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. 

**The Process:** To find `dp[i]`, we look back at all elements `j` (where `j < i`). If `nums[i] > nums[j]`, then `nums[i]` can extend the subsequence ending at `j`. The recurrence relation becomes:  
`dp[i] = max(dp[i], dp[j] + 1)`.

*Note: I initially struggled with the sub-problem definition and had to consult a hint, but the $O(n^2)$ DP approach clicked once I visualized the dependency on previous indices.*

---

## Revision 1: 39. Combination Sum

**The Insight:** Backtracking is essentially navigating a decision tree. It’s similar to traversing a matrix, but instead of physical coordinates, you are managing the "state" of your current sum and current index.

**Key Base Conditions:**
1. **Target Achieved:** `total == target` (Success).
2. **Out of Bounds:** Index exceeds array length.
3. **Overflow:** `total > target` (Prune the branch).

**Lessons Learned:**
* **Deep Copy Ritual:** I fumbled by pushing a reference to the combination array into the results instead of a deep copy. In JavaScript/Python, if you don't copy, the final result will just be a list of empty arrays after the backtrack finishes.
* **The Traversal Trick:** To allow for the same number to be reused, you must branch by passing the **same index** with the updated sum, and a separate branch with the **next index** and the old sum.

---

## Revision 2: 269. Alien Dictionary (Hard)

**The Insight:** This is a classic **Topological Sort** problem masked behind a string comparison logic. It requires building a Directed Acyclic Graph (DAG) based on the lexical order of words.

**The Workflow:**
1. Build an adjacency list by comparing adjacent words.
2. Track "In-degrees" (how many edges point to a node).
3. Use a Queue to process nodes with an in-degree of 0 (Kahn’s Algorithm).

**The Pitfalls:**
* **Cycles:** If you can't process all unique characters, there’s a cycle (invalid order).
* **The Prefix Edge Case:** If "apple" comes before "app", it's an invalid dictionary—something I missed today.
* **Optimization:** Use a `Set` within your adjacency list for each character to handle duplicate edge cases efficiently.

---

**Summary for Today:**
DP requires clear sub-problem definitions. Backtracking requires strict state management (copying results). Graphs require extreme attention to edge cases like cycles and empty dependencies. Onward to tomorrow's two-problem goal!
