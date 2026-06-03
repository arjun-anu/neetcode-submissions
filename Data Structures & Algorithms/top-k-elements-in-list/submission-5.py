class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        sorted_counts = dict(sorted(counts.items(),key=lambda item: item[1], reverse=True))
        num = 0
        result = []
        for i,n in sorted_counts.items():
            if num < k:
                result.append(i)
                num += 1
            else:
                break
        return result
            


