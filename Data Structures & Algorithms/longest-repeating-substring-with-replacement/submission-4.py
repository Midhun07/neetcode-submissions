class Solution:
    def get_count_non_max(self, store):
        count, maxc = 0, 0
        for k, v in store.items():
            count += v
            maxc = max(maxc, v)
        return count - maxc

    def characterReplacement(self, s: str, k: int) -> int:
        # start from left, we keep the count of characters,
        # at any point check if the sum of number of characters other than max occuring character is 
        # less than k.
        # if no count is less than that then shift left else continue shifting right
        # and keep updating max len with max(max_len, (r - l + 1)).

        # How to find all the characters with count less than k??
        # keep count of all 26 characters, complexity will be of O(26 n) ~ O(n).

        store = {}
        i, j, max_len = 0, 0, 0

        while i <= j < len(s):
            if store.get(s[j]) is None:
                store[s[j]] = 1
            else:
                store[s[j]] += 1

            if self.get_count_non_max(store) <= k:
                max_len = max(max_len, j - i + 1)        
            else:
                store[s[i]] -= 1
                i += 1
            j += 1
        
        return max_len