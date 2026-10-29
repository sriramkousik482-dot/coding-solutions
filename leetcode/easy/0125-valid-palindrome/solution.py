class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s[0]==s[::-1]:
            return True
        else:
            return False

                