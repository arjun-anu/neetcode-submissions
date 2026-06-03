import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        poseed = [0] * len(position)
        for i in range(len(position)):
            poseed[i] = (position[i], speed[i])
        timestack = []
        poseed.sort(reverse = True)
        for pair in poseed:
            time = (target - pair[0])/(pair[1])
            if timestack and time > timestack[-1]:
                timestack.append(time)
            elif timestack and time <= timestack[-1]:
                continue
            else:
                timestack.append(time)
        return len(timestack)
            

        