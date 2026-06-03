class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = set()
        for num in nums:
            if num not in uniq:
                uniq.add(num)
            else:
                return num
                
        