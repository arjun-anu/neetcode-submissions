class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for i,word in enumerate(strs):
            print(f"index = {i} and word = {word}")
            if tuple(sorted(word)) not in counts:
                counts[tuple(sorted(word))] = [word]
            else:
                counts[tuple(sorted(word))].append(word)
        result = []
        for key,value in counts.items():
            result.append(value)
            
        return result
        