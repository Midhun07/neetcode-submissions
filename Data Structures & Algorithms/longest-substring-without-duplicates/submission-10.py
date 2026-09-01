class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep = {}
        l, r = 0, 1
        maxl = 1
        if not s:
            return 0
        rep[ord(s[l])] = l

        while l <= r < len(s):
            if ord(s[r]) in rep:
                maxl = max(maxl, r - l)
                for i in range(l, rep[ord(s[r])]):
                    del rep[ord(s[i])]
                l = rep[ord(s[r])] + 1
                rep[ord(s[r])] = r
                r += 1
            else:
                rep[ord(s[r])] = r
                r += 1
        maxl = max(maxl, r - l)
        return maxl