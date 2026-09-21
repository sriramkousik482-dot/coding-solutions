# Intersection of Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integer arrays `nums1` and `nums2`, return  *an array of their intersection*. Each element in the result must be  **unique**  and you may return the result in  **any order**.

 

 **Example 1:** 

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

 **Example 2:** 

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```

 

 **Constraints:** 

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 36 ms (beats 5.00%)  
**Memory:** 19.3 MB (beats 45.44%)  
**Submitted:** 2026-09-21T05:19:08.424Z  

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        for i in nums1:
            for j in nums2:
                if i==j and i not in result:
                    result.append(i)
        return result
        
```

---

[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)