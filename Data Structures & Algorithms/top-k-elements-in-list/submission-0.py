class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        
        result = []
        for i in range(0,k):
            max_value = max(counts,key = counts.get)
            result.append(max_value)
            del counts[max_value]
        return result


