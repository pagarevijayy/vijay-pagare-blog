+++
date = '2026-04-14T22:00:00+05:30'
title = 'DSA - 2 new (Intervals: Merge & Insert)'
description = 'Covered interval merging patterns with sorting and traversal insights.'
tags = ["leetcode", "dsa"]
+++
---
### New

**56. Merge Intervals**  
**Insight:** Optimised approach is to sort intervals by start time, then iterate and merge overlapping intervals by comparing current start with previous end.  
**Complexity:** O(n log n) due to sorting; merging is O(n).  
**Comment:** Initially thought of an O(n²) solution using nested loops and hashing. Midway realised sorting simplifies the problem significantly. Intuition came from previously solved interval patterns. Solved in ~35 minutes.

**57. Insert Interval**  
**Insight:** Combination of traversal + interval merging. Need to handle three cases: no overlap (before), overlap (merge), and after insertion.  
**Comment:** Logic was clear conceptually but struggled with implementation and edge cases. Not fluent with array manipulation. Learned that using `while` loops could simplify control flow. After hints and reference, able to handle all edge cases.

---
### Learnings

- Learned about [for vs while](/for-vs-while-loop)
- Sorting often converts complex interval problems into linear scans
- Implementation fluency can be better
