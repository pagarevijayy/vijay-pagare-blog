+++
title = "DSA - 1 new - Word Search (DFS + Backtracking)"
date = 2026-04-22
slug = "2026-04-22-word-search-dfs-backtracking"
tags = ["dsa", "leetcode"]
+++
---

## 79. Word Search

Grid traversal + backtracking problem.

### Insight

- Traverse the matrix using **DFS**.
- At each cell:
  - Match current character.
  - Explore all 4 directions (up, down, left, right).
- Use backtracking to revert state after exploring paths.
- Key Optimization: Instead of maintaining a separate `visited` matrix:
    - Mark the current cell as `'#'` (visited).
    - Restore it after DFS call (backtrack).
  This reduces extra space and keeps logic tight.

⚡ JS Refreshers
- Strings are immutable → cannot modify in-place.
- splice() works only on arrays, not strings.
- Know CRUD operations by heart on these structures: Map, Set, Object, Array
