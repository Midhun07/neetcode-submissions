class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we can precompute a sum array of s2 of ascii values of the characters
        # of s2. Then in another loop slide a window of length s1 check if
        # the sum of window matches the sum of s1

        s1 = sorted(s1)
        
        i, j = 0, len(s1) - 1
        while j < len(s2):
            if sorted(s2[i:j+1]) == s1:
                # print(i, j)
                return True
            i, j = i+1, j+1
        return False
        