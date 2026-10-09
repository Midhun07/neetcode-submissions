class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subsets = []

        def backtrack(sid):
            result.append(list(subsets))
            for i in range(sid, len(nums)):
                if i > sid and nums[i] == nums[i-1]:
                    continue
                subsets.append(nums[i])
                backtrack(i+1)
                subsets.pop()
        backtrack(0)
        return result
                