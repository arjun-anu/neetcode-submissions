class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+ 1
            temp = s[i:i + length]
            result.append(temp)
            i += length
        return result
