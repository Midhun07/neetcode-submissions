class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep counts of all characters in t
        # from start, update counter of every character in s and check if they <= the count in s
        # shift l if false else continue, whenever count list of both strings match return the substring

        t_cl = [0] * 128
        unique = 0
        for i in t:
            t_cl[ord(i)] += 1
            unique = unique + 1 if t_cl[ord(i)] == 1 else unique

        i, j = 0, 0
        s_cl = [0] * 128
        satisfied = 0
        maxs = (len(s), (i,j))
        while j < len(s):
            s_cl[ord(s[j])] += 1

            if t_cl[ord(s[j])] and s_cl[ord(s[j])] == t_cl[ord(s[j])]:
                satisfied += 1

            while satisfied == unique:
                maxs = maxs if maxs[0] < (j - i + 1) else (j - i + 1, (i,j))
                if s_cl[ord(s[i])] - 1 < t_cl[ord(s[i])]:         
                    break
                s_cl[ord(s[i])] -= 1
                i += 1
            j += 1
        
        i, j = maxs[1]
        return s[i:j+1] if satisfied == unique else ""
        