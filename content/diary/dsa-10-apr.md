+++
date = '2026-04-10T21:00:00+05:30'
title = 'DSA - 1 new, 2 revision (Hashing, Linked List, Strings)'
description = 'Group Anagrams, Merge Two Sorted Lists, Encode & Decode Strings — hashing trick, linked list template, and better pointer handling.'
featured_image = "images/ccc-banner.png"
tags = ["leetcode", "dsa"]
+++

### 📌 Today’s Progress
**1 New • 2 Revisions**

---

###  New Problem

**49. Group Anagrams**  
**Insight:** Sort characters of each word and use it as a key in a hashmap to group anagrams.  
**Comment:** Easy overall, but needed a hint to recall the sorting trick.

**Observation (JS Quirk):**
- `arr.sort()` sorts alphabetically (case-sensitive) by default  
- For numbers → `(a, b) => a - b` works  
- For alphabets → direct sort works, comparator logic differs  

---

### Revisions

**21. Merge Two Sorted Lists**  
**Insight:**  
Used standard linked list template:
- `dummy`, `curr`, and `head` pattern  
- Traverse using `curr`  
- Return `dummy.next`  
- Append remaining nodes after one list ends  

**Comment:** Felt straightforward — template becoming natural.

---

**271. Encode and Decode Strings**  
**Insight:**  
- Use **length prefixing** for each string  
- Add delimiter between length and string  
- Carefully handle empty strings and edge cases  
- Pointer movement is key  

**Comment:** Getting more comfortable managing pointers and parsing logic.

---

### 💭 Reflection

Good, productive day overall.  
Balanced problem-solving with understanding patterns instead of just solving.

Had the **mid-sem dissertation viva** — went well, and the progress so far feels solid.  
Got an interesting push from the examiner to **write a research paper** based on this work.

That’s something worth exploring seriously.

Momentum is building ⚡
