class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            print(f"mid = {mid}")
            print(f"midnum = {nums[mid]}")
            print(f"l = {l}, r = {r}")
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
            

