from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We can eat atmost a pile, max pile, in an hour
        # We sort the array, so the max pile is max K possible
        # With maxK we can eat all piles in n hours and h>=n

        piles.sort()
        l,r = 1, piles[-1]
        k = r
        mid = (l + r) // 2

        while l < r:
            sumt = 0
            for i in piles:
                sumt += ceil(i / mid)
            if sumt <= h:
                k = mid
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2
        return k
        