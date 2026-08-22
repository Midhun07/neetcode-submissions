from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 2 pass strategy:
        # During both passes find the next min from i
        # use monotonic stack for this.
        # use 2 arrays to keep track of min till i

        rm = [len(heights)-1] * len(heights)
        lm = [0] * len(heights)
        stack = deque()
        max_rec = 0

        # right pass
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                rm[stack[-1]] = i-1
                stack.pop()
            stack.append(i)
        stack.clear()
        # left pass
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                lm[stack[-1]] = i+1
                stack.pop()
            stack.append(i)
        
        for i in range(len(heights)):
            max_rec = max(max_rec, heights[i] * (rm[i] - lm[i] + 1))
        
        return max_rec

        