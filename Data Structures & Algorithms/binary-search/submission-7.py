class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        # why l <= r?
        # becase when l == r there is still one candidate left to check,
        # and since we're manually checking and not converging in one answer, 
        # we need to check when l <= r

        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m 
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1