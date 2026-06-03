class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l=0
        r=0
        maxlen = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l,mp[s[r]] + 1)
            mp[s[r]] = r
            maxlen = max(maxlen, r - l + 1)
        return maxlen


