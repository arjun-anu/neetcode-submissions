class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i,word in enumerate(strs):
            if tuple(sorted(word)) not in anagrams:
                anagrams[tuple(sorted(word))] = [word]
            else:
                anagrams[tuple(sorted(word))].append(word)
        dp = []
        for i,anagrams in anagrams.items():
            dp.append(anagrams)
        return dp