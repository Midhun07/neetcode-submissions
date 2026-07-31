class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Remove all non-alphanumeric character
        # Start with 2 pointers, one from the start and other from end
        # Go for N // 2 iterations and check if both pointer data match
        # if no then return False, if no mismatch till N//2 then return true

        sanitized = ''.join(c for c in s if c.isalnum()).lower()

        print(sanitized)

        len_s = len(sanitized) // 2

        for i in range(len_s):
            if sanitized[i] != sanitized[-(i+1)]:
                return False
        
        return True