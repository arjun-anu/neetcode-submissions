class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for i in range(0, len(temperatures)):
            counter= 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = counter
                    break
                else:
                    counter += 1
        return res
        