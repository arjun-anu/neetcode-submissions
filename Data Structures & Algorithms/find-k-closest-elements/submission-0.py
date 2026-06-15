class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = {}
        for i in range(len(arr)):
            diff[i] = abs(arr[i] - x)
        diff_sorted = dict(sorted(diff.items(), key = lambda item: item[1]))
        #print(diff_sorted)
        res = []
        for key in diff_sorted.keys():
            res.append(arr[key])
        return sorted(res[0:k])

        
