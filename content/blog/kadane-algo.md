+++
title = "The Pattern Behind Kadane's Algorithm"
date = "2026-04-12T00:04:00+05:30"
slug = "kadanes-algorithm-pattern"
description = "A deep dive into the local vs. global optimization strategy for solving the Maximum Subarray Sum problem in linear time."
tags = ["dsa", "engineering"]
+++

Kadane’s Algorithm is a classic dynamic programming technique used to find the Maximum Subarray Sum within a one-dimensional array of numbers. It’s famous for its efficiency, turning what could be a brute-force $O(N^2)$ problem into a sleek $O(N)$ linear scan.

---
## 1. What is Kadane’s Algorithm?

The algorithm iterates through an array, keeping track of the maximum sum ending at the current position. It makes a simple choice at every element:

Should I add the current element to the existing subarray?

Or should I start a brand-new subarray starting at the current element?

The "magic" is that it discards any prefix that has a negative sum, as it would only decrease the potential sum of any future subarray.

### Psuedocode (core logic)
```
  let maxSoFar = -Infinity;
  let maxEndingHere = 0;
  
  for (let x of array) {
      maxEndingHere = Math.max(x, maxEndingHere + x);
      maxSoFar = Math.max(maxSoFar, maxEndingHere);
  }
```

---
## 2. Where does it get applied?
While the most famous use case is the Maximum Subarray Sum, the logic extends to several domains:

**Stock Market Analysis:** Finding the best period of gains (or minimizing losses) over a timeline.

**Computer Vision:** Used in "Maximum Weight Submatrix" problems (the 2D version of Kadane’s) to detect the brightest or most feature-dense area in an image.

**Genomic Sequence Analysis:** Identifying protein-coding segments or regions with high GC-content.

**Data Mining:** Finding periods of peak activity in sensor logs or web traffic.

---
## 3. What is the Core Pattern?
The core pattern is Local vs. Global Optimization.

- Local Maximum: The best you can do right now (at index $i$).
- Global Maximum: The best you have ever done during the entire traversal.

It relies on the Optimal Substructure property: The maximum subarray ending at index $i$ depends only on the maximum subarray ending at $i-1$.

---
## 4. Niche-based or Pattern-applicable?

It is definitely pattern-applicable. It isn't just for "Maximum Sum"; it's for any problem involving contiguous sub-segments where you need to decide whether to "extend or restart."

When to think of Kadane's:
1. **Contiguity:** The problem requires a contiguous subarray (not a subsequence).
2. **Cumulative Property:** You are tracking a value that can increase or decrease (sum, product, etc.).
3. **Linear Time Requirement:** You need to solve it in $O(N)$ because the input size is large ($10^5$ or more).

---
## Variations of the Pattern:

1. **Maximum Product Subarray:** A slight twist where you must also track the minimum product (because two negatives make a positive).
2. **Circular Subarray Sum:** Using Kadane’s twice—once for the normal array and once to find the "minimum" subarray to subtract from the total sum.
3. **Flip Bits:** Finding the maximum number of 1s you can get by flipping a contiguous segment of 0s.
