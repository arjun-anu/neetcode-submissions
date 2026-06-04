class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0, n - 1
        while l < r:
            add = numbers[l] + numbers[r]
            if add == target:
                return [l+1,r+1]
            elif add < target:
                l += 1
            else:
                r -= 1