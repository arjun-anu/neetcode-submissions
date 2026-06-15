class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = float('inf')
        curSum = 0
        for r in range(len(nums)):
            curSum = sum(nums[l:r + 1])
            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                l += 1
                curSum = sum(nums[l:r + 1])
                
        if minLen == float('inf'):
            return 0
        return minLen

        