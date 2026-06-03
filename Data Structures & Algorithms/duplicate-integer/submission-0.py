class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = set()
        for i in nums:
            if i not in dp:
                dp.add(i)
            else:
                return True
        return False
        