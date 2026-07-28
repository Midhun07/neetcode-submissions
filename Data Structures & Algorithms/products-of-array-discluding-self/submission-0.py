class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        output2 = [1] * len(nums)
        # [2, 4, 1, 7, 6]
        # p1: [1, 2, 8, 8, 56]
        # p2: [84, 42, 42, 6, 1]
        # 2 pass strategy
        # in the 1st pass store product of all elements upto i-1
        # in the second pass from reverse do the same
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            output2[i] = output2[i + 1] * nums[i + 1]

        for i in range(len(output)):
            output[i] *= output2[i]

        return output