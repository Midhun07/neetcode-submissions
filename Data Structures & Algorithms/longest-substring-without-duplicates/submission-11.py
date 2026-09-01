class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        rep = {}

        for r, c in enumerate(s):
            if c in rep and l <= rep[c]:
                l = rep[c] + 1
            maxl = max(maxl, r - l + 1)
            rep[c] = r
        return maxl