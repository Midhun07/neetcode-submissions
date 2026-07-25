class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_list = {i: ind for ind, i in enumerate(nums)}

        for i, item in enumerate(nums):
            rem = target - item
            if rem in s_list.keys():
                if i != s_list[rem]:
                    return [i, s_list[rem]]

