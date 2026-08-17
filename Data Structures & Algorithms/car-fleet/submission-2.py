from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monotonically increasing event
        # A faster car behind can reach the car infront of it
        # A can can either reach the destination or reach the car ahead of it 
        # whichever is faster, if we see number lower than time to dest then that
        # this max for that number.

        # [4,1,0,7] and [2,2,1,1]
        # [3,4,10,3]
        # same number or less comes then fleet is same, if greater then +1
        time_dict = {}
        for i in range(len(position)):
            time_dict[position[i]] = speed[i]
        
        position.sort(reverse=True)
        stack = deque()
        stack.append((target - position[0]) / time_dict[position[0]])
        for i in range(1, len(speed)):
            time = (target - position[i]) / time_dict[position[i]]
            while stack and stack[-1] < time:
                stack.append(time)

        return len(stack)