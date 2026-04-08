+++
title = "Academic AI Fundamentals"
date = "2025-09-16T01:45:39+05:30"
description = "Study notes for Artificial & Computational Intelligence — Fundamentals & Foundationals."
featured_image = "images/rama-dfs-bfs.png"
tags = ["Engineering"]
+++

Lord Rama, was doing BFS search until he met Jatayu, then he started DFS.

  <img src="/images/rama-dfs-bfs.png" alt="Lord Rama and BFS, DFS analogy" />

{{< callout emoji="" >}}
Note - This document was created on [notion](https://www.notion.so/pagarevijayy/Notes-AI-Fundamentals-26f41fc193de80f0b2bddc69f32573a1?source=copy_link). It looks more readable there.
{{< /callout >}}

## Search Methods for Problem Solving.

#### State space search

- should be precise
- be able to analyse
- ` S = { S, A, Action(s), Result(s,a), Cost(s,a) } `
    
#### Search Types: Uninformed (blind, brute force) and Informed (heuristic)
    

<table>
  <tr>
    <td><b>Uninformed</b></td>
    <td><b>Informed</b></td>
  </tr>
  <tr>
    <td>search without information</td>
    <td>search with information</td>
  </tr>
  <tr>
    <td>no knowledge</td>
    <td>use knowledge to find steps to solution</td>
  </tr>
  <tr>
    <td>time consuming</td>
    <td>quicker solution</td>
  </tr>
  <tr>
    <td>more complexity (time, space)</td>
    <td>less complexity (time, space)</td>
  </tr>
  <tr>
    <td>DFS, BFS</td>
    <td>A*, Heuristic DFS, Best first search</td>
  </tr>
</table>


#### BFS - uninformed - breadth first search
    


- uninformed search technique
- FIFO (queue)
- Shallowest node
- complete (means it will provide the answer)
- optimal (shortest result/cost)
- time complexity = O(V + E) in Data Structures; in `AI → O(b^d)` where b: branch factor and d: depth (of tree)
- example: tree

#### DFS - uninformed - depth first search

- uninformed search technique
- stack (LIFO)
- deepest node
- incomplete (possible that dfs doesn’t give a solution gets stuck in a loop or infinite search space)
- non-optimal ()
- time complexity = O(V+E); in `AI → O (b^d)`; b: branching factor, d: depth
- space complexity = O(b*d)
- example: [tree](https://www.youtube.com/watch?v=f8luGFRtshY&list=PLAXUYU7PbJhhg1jaU2gasFmh4FlMXvq-P&index=4)

#### DFS family - Depth Bounded, Iterative Deepening
    
<table>
  <tbody>
    <tr>
      <td><b>Depth-Limited Search (DLS)</b></td>
      <td><b>Iterative Deepening Depth-First Search (IDDFS)</b></td>
    </tr>
    <tr>
      <td>Depth is fixed — search is restricted to a certain depth so that it doesn’t encounter a loop or go into infinitely deep space.</td>
      <td>Iteratively first checks for depth 1, then 2, then 3, and so on... till the goal is found.</td>
    </tr>
    <tr>
      <td><b>Completeness:</b> NO (if the solution is beyond the depth limit)</td>
      <td><b>Completeness:</b> YES (if the branching factor 'b' is finite)</td>
    </tr>
    <tr>
      <td><b>Optimality:</b> NO (it might find a non-optimal solution if a solution exists at a shallower depth but is not explored due to the limit)</td>
      <td><b>Optimality:</b> YES (it is guaranteed to find the shallowest goal)</td>
    </tr>
    <tr>
      <td><b>Time Complexity:</b> $O(b^l)$ where 'l' is the depth limit.</td>
      <td><b>Time Complexity:</b> $O(b^d)$ where 'd' is the depth of the shallowest solution. (This is asymptotically equivalent to BFS and DFS for large d)</td>
    </tr>
    <tr>
      <td><b>Space Complexity:</b> $O(bl)$ where 'l' is the depth limit. (Same as DFS)</td>
      <td><b>Space Complexity:</b> $O(bd)$ where 'd' is the depth of the shallowest solution. (Same as DFS)</td>
    </tr>
  </tbody>
</table>

#### Bidirectional search (extension of BFS, DFS)
  - Two simultaneous searches - from initial to goal & from goal to initial, stops when two meets.
  - time [complexity](https://www.youtube.com/watch?v=rEema9uQ02c&list=PLAXUYU7PbJhhg1jaU2gasFmh4FlMXvq-P&index=6) = O(2* b^d/2)
  - complete in BFS, not complete in DFS

#### Heuristics - Informed search
- Used to solve a problem quickly
- For solving non-polynomial problem (i.e. the ones having exponential complexity) in polynomial times.
- a good enough solution will be reached (may not be the optimal)
- [Technique](https://www.youtube.com/watch?v=5F9YzkpnaRw&list=PLAXUYU7PbJhhg1jaU2gasFmh4FlMXvq-P&index=7):
    - eucledian distance
    - manhatten distance or no. of misplaced tiles (8 puzzle problem - complexity O(3^20))

#### Greedy best first search
  - Combines BFS and DFS to form best first search
  - use of heuristic
  - admissibility: h(n) ≤ h*(n) i.e. h(n) should always be less than or equal to actual cost. (heuristic function should not over estimate.)
  - if f(n) = h(n) → optimal solution. (i.e. actual cost = heuristic function); sometimes the solution can be optimal even if actual cost is greater. [[but actual cost cant be less](https://www.youtube.com/watch?v=O9Bp5O2aeu0&list=PLAXUYU7PbJhhg1jaU2gasFmh4FlMXvq-P&index=8)]
  - completeness - NO, optimality - NO
  - time and space complexity = O(b^m)
#### A* - informed search
  - `f(n) = g(n) + h(n)` where g(n) is actual cost from start node to n; h(n) is estimation cost from n to goal node.
  - Example - [directed graph](https://www.youtube.com/watch?v=tvAh0JZF2YE&list=PLAXUYU7PbJhhg1jaU2gasFmh4FlMXvq-P&index=10)
  - optimal
  - time and space complexity = O(b^d)
#### A* admissibility - underestimate, overestimate
  - h(n) ≤ h*(n) → **underestimation [ optimal solution ]**
      - h(n) is heuristic value and h*(n) is the actual/optimal value
      - we always get optimal solution in case of *underestimation*
  - h(n) ≥ h*(n) → **overestimation** (may not be the optimal)
  - [example](https://www.youtube.com/watch?v=xz1Nq6cZejI&list=PLxCzCOWd7aiHGhOHV-nwb0HR5US5GFKFI&index=21)
#### Hill climbing - Local search algorithm
  - Local search algorithm, [no backtracking](https://www.youtube.com/watch?v=3SiWtAnUROs&list=PLAXUYU7PbJhhg1jaU2gasFmh4FlMXvq-P&index=9)
  - Algorithm:
      1. Evaluate initial state
      2. Loop until a solution is found or there are no operators left
          1. select and apply a new operator
          2. evaluate the new state
          3. if goal then quit
          4. if better than current state then it is new current state
  - Problems: local maxima, plateau/flat maxima, ridge
  - Good for a few problems.
  - Better space complexity



**tbd:**

- Simulated annealing
- Local Beam Search
- Genetic Algorithm
- Ant Colony Optimization (ACO)
- Particle Swarm Optimization (PSO)
- Intro & Intelligent agents

{{< details summary="References" >}}
YT playlists
    - [GATE smasher](https://www.youtube.com/playlist?list=PLxCzCOWd7aiHGhOHV-nwb0HR5US5GFKFI)
    - [NPTEL](https://www.youtube.com/playlist?list=PLbMVogVj5nJSFZoiF6RDqyz_m6Srjx_MY)
    - [CS50](https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv)
{{< /details >}}
