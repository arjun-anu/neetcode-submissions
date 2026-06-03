class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        maxCount = 0
        for num in num_set:
            if num-1 not in num_set:
                count = 1
                while (num + count) in num_set:
                    count += 1
                maxCount = max(maxCount, count)
        return maxCount
        

        