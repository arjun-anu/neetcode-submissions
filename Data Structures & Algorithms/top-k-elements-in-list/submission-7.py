class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indices = {}
        for i,n in enumerate(nums):
            if n not in indices:
                indices[n] = 1
            else:
                indices[n] += 1
        sorted_counts = dict(sorted(indices.items(), 
        key=lambda item: item[1], reverse = True))
        res = []
        print(list(sorted_counts.keys())[:k])
        for i in list(sorted_counts.keys())[:k]:
            res.append(i)
        return res
            

            


