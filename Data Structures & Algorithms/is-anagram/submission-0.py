class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {i:0 for i in s}
        t_dict = {i:0 for i in t}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        if s_dict == t_dict:
            return True
        else:
            return False
