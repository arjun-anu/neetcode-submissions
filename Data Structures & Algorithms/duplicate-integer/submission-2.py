class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = set()
        for num in nums:
            if num not in dp:
                dp.add(num)
            else:
                return True
        return False