class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        diff = {}
        for i in range(len(arr)):
            diff[i] = abs(arr[i] - x)
        diff_sorted = dict(sorted(diff.items(), key = lambda item: item[1]))
        #print(diff_sorted)
        res = []
        for key in diff_sorted.keys():
            res.append(arr[key])
        return sorted(res[0:k])
        '''
        l ,r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x-arr[l]) <= abs(x- arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]

        
