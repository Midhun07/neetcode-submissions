class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        # [2, 3, 4, 4, 5, 10, 20]

        sums = 1
        max_sum = 1

        for i in range(1, len(nums)):
            # if nums[i] == nums[i-1] + 1:
            #     output[i] = output[i-1] + 1 
            # elif nums[i] == nums[i-1]:
            #     output[i] = output[i-1]
            # else:
            #     output[i] = 1
            sums = sums + 1 if nums[i] == nums[i-1] + 1 else (sums if nums[i] == nums[i-1] else 1)
            max_sum = max(sums, max_sum)
        return max_sum