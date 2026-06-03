class Solution:
    def isPalindrome(self, s: str) -> bool:
        pling = ""
        for c in s:
            if c.isalnum():
                pling += c.lower()
        if pling == pling[::-1]:
            return True
        return False
        