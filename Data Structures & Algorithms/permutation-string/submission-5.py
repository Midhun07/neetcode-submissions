from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we can precompute a sum array of s2 of ascii values of the characters
        # of s2. Then in another loop slide a window of length s1 check if
        # the sum of window matches the sum of s1

        s1_lc = [0] * 26
        for i in s1:
            ind = ord(i) - ord('a')
            s1_lc[ind] += 1
        
        s2_lc = [0] * 26
        i, j = 0, 0

        while j < len(s2):
            s2_lc[ord(s2[j]) - ord('a')] += 1
            if j - i >= len(s1):
                s2_lc[ord(s2[i]) - ord('a')] -= 1
                i += 1
            if s2_lc == s1_lc:
                return True
            j += 1
        return False

        