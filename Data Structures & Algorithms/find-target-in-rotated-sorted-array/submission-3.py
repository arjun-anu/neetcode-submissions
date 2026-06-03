class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m 
        pivot = l
        
        if target >= nums[l] and target <= nums[len(nums) - 1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0
        while l <= r:
            m = l + (r - l)//2
            print(nums[m])
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:

                return m 
        return -1
            
        