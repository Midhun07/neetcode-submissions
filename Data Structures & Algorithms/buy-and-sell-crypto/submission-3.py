class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while l <= r < len(prices):
            if prices[l] <= prices[r]:
                maxp = max(maxp, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxp
        