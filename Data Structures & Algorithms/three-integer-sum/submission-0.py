class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        result = []
        for i in range(len(snums)-1):
            if i > 0 and snums[i-1] == snums[i]:
                continue
            l = i + 1
            r = len(snums) - 1
            while l < r:
                threeSum = snums[i] + snums[l] + snums[r]
                if threeSum == 0:
                    result.append([snums[i], snums[l], snums[r]])
                    l += 1
                    r -= 1
                    while snums[l] == snums[l - 1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
        return result
        