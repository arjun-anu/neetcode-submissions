class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        result = 0
        i = 0

        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j],0) + 1
            maxFreq = max(freq.values())
            curLen = j - i + 1
            print(s[i:j+1])
            #print(f'curLen = {curLen} and maxFreq = {maxFreq}')

            if curLen - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
            print(freq)
            result = max(j - i + 1, result)
        return result
        