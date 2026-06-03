class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ta = 0
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) -1
            if target >= matrix[i][l] and target <= matrix[i][r]:
                ta = i

        print(ta)
        l,r = 0, len(matrix[ta])-1
        while l <= r:
            m = l + (r-l)//2
            if target < matrix[ta][m]:
                r = m - 1
            elif target > matrix[ta][m]:
                l = m + 1
            else:
                return True
        return False


        