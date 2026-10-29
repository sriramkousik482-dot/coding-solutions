
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
