# Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A phrase is a  **palindrome**  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a  **palindrome**, or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

 **Example 2:** 

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

 **Example 3:** 

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

 **Constraints:** 

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 81.08%)  
**Memory:** 19.5 MB (beats 92.72%)  
**Submitted:** 2026-10-29T06:20:23.481Z  

```py

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ""
        for ch in s:
            if ch.isalnum():
                news += ch
        if news == news[::-1]:
            return True
        else:
            return False

```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)