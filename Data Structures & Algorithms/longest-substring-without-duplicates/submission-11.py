class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        r = 0
        maxLen = 0
        while r < len(s):
            if s[r] in mp:
                # prevent l going backwards
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen


        




