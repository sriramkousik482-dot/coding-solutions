# Sort Colors

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `nums` with `n` objects colored red, white, or blue, sort them  **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

 **Example 1:** 

 **Input:**  nums = [2,0,2,1,1,0]

 **Output:**  [0,0,1,1,2,2]

 **Explanation:** 

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

 **Example 2:** 

 **Input:**  nums = [2,0,1]

 **Output:**  [0,1,2]

 **Explanation:** 

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

 

 **Follow up:**  Could you come up with a one-pass algorithm using only constant extra space?

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 2.39%)  
**Memory:** 19.4 MB (beats 24.27%)  
**Submitted:** 2026-09-22T15:10:11.591Z  

```py
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n=len(nums)
        for i in range(n):
            for j in range(1,n):
                if nums[j]<nums[j-1]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
        print(*nums)
            

        
        
```

---

[View on LeetCode](https://leetcode.com/problems/sort-colors/)