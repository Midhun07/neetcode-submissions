import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        maxl = []
        heap = []
        
        for i, v in enumerate(nums):
            heapq.heappush(heap, (-v, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                maxl.append(-heap[0][0])
        return maxl