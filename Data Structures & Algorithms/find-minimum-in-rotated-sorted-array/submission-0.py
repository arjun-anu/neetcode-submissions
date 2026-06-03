class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0,len(nums) -1 
        while l < r:
            m = l + (r-l)//2
            print(f"m = {nums[m]}")
            if nums[m] > nums[r]:
                l = m + 1
                print(f"l = {nums[l]}")
            elif nums[m] < nums[r]:
                r = m
                print(f"r = {nums[r]}")
        return nums[l]
                    
        