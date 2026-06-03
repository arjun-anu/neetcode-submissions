class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1)>len(s2):
            return False
        freq_count = {}
        for char in s1:
            if char not in freq_count:
                freq_count[char] = 1
            else:
                freq_count[char] += 1
        flag = 0
        for l in range(len(s2)-len(s1)+1):
            sub = s2[l:l+len(s1)]
            for char in freq_count:
                if sub.count(char) != freq_count[char]:
                    flag = 0
                    break
                else:
                    flag = 1
                    continue
            if flag == 1:
                return True
        return False
            
        
        