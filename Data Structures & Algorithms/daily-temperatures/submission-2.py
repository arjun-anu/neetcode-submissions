class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack apporach
        res = [0] * len(temperatures)
        stack = []
        for i,n in enumerate(temperatures):
            if stack and n <= stack[-1][0]:
                stack.append((n,i))
            elif not stack:
                stack.append((n,i))
            elif stack and n > stack[-1][0]:
                while stack and n > stack[-1][0]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append((n,i))
            
            
        return res
        


        # brute force approach

        #res = [0]*len(temperatures)
        # for i in range(0, len(temperatures)):
        #     counter= 0
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = counter
        #             break
        #         else:
        #             counter += 1
        # return res
        
        