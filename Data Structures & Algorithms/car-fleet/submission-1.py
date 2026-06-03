import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        poseed = [0]*len(speed)
        for i,n in enumerate(position):
            poseed[i] = (n,speed[i])
        print(poseed)
        poseed.sort(reverse=True)
        print(poseed)
        stack = []
        for pair in poseed:
            time = ((target-pair[0])/pair[1])
            print(time)
            if stack and time > stack[-1]:
                stack.append(time)
            elif stack and time <= stack[-1]:
                continue
            elif not stack:
                stack.append(time)

        return len(stack)
            

        