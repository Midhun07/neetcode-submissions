import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = Counter(nums)
        
        inv_dict = [(-v,s) for s,v in f_dict.items()]
        heapq.heapify(inv_dict)

        output_list = []
        while k:
            _, ind = heapq.heappop(inv_dict)
            k -= 1
            output_list.append(ind)
        
        return output_list