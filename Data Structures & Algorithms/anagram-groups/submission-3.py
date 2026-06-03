class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i,word in enumerate(strs):
            if tuple(sorted(word)) not in anagrams:
                anagrams[tuple(sorted(word))] = [word]
            else:
                anagrams[tuple(sorted(word))].append(word)
        res =[]
        for value in anagrams.values():
            res.append(value)

        return res
