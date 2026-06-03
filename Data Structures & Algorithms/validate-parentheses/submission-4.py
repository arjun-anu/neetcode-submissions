class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s or len(s)==1:
            return False
        mp = {"}": "{", ")": "(", "]": "["}
        for i in range(len(s)):
            if s[i] not in mp:
                stack.append(s[i])
            elif stack and stack[-1] == mp[s[i]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
        
        