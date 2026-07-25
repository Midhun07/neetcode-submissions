class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {i:0 for i in nums}
       
        for i in nums:
            seen[i] += 1

        for i in nums:
            if seen[i] > 1:
                return True
        
        return False