class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rem_dict = {target - j:i for i, j in enumerate(numbers)}

        for i, num in enumerate(numbers):
            pos = rem_dict.get(num)
            if pos is not None:
                return [i+1, pos+1]