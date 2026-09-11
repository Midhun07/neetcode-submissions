class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            counts[idx] += 1
            max_freq = max(max_freq, counts[idx])
            
            # If current window requires more than k replacements, shift left
            while (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len